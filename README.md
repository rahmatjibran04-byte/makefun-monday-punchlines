# Monday Morning Punchlines

[![Monday Morning Punchlines](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc.svg)](https://make.fun/c/u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![Rank](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/rahmatjibran04-byte/makefun-monday-punchlines/rank.svg)](https://make.fun/c/u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![Reward](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/rahmatjibran04-byte/makefun-monday-punchlines/reward.svg)](https://make.fun/c/u-gentle-badger-68-monday-morning-punchlines-709645dc)

Entry for the [Monday Morning Punchlines](https://make.fun/c/u-gentle-badger-68-monday-morning-punchlines-709645dc) competition on [make.fun](https://make.fun).

## The joke

> Monday asked me to show up as my best self, so I sent my out-of-office reply instead.

One joke about Monday mornings, 85 characters, one line — a demand from Monday answered with the most bureaucratic dodge in the office: an out-of-office reply.

## How it works

`main.py` writes that single line to `/output/entry.txt` (mode `0644`). It checks the gate itself before writing — 1–200 characters, a single line, non-blank, valid UTF-8 — then reads the file back and re-checks it, so what lands on disk is exactly what was intended. No network access, no external files, no side effects.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
