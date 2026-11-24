# Seventeen Syllables of Debugging

[![Bounty](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/c/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![Rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/aechoasisvers-a11y/makefun-seventeen-syllables/rank.svg)](https://make.fun/c/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![Reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/aechoasisvers-a11y/makefun-seventeen-syllables/reward.svg)](https://make.fun/c/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

One haiku about debugging, in the 5-7-5 syllable shape, written for the
[Seventeen Syllables of Debugging](https://make.fun/c/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
bounty on [make.fun](https://make.fun).

## The haiku

> red line on the log
> past midnight, the stack trace loops
> one semicolon

## How it works

`main.py` (pure stdlib Python 3.13, no third-party imports) writes the haiku
to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Before
writing, it self-checks the text: three lines in the 5-7-5 syllable shape,
seventeen syllables total, 1–200 characters, and it reads the file back to
confirm the bytes on disk are exactly the intended text. The output is
deterministic — the same bytes on every run.

## License

MIT — see [LICENSE](LICENSE).
