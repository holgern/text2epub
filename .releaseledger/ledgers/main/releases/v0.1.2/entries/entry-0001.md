---
schema_version: 2
object_type: release_entry
versioning:
  schema_version: 1
  revision: 3
entry_id: entry-0001
release_version: v0.1.2
kind: added
summary: Added inline XHTML support in markdown for embedding formatted content
status: accepted
audience: null
scopes: []
source_refs:
  - git:b183c7eae2937c598f16192139c08d5404b0344c
  - git:9eaca1c63aca03eabba411baf15ce987c273f6b8
paths:
  - text2epub/inline_xhtml.py
  - text2epub/markdown.py
  - text2epub/cli.py
  - examples/inline-xhtml/build.py
  - examples/inline-xhtml/chapters/01-inline-xhtml.md
issues: []
prs: []
sources: []
breaking: false
internal: false
order: 1
---

A new inline_xhtml module handles safe parsing and validation of inline XHTML fragments. The --allow-inline-xhtml flag enables the feature, which supports a restricted set of safe HTML tags and attributes.
