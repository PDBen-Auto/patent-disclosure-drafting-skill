<!-- skill-i18n:start -->
[简体中文](README.zh-CN.md) | [English](README.en.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Português](README.pt.md)

### Complete specification

- [Patent disclosure drafting](references/i18n/en.md) · `patent-disclosure-drafting`

Use the user's explicitly requested output language; otherwise follow the request language. Keep commands, skill IDs, JSON keys, enum values, units and source quotations unchanged. Separate translations from originals. Never infer country, currency or jurisdiction from language. Read the relevant detailed references in the complete specification and retain all existing validation and authorization gates.

This localized operating guide covers purpose, prerequisites, inputs, outputs, workflow, examples and boundaries; it is not a line-by-line translation of every reference. Detailed technical references, historical cases, script errors, example interfaces and images retain their original language. The assistant can explain them in the requested language. Structural, link and key-constraint checks are performed; native-speaker editorial review for each language is not claimed.
<!-- skill-i18n:end -->

# Patent Disclosure Drafting Skill

Turn product briefs, sketches, photos, CAD views, and inventor notes into an auditable patent disclosure package for patent-agent review.

The Skill separates design disclosure from utility-model or utility-patent technical disclosure, tracks evidence status, normalizes components and reference numerals, checks figure consistency, and creates a synthetic public case when the source project is confidential.

It is not legal advice, a patentability opinion, an FTO opinion, a filing service, or a grant guarantee. A qualified patent agent or attorney must review the package before filing.

Install:

```bash
npx skills add PDBen-Auto/patent-disclosure-drafting-skill --skill patent-disclosure-drafting
```

See [README.md](README.md) for the Chinese workflow, examples, output contract, and release boundaries.
