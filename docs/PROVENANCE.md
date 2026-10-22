# Repository Provenance

## Literature sources

The initial catalog was prepared from the survey's author-supplied BibTeX bibliography and one-page LaTeX classification tree, supplied on 22 October 2026.

- The bibliography contains 415 entries. Two explicit template-testing entries (`smith2024example` and `doe2023benchmark`) are excluded, leaving 413 references.
- The classification tree cites 263 distinct references in 392 placements across eight chapters and 29 subsections. All citation keys resolve to bibliography entries.
- The remaining 150 references are retained in the complete index as additional bibliography entries. No classification has been inferred for them.
- Publication metadata, source URLs, and classification labels follow the supplied materials. Their presence is not a claim of independent source verification, publication status verification, or demonstrated RSI evidence.
- Paragraphs introducing the process framework use the survey's S1–S4/RI definitions. The local survey draft was consulted for context; the manuscript itself is not distributed here.

The catalog does not add paper-specific experimental results, abstracts, or evidence ratings. Source metadata remains in `data/papers.json`; `data/taxonomy.json` preserves the supplied hierarchy. Both the reading list and complete index can be regenerated with the standard-library-only script.

## Figure selection

The survey project source archive was downloaded from the author's open Overleaf project on 22 October 2026. The archive contains `assets/main_figure.pdf` and `assets/abstract_figure.png`.

**Homepage overview:** `assets/overview.pdf` is an unchanged copy of `assets/main_figure.pdf`. Its 1042 × 642 pt page was rendered at 2.5× into `assets/overview.png` for inline GitHub display. It was selected because it explicitly connects the four trustworthiness themes, S1–S4, recursive improvement, evaluation, applications, and open problems to the survey chapters.

**Supplementary visual abstract:** `assets/visual-abstract.png` is an unchanged copy of `assets/abstract_figure.png`. Its landscape illustration provides an accessible visual entry point and is available in a collapsible block below the introduction.

The original image artwork and PDF content were not redesigned or rewritten.

## Presentation reference

[Awesome RSI](https://github.com/lobehub/awesome-rsi) inspired the overview-image placement, navigable contents, topic hierarchy, and linked-paper format. Its README prose, artwork, and paper summaries were not copied into this repository.

## Local validation

`scripts/validate.py` checks citation-key resolution, duplicate IDs and placements, required metadata, source-URL syntax, complete BibTeX/JSON field agreement, generated-file consistency, figure signatures, and repository-local Markdown file and anchor targets. It does not test external URL availability or independently audit the scientific content of the references.

The initial publishing credential permits repository content updates but does not have GitHub's `workflow` scope. The validation workflow is therefore distributed as an optional template in `docs/ci/validate.yml`; automatic GitHub Actions checks are not enabled by this initial publication. The same validation was completed locally before publication.
