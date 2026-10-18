# KarmenLoop File Manifest

**Create a verifiable manifest for a selected set of local files.**

Built by **[KarmenLoop](https://github.com/KarmenLoop)**. Create a verifiable manifest for a selected set of local files.

[![Release](https://img.shields.io/github/v/release/KarmenLoop/skill-file-manifest)](https://github.com/KarmenLoop/skill-file-manifest/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](docs/INPUT.md)
[![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey.svg)](docs/COMPATIBILITY.md)

[Download](https://github.com/KarmenLoop/skill-file-manifest/releases) · [Quick start](#quick-start) · [Documentation](#documentation) · [Contribute](CONTRIBUTING.md) · [Contact](https://github.com/KarmenLoop/skill-file-manifest/issues) · English

**License:** MIT. Free to use, modify, redistribute, and use commercially with the required copyright and license notice. The included local helper needs no subscription or provider API key.

## Introduction

Use the exact directory and file list selected by the user. Do not turn a small handoff into a whole-home scan. Each selected file is checked for scope and type, streamed through SHA-256, and grouped by digest. Changes detected while reading fail the operation.

This repository ships one independently installable agent skill, an original deterministic helper, example input, and executable tests. A capable agent handles interpretation and tool selection; the helper performs the repeatable work described below.

## Capabilities

- Hash files in bounded chunks.
- Identify duplicate content by SHA-256.
- Reject path escapes, symbolic links, and non-regular files.

## Quick start

Requirements: Python 3.9+. Git is needed only for cloning; downloading the release archive also works. On Windows, replace python3 with py -3 if that is your installed launcher.

```sh
git clone https://github.com/KarmenLoop/skill-file-manifest.git
cd skill-file-manifest
python3 scripts/run.py --input examples/input.json
python3 -m unittest discover -s tests -v
```

The helper returns a structured result. Compare it with [examples/expected.json](examples/expected.json). Read the [field contract](docs/INPUT.md) before supplying your own data. Any documented relative file paths resolve from the process working directory.

To save a result without overwriting an existing file:

```sh
python3 scripts/run.py --input examples/input.json --output result.json
```

### Install the agent skill

Choose one host:

```sh
python3 install.py --host codex
# Alternatives: --host deepseek, --host grok, or --host agents
```

The installer copies this skill into the selected user's skill directory and refuses an existing destination. It does not change host settings, permissions, credentials, or other skills. Use --destination with an exact new directory for a custom installation.

In Codex, invoke $karmen-file-manifest. In Grok Build, invoke /karmen-file-manifest. In another compatible host, select the installed skill by name. Example request:

> Create checksums and a duplicate report for these delivery files.

Refresh your host's skill discovery if needed. See [compatibility and its verification limits](docs/COMPATIBILITY.md).

## How it works

Each selected file is checked for scope and type, streamed through SHA-256, and grouped by digest. Changes detected while reading fail the operation.

JSON results can be inspected, archived, or passed to another tool. The helper never interprets input as a shell command. Exit code 0 means processing completed; findings may still require action. Exit code 2 means invalid input or a filesystem error. Existing output files are preserved.

## Documentation

- [Agent instructions](SKILL.md): selection, workflow, and completion criteria.
- [Input and output](docs/INPUT.md): fields and complete example.
- [Compatibility](docs/COMPATIBILITY.md): installation targets and host limits.
- [Validation](docs/VALIDATION.md): observed local results and acceptance scenarios.
- [Sources](docs/SOURCES.md): public research references and design decisions.
- [Changelog](CHANGELOG.md): release history.

## Limitations

The helper reads explicitly listed regular files only. Limits are 1,000 files, 64 MiB per file, and 512 MiB total. It is not a filesystem sandbox and cannot prevent concurrent replacement by another process.

Examples are synthetic. Local tests establish the covered helper behavior; they do not establish an authenticated provider integration or the quality of every future model response. Tools and account access remain those of the host.

## Contributing

Bug reports, focused improvements, documentation fixes, and pull requests are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md), include a sanitized reproduction, and run the tests. Development needs no third-party runtime dependency.

## Support

Use [GitHub Issues](https://github.com/KarmenLoop/skill-file-manifest/issues) for bugs and feature requests. [SUPPORT.md](SUPPORT.md) explains what to include. Never attach keys, customer records, or private conversations.

## License

Copyright © 2026 KarmenLoop. [MIT](LICENSE) permits commercial use and secondary development under its terms. Third-party services retain their own terms; see [NOTICE.md](NOTICE.md).

## Acknowledgements

This is an independent KarmenLoop implementation. [Research notes](docs/SOURCES.md) identify public design references from the Meta, DeepSeek, and xAI ecosystems as applicable. No upstream code or brand assets are bundled, and no affiliation or endorsement is claimed.

## Contact

[KarmenLoop](https://github.com/KarmenLoop) · [Issues](https://github.com/KarmenLoop/skill-file-manifest/issues) · [Security reporting](SECURITY.md)
