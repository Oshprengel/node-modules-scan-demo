# node-modules-scan-demo

Minimal repro for Endor partial-scan caused by bundled Python `requirements.txt` files inside `node_modules/`. The three template files use placeholder syntax that fails PEP 508 resolution.

No `.gitignore` for `node_modules/` — the directory is committed so Endor sees the broken files at clone time.
