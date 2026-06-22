# Markdown to EPUB

The Markdown workflow renders Markdown to XHTML chapters, packages local image assets, generates EPUB metadata files, and writes a deterministic ZIP package by default.

## Inputs

`text2epub markdown` accepts either one Markdown file or a directory. For directories, direct `*.md` children are sorted by filename and used as spine order.

```bash
text2epub markdown manuscript/ -o book.epub --title "Book" --language en
```

## Front matter

The first Markdown file may include simple YAML-like front matter. Only `key: value` lines are parsed.

```markdown
---
title: Front Matter Title
language: en
author: Ada Lovelace
publisher: Example Press
description: Short description.
rights: Copyright holder/date.
date: 2026-06-22
identifier: urn:uuid:example
---

# Chapter One
```

Explicit metadata passed through the Python API or CLI takes precedence over front matter.

## Headings

Headings receive stable IDs generated from heading text:

```markdown
# Hello World

## Hello World
```

The rendered IDs become `hello-world` and `hello-world-2`.

## Images

Local images are copied into `OEBPS/Images/` and chapter image references are rewritten to relative package paths.

```markdown
![Cover](cover.png)
```

Remote images are rejected by default. Set `allow_remote_resources=True` in `BuildOptions` or pass `--allow-remote-resources` to leave remote image URLs external. External resources may not be accepted by all stores or reading systems.

## Links and raw HTML

Raw HTML in Markdown is disabled. Links with `javascript:` URLs are rejected. Other links are escaped during XHTML serialization.
