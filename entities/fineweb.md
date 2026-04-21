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
FineWeb is the high-quality pre-training dataset used by Karpathy as the reference dataset in his "Deep Dive into LLMs" video. Derived from Common Crawl (~2.7B pages as of 2024), it undergoes aggressive filtering: URL filtering, language detection (>65% English), deduplication, and PII removal — resulting in ~44TB of high-quality text, approximately 15 trillion tokens.

## Key Facts
- Source: Common Crawl (~2.7B pages as of 2024)
- Size: ~44TB / ~15 trillion tokens (after filtering)
- Filtering steps: URL filtering → text extraction → language filtering → deduplication → PII removal

## Related Entities
- [[deep-dive-into-llms-7xTGNNLPyMI]] — FineWeb as pre-training dataset
