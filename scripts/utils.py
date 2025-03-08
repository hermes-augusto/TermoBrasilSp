import requests
import pandas as pd

def fetch_clima_data(latitude, longitude, start_date, end_date):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "daily": ["temperature_2m_max", "temperature_2m_min"],
        "timezone": "America/Sao_Paulo"
    }
    url = "https://archive-api.open-meteo.com/v1/archive"
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame({
            "date": pd.to_datetime(data["daily"]["time"]),
            "temp_max": data["daily"]["temperature_2m_max"],
            "temp_min": data["daily"]["temperature_2m_min"]
        })
        df["year_month"] = df["date"].dt.to_period("M").astype(str)
        df["year"] = df["date"].dt.year
        return df
    else:
        raise ValueError(f"Erro na requisição: {response.status_code}")
