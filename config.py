"""Project settings for Smog Watch."""

# City coordinates used to request air-quality data from Open-Meteo.
CITIES = {
    "Karachi, Pakistan": (24.8607, 67.0011),
    "Lahore, Pakistan": (31.5204, 74.3587),
    "Islamabad, Pakistan": (33.6844, 73.0479),
    "Peshawar, Pakistan": (34.0151, 71.5249),
    "Quetta, Pakistan": (30.1798, 66.9750),
    "Hyderabad, Pakistan": (25.3960, 68.3578),
}

API_URL = "https://air-quality-api.open-meteo.com/v1/air-quality"
REQUEST_TIMEOUT = 15

CURRENT_FIELDS = "us_aqi,european_aqi,pm2_5,pm10"
