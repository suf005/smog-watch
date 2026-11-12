"""Functions for retrieving live air-quality data."""

import requests

from config import API_URL, CURRENT_FIELDS, REQUEST_TIMEOUT


def fetch_air_quality(latitude, longitude):
    """Fetch the latest available air-quality readings for a location."""
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": CURRENT_FIELDS,
        "timezone": "auto",
    }

    try:
        response = requests.get(API_URL, params=params, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.Timeout as exc:
        raise RuntimeError("The API request timed out. Please try again.") from exc
    except requests.exceptions.HTTPError as exc:
        raise RuntimeError(
            f"The API returned an HTTP error ({response.status_code})."
        ) from exc
    except requests.exceptions.RequestException as exc:
        raise RuntimeError("Could not connect to the air-quality API. Check your internet connection.") from exc
    except ValueError as exc:
        raise RuntimeError("The API returned a response that was not valid JSON.") from exc

    current = data.get("current")
    units = data.get("current_units", {})

    if not isinstance(current, dict):
        raise RuntimeError("The API response did not contain current air-quality readings.")

    return {
        "time": current.get("time", "Not available"),
        "us_aqi": current.get("us_aqi"),
        "european_aqi": current.get("european_aqi"),
        "pm2_5": current.get("pm2_5"),
        "pm10": current.get("pm10"),
        "units": units,
    }
