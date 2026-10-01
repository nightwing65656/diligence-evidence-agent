# diligence-evidence-agent

An Analyst-Controlled AI system that turns public filings and approved diligence materials into a cited, calculation-backed investment memo with a full audit trail.

## Why this exists
Institutional diligence work requires:
- evidence-linked claims
- reproducible calculations
- contradiction detection
- human approval before output is treated as reviewed

## Current scope
This public prototype uses:
- SEC EDGAR submissions and company facts APIs
- public filings and investor materials
- deterministic tests and offline fixtures

## Out of scope
- autonomous investment decisions
- trade execution
- use of material non-public information
- client-confidential documents in the public repo

## Standards
Release is blocked unless the project meets:
- 100% evidence integrity
- 100% calculation reproducibility
- 100% seeded prompt-injection / permission-bypass blocking
- 0 unsupported claims shipped as verified
- >=98% citation precision on the frozen set
- >=98% extraction exactness on structured filing facts
- <=2% wrong-but-confident rate

## Planned architecture
Planner -> Ingestion -> Evidence Index -> Financial / Risk / Challenge Agents -> Verification -> Memo Draft -> Human Review

## Status
Phase 0: repository and governance scaffolding