# Trustworthy RSI website

Public URL: https://pujiayue.github.io/Trustworthy-RSI/

GitHub Pages serves this static site from the root of the `gh-pages` branch.
The survey bibliography and taxonomy remain on `main`.

Edit and validate this branch, retain `.nojekyll`, commit, and push to `gh-pages`.
GitHub's native Pages build publishes the update. All application asset paths are relative and work under `/Trustworthy-RSI/`.

The current design is implemented by `styles.css` plus `theme.css`. `app.js` handles the process explorer, bibliography filters, saved reading list, shared filter URLs, exports, and dialogs. `data.js` contains the supplied bibliography and taxonomy.

Fonts: locally hosted Inter, licensed in `assets/Inter-LICENSE.txt`.
Behavioral tests: `npm --prefix tests ci && npm --prefix tests test`.
Design and content review: [DESIGN_REVIEW.md](DESIGN_REVIEW.md).
