# 导入库
import streamlit as st
import requests

# ======================
# 天气查询函数
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
            return {"error": f"未找到城市：{city_name}"}

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
                "weather": weather_descriptions.get(current["weather_code"], "未知")
            },
            "forecast": []
        }

        for i in range(len(daily["time"])):
            result["forecast"].append({
                "date": daily["time"][i],
                "max_temp": f"{daily['temperature_2m_max'][i]}°C",
                "min_temp": f"{daily['temperature_2m_min'][i]}°C",
                "weather": weather_descriptions.get(daily["weather_code"][i], "未知")
            })

        return result

    except:
        return {"error": "查询失败"}

# ======================
# 页面配置
# ======================
st.set_page_config(
    page_title="熊熊的主页",
    page_icon="🐻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================
# 暗黑样式
# ======================
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(180deg, #0a0a0a 0%, #121212 100%) !important;
    }
    [data-testid="stSidebar"] {
        background-color: #111 !important;
        border-right: 1px solid #222;
    }
    .card {
        background: rgba(30,30,30,0.6);
        border-radius: 20px;
        padding: 30px;
        margin-bottom: 25px;
        border: 1px solid rgba(255,255,255,0.08);
    }
    h1, h2, h3 { color: #fff !important; }
    p, div { color: #b0b0b0 !important; }
</style>
""", unsafe_allow_html=True)

# ======================
# 左侧边栏
# ======================
with st.sidebar:
    st.title("🐻 熊熊主页")
    st.divider()

    st.subheader("📋 菜单")
    st.button("🏠 首页", use_container_width=True)
    st.button("👤 关于我", use_container_width=True)
    st.button("💬 交友动态", use_container_width=True)

    st.divider()

    # ======================
    # ✅ 熊熊晴雨表查询（显眼版）
    # ======================
    st.subheader("🌤️ 熊熊晴雨表查询")
    city_input = st.text_input("输入城市", placeholder="例如：上海", label_visibility="visible")
    
    if st.button("🔍 查询天气", use_container_width=True):
        if city_input:
            data = get_weather(city_input)
            if "error" in data:
                st.error(data["error"])
            else:
                st.success(f"✅ {data['city']}")
                curr = data["current"]
                st.info(f"天气：{curr['weather']}")
                st.info(f"温度：{curr['temperature']}")

    st.divider()
    st.caption("© 2026 熊熊交友平台")

# ======================
# 右侧主内容
# ======================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.title("🐻 欢迎来到熊熊的交友主页")
st.write("真诚 · 稳重 · 温暖 · 热爱生活")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("关于我")
st.write("""
你好，我是熊熊。
毕业于上海大学，曾服役于部队，性格踏实稳重，待人真诚。
期待认识温暖、靠谱、三观契合的朋友。
""")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("交友理念")
st.write("尊重、真诚、双向奔赴，不敷衍、不冷暴力。")
st.markdown("</div>", unsafe_allow_html=True)
