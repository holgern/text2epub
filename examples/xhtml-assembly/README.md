# xhtml-assembly

Builds an EPUB from already-rendered XHTML chapter bodies using the lower-level
`create_epub` builder. This is the workflow to reach for when you generate or
hand-author XHTML yourself and do not want a Markdown step.

## What it demonstrates

- `create_epub` with a sequence of `XhtmlChapter` objects.
- Hand-authored `body_xhtml` fragments with stable heading IDs and a
  cross-chapter link (`chapter-001.xhtml#p-intro`).
- Full `EpubMetadata`: multiple creators supplied as both `Author` objects and
  plain strings, plus a contributor, publisher, description, rights, date, and
  a fixed identifier.
- `BuildOptions` toggles: `include_default_css=False` with a custom `css_text`
  stylesheet, `include_ncx=True`, and deterministic output.

## Run it

From the repository root, with `text2epub` installed:

```bash
python examples/xhtml-assembly/build.py
```

The package is written to `dist/handbook.epub`. Validate it separately with:

```bash
text2epub validate examples/xhtml-assembly/dist/handbook.epub
```

## Notes

- `body_xhtml` is inserted inside `<body>`. Do not include the surrounding
  `<html>` or `<body>` tags; the builder adds them.
- There is no Markdown safety net here. Ensure your XHTML is well formed,
  because `create_epub` serializes the fragments you give it.
