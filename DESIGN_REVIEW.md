# Website review and revision — 23 October 2026

Public site: https://pujiayue.github.io/Trustworthy-RSI/

## Latest revision: light interface

The user subsequently requested a light background. This revision supersedes the midnight palette described in the earlier review below.

- Warm off-white canvas, soft blue section backgrounds, and dark navy typography.
- Sage, sand, lavender, and blue module cards with stronger action labels and quieter borders.
- Blue primary actions and a gold saved state; the literature workspace has its own light-blue toolbar and white result cards.
- Refined figure frames, rounded controls, spacing, and application-context cards. Original figure colors and crop remain intact.
- Mobile and desktop visual checks include the homepage, theme cards, library toolbar, search, and saved state. No horizontal overflow at the tested 390-pixel mobile viewport; no browser warnings or errors observed.
- Scientific wording, bibliography data, and application logic remain unchanged.
- Stylesheet URL includes a version marker to avoid retaining the previous dark theme in cache.

The remainder records the earlier content/functionality review and its design references.

## Reference study

The review examined current academic project pages and their public HTML/CSS. The following ideas informed this revision; the midnight palette is a choice for this project, not a claim that these references use dark themes.

| Reference | Patterns studied | Applied here |
| --- | --- | --- |
| [World Model Benchmarks survey](https://world-model-benchmarks.github.io/) (2026) | Taxonomy connected to an explorable collection; filtering and export | Prominent literature tools, chapter entry points, filtered BibTeX export |
| [Data for Coding Agents survey](https://linjh1118.github.io/coding-agent-data/) (2026) | Section-level reading routes, figure viewing and source links | Four module entrances, manuscript section notes, full-size figures and original PDF access |
| [Long-Horizon Agents](https://long-horizon-agents.github.io/) | Strong resource hierarchy, typographic contrast, section narratives | Larger headings, clear primary action, consistent section hierarchy and navigation |

## Findings and changes

| Issue identified | Implemented change |
| --- | --- |
| Light backgrounds and similar-looking sections weakened hierarchy. | Midnight canvas with navy panels; teal, amber, blue, and violet distinguish functional modules. Scientific figures retain their original colors. |
| The page required too much scrolling to discover what it offered. | Four colored entrances immediately after the abstract: RSI Process, Risks & Safeguards, Evidence & Claims, Literature Explorer. |
| Library functions were less prominent than explanatory text. | Dedicated All/Saved controls, search/year/sort bar, active filter chips, share action, and result-counted export. |
| Reading progress and current position were unclear. | Sticky navigation with active section, reading progress, and back-to-top. The framework figure maps to RSI Process in navigation. |
| Chapter filters consumed excessive mobile space. | Collapsible chapter drawer, closed initially on narrow screens. |
| Readers could not keep or export a focused reading list. | Browser-local saved records, filtered/saved BibTeX export, and filter URLs restored on reload. Shared links do not transmit the local reading list. |
| Very long author and placement metadata obscured scanning. | Compact card with expandable full reference details and clickable chapter tags. |
| Condensed labels could be mistaken for manuscript headings or process stages. | Formal chapter titles retained; §2, §7, and §8 subsection labels aligned with the supplied current manuscript. Three analytical roles are explicitly distinguished from S1–S4/RI. |
| A successful update could be mistaken for proof of trustworthy RSI. | Explicit evidence-scope panel; separate update, successor, and meta-improvement requirements. |
| Counts could imply deduplicated papers or direct RSI validation. | “Bibliography records” used consistently: 413 total, 263 classified. Alternate records and overlapping chapters are disclosed. Placement is not an evidence rating. |

## Manuscript alignment

The source of scientific wording is the supplied survey LaTeX, not the reference websites. Active manuscript sections were used; commented historical drafts were excluded.

- **§1 / §2.3:** improvement validity, constraint preservation, and effective oversight describe analytical roles.
- **§2.1–2.2:** policy `h`, inductive bias `B`, bias update function `U`; diagnosis, proposal generation, proposal evaluation, implementation, and recursive revision of `U`. The coding-agent example follows the manuscript.
- **§3–6:** formal trustworthiness themes and their distinct scopes are preserved.
- **§7:** update validity, preservation in successors, and meta-improvement require different evidence. Paired continuations use common initial state and matched budgets; revised checks and controls also require reassessment.
- **§8.2–8.3:** editable surface, feedback control, consequences of commitment, and the seven future-direction headings are retained in condensed web form.
- The supplied visual abstract remains the first figure. The organizing framework uses a whitespace-trimmed display crop in both the page and zoom view; the original PDF remains available.

All 413 bibliographic records and taxonomy memberships are unchanged in this revision. Only selected display headings changed. No automatic deduplication, invented author list, publication status, or evidence scores were added.

## Validation

- 22 DOM behavioral checks pass: combined filters, URL restoration, persistence, empty states, exact export membership, pagination, bounds, escaped input, internal anchors, and process keyboard navigation.
- Actual browser tests: title search; save, reload, and unsave; copied filter URL; real BibTeX download; mobile chapter/subsection filtering; menu; figure zoom.
- Browser-downloaded export contains exactly the two filtered records, including their complete supplied BibTeX.
- Desktop and 390-pixel mobile viewport reviewed. No horizontal overflow at the tested mobile width. Narrow-screen chapter drawer starts collapsed.
- No browser errors or warnings observed during the tested interactions.
- Data comparison confirms all original bibliography contents and taxonomy membership arrays are preserved.

Run the behavioral checks with `npm --prefix tests ci` followed by `npm --prefix tests test`. Tests use jsdom; this is not a substitute for the browser visual checks above.

## Remaining limits

- Saved references are local to a browser and do not sync between devices. Export provides a portable copy.
- Bibliography metadata is inherited from the supplied sources. This design revision does not independently verify every paper or establish the evidential status of each citation.
- Website summaries condense the manuscript. The supplied original figures and bibliography remain the authoritative downloadable artifacts here.
- Manual visual checks cover the tested desktop and mobile widths; this is not an exhaustive assistive-technology or cross-browser audit.
