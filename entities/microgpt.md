---
title: microgpt
created: 2026-04-21
updated: 2026-04-21
type: entity
tags: [model, training, transformer, autograd, from-scratch]
sources: [https://gist.github.com/karpathy/8627fe009c40f57531cb18360106ce95]
---

# microgpt

> Source: [GitHub Gist](https://gist.github.com/karpathy/8627fe009c40f57531cb18360106ce95) by Andrej Karpathy · February 2026 · 5,000+ stars
> ~300 lines of pure, dependency-free Python. No PyTorch, no numpy. Only `os`, `math`, `random`.

## What It Is

The most atomic GPT implementation: a full transformer (forward pass, backward pass, and inference) in ~300 lines of vanilla Python. Karpathy's philosophy: **everything else is just efficiency.** The full algorithm is here — tensors, automatic differentiation, optimization, and autoregressive generation — all as scalar operations with no external libraries.

Companion to [[micrograd-neural-networks-backpropagation-VMj-3S1tku0]]: same from-scratch philosophy, scaled up from a single neuron to a full transformer.

## Architecture

| Component | Detail |
|---|---|
| **Tokenizer** | Character-level. Each unique char in dataset becomes token ID 0..n-1. Plus one BOS (Beginning of Sequence) token. |
| **Vocab size** | 27 tokens (26 chars + BOS, for names.txt) |
| **Embedding** | 16-dimensional (`n_embd = 16`) |
| **Context window** | 16 characters (`block_size = 16`) |
| **Attention** | 4 heads, each 4-dimensional (`head_dim = n_embd // n_head`) |
| **Transformer layers** | 1 (`n_layer = 1`) |
| **Total parameters** | ~8,000 |

Model weights stored as nested lists of `Value` objects in `state_dict`:
- `wte`: token embedding matrix `(vocab_size, n_embd)`
- `wpe`: position embedding matrix `(block_size, n_embd)`
- `lm_head`: language model head `(vocab_size, n_embd)`
- Per layer: `attn_wq`, `attn_wk`, `attn_wv`, `attn_wo`, `mlp_fc1`, `mlp_fc2`

## Key Implementation Decisions

### No LayerNorm — RMSNorm only
No bias terms anywhere. RMSNorm formula: `scale = (mean_square + 1e-5) ** -0.5` applied to token + position embeddings before attention and MLP blocks. The residual connection makes LayerNorm redundant.

### ReLU not GeLU
Deliberate simplification. MLP: `linear → ReLU → linear`. 4x expansion in first linear layer (standard GPT hidden dimension rule).

### Manual KV cache
During autoregressive inference, `keys[layer]` and `values[layer]` are Python lists that grow each forward pass. No `past_key_values` tuple. The attention dot-products are computed over the full accumulated context.

### Custom Adam optimizer
Implemented from scratch with scalar operations:
- `m` (first moment) and `v` (second moment) as flat lists of floats
- Bias correction: `m_hat = m / (1 - beta1^(step+1))`
- Update: `p.data -= lr_t * m_hat / (v_hat^0.5 + eps)`

### Cross-entropy via log-probabilities
Loss at each position: `-log(probs[target_id])`. Final loss is average across all positions in the sequence.

## The Value Class (Autograd Engine)

The heart of the system — a scalar wrapper that tracks computation graph:

```python
class Value:
    __slots__ = ('data', 'grad', '_children', '_local_grads')
    
    def __add__(self, other): return Value(self.data + other.data, (self, other), (1, 1))
    def __mul__(self, other): return Value(self.data * other.data, (self, other), (other.data, self.data))
    def log(self): return Value(math.log(self.data), (self,), (1/self.data,))
    def exp(self): return Value(math.exp(self.data), (self,), (math.exp(self.data),))
    def relu(self): return Value(max(0, self.data), (self,), (float(self.data > 0),))
    
    def backward(self):
        # Topological sort + chain rule accumulation
        # Same as PyTorch's autograd engine
```

Forward pass builds the graph via `__add__`, `__mul__`, etc. Backward pass traverses the graph in reverse topological order, calling `child.grad += local_grad * parent.grad` for each edge.

## Training Loop

- **Dataset**: ~32K first names from `names.txt` (downloaded from makemore repo)
- **Shuffle**: Dataset shuffled once at startup
- **Sequence**: Single document per step. Tokenized with BOS on both ends.
- **Context truncation**: `n = min(block_size, len(tokens) - 1)` — works for names shorter than 16 chars
- **LR schedule**: Linear decay from 0.01 to 0 over 1000 steps
- **Batch**: One document at a time (no batching — efficiency is not the point)

## Inference

After training: autoregressive generation with temperature sampling:
- Start with BOS token
- Each step: forward pass → softmax → `random.choices(weights=probs)`
- Stop when BOS is generated or block_size reached
- Temperature < 1 makes output more deterministic; > 1 makes it more random

## What This Teaches

- The transformer architecture in its minimal form
- How autograd actually works (not just forward-mode backprop, but the full reverse-mode chain rule traversal)
- That modern DL libraries are entirely about efficiency — the algorithm itself is small
- The gap between a character-level name generator and an LLM is mostly scale (parameters, data, compute) and vocabulary (byte-pair vs character-level)

## Related

- [[micrograd-neural-networks-backpropagation-VMj-3S1tku0]] — building micrograd from scratch; derivatives, chain rule, MLP; the logical precursor to microgpt
- [[transformer]] — the full transformer architecture that microgpt implements in minimal form
- [[andrej-karpathy]] — creator of both micrograd and microgpt
