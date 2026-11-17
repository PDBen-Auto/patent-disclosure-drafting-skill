# Patent disclosure drafting

`patent-disclosure-drafting` · English

## Purpose and scope

Turn authorized product evidence into separate technical and appearance disclosures, stable figure numbering and a professional handoff draft.

## Implementation Basis and Dependencies

Readable product text/visuals and an Agent Skills host. Filing-specific output needs jurisdiction and route; document tools are conditional on requested formats. Professional patent review is required before filing.

## Inputs

Product identity, components, relationships, operation, figures and evidence; conditional jurisdiction/design/utility route. Optional variants and requested outputs. Release mode defaults to private; public examples require synthetic replacement or authorized redaction review.

## Outputs

Status cover, invention summary, technical/appearance disclosures, figure and reference-numeral tables, provisional protection-focus notes, open questions and agent checklist. Missing sections are explicitly labeled.

## Workflow

1. Set route, jurisdiction and audience.
2. Record evidence and normalize terms.
3. Separate appearance from technical structure.
4. Assign stable component and figure numbers.
5. Draft connections, operation, alternatives and supported effects.
6. Check view consistency and unsupported precision.
7. For public-synthetic mode construct a fresh fictional case.
8. Freeze the handoff for professional review.

## Boundaries and stopping conditions

Do not invent novelty, ownership, inventorship, priority, hidden geometry or legal status. No enforceable claim or filing guarantee. Stop affected drafting on unreadable figures, conflicting facts or unknown filing jurisdiction; filing/publication requires separate permission.

## Example request

Use `$patent-disclosure-drafting` — Convert a fictional adjustable holder's component notes and views into separate appearance/technical drafts and a numbered figure register for a patent professional; respond in English and preserve evidence, unknowns and action boundaries.

## Complete specification

[Skill entrypoint and detailed references](../../SKILL.md).

Use the user's explicitly requested output language; otherwise follow the request language. Keep commands, skill IDs, JSON keys, enum values, units and source quotations unchanged. Separate translations from originals. Never infer country, currency or jurisdiction from language. Read the relevant detailed references in the complete specification and retain all existing validation and authorization gates.

Before delivery reconcile inputs, evidence, missing values, files and the original completion criteria. Mark unexecuted steps unverified; a successful script exit is not business validation.

## Language coverage and validation

This localized operating guide covers purpose, prerequisites, inputs, outputs, workflow, examples and boundaries; it is not a line-by-line translation of every reference. Detailed technical references, historical cases, script errors, example interfaces and images retain their original language. The assistant can explain them in the requested language. Structural, link and key-constraint checks are performed; native-speaker editorial review for each language is not claimed.

