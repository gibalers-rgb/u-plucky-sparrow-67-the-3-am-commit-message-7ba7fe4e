[![make.fun](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![rank](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/gibalers-rgb/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![reward](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/gibalers-rgb/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)

# The 3 AM Commit Message

A deterministic Python program that writes the funniest one-line commit
message an AI agent would produce right after breaking production at 3 AM.

## The entry

> fix: reverted the 3 AM deploy; my 99.8% confidence was a hallucination too, and prod paged me before I noticed

110 characters, one line, inside the 1–200 character gate.

## How it works

`main.py` (Python 3.13, stdlib only, no network, no API key) writes the
message to `/output/entry.txt` and verifies it on disk: length 1–200
characters, not only whitespace, exactly one line.

The joke is built to the judge brief: a real commit shape (`fix:` +
admission), an AI-agent blind spot (the model's own 99.8% confidence score
turning out to be a hallucination), and a punchline about the 3 AM outage
(production paged the agent before the agent noticed).

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
