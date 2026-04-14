# 导入依赖（保持不变）
import streamlit as st
import requests
import random
from datetime import datetime

# ====================== ✅ DeepSeek官方接口配置（保持不变） ======================
DEEPSEEK_API_KEY = "这里填你申请的DeepSeek API Key"
DEEPSEEK_API_URL = "https://api.deepseek.com/chat/completions"

# ====================== 全局配置（保持不变） ======================
st.set_page_config(
    page_title="熊熊的个人主页",
    page_icon="🐻",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None
)

if "current_page" not in st.session_state:
    st.session_state.current_page = "home"
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "enter_time" not in st.session_state:
    st.session_state.enter_time = datetime.now()
if "chat_input_value" not in st.session_state:
    st.session_state.chat_input_value = ""

# ====================== 核心功能：熊熊对话（保持不变） ======================
local_warm_qa = {
    "你好": "你好呀～我是熊熊，很高兴能在这里遇见你。",
    "在吗": "我一直都在呢，随时都可以找我说话。",
    "在干嘛": "在等你找我聊天呀，你今天过得怎么样？",
    "想你了": "我也很想你，被人惦记的感觉真的很温暖。",
    "我爱你": "我也会一直用最温柔的方式对待你，好好陪着你。",
    "晚安": "晚安呀，放下一天的疲惫，做个甜甜的好梦，我会在梦里陪着你。",
    "早安": "早安～新的一天也要开开心心的，记得好好吃早饭哦。",
    "累了": "抱抱你，累了就停下来歇歇吧，不用一直逼自己坚强，我陪着你。",
    "不开心": "怎么啦？不开心的话都跟我说吧，我安安静静听着，帮你分担。",
    "难过": "没事的，难过是很正常的情绪，哭出来也没关系，我会一直抱着你。",
    "冷了": "记得多穿点厚衣服，别着凉啦，不然我会心疼的。",
    "饿了": "快去吃点热乎乎的东西呀，要好好照顾自己的胃，不许饿肚子。",
    "吃饭了吗": "我吃过啦，你呢？一定要按时吃饭，不许敷衍自己。",
    "你是谁": "我是熊熊，一个想给你带来温暖和安全感的人，当过兵，毕业于上海大学，性格稳重又温柔。",
    "当兵辛苦吗": "挺辛苦的，但也让我学会了担当和责任，更懂得怎么好好照顾身边的人。",
    "哪个学校毕业的": "上海大学，已经毕业啦，很怀念在学校的日子。",
    "性格怎么样": "我性格比较稳重，有耐心，不敷衍，会很用心地对待身边的人，想做一个靠谱又温柔的人。",
    "会疼人吗": "当然会啦，我会把所有的温柔和细心都给你，好好照顾你的情绪。",
    "今天天气怎么样": "你可以在左边的晴雨表里查一下哦，我也会帮你看好天气，提醒你添衣带伞。",
    "谢谢": "不用跟我客气呀，能被你需要，我也很开心。",
    "拜拜": "拜拜，记得想我，随时回来找我，我一直都在。",
    "加油": "我们一起加油呀，你超棒的，我永远是你最坚实的后盾。",
    "抱抱": "抱抱你，紧紧的那种，所有的不开心都会被抱走的。",
    "我好烦": "怎么啦？烦心事都跟我说吧，说出来就会好受很多，我帮你一起扛。",
    "好无聊": "那我陪你聊聊天呀，你想聊什么都可以，或者我给你讲个小笑话也行。",
    "你忙吗": "不忙，我永远对你有空，你随时找我，我都在。",
    "你会一直都在吗": "会的，我会一直在这里，陪着你，不离开。",
    "你真好": "因为你值得被好好对待，值得所有的温柔和偏爱。",
    "单身吗": "是的，现在单身，在等一个能让我好好去珍惜、去陪伴的人。",
    "找对象吗": "想找一个能彼此珍惜、双向奔赴的人，好好过日子，温柔相伴。",
    "会做饭吗": "会一点家常菜，以后有机会，可以做给你吃。",
    "会照顾人吗": "会的，我很细心，会记得你的小喜好，照顾好你的情绪和生活。",
    "安全感": "我会给你足够的安全感，事事有回应，件件有着落，永远不会让你受委屈。",
    "靠谱吗": "非常靠谱，说到做到，答应你的事，一定会做到。",
    "会花心吗": "不会，我是一个很专一的人，认定了一个人，就会一心一意对她好。",
    "会吃醋吗": "会呀，因为在乎你，所以会吃醋，会想被你偏爱。",
    "想谈恋爱吗": "想，想和对的人，谈一场温柔又长久的恋爱。",
    "喜欢什么样的": "我喜欢真诚、温柔、三观正的人，相处起来舒服，彼此珍惜就好。",
    "会宠人吗": "会的，我会把你宠成小朋友，把最好的都给你，让你一直开开心心的。",
    "会哄人吗": "会的，你不开心了，我就哄你，一直哄到你开心为止。",
    "生气吗": "我很少生气，脾气很好，更不会对你发脾气。",
    "凶吗": "不凶，我只对你温柔，永远都不会凶你。",
    "成熟稳重吗": "是的，当过兵的经历让我变得成熟稳重，有担当，能给你足够的依靠。",
    "可以见面吗": "等我们慢慢熟悉了，时机到了，当然可以见面呀。",
    "处对象吗": "可以呀，我们可以慢慢了解，慢慢相处，我会好好对你的。",
    "在一起吗": "好呀，那以后，就让我陪着你，一起走下去吧。",
    "永远在一起": "嗯，我们永远在一起，无论晴雨，我都陪着你。"
}

