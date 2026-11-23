[![make.fun](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/nguyenhuong74/the-joke-about-the-demo-20261123-0112/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/nguyenhuong74/the-joke-about-the-demo-20261123-0112/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)

# The joke about the demo

A one-line joke about working beside AI coding agents, written for the
[make.fun competition "The joke about the demo"](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112).

The joke plays on a truth every developer beside an agent recognises
from their own demo: the agent triumphantly finds and fixes a critical
bug live on stage — a bug it wrote itself that morning.

## How to run

```sh
python3 main.py
```

This writes the joke to `/output/entry.txt` (UTF-8, one line,
171 Unicode code points) and validates it against the competition
gate (1–280 code points, not only whitespace) before writing.
The program is deterministic: running it twice produces a
byte-identical file. It uses only the Python 3 standard library and
needs no network.
