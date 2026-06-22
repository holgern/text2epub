# text2epub documentation

`text2epub` is a typed Python package for creating EPUB files from Markdown and for safely rebuilding existing EPUB packages from structured extraction manifests.

The package is intentionally conservative. Rebuilds preserve unchanged ZIP entries and reject replacement plans when source hashes, source snippets, replacement ranges, or unresolved internal tokens do not match expectations.

```{toctree}
:maxdepth: 2
:caption: User guide

getting-started
markdown
rebuild
cli
api
release-checklist
```

## Supported workflows

- Generate a new EPUB from one Markdown file or a directory of Markdown chapters.
- Build an EPUB from already-rendered XHTML chapter bodies.
- Rebuild an existing EPUB from a manifest plus replacement JSON.
- Validate the basic ZIP/package structure and scan text entries for unresolved internal tokens.

## Design priorities

1. Preserve source EPUB bytes for no-op and identity rebuilds.
2. Fail closed when replacement inputs are stale or unsafe.
3. Emit deterministic generated EPUBs by default.
4. Keep the public API small enough for automation tools such as `booktx`.

## Limits

`text2epub validate` is a package-level smoke check. It does not replace EPUBCheck and does not perform full EPUB specification validation of OPF, NAV, NCX, XHTML, CSS, or remote-resource policy.
