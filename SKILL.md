---
name: patent-disclosure-drafting
description: Turn a physical-product brief, sketches, photos, CAD views, or slide notes into a structured patent disclosure package for design and utility-model/utility-patent review. Use when the user asks to draft a patent technical disclosure, prepare figure lists and reference numerals, separate appearance and structural protection routes, or hand a concept to a patent agent. Do not use as legal advice, a filing guarantee, or a substitute for patent counsel.
---

# Patent Disclosure Drafting

Convert incomplete product evidence into an auditable, agent-ready patent disclosure package. Keep observed facts, inventor explanations, assumptions, and drafting proposals separate so a patent agent can review the package without mistaking a concept for an established legal conclusion.

## When To Use

Use this skill for:

- an external design patent or registered-design disclosure draft;
- a utility-model or utility-patent technical disclosure draft;
- a combined appearance-plus-structure invention intake;
- a figure inventory, reference-numeral table, or view-consistency review;
- a redacted public case study derived from an internal drafting workflow.

Do not use it for a formal patentability opinion, freedom-to-operate opinion, infringement conclusion, final claim construction, or unattended filing. Route those requests to qualified patent counsel.

## Operating Principles

1. **Preserve evidence status.** Label each material statement as `observed`, `inventor-provided`, `inferred`, `proposed wording`, or `unknown`.
2. **Split protection routes early.** Treat ornamental appearance and technical structure as separate workstreams even when they describe one product.
3. **Draft from relationships.** For structural disclosures, explain parts, connections, relative positions, operation, and the technical effect. For appearance disclosures, explain the overall visual impression and the complete view set.
4. **Do not invent precision.** Missing dimensions, materials, tolerances, test data, ownership, dates, or inventor information remain `unknown` until supplied.
5. **Keep drawings coherent.** Every reference numeral must map to one stable component meaning across every figure and text section.
6. **Make review boundaries visible.** Mark the package as a draft for agent review and list unresolved questions before any filing decision.

## Implementation Basis And Dependencies

The workflow relies on structured intake, document parsing, image/CAD inspection, figure-numbering discipline, and a jurisdiction-aware patent-agent review. It can work with text-only input, but appearance conclusions require usable product views and structural conclusions require enough evidence to describe connections and operation.

| Dependency | Why needed | Required | Validation | Fallback |
| --- | --- | --- | --- | --- |
| Product brief or inventor interview | Establish intended problem, solution, and variants | Yes | Confirm product identity and intended use | Return an intake questionnaire and do not draft claims as facts |
| Figures, photos, sketches, or CAD views | Support appearance scope and component mapping | Conditional by deliverable | Check readability, view labels, and whether key surfaces/connections are visible | Produce text-only draft with missing-view warnings |
| Requested jurisdiction and route | Terminology and disclosure depth vary by jurisdiction | Yes for filing-oriented output | Record country/region and whether design, utility model, or utility patent is requested | Use neutral technical-disclosure language and mark local review required |
| Document/PDF/image tools | Read source files and inspect visual evidence | Optional by source type | Verify the tool or local parser is available | Ask for text or export a simplified evidence set |
| Patent agent or attorney review | Validate formal sufficiency, novelty strategy, claims, and filing compliance | Required before filing | Identify named reviewer or record `not yet assigned` | Deliver only a review-ready draft, never a filing-ready guarantee |
| Public-release authorization | Needed for any redacted case or repository publication | Required for public case | Confirm the user authorized publication of the sanitized package | Keep the case local and remove public-release sections |

## Inputs

| Input | Purpose | Requirement and format | Validation and missing-input behavior | Sensitivity |
| --- | --- | --- | --- | --- |
| `product_identity` | Names the object being documented | Required; neutral working name, product category, intended use | Replace brand or confidential name with a project alias in public examples | May contain trade secrets |
| `problem_and_effect` | Connects the problem to the proposed technical solution | Required; prose or interview notes | Separate measured effect from hoped-for effect; unknowns stay open | May disclose roadmap or customer pain |
| `component_and_connection_data` | Supports structural disclosure | Required for utility route; table, notes, CAD labels, or photos | Normalize each part and connection; flag contradictions instead of choosing silently | Often confidential |
| `appearance_evidence` | Supports design route | Conditional; clean views, sketches, photos, or CAD renders | Inventory perspective, front, rear, top, bottom, side, and detail views; mark missing views | May include unpublished design |
| `variants_and_alternatives` | Preserves fallback embodiments | Optional but recommended; list of variants and optional features | Distinguish tested alternatives from hypothetical variants | May reveal future products |
| `jurisdiction_and_route` | Controls terminology and review questions | Required for filing-oriented output; country/region plus design, utility model, or utility patent | Do not infer jurisdiction from language | Legal/commercial scope |
| `requested_outputs` | Selects the package | Required; one or more output types below | Default to both route summaries, an evidence table, figure list, and open questions | User preference |
| `public_release_mode` | Controls sanitization | Optional; `private`, `internal`, or `public-synthetic` | Default to `private`; public mode requires a fresh synthetic case or explicit redaction review | Publication authorization |

## Outputs

Every complete run should produce the applicable items below and label anything not produced.

