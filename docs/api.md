# Python API reference

This page documents the stable public API exposed from `text2epub.__init__`.

## Models

```{eval-rst}
.. autoclass:: text2epub.Author
   :members:

.. autoclass:: text2epub.EpubMetadata
   :members:

.. autoclass:: text2epub.BuildOptions
   :members:

.. autoclass:: text2epub.MarkdownBook
   :members:

.. autoclass:: text2epub.MarkdownChapter
   :members:

.. autoclass:: text2epub.XhtmlChapter
   :members:

.. autoclass:: text2epub.Replacement
   :members:

.. autoclass:: text2epub.ReplacementPlan
   :members:

.. autoclass:: text2epub.ReplacementReport
   :members:
```

## Builders

```{eval-rst}
.. autofunction:: text2epub.create_epub_from_markdown

.. autofunction:: text2epub.create_epub
```

## Rebuilds

```{eval-rst}
.. autofunction:: text2epub.rebuild_epub
```

## Exceptions

```{eval-rst}
.. automodule:: text2epub.errors
   :members:
```
