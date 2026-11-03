# units

Convert between units from the command line: `units 2 km mi`.

A small demo driven by the forger work loop on a Python stack: requests are
GitHub issues labelled `ready-for-agent`, and a PR merges only when the gates in
`.forger/workloop.config.json` and CI pass.

## Develop

```
uv sync
uv run pytest
```