1. **Draft cover and status block**: working title, route, jurisdiction, version, evidence cutoff, authoring status, and review boundary.
2. **Invention summary**: problem, solution, main effect, use context, and evidence status for each statement.
3. **Technical disclosure**: components, reference numerals, connections, operating sequence, alternatives, manufacturing notes, and technical effects.
4. **Appearance disclosure**: product name, ornamental subject, view inventory, visible features, omitted/environmental portions, and consistency notes.
5. **Figure register**: `Fig. 1` onward, view type, purpose, source file, included parts, and missing/unclear regions.
6. **Reference-numeral table**: one stable numeral per component or subassembly, with synonyms and figure coverage.
7. **Protection-focus draft**: non-final drafting prompts for the agent, including essential relationships, optional features, and variants. Never present it as an enforceable claim.
8. **Open-question register**: missing facts, conflicts, tests, ownership, dates, inventorship, and jurisdiction decisions.
9. **Agent handoff checklist**: records to verify before filing, including prior-art strategy, drawings, signatures, translations, and formal requirements.
10. **Public synthetic case** when requested: a fully fictional example with a redaction audit and no source-project identifiers.

### Output Acceptance Criteria

- Every material conclusion is traceable to an input, an inference, or a proposal.
- Figure labels and reference numerals are consistent across text and tables.
- Design and utility routes are clearly separated.
- Unknown or conflicting facts are visible and never silently filled.
- The final artifact states that a patent agent or attorney must review it before filing.
- Public mode contains no original names, files, dimensions, images, identifiers, credentials, or confidential strategy.

## Workflow

1. **Set the drafting boundary.** Record the working title, jurisdiction, route, intended audience, date, and whether this is private, internal, or public-synthetic.
2. **Ingest and classify evidence.** Build an evidence ledger. Preserve source wording, then create a normalized product vocabulary. Label facts, assumptions, and proposals.
3. **Separate the routes.** Decide whether the package needs design, utility model, utility patent, or multiple route sections. Do not merge appearance language with structural claim logic.
4. **Normalize the structure.** Create a component table with stable numerals, connection verbs, relative positions, operation, and technical effects. Resolve synonyms without erasing the original term.
5. **Inventory the figures.** Number figures by view purpose, map each to a source, identify missing views, and flag perspective or geometry conflicts.
6. **Draft the technical disclosure.** Write the problem, solution, embodiments, alternatives, operation, manufacture/assembly options, and effect. Keep optional features explicitly optional.
7. **Draft the appearance disclosure.** Describe the overall visual impression and visible relationships, not a list of functional features. State which surfaces are shown, omitted, broken-line, or environmental only when the evidence supports it.
8. **Prepare agent prompts.** Convert the evidence into review questions and non-final protection-focus notes. Do not fabricate claims, novelty, priority, inventorship, or legal status.
9. **Run consistency checks.** Verify numeral uniqueness, figure coverage, terminology, route separation, unresolved questions, and unsupported precision.
10. **Run the public-release gate.** If `public-synthetic`, replace the project with a new fictional case, scan for identifiers and source fingerprints, and include only sanitized teaching material.
11. **Freeze the handoff.** Produce the requested files, a change/status block, and the agent review checklist. Filing or external publication is a separate authorized action.

Read [references/workflow.md](references/workflow.md) for the detailed procedure, [references/intake-and-output-contract.md](references/intake-and-output-contract.md) for schemas, [references/figure-numbering.md](references/figure-numbering.md) for drawing rules, and [references/anonymization.md](references/anonymization.md) for public cases.

## Risk And Evidence Rules

- A technical disclosure is not a patent application and does not establish novelty, inventive step, validity, or infringement status.
- Do not describe a feature as essential unless the source evidence and the requested route support that conclusion; offer it as a review question when uncertain.
- Do not infer hidden geometry, tolerances, load capacity, test results, or manufacturing feasibility from a single image.
- Do not copy a real confidential project into a public example. Use a fresh synthetic product and fresh wording.
- Do not publish original CAD, slides, drawings, filenames, identifiers, customer data, supplier data, or personal information.
- Generated or redrawn figures are illustrative unless a qualified professional verifies them for filing.
- Preserve the user's original files in place; work from copies or extracted notes when preparing a public package.

## Stopping Conditions

Stop or return a limited package when:

- the product cannot be uniquely identified;
- the requested route or jurisdiction is unknown and the user expects filing-specific language;
- the figures are unreadable or key connections are hidden;
- source facts conflict and no authorized decision resolves the conflict;
- the user requests a legal guarantee, a final filing, or an infringement conclusion;
- public release is requested without authorization to sanitize or replace the source case.

When stopping, preserve the evidence ledger and state the exact missing input or review step.

## Example Trigger Patterns

Activate for:

- “把这个产品整理成外观设计和实用新型技术交底书。”
- “根据图片和结构说明生成专利附图编号表、部件编号和代理师交接清单。”
- “把内部专利起草案例脱敏成一个可公开的合成案例。”

Do not activate for:

- “帮我查某专利是否侵权” without a drafting request;
- a generic market-sizing report;
- a request to file or sign a patent without professional review;
- a request to reproduce a confidential project or publish its original files.

## Definition Of Done

The run is complete when the requested disclosure sections, figure register, numeral table, open questions, review boundary, and—when applicable—public-release audit are present, internally consistent, and marked as draft material for agent review. Validate the package with the included tests before release.
