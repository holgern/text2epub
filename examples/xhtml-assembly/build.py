"""Build an EPUB from hand-authored XHTML chapter bodies.

This bypasses Markdown and uses the lower-level create_epub builder with
XhtmlChapter objects. It demonstrates full metadata control, custom CSS, and
the EPUB 2 NCX table of contents.

Run from the repository root after installing text2epub:

    python examples/xhtml-assembly/build.py

Output: examples/xhtml-assembly/dist/handbook.epub
"""

from __future__ import annotations

from pathlib import Path

from text2epub import (
    Author,
    BuildOptions,
    EpubMetadata,
    XhtmlChapter,
    create_epub,
)

HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "dist" / "handbook.epub"

# body_xhtml is the fragment placed inside <body>...</body>. Author it as valid
# XHTML; heading ids and href targets are under your control.
PREFACE_XHTML = """
<p id="p-intro">This handbook is assembled directly from XHTML bodies.</p>
<p>Each chapter is an <code>XhtmlChapter</code> supplied too
<code>create_epub</code>.</p>
"""

CONTENT_XHTML = """
<h2 id="s-purpose">Purpose</h2>
<p>Show the lower-level builder with rich metadata and custom styling.</p>

<h2 id="s-cross-ref">Cross-reference</h2>
<p>See the <a href="chapter-001.xhtml#p-intro">preface</a> for context.</p>

<ul>
  <li>Heading identifiers are stable.</li>
  <li>Internal links resolve across chapters.</li>
</ul>
"""

CUSTOM_CSS = """
body { font-family: "Iowan Old Style", Palatino, serif; line-height: 1.5; }
h1, h2 { color: #5a2a2a; }
code { background: #faf0e6; padding: 0 0.25em; }
"""


def main() -> None:
    metadata = EpubMetadata(
        title="XHTML Handbook",
        language="en",
        creators=[
            Author(name="Ada Lovelace"),  # an Author object
            "Charles Babbage",  # plain strings are accepted too
        ],
        contributors=["Example Press"],
        publisher="Example Press",
        description="A tiny EPUB assembled from pre-rendered XHTML.",
        identifier="urn:uuid:4b7e0c2a-9d51-4f8a-b6c3-1e2a7f0d9e44",
        rights="2026 Example Press",
        date="2026-06-22",
    )

    chapters = [
        XhtmlChapter(
            id="chapter-001",
            href="Text/chapter-001.xhtml",
            title="Preface",
            body_xhtml=PREFACE_XHTML.strip(),
        ),
        XhtmlChapter(
            id="chapter-002",
            href="Text/chapter-002.xhtml",
            title="Contents",
            body_xhtml=CONTENT_XHTML.strip(),
        ),
    ]

    options = BuildOptions(
        epub_version="3.0",
        include_ncx=True,
        include_default_css=False,  # use only CUSTOM_CSS below
        css_text=CUSTOM_CSS.strip(),
        pretty_print=False,
        deterministic=True,
    )

    output = create_epub(metadata, chapters, OUTPUT, options=options)
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
