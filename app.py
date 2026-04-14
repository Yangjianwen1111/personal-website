# 导入库
import streamlit as st
import requests

# ======================
# 天气查询函数（你写的）
# ======================
def get_weather(city_name: str) -> dict:
    geocode_url = "https://geocoding-api.open-meteo.com/v1/search"
    weather_url = "https://api.open-meteo.com/v1/forecast"

    try:
        geocode_params = {
            "name": city_name,
            "count": 1,
            "language": "zh",
            "format": "json"
        }

        geo_response = requests.get(geocode_url, params=geocode_params, timeout=10)
        geo_response.raise_for_status()
        geo_data = geo_response.json()

        if not geo_data.get("results"):
            return {"error": f"未找到城市: {city_name}"}

        location = geo_data["results"][0]
        latitude = location["latitude"]
        longitude = location["longitude"]
        city = location["name"]
        country = location.get("country", "未知")

        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": ["temperature_2m", "relative_humidity_2m", "weather_code", "wind_speed_10m", "apparent_temperature"],
            "daily": ["temperature_2m_max", "temperature_2m_min", "weather_code"],
            "timezone": "auto",
            "forecast_days": 3
        }

        weather_response = requests.get(weather_url, params=weather_params, timeout=10)
        weather_response.raise_for_status()
        weather_data = weather_response.json()

        current = weather_data["current"]
        daily = weather_data["daily"]

        weather_descriptions = {
            0: "晴朗", 1: "主要晴朗", 2: "部分多云", 3: "阴天",
            45: "雾", 48: "雾凇", 51: "小毛毛雨", 53: "中度毛毛雨",
            55: "大毛毛雨", 61: "小雨", 63: "中雨", 65: "大雨",
            71: "小雪", 73: "中雪", 75: "大雪", 95: "雷雨"
        }

        result = {
            "city": city,
            "country": country,
            "current": {
                "temperature": f"{current['temperature_2m']}°C",
                "feels_like": f"{current['apparent_temperature']}°C",
                "humidity": f"{current['relative_humidity_2m']}%",
                "wind_speed": f"{current['wind_speed_10m']} km/h",
                "weather": weather_descriptions.get(current['weather_code'], "未知")
            },
            "forecast": []
        }

        for i in range(len(daily["time"])):
            result["forecast"].append({
                "date": daily["time"][i],
                "max_temp": f"{daily['temperature_2m_max'][i]}°C",
                "min_temp": f"{daily['temperature_2m_min'][i]}°C",
                "weather": weather_descriptions.get(daily['weather_code'][i], "未知")
            })

        return result

    except requests.exceptions.RequestException as e:
        return {"error": f"请求失败: {str(e)}"}
    except Exception as e:
        return {"error": f"发生错误: {str(e)}"}

# ======================
# 页面配置
# ======================
st.set_page_config(
    page_title="熊熊的主页",
    page_icon="🐻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ======================
# 强制暗黑风格
# ======================
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(180deg, #0a0a0a 0%, #121212 100%) !important;
    }
    [data-testid="stHeader"] { background: #0a0a0a !important; }
    .card {
        background: rgba(30,30,30,0.6);
        border-radius: 24px;
        padding: 40px;
        margin-bottom: 30px;
        border: 1px solid rgba(255,255,255,0.08);
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }
    h1 { color: white !important; }
    h3 { color: #f0f0f0 !important; }
    p { color: #b0b0b0 !important; }
    .divider { height:1px; background: rgba(255,255,255,0.1); margin:20px 0; }
</style>
""", unsafe_allow_html=True)

# ======================
# 网站主体
# ======================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.title("🐻 熊熊的主页")
st.write("真诚交友 · 温暖陪伴 · 双向奔赴")
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
st.write("毕业于上海大学 · 退役军人 · 热爱生活")
st.markdown("</div>", unsafe_allow_html=True)

# ======================
# ✅ 天气查询功能（已嵌入）
# ======================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("🌤️ 天气查询工具")
city = st.text_input("请输入城市名称：", placeholder="例如：上海 北京 广州")

if st.button("🔍 查询天气"):
    if city:
        data = get_weather(city)
        if "error" in data:
            st.error(data["error"])
        else:
            st.success(f"📍 {data['city']}, {data['country']}")
            c = data["current"]
            st.write(f"🌤 当前天气：{c['weather']}")
            st.write(f"🌡 温度：{c['temperature']} | 体感：{c['feels_like']}")
            st.write(f"💧 湿度：{c['humidity']} | 💨 风速：{c['wind_speed']}")

            st.subheader("📅 未来3天预报")
            for day in data["forecast"]:
                st.write(f"{day['date']} | {day['min_temp']} ~ {day['max_temp']} | {day['weather']}")
st.markdown("</div>", unsafe_allow_html=True)

# ======================
# 关于我
# ======================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("关于我")
st.write("""
你好，我是熊熊。
毕业于上海大学，曾服役于部队，性格稳重、待人真诚。
期待认识同样真诚、温暖、热爱生活的朋友～
""")
st.markdown("</div>", unsafe_allow_html=True)

# ======================
# 页脚
# ======================
st.markdown("<div style='text-align:center;color:#666;margin-top:50px'>© 2025 熊熊的交友主页</div>", unsafe_allow_html=True)
