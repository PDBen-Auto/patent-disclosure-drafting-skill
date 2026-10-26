# Detailed Workflow

## 1. Drafting brief

Start with a compact status block:

```text
Working title:
Jurisdiction:
Route: design / utility model / utility patent / combined
Evidence cutoff:
Audience: inventor / designer / patent agent / public reader
Status: draft for review
```

Use a neutral working title. If the source title is sensitive, create a private alias and keep the mapping outside the public package.

## 2. Evidence ledger

Use one row per material statement:

| ID | Statement | Source | Status | Confidence | Follow-up |
| --- | --- | --- | --- | --- | --- |
| E-01 | A front frame surrounds the optical module | Photo set A, view 2 | observed | high | Confirm rear attachment |
| E-02 | The frame is injection molded | Inventor note | inventor-provided | medium | Request process evidence |
| E-03 | The recess improves glare control | Draft interpretation | proposed wording | low | Request test or explanation |

Never promote a proposed wording row into an observed fact without a source.

## 3. Route split

### Design route

Capture the overall visual impression, visible contours, proportions, transitions, surface breaks, ornamentation, and view coverage. Avoid functional claim language. If broken-line or environmental portions are proposed, mark them as a drafting decision for agent review.

### Utility route

Capture the problem, technical solution, parts, connections, operation, alternatives, manufacturing/assembly options, and technical effects. Use relationship language such as `coupled to`, `positioned within`, `supported by`, `adjustable relative to`, and `configured to` only when evidence supports it.

## 4. Component normalization

Create the component table before drafting prose:

| Numeral | Preferred name | Source synonyms | Subassembly | Connection | Figure coverage | Status |
| --- | --- | --- | --- | --- | --- | --- |
| 10 | base frame | outer frame, support ring | 100 | joined to 20 | Fig. 1-6 | observed |
| 20 | insert module | lamp cartridge | 100 | retained in 10 | Fig. 2-5 | observed |

Do not reuse a numeral for two physical meanings. If a component has variants, keep the numeral stable and add a variant suffix in prose rather than silently renumbering.

## 5. Figure register

The register should explain why each figure exists:

| Figure | View | Purpose | Source | Included parts | Missing/unclear |
| --- | --- | --- | --- | --- | --- |
| Fig. 1 | perspective | overall appearance | render-01 | 10, 20, 30 | underside not shown |
| Fig. 2 | exploded perspective | connection order | sketch-02 | 10, 20, 40 | fastener detail unknown |

Keep view names stable. A perspective render is not a substitute for a required side or rear view when the side/rear silhouette affects the design route.

## 6. Drafting order

Draft in this order:

1. title and status block;
2. problem and intended effect;
3. short solution summary;
4. component and connection table;
5. detailed embodiments and alternatives;
6. operating sequence;
7. manufacture/assembly options;
8. appearance disclosure and view notes;
9. figure register and numeral table;
10. protection-focus prompts and open questions.

This order prevents a polished claim-like paragraph from outrunning the evidence table.

## 7. Consistency review

Check that:

- every numeral in prose exists in the table;
- every table numeral appears in at least one figure or is explicitly text-only;
- each figure uses one meaning for each numeral;
- the route section does not turn a functional feature into an ornamental conclusion;
- optional embodiments are labeled optional;
- dimensions, materials, tests, priority dates, and inventorship are sourced or marked unknown;
- the public case contains no source-project fingerprints.

## 8. Agent handoff

End with questions, not a legal conclusion:

- Which jurisdiction and filing route will be used?
- Which features are intended to be essential, and which are optional?
- Are the views complete and consistent with the proposed line treatment?
- What evidence supports each technical effect?
- What are the true inventors, applicant, ownership chain, and earliest disclosure date?
- What prior-art and formal drawing review is required before filing?
