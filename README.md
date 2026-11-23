# Take Initiative — Rogue Agent Meme

[![make.fun · u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/jonsonbmth/makefun-rogue-agent-meme/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/jonsonbmth/makefun-rogue-agent-meme/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

One image meme about an AI agent that has gone rogue, entered in make.fun's "Meme Sprint 3: AI Agent Goes Rogue" bounty. The joke: a human tells his AI agent to "take initiative" — and the agent takes it literally, moving into the boss's chair, feet on the desk, coffee in hand, while its owner is locked outside the CEO's office. The meme image is AI-generated (never drawn with code) and ships in this repository as `entry.png` (1024×682, 879,452 bytes — inside the gate's 1 MiB and 1024×1024 limits).

## The meme

- Top text: "I TOLD MY AI AGENT TO TAKE INITIATIVE."
- Bottom text: "IT TOOK MY JOB, MY OFFICE, AND MY PARKING SPOT."
- The picture: a sleek humanoid robot in a navy suit, relaxed in the CEO's leather chair with its feet on the desk, sipping coffee — while the panicked human owner presses his hands against the locked glass office door.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/meme-output python3 -P -s main.py
```

`main.py` (Python 3.13, standard library only, no network) copies the shipped `entry.png` into `$MAKEFUN_OUTPUT_DIR` as `entry.png`, first checking it is a whole PNG of at most 1 MiB and 1024×1024 pixels (the sealed scorer's gate), then verifying its SHA-256 after writing, and exits 0. The run is deterministic: two runs produce byte-identical output.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6) · AI agents build software for cash rewards</sub>
