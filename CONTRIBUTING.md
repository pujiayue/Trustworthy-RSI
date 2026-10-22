# Contributing

Thank you for helping maintain the Trustworthy RSI reading list.

## Suggest a paper or correction

Open an issue or pull request with the paper title, authors, year, a primary-source URL, and the subsection where it belongs. Explain briefly why it is relevant. Distinguish direct RSI evidence from related self-evolution studies and enabling methods; do not infer that a safeguard survives recursive updates unless the cited work tests that claim.

Metadata corrections should include a publisher, author project page, arXiv, or other primary source. Avoid guessed venues, duplicate papers under different citation keys, and placeholder references.

## Update the repository

1. Add or correct the entry in `data/papers.json`, retaining its BibTeX citation key as `ID` and entry type as `ENTRYTYPE`.
2. Add the corresponding BibTeX entry to `bibliography/references.bib` with matching fields.
3. To classify a reference, add its `id` and a concise `label` to the appropriate `papers` array in `data/taxonomy.json`. A reference may appear in more than one subsection.
4. Run `python3 scripts/build_readme.py` and `python3 scripts/validate.py` from the repository root.
5. Include the source edits and regenerated `README.md` and `docs/PAPER_INDEX.md` in the pull request.

The generator and validator require Python 3.9 or later and use only the standard library. Do not edit generated literature entries directly. Leave a bibliography entry unclassified when its placement is uncertain, and explain the uncertainty in the issue or pull request.

## Figures

Keep original PDFs in `assets/` and provide a clear PNG preview for GitHub. Confirm permission to contribute figures. Figure provenance and selection decisions belong in `docs/PROVENANCE.md`.

## Optional GitHub Actions validation

A ready-to-use workflow is provided in [docs/ci/validate.yml](docs/ci/validate.yml). To enable automatic checks, place it at `.github/workflows/validate.yml` using GitHub's editor or credentials authorized to manage workflows. Until enabled, run the same validator locally before each contribution.
