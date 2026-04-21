---
title: "FineWeb"
created: 2026-04-21
updated: 2026-04-21
type: entity
tags: [dataset, pre-training]
sources: []
---

# FineWeb

## Summary
FineWeb is the high-quality pre-training dataset used by Karpathy as the reference dataset in his "Deep Dive into LLMs" video. It is derived from Common Crawl (~2.7B pages as of 2024) and经过了严格的URL过滤、语言识别 (>65% English)、去重和PII移除，最终达到约44TB、15万亿token的高质量文本。

## Key Facts
- Source: Common Crawl
- Size: ~44TB / ~15 trillion tokens (after filtering)
- Filtering steps: URL过滤 → 文本提取 → 语言过滤 → 去重 → PII移除

## Related Entities
- [[entities/Deep Dive into LLMs like ChatGPT [7xTGNNLPyMI].en.md]] — FineWeb as pre-training dataset
- [[Common Crawl]] — Original data source
- [[Hugging Face]] — Dataset hosting
