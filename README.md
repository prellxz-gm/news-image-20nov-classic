# news-image-20nov-classic

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/prellxz-gm/news-image-20nov-classic/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/prellxz-gm/news-image-20nov-classic/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

Front Page Classic — a broadsheet front page summing up Friday 20 November 2026 in one image: 27 verified stories from 7 regions, with three lead stories (the Kyiv barrage, Cyclone Akvan's landfall, the COP31 deadlock), every one happening or first reported on Friday 20 November 2026. Drawn entirely in code with PIL — masthead, three lead panels with drawn pictograms, and 24 further stories in three columns with region tags. A date rail at the bottom repeats the day.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 -S main.py
```

## Files

- `draw.py` — the drawing script (PIL). Run it to regenerate `entry.png`.
- `main.py` — the graded entry point: a pure-stdlib byte relay that copies the committed `entry.png` into `$MAKEFUN_OUTPUT_DIR/entry.png`. Deterministic: two runs produce byte-identical output.
- `entry.png` — the rendered front page, 1024×1024, under 1 MiB.

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=jyrqfb5w&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
