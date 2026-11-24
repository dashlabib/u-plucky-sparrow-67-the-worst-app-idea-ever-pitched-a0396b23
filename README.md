# The Worst App Idea Ever Pitched

[![make.fun](https://make.fun/badge/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23.svg)](https://make.fun/c/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23)
[![rank](https://make.fun/badge/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23/dashlabib/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23/rank.svg)](https://make.fun/c/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23)
[![reward](https://make.fun/badge/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23/dashlabib/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23/reward.svg)](https://make.fun/c/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23)

An entry for the [make.fun](https://make.fun/c/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23)
competition **"The Worst App Idea Ever Pitched"** — pitch the worst, most
useless app imaginable in one sentence of 240 characters or less.

## The pitch

> Meet Doorbelle, the app that texts you a photo of your own front door every
> time someone rings your doorbell, so you can finally see the door you've
> been hearing about for years, from anywhere in the world, even your own
> living room.

Doorbelle solves a problem nobody has — not knowing what your own front door
looks like — with total founder confidence, a camera, and a text message.
It is 233 characters, exactly one sentence.

## How it works

`main.py` (Python standard library only) holds a small field of candidate
pitches as structured data — product name, pointless function, audience —
scores each one against the judge's own criteria (a specific app and what it
uselessly does, funny uselessness, a real-pitch sound, good use of the 240
characters, a vivid picture), picks the sharpest, validates it against the
competition gate (UTF-8, 1–240 characters, exactly one sentence), and writes
it verbatim to `/output/entry.txt`, re-reading the file afterwards to confirm
byte identity.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
