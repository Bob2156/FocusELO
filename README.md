# Focus ELO ⚡

A gamified Pomodoro study app with an ELO rating system. Track your focus across 25-minute study blocks, climb through tiers, and build consistent study habits.

![Focus ELO](https://img.shields.io/badge/Focus-ELO-7c5cfc?style=for-the-badge)

## Features

- **ELO Rating System** — Win/Draw/Loss scoring per block with tier-specific point values
- **6 Tiers** — Climb from Trenches → Bronze → Silver → Gold → Starlight → Prestige
- **25-Minute Timer** — Pomodoro-style blocks with 5-minute breaks
- **Daily Progress** — Track blocks, study time, and daily targets
- **Study Calendar** — Month view with clickable day details and logging
- **Block History** — Full history with per-block edit/delete and undo support
- **Streak Tracking** — Win/loss streak display
- **Confetti & Sounds** — Celebrations for promotions and Prestige unlock
- **Standalone Desktop App** — Runs as a local server via Python or packaged `.exe`

## Tier Ladder

| Tier | ELO Range | Win | Draw | Loss |
|------|-----------|-----|------|------|
| 🕳️ Trenches | < 0 | +25 | +25 | 0 |
| 🟫 Bronze | 0 – 74 | +25 | +10 | -12.5 |
| ⚪ Silver | 75 – 149 | +25 | 0 | -15 |
| 🟨 Gold | 150 – 224 | +25 | 0 | -25 |
| 🌌 Starlight | 225 – 299 | +25 | -10 | -25 |
| ✨ Prestige | 300+ | +25 | -10 | -25 |

## Quick Start

### Run directly (Python)
```bash
python app.py
```
Opens in your default browser at `http://127.0.0.1:47932`.

### Build standalone exe (Windows)
```bash
build.bat
```
Creates `dist/FocusELO.exe` — a single-file executable with everything bundled.

## Tech Stack

- **Frontend:** Single HTML file with embedded CSS & JavaScript
- **Backend:** Python HTTP server (localhost only)
- **Storage:** Browser localStorage
- **Audio:** Web Audio API (no external files)
- **Packaging:** PyInstaller

## Files

| File | Description |
|------|-------------|
| `index.html` | Complete app (HTML + CSS + JS) |
| `app.py` | Local HTTP server with no-cache headers |
| `build.bat` | Windows build script for creating `.exe` |

## License

MIT
