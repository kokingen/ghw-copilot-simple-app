# Lantern Lighthouse

A choose-your-own-adventure command-line game written in Python 3 with no external dependencies.

## Overview

You've washed ashore near a mysterious lighthouse. Navigate through choices, collect items, and uncover the secrets of Lantern Lighthouse. Will you escape? Will you free a trapped spirit? Or will the lighthouse claim you?

## Features

- **6 Main Scenes** with branching paths and multiple endings
- **Inventory System** – Collect items like a lantern and journal that affect available choices
- **4 Distinct Endings** – 2 good endings (rescue and peace) and 2 bad endings (trapped and lost)
- **Input Validation** – Invalid choices prompt re-entry
- **Replay Prompt** – Play multiple games without restarting
- **Single File** – No external dependencies required

## How to Play

```bash
python3 lantern_lighthouse.py
```

Type the number (or letter) of a choice and press Enter. Invalid input re-prompts. At an ending you can choose to play again.

## Built with GitHub Copilot

This game was generated with **GitHub Copilot Chat (Copilot Free)** on github.com/copilot for the MLH Global Hack Week: Hacktoberfest challenge *"Use GitHub Copilot to Build a Simple Application"*. The prompt asked for a single-file Python choose-your-own-adventure game with 6+ scenes, an inventory, 2 good and 2 bad endings, input validation and a play-again prompt; Copilot wrote both `lantern_lighthouse.py` and this README. `test_smoke.sh` plays through random paths to check every run reaches an ending.
