# Python — Guessing Game

Interactive number guessing game built with a modular architecture
in Python.

Developed as part of the Master's in Data Science at
Universidad Complutense de Madrid.

## Features
- Single player mode against the machine
- Two player mode with hidden input
- 3 difficulty levels
- Progressive hints system (hot/warm/cold)
- Full statistics saved to Excel with rankings
- Persistent configuration via JSON

## Project structure
- `adivinando_juego.ipynb` — main entry point
- `adivinando_modulo.py` — game logic and menus
- `estadisticas_modulo.py` — statistics management
- `configuracion.py` — configuration persistence (JSON)

## How to run
1. Make sure all `.py` files are in the same folder
2. Open `adivinando_juego.ipynb` in Jupyter
3. Run the main cell

Files generated automatically on first run:
- `config.json` — game configuration
- `estadisticas.xlsx` — game statistics database

## Installation
```bash
pip install pandas openpyxl
```

## Tools
Python · pandas · openpyxl · Jupyter
