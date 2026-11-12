# Smog Watch

Smog Watch is a Python command-line application that fetches live air-quality data for a selected Pakistani city from the [Open-Meteo Air Quality API](https://open-meteo.com/en/docs/air-quality-api).

It displays:
- US Air Quality Index (US AQI) and its category
- European Air Quality Index
- PM2.5 concentration
- PM10 concentration
- The timestamp of the API reading

The readings are fetched from the API each time the program runs; pollution readings are not hardcoded.

## Requirements

- Python 3.9 or newer
- An internet connection

No API key is required for this public, non-commercial API use.

## Installation

Open a terminal in the project folder.

### Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If PowerShell blocks activation, use Command Prompt:

```bat
.venv\Scripts\activate.bat
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

Choose a city from the menu when prompted. The report displays the city name; its coordinates are used behind the scenes for the API request. To add or change cities, edit `CITIES` in `config.py`.

## Example output

The readings below are **illustrative only**. Actual values are fetched live and will vary.

```text
================================================
                 SMOG WATCH
================================================
Location:             Karachi, Pakistan
Reading time:         2026-11-10T21:00
------------------------------------------------
AIR QUALITY
US AQI:               118
US AQI category:      Unhealthy for Sensitive Groups
European AQI:         42
------------------------------------------------
POLLUTANT LEVELS
PM2.5:                42.5 μg/m³
PM10:                 61.2 μg/m³
================================================
Source: Open-Meteo Air Quality API
================================================
```

## API integration

The application sends an HTTP GET request to:

`https://air-quality-api.open-meteo.com/v1/air-quality`

It requests the current `us_aqi`, `european_aqi`, `pm2_5`, and `pm10` fields using the selected city's latitude and longitude. The JSON response is parsed and displayed in the terminal.

Official documentation: https://open-meteo.com/en/docs/air-quality-api

## Project files

- `main.py` — application entry point and terminal report
- `air_quality.py` — API request and response handling
- `config.py` — location and API settings
- `requirements.txt` — Python dependency list
- `.gitignore` — excludes virtual environments and generated files

## Limitations

Data availability and update frequency depend on the API. AQI values are informational and are not medical advice.
