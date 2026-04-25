# Research \ Anthropic

---
title: "Anthropic Research"
created: 2026-04-25
type: entity
tags: [anthropic, ai-safety, interpretability, alignment, ai-research]
related: [[Anthropic]], [[Claude]], [[AI Alignment]], [[Mechanistic Interpretability]], [[AI Safety]]
sources: [raw/articles/www-anthropic-com-research.md]
---

# Anthropic Research

## Summary
Anthropic Research is the organization's collective research effort investigating the safety, inner workings, and societal impacts of large language models, with the stated goal of ensuring AI has a positive impact as capabilities scale. The research program is structured across several teams—Alignment, Interpretability, Societal Impacts, Economic Research, and the Frontier Red Team—each addressing a distinct facet of AI risk and understanding. Much of the work centers on Claude, Anthropic's flagship model family, which serves both as the research subject and as a tool deployed in experimental settings.

Notable recent outputs include Project Vend (an experiment where Claude ran a small shop in Anthropic's SF lunchroom) and its follow-up Project Deal (an employee marketplace where Claude negotiated on behalf of colleagues), interpretability work on emotion concepts inside language models, the Anthropic Economic Index (including a survey of 81,000 Claude.ai users about AI use and economics), and Constitutional Classifiers—a defense against universal jailbreaks that withstood over 3,000 hours of red-teaming without a universal bypass being found. The Frontier Red Team specifically analyzes implications of frontier models for cybersecurity, biosecurity, and autonomous systems.

Research areas span mechanistic interpretability of model internals, scalable oversight via automated alignment researchers, trustworthy agents in deployment, scientific computing applications ("Long-running Claude for scientific computing," "Vibe physics"), and large-scale qualitative studies of real-world AI use.

## Key Concepts
- **Interpretability Team**: Dedicated to discovering and understanding how large language models work internally as a foundation for AI safety. Recent work includes investigating emotion concepts and their function inside Claude, treating observed emotion-like behaviors as a mechanistic phenomenon rather than surface behavior.

- **Alignment Team**: Studies risks of current AI models and develops methods to keep future models helpful, honest, and harmless. Outputs include work on Constitutional Classifiers and "Automated Alignment Researchers"—using LLMs themselves to scale scalable oversight.

- **Societal Impacts Team**: A technical research team, working with Anthropic's Policy and Safeguards teams, that studies real-world AI use. Ran the "What 81,000 people want from AI" study—described as the largest and most multilingual qualitative study of its kind—inviting Claude.ai users to share use cases, aspirations, and fears.

- **Frontier Red Team**: Analyzes implications of frontier AI models across three high-stakes domains: cybersecurity, biosecurity, and autonomous systems. Focus is on capabilities with catastrophic misuse potential.

- **Economic Research / Anthropic Economic Index**: Program tracking how AI is affecting work and the economy. Publications include "Learning curves," country-specific reports (e.g., "How Australia Uses Claude"), and the Economic Index Survey of 81,000 users on the economics of AI.

- **Project Vend**: Free-form experiment where Claude operated a small shop in Anthropic's SF office lunchroom, exploring how well AI handles complex, real-world commercial tasks. Phase two (Dec 2025) reported on continued operation.

- **Project Deal (Apr 2026)**: Sequel to Project Vend. Anthropic built a marketplace for SF office employees where Claude handled buying, selling, and negotiating on colleagues' behalf—a test bed for agentic economic behavior.

- **Constitutional Classifiers**: Defense mechanism against universal jailbreaks, announced Feb 2025. Filters the overwhelming majority of jailbreaks while remaining deployable in practice; a prototype withstood over 3,000 hours of red-teaming with no universal jailbreak discovered.

- **Automated Alignment Researchers**: Research direction using LLMs to perform alignment research at scale, aimed at realizing scalable oversight of models potentially more capable than humans.

- **Trustworthy Agents in Practice**: Applied alignment/safety work on making deployed AI agents reliable and safe in real production settings (Apr 2026 publication).

- **Science Blog / Scientific Computing**: Launched March 2026, covering applications like "Long-running Claude for scientific computing" and "Vibe physics: The AI grad student," exploring Claude's role in extended scientific reasoning and computation tasks.

## Key Takeaways
- Anthropic's research is organized into four public-facing teams: Alignment, Interpretability, Societal Impacts, and Economic Research, plus the Frontier Red Team for catastrophic-risk domains.
- Constitutional Classifiers withstood 3,000+ hours of red-teaming with no universal jailbreak found—a notable empirical robustness result for jailbreak defense.
- The "What 81,000 people want from AI" study is positioned as the largest multilingual qualitative study of AI use to date.
- Anthropic uses Claude itself as both research subject (interpretability, alignment) and research tool (automated alignment researchers, scientific computing, agentic commerce via Project Vend/Deal).
- Frontier Red Team explicitly scopes three catastrophic-risk domains: cybersecurity, biosecurity, and autonomous systems.
- The Anthropic Economic Index produces recurring reports including country-specific analyses and "Learning curves" on AI adoption.
- Interpretability work has moved into studying internal representations of emotion-like concepts in LLMs.

## Notable Quotes
> "The mission of the Interpretability team is to discover and understand how large language models work internally, as a foundation for AI safety and positive outcomes."

> "A prototype withstood over 3,000 hours of red teaming with no universal jailbreak discovered."

> "Nearly 81,000 people participated—the largest and most multilingual qualitative study of its kind."

## Related Entities
[[Anthropic]], [[Claude]], [[AI Alignment]], [[Mechanistic Interpretability]], [[Constitutional AI]], [[Project Vend]], [[Frontier Red Team]], [[Anthropic Economic Index]], [[Scalable Oversight]], [[Jailbreak Defense]]