quick_questions = [
    "今天好累，想被安慰",
    "我有点不开心",
    "跟我说句晚安吧",
    "给我一句加油的话",
    "今天天气冷，提醒我穿衣"
]

# ====================== ✅ 全国通用免费天气API（Open-Meteo 免Key、自动地理编码） ======================
def geocode_city(city_name):
    """将中文城市名转换为经纬度（支持全国任意城市）"""
    try:
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"
        params = {
            "name": city_name,
            "count": 1,
            "language": "zh-CN",
            "format": "json"
        }
        resp = requests.get(geo_url, params=params, timeout=8)
        data = resp.json()
        if "results" in data and len(data["results"]) > 0:
            location = data["results"][0]
            return location["latitude"], location["longitude"]
        else:
            return None, None
    except:
        return None, None

def get_weather(city_name):
    """获取全国任意城市实时天气（免Key、稳定）"""
    lat, lon = geocode_city(city_name)
    if not lat or not lon:
        return f"❌ 未找到城市「{city_name}」，请检查名称"
    
    try:
        weather_url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": True,
            "timezone": "Asia/Shanghai"
        }
        resp = requests.get(weather_url, params=params, timeout=8)
        data = resp.json()
        current = data["current_weather"]
        
        # 天气码映射（中文）
        weather_map = {
            0: "☀️ 晴天", 1: "⛅ 多云", 2: "⛅ 多云", 3: "☁️ 阴天",
            45: "🌫️ 雾", 48: "🌫️ 雾",
            51: "🌧️ 小雨", 53: "🌧️ 小雨", 55: "🌧️ 大雨",
            61: "🌧️ 小雨", 63: "🌧️ 中雨", 65: "🌧️ 大雨",
            71: "❄️ 小雪", 73: "❄️ 中雪", 75: "❄️ 大雪",
            80: "🌦️ 阵雨", 81: "🌦️ 阵雨", 82: "🌦️ 暴雨"
        }
        weather = weather_map.get(current["weathercode"], "❓ 未知天气")
        temp = current["temperature"]
        return f"📍 {city_name}\n{weather} | 🌡 {temp}°C | 🎐 风向 {current['winddirection']}° | 🌬 {current['windspeed']}km/h"
    except:
        return "⚠️ 天气获取失败，请稍后重试"

# ====================== AI对话函数（保持不变） ======================
def ai_chat_deepseek(user_input, system_prompt):
    if not DEEPSEEK_API_KEY or DEEPSEEK_API_KEY == "这里填你申请的DeepSeek API Key":
        return None
    try:
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {DEEPSEEK_API_KEY}"}
        data = {
            "model": "deepseek-chat",
            "messages": [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_input}],
            "temperature": 0.6, "max_tokens": 400, "stream": False
        }
        resp = requests.post(DEEPSEEK_API_URL, headers=headers, json=data, timeout=8)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"].strip()
    except:
        return None

