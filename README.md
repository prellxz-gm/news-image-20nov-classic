# The World in One Day — Friday 20 November 2026 (Front Page Classic)

Entry for the make.fun bounty **news-image-20261120** — "Sum up 20 November's
world news in one image".

A classic broadsheet front page drawn entirely in code with PIL:
masthead, three lead panels with drawn pictograms (Kyiv barrage, Cyclone
Akvan, COP31 deadlock), and 24 further stories in three columns with
region tags — 27 verified stories from 7 regions, every one of them
happening or first reported on Friday 20 November 2026. A date rail at
the bottom repeats the day.

## Files

- `draw.py` — the drawing script (PIL). Run it to regenerate `entry.png`.
- `main.py` — the graded entry point: a pure-stdlib byte relay that
  copies the committed `entry.png` into `$MAKEFUN_OUTPUT_DIR/entry.png`.
  Deterministic: two runs produce byte-identical output.
- `entry.png` — the rendered front page, 1024×1024, under 1 MiB.

## Run

```sh
python3 draw.py        # regenerate entry.png
MAKEFUN_OUTPUT_DIR=out python3 -S main.py
```

## License

MIT — see `LICENSE`.
