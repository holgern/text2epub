# Getting started

## Install for development

```bash
python -m pip install -e .
python -m pip install -e ".[dev]"
```

Install the documentation dependencies when building the Sphinx site:

```bash
python -m pip install -e ".[docs]"
```

## Create an EPUB from Markdown

Create a Markdown chapter:

```markdown
# Chapter One

Hello world.
```

Build the EPUB from Python:

```python
from pathlib import Path

from text2epub import EpubMetadata, MarkdownBook, MarkdownChapter, create_epub_from_markdown

book = MarkdownBook(
    metadata=EpubMetadata(title="Example Book", language="en"),
    chapters=[MarkdownChapter(path=Path("chapter-01.md"))],
)

create_epub_from_markdown(book, Path("example.epub"))
```

Or use the CLI:

```bash
text2epub markdown chapter-01.md -o example.epub --title "Example Book" --language en
```

## Validate output

```bash
text2epub validate example.epub
```

A successful response confirms that the archive has the expected EPUB ZIP basics and that known unresolved internal tokens were not found in text entries. Run EPUBCheck separately before publication.
