# markdown-essays

Generates a multi-chapter EPUB entirely from Markdown. This is the high-level
`create_epub_from_markdown` workflow.

## What it demonstrates

- A book built from every `*.md` file in `chapters/`, sorted into spine order.
- YAML-like front matter in the first chapter drives the EPUB metadata.
- Headings get stable IDs (`on-markdown`, `a-table-of-features`).
- A local image (`assets/cover.png`) is copied into the package and rewritten to
  a relative path.
- A table, a fenced code block, a blockquote, and a link render to XHTML.
- A custom stylesheet (`style.css`) is merged with the default CSS.

## Run it

From the repository root, with `text2epub` installed:

```bash
python examples/markdown-essays/build.py
```

The package is written to `dist/essays.epub`. The builder validates the ZIP
package on the way out. To run the standalone token/package check:

```bash
text2epub validate examples/markdown-essays/dist/essays.epub
```

## Equivalent CLI

```bash
text2epub markdown examples/markdown-essays/chapters \
  -o examples/markdown-essays/dist/essays.epub
```

Note that the CLI does not load a custom `css_files` stylesheet; it only applies
the built-in default CSS. Use the Python API shown in `build.py` for custom CSS.
