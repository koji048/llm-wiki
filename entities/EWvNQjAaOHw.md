---
title: How I Use LLMs
created: 2026-04-20
updated: 2026-04-21
type: entity
tags: [LLM, prompting, practical-applications, ChatGPT, custom-gpts, multimodal]
sources: [raw/transcripts/EWvNQjAaOHw]
---

# How I Use LLMs

In this practical guide, Andrej Karpathy demonstrates how he personally uses large language models in his daily work and life. The video is a comprehensive tour of the modern LLM ecosystem, covering everything from basic prompting to advanced customization.

## Prompting Strategies

### Zero-Shot Prompting

The simplest approach: just ask the model a question or give it a task without any examples. For straightforward tasks (facts, simple transformations, basic questions), zero-shot works well.

**Example:**
> "Translate this paragraph to Spanish."

### Few-Shot Prompting

Provide a few examples of the input-output pattern you want. The model learns from these examples and applies the pattern to your query. This is especially useful when:
- The task is ambiguous
- The output format needs to be specific
- The task requires a particular tone or style

**Example:**
> "Rewrite these sentences in the style of Shakespeare:  
> 'The weather is nice today' → 'The heavens doth smile upon this day'  
> 'I am going to the store' → ..."

### Chain-of-Thought Prompting

Ask the model to reason step-by-step before giving the final answer. Prefix with "Let's think step by step" or "Explain your reasoning." This elicits [[chain-of-thought]] reasoning, which significantly improves performance on complex reasoning tasks (math, logic, multi-step problems).

### System Prompts

The **system prompt** (in ChatGPT, this is set in the System field) establishes the model's persona, behavior rules, and context. Key uses:
- Setting the tone (e.g., "Be concise and technical")
- Defining constraints (e.g., "Never make up facts; say 'I don't know' instead")
- Providing background context (e.g., "You are an expert at X")
- Specifying output format (e.g., "Always respond in JSON")

## Conversation Management

Karpathy emphasizes the importance of **starting new conversations** when switching topics or tasks. Each conversation has:
- Its own [[context-window]] (working memory)
- No memory of other conversations

**Best practices:**
- Use a new chat when the topic shifts significantly
- Keep related conversation in the same thread for context continuity
- Periodically summarize and start fresh if the conversation becomes too long

### Thread Organization

For ongoing projects, keep a document of conversation summaries or pinned messages. Use the model itself to help organize — paste in a summary of what you've discussed so far.

## Custom GPTs

Custom GPTs (also called GPTs) allow creating no-code custom assistants without any programming. Available in the ChatGPT interface, they let you:
- Define a system prompt for a specific persona or task
- Upload **knowledge files** (PDFs, text, documents) that the GPT can reference
- Define **actions** — APIs the GPT can call (e.g., searching a database, sending emails)
- Set specific behaviors, constraints, and capabilities

Karpathy uses custom GPTs for repetitive tasks like:
- Reviewing code in a particular style
- Acting as a domain-specific tutor
- Helping with specific writing formats

These are distinct from fine-tuning — customization is done through prompting and retrieval, not retraining the model.

## Memory Feature

ChatGPT has a **memory** feature that persists information across conversations:
- **Per-conversation memory**: You can explicitly tell the model to remember something, and it will be available in future conversations
- **Global memory**: The model may remember things you've told it across multiple chats

This is distinct from the context window, which resets each conversation. Memory is more persistent but requires explicit management.

## Multimodal Capabilities

### Image Upload

GPT-4o and later support image analysis. You can:
- Upload screenshots of errors or UI
- Share photos for analysis or identification
- Send diagrams or charts for explanation

### File Upload

Upload documents (PDFs, Word files, Excel spreadsheets) for analysis:
- Ask questions about the content
- Get summaries of long documents
- Extract specific information
- Analyze data in spreadsheets

### PDF Analysis

Especially powerful for research — upload academic papers and ask for:
- Summary of key findings
- Explanation of specific sections
- Comparison across multiple papers
- Identification of methodological issues

## Model Tiers and When to Use Each

### GPT-4o (Omni)

The balanced, general-purpose model. Good at most tasks with fast response times. Supports text, images, audio, and video input.

**Use for:** Most everyday tasks, writing, coding, analysis, conversation.

### o1 and o3 (Reasoning Models)

Specialized for deep reasoning and complex problem-solving. These models:
- Spend more compute "thinking" before responding
- Are trained with reinforcement learning for reasoning tasks
- Excel at math, science, coding competitions, and multi-step logic

**Use for:** Hard math problems, competitive programming, complex debugging, scientific reasoning.

### Claude (Anthropic)

Often preferred for:
- Long documents and extended writing
- Philosophical discussions
- Nuanced ethical reasoning
- Code that requires careful analysis

### Gemini (Google)

Integrated with Google products:
- Better for tasks involving Google search or YouTube
- Strong multimodal integration
- Good for research with real-time information

**Use for:** When you need up-to-date information via search, or when working within the Google ecosystem.

## Practical Workflow Examples

### Language Learning

Use the model as a conversation partner and tutor:
- Practice writing in the target language
- Get grammar corrections and explanations
- Have the model explain idioms and cultural context

### Coding Workflow

- **Debugging**: Paste error messages and code; ask for diagnosis
- **Code review**: Use a custom GPT with specific style guidelines
- **Learning new APIs**: Ask for explanations and examples
- **Pair programming**: Describe what you want; iterate on the code together

### Research Workflow

1. Upload papers as PDFs
2. Ask for summaries and key findings
3. Compare claims across papers
4. Identify gaps or contradictions
5. Generate literature review drafts

### Content Creation

- Brainstorming with the model
- Getting feedback on drafts
- Repurposing content for different formats
- Creating outlines and structures

## The Broader LLM Ecosystem

Beyond ChatGPT, Karpathy discusses:
- **Claude** (Anthropic) — strong for long-form writing and analysis
- **Gemini** (Google) — integrated with search and Google products
- **Grok** (xAI/Elon Musk) — more opinionated, real-time knowledge via X
- **DeepSeek** — open-source models gaining popularity
- **Llama** (Meta) — open weights, can run locally

## Key Concepts

- [[prompting]] — The art of communicating with LLMs
- [[chain-of-thought]] — Eliciting step-by-step reasoning
- [[custom-gpts]] — No-code custom assistants
- [[multimodal]] — Beyond text: images, files, PDFs
- [[context-window]] — The working memory constraint
- [[reasoning-models]] — Specialized for deep reasoning (o1/o3)
- [[Andrej Karpathy]] — The presenter
- [[Deep Dive into LLMs]] — Technical deep dive on training

## Related Entities
- [[Andrej Karpathy]]
- [[Deep Dive into LLMs]]
- [[ChatGPT]]
- [[GPT]]

## Source
[[raw/transcripts/EWvNQjAaOHw]]
