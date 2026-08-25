from langchain_core.tools import tool
import json
import httpx


def get_location(city: str):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": city,
        "count": 1,
        "language": "zh",
        "format": "json",
    }
    response = httpx.get(url, params=params)
    data = response.json()
    if "results" not in data:
        raise ValueError(f"找不到城市：{city}")
    location = data["results"][0]
    result = {
        "name": location["name"],
        "country": location.get("country"),
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "timezone": location.get("timezone", "Asia/Shanghai"),
    }
    return result

@tool
def get_weather(loc: str) -> str:
    """
    查询指定城市的即时天气。

    参数:
        loc: 城市名称字符串。为了提高调用成功率，建议优先传英文城市名，
             如 Beijing、Shanghai。

    返回:
        OpenWeather 当前天气接口返回的 JSON 字符串，包含气温、体感温度、
        湿度、风速、天气描述等信息。
    """
    location = get_location(loc)
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "location": location["name"],
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,weather_code,wind_speed_10m",
        "timezone": location["timezone"],
    }
    response = httpx.get(url, params=params)
    data = response.json()
    return json.dumps(data)

result = get_weather.invoke("nanchang")
print(result)
