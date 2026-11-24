# The Long Roast: Lawmakers and the File They Cannot Convert

One satirical sentence roasting lawmakers who would regulate AI, crypto or
the internet but cannot convert a file to PDF — entered in
[The Long Roast: Lawmakers and the File They Cannot Convert](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7).

![Bounty](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7.svg)
![Rank](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/freysiatiara/long-roast-lawmakers-20261124/rank.svg)
![Reward](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/freysiatiara/long-roast-lawmakers-20261124/reward.svg)

## The sentence

> The congressman who spent the morning grilling tech CEOs on accountability forwarded his own bill as a screenshot of a Word document and asked an intern to convert it, because the man writing the rules for the digital age still thinks Save As is a suggestion.

## How it works

`main.py` (Python 3, standard library only) writes that single sentence to
the entry output file — `ENTRY_OUTPUT` if set, otherwise
`$OUTPUT_DIR/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`), falling back
to `/output/entry.txt`. It validates the entry first: 1–320 UTF-8
characters, exactly one sentence, not whitespace only. The file is written
with a plain `open`/`write` and `os.chmod(path, 0o644)`.

```sh
python3 main.py
```
