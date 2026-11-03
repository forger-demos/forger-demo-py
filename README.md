# units

Convert between units from the command line: `units 2 km mi`.

A small demo driven by the forger work loop on a Python stack: requests are
GitHub issues labelled `ready-for-agent`, and a PR merges only when the gates in
`.forger/workloop.config.json` and CI pass.

## Supported units

- Length: `m`, `km`, `cm`, `mi`, `ft`
- Mass: `g`, `kg`, `lb`, `oz`
- Temperature: `C`, `F`, `K`

Units are case-sensitive. Converting between quantities (`units 1 km kg`)
exits 2 and names both units. Running `units` with no arguments lists them.

## Develop

```
uv sync
uv run pytest
```
