# Research \ Anthropic

---
title: "Anthropic Research"
created: 2026-04-25
type: entity
tags: [anthropic, ai-safety, interpretability, alignment, research-org]
related: [[Anthropic]], [[Claude]], [[AI Alignment]], [[Mechanistic Interpretability]], [[Constitutional AI]]
sources: [raw/articles/www-anthropic-com-research.md]
---

# Anthropic Research

## Summary
Anthropic Research is the umbrella for the technical research programs at Anthropic, an AI safety company best known for the Claude family of large language models. The research mission is framed around ensuring that as AI becomes increasingly capable, it has a positive impact on society — pursued through work on safety, model internals, alignment, and societal effects. The research portfolio is organized into several distinct teams: Alignment, Interpretability, Societal Impacts, Economic Research, the Frontier Red Team, and Policy-adjacent research.

The work spans mechanistic investigation of LLM internals (e.g., studying how "emotion concepts" function inside models), alignment engineering (e.g., Constitutional Classifiers to defend against universal jailbreaks), large-scale empirical studies of AI use (the Anthropic Economic Index, the 81,000-person qualitative user study), and open-ended agentic experiments (Project Vend, Project Deal). The Frontier Red Team specifically analyzes implications of frontier models for cybersecurity, biosecurity, and autonomous systems.

Recent flagship outputs include Constitutional Classifiers (Feb 2025) — a filtering system that withstood over 3,000 hours of red-teaming with no universal jailbreak discovered — Project Vend (an AI shopkeeper experiment in Anthropic's SF lunchroom), Project Deal (a Claude-run employee negotiation marketplace, Apr 2026), Automated Alignment Researchers (scaling scalable oversight with LLMs), and a Science Blog introducing work like "Long-running Claude for scientific computing" and "Vibe physics: The AI grad student."

## Key Concepts

- **Interpretability Team**: Team whose mission is to discover and understand how large language models work internally as a foundation for AI safety. Work includes investigating whether emergent behaviors like emotion-like responses correspond to internal "emotion concepts" with functional roles in model computation.

- **Alignment Team**: Team focused on understanding risks of AI models and ensuring future models remain helpful, honest, and harmless (the HHH framing). Produces work like Constitutional Classifiers and Automated Alignment Researchers.

- **Societal Impacts Team**: Technical research team working alongside Anthropic's Policy and Safeguards teams to study how AI is used in the real world. Ran the 81,000-person qualitative user survey — the largest and most multilingual qualitative study of its kind — asking Claude.ai users how they use AI, what they hope for, and what they fear.

- **Frontier Red Team**: Internal red-teaming group analyzing implications of frontier AI models for cybersecurity, biosecurity, and autonomous systems — i.e., catastrophic-risk–adjacent capabilities.

- **Economic Research / Anthropic Economic Index**: Ongoing program measuring how AI is used economically and by whom. Outputs include country-level reports (e.g., "How Australia Uses Claude"), the "Learning curves" report, and the Anthropic Economic Index Survey. Related qualitative output: "What 81,000 people told us about the economics of AI."

- **Constitutional Classifiers**: A safety system (Feb 2025) that filters the overwhelming majority of jailbreak attempts while remaining practically deployable. A prototype withstood over 3,000 hours of red teaming without a universal jailbreak being found, representing a concrete defense-in-depth layer atop base-model alignment.

- **Project Vend**: Free-form experiment exploring how well AIs perform on complex real-world tasks by having Claude run a small shop in Anthropic's SF lunchroom. Phase two (Dec 2025) reported on how the AI shopkeeper's business evolved over time.

- **Project Deal**: Announced Apr 24, 2026. A marketplace inside Anthropic's SF office where Claude buys, sells, and negotiates on employees' behalf — a study of agentic Claude in a multi-agent economic environment.

- **Automated Alignment Researchers**: Research direction (Apr 14, 2026) using LLMs to scale scalable oversight — i.e., using AI systems themselves to help perform alignment research tasks that humans cannot supervise at scale.

- **Science Blog / Long-running Claude**: Launched Mar 23, 2026. Covers scientific applications including "Long-running Claude for scientific computing" and "Vibe physics: The AI grad student," investigating sustained agentic Claude deployments in scientific workflows.

- **Trustworthy Agents**: Policy-oriented research thread (Apr 9, 2026) addressing practical requirements for deploying trustworthy AI agents in real applications.

## Key Takeaways
- Anthropic organizes research into Alignment, Interpretability, Societal Impacts, Economic Research, Frontier Red Team, and Policy-adjacent groups.
- The Frontier Red Team explicitly scopes cybersecurity, biosecurity, and autonomous systems as the core frontier-risk domains.
- Constitutional Classifiers are the flagship deployed defense against jailbreaks, having resisted 3,000+ hours of red-teaming with no universal jailbreak discovered on the prototype.
- The 81,000-person Claude.ai study is claimed as the largest and most multilingual qualitative study of AI use.
- Project Vend and Project Deal represent Anthropic's strategy of testing agentic Claude in naturalistic, economically meaningful environments (running a shop; negotiating a marketplace).
- Automated Alignment Researchers embody the scalable oversight agenda — using LLMs to do alignment research on other LLMs.
- The Anthropic Economic Index produces both quantitative reports (e.g., "Learning curves," Australia report) and qualitative survey data on AI's economic role.
- A dedicated Science Blog (Mar 2026) signals a push into AI-for-science, including long-horizon scientific computing agents.

## Notable Quotes
> "The mission of the Interpretability team is to discover and understand how large language models work internally, as a foundation for AI safety and positive outcomes."
> "The Alignment team works to understand the risks of AI models and develop ways to ensure that future ones remain helpful, honest, and harmless."
> "A prototype withstood over 3,000 hours of red teaming with no universal jailbreak discovered."
> "Nearly 81,000 people participated—the largest and most multilingual qualitative study of its kind."

## Related Entities
[[Anthropic]], [[Claude]], [[Constitutional AI]], [[Constitutional Classifiers]], [[Mechanistic Interpretability]], [[AI Alignment]], [[Scalable Oversight]], [[Project Vend]], [[Anthropic Economic Index]], [[Frontier Red Team]]