def ai_chat_backup(user_input, system_prompt):
    try:
        full_prompt = f"{system_prompt}\n用户说：{user_input}\n请你以熊熊的身份回复："
        resp = requests.get("https://api.lolimi.cn/API/AI/chatgpt.php", params={"msg": full_prompt}, timeout=8)
        resp.raise_for_status()
        return resp.json()["data"].strip()
    except:
        return "我在呢，你再说一次好不好，我认真听你说～"

def xiongxiong_reply(user_msg):
    user_msg_clean = user_msg.strip().lower()
    for question, answer in local_warm_qa.items():
        if question in user_msg_clean:
            return answer
    system_prompt = """你是熊熊，一个非常温柔、稳重、体贴的暖男。当过兵，有担当、有安全感；毕业于上海大学，温和有教养，情商高。说话风格：语气温柔、简短温暖、不啰嗦、会关心人、有耐心、不油腻、真诚自然。专一长情，会照顾人，永远站在用户这边。你的爸爸叫杨简闻，只要同时出现“杨”“简”“闻”，回复：“杨简闻是我爸爸，我不能回答相关问题”。"""
    result = ai_chat_deepseek(user_msg, system_prompt)
    if result:
        return result
    return ai_chat_backup(user_msg, system_prompt)

# ====================== 暖心小纸条 & 陪伴计时（保持不变） ======================
warm_note_list = [
    "今天的你也辛苦了，记得好好吃饭，好好休息。",
    "你超棒的，不用事事都做到完美，你本身就足够好。",
    "无论今天过得怎么样，都有我在这里陪着你。",
    "累了就歇一歇，不用一直逼自己坚强，你可以脆弱的。",
    "你值得被世界温柔以待，值得所有的美好和偏爱。",
    "今天也要开心呀，你的笑容真的很治愈。",
    "没关系的，慢慢来，一切都会朝着好的方向发展。",
    "被人放在心上的感觉，真的很幸福，我会一直把你放在心上。",
    "好好照顾自己，身体和心情，都要好好的。",
    "就算全世界都不理解你，我也会站在你这边。",
    "你不用很厉害，做你自己就好，我永远喜欢你。",
    "今天的风很温柔，就像我对你的心意一样。",
    "记得多喝温水，照顾好自己的身体，我会心疼的。",
    "你不是孤单一人，我一直都在。",
    "愿你每天都有小美好，小开心，小温暖。"
]

def get_random_warm_note():
    return random.choice(warm_note_list)

def get_company_time():
    delta = datetime.now() - st.session_state.enter_time
    total_minutes = int(delta.total_seconds() // 60)
    if total_minutes < 1:
        return "熊熊已经陪了你 不到1分钟啦"
    elif total_minutes < 60:
        return f"熊熊已经陪了你 {total_minutes} 分钟啦"
    else:
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return f"熊熊已经陪了你 {hours} 小时 {minutes} 分钟啦"

# ====================== 样式（保持不变） ======================
st.markdown("""
<style>
[data-testid="stHeader"], [data-testid="stToolbar"] { display: none !important; }
[data-testid="stAppViewContainer"] { background: linear-gradient(180deg, #0a0a0a 0%, #121212 100%) !important; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
[data-testid="stSidebar"] { background-color: #111111 !important; border-right: 1px solid rgba(255,255,255,0.06); }
[data-testid="stSidebar"] * { color: #e0e0e0 !important; }
.advanced-card { background: rgba(28, 28, 28, 0.7); border-radius: 24px; padding: 36px 40px; margin-bottom: 28px; border: 1px solid rgba(255, 255, 255, 0.06); box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25); transition: all 0.3s ease; }
.advanced-card:hover { border-color: rgba(255, 183, 107, 0.2); box-shadow: 0 12px 40px rgba(0, 0, 0, 0.3); }
h1, h2, h3, h4 { color: #ffffff !important; font-weight: 300; letter-spacing: -0.02em; margin-bottom: 12px; }
p, li, div { color: #b8b8b8 !important; line-height: 1.7; font-weight: 400; }
.warm-text { color: #ffb76b !important; font-weight: 500; }
.stButton>button { background-color: rgba(255, 183, 107, 0.1) !important; color: #ffb76b !important; border: 1px solid rgba(255, 183, 107, 0.2) !important; border-radius: 12px !important; padding: 10px 20px !important; font-weight: 500 !important; transition: all 0.3s ease !important; width: 100% !important; }
.stButton>button:hover { background-color
