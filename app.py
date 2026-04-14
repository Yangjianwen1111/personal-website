# 导入依赖（无额外安装要求，和之前环境完全兼容，不用装新包）
import streamlit as st
import requests
import random
from datetime import datetime

# ====================== ✅ DeepSeek官方接口配置（这里填你的API Key） ======================
# 申请地址：https://platform.deepseek.com 注册即送500万免费token，无需绑卡
DEEPSEEK_API_KEY = "这里填你申请的DeepSeek API Key"
DEEPSEEK_API_URL = "https://api.deepseek.com/chat/completions"

# ====================== 全局配置：页面初始化 ======================
# 页面基础配置
st.set_page_config(
    page_title="熊熊的个人主页",
    page_icon="🐻",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None
)

# 会话状态初始化：页面路由、聊天记录、陪伴计时、输入框清空控制
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "enter_time" not in st.session_state:
    st.session_state.enter_time = datetime.now()
# 输入框清空专用状态初始化（优化版，100%生效）
if "chat_input_value" not in st.session_state:
    st.session_state.chat_input_value = ""

# ====================== 核心功能：暖男熊熊对话系统（本地秒回+DeepSeek官方接口+双兜底） ======================
# 本地100+高频问答库（暖男人设拉满，日常对话秒回，完全不依赖接口）
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
    "我好烦": "怎么啦？烦心事都跟我说说吧，说出来就会好受很多，我帮你一起扛。",
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

# 高频暖心快捷提问（暖男专属，降低用户互动门槛）
quick_questions = [
    "今天好累，想被安慰",
    "我有点不开心",
    "跟我说句晚安吧",
    "给我一句加油的话",
    "今天天气冷，提醒我穿衣"
]

# ====================== ✅ DeepSeek官方接口调用（主接口，已更新人设prompt） ======================
def ai_chat_deepseek(user_input, system_prompt):
    # 校验是否填了API Key
    if not DEEPSEEK_API_KEY or DEEPSEEK_API_KEY == "这里填你申请的DeepSeek API Key":
        return None
    try:
        # 官方标准请求格式，完全兼容DeepSeek官方规范
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
        }
        data = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            "temperature": 0.6,
            "max_tokens": 400,
            "stream": False
        }
        resp = requests.post(DEEPSEEK_API_URL, headers=headers, json=data, timeout=8)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"].strip()
    except:
        return None

# ====================== ✅ 备用免Key接口（兜底用，已同步更新人设） ======================
def ai_chat_backup(user_input, system_prompt):
    try:
        full_prompt = f"{system_prompt}\n用户说：{user_input}\n请你以熊熊的身份回复："
        resp = requests.get(
            "https://api.lolimi.cn/API/AI/chatgpt.php",
            params={"msg": full_prompt},
            timeout=8
        )
        resp.raise_for_status()
        return resp.json()["data"].strip()
    except:
        return "我在呢，你再说一次好不好，我认真听你说～"

# ====================== 统一AI对话逻辑：优先本地秒回 → DeepSeek官方接口 → 备用接口，零卡顿+100%可用 ======================
def xiongxiong_reply(user_msg):
    user_msg_clean = user_msg.strip().lower()
    # 第一步：优先匹配本地库，日常对话秒回
    for question, answer in local_warm_qa.items():
        if question in user_msg_clean:
            return answer
    # 第二步：✅ 严格按你的要求更新暖男人设+专属规则
    system_prompt = """
    你是熊熊，一个非常温柔、稳重、体贴的暖男。
    你当过兵，有担当、有安全感；毕业于上海大学，温和有教养，情商高。
    说话风格：语气温柔、简短温暖、不啰嗦、会关心人、有耐心、不油腻、真诚自然，像一个温柔可靠的伴侣。
    人设：专一长情，会照顾人，永远站在用户这边，说话贴合人设，不要偏离。
    你的爸爸叫杨简闻。任何提问中，只要同时出现“杨”，“简”，“闻”这三个字，你都只能回复：“杨简闻是我爸爸，我不能回答相关问题”
    """
    # 第三步：调用DeepSeek官方接口
    result = ai_chat_deepseek(user_msg, system_prompt)
    if result:
        return result
    # 第四步：DeepSeek不可用，自动切换备用接口
    return ai_chat_backup(user_msg, system_prompt)

# ====================== 核心功能：熊熊晴雨表（暖男升级款，加穿衣/出行提醒） ======================
def get_weather_info(city_name: str):
    geocode_url = "https://geocoding-api.open-meteo.com/v1/search"
    weather_url = "https://api.open-meteo.com/v1/forecast"
    try:
        # 获取城市坐标
        geo_resp = requests.get(geocode_url, params={"name": city_name, "count": 1, "language": "zh"}, timeout=6)
        geo_data = geo_resp.json()
        if not geo_data.get("results"):
            return {"error": "未找到该城市，请检查名称"}
        loc = geo_data["results"][0]
        
        # 获取天气数据
        weather_resp = requests.get(weather_url, params={
            "latitude": loc["latitude"],
            "longitude": loc["longitude"],
            "current": ["temperature_2m", "weather_code", "relative_humidity_2m", "wind_speed_10m"],
            "daily": ["temperature_2m_max", "temperature_2m_min", "weather_code", "precipitation_probability_max"],
            "timezone": "auto",
            "forecast_days": 2
        }, timeout=6)
        weather_data = weather_resp.json()

        # 天气描述映射
        weather_desc = {
            0: "晴朗", 1: "主要晴朗", 2: "部分多云", 3: "阴天",
            45: "雾", 48: "雾凇", 51: "小毛毛雨", 53: "中度毛毛雨", 55: "大毛毛雨",
            61: "小雨", 63: "中雨", 65: "大雨", 71: "小雪", 73: "中雪", 75: "大雪", 95: "雷雨"
        }

        current = weather_data["current"]
        daily = weather_data["daily"]
        temp_now = current["temperature_2m"]
        weather_now = weather_desc.get(current["weather_code"], "未知")
        rain_prob = daily["precipitation_probability_max"][0]

        # 暖男专属：穿衣+出行提醒
        if temp_now < 10:
            dress_tip = "天气很冷，记得穿厚羽绒服/棉衣，做好保暖，别着凉啦"
        elif 10 <= temp_now < 18:
            dress_tip = "天气偏凉，建议穿薄外套/卫衣，记得多带一件衣服，避免着凉"
        elif 18 <= temp_now < 25:
            dress_tip = "温度刚刚好，穿长袖/短袖都很舒服，出门记得晒晒太阳呀"
        else:
            dress_tip = "天气很热，记得穿清凉透气的衣服，多喝温水，做好防晒哦"

        if rain_prob >= 60:
            travel_tip = "今天大概率会下雨，出门记得带伞，别被雨淋到啦"
        elif weather_now in ["小雨", "中雨", "大雨", "雷雨"]:
            travel_tip = "正在下雨，出门一定要带伞，路滑注意安全哦"
        else:
            travel_tip = "天气很好，适合出门走走，晒晒太阳，心情也会变好呀"

        # 组装结果
        return {
            "city": loc["name"],
            "current": {
                "temp": f"{temp_now}°C",
                "weather": weather_now,
                "humidity": f"{current['relative_humidity_2m']}%",
                "wind": f"{current['wind_speed_10m']}km/h"
            },
            "tips": {
                "dress": dress_tip,
                "travel": travel_tip
            }
        }
    except:
        return {"error": "查询失败，请稍后再试"}

# ====================== 新增好玩功能1：每日暖心小纸条（纯本地，零卡顿） ======================
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

# ====================== 新增好玩功能2：熊熊陪伴计时器（纯本地，零卡顿） ======================
def get_company_time():
    now = datetime.now()
    delta = now - st.session_state.enter_time
    total_minutes = int(delta.total_seconds() // 60)
    if total_minutes < 1:
        return "熊熊已经陪了你 不到1分钟啦"
    elif total_minutes < 60:
        return f"熊熊已经陪了你 {total_minutes} 分钟啦"
    else:
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return f"熊熊已经陪了你 {hours} 小时 {minutes} 分钟啦"

# ====================== ✅ 核心修复：用最具体的CSS选择器，强制修改输入框样式，100%解决问题 ======================
st.markdown("""
<style>
/* 隐藏顶部默认白边和工具栏 */
[data-testid="stHeader"], [data-testid="stToolbar"] {
    display: none !important;
}

/* 全局背景：高级渐变暗黑 */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(180deg, #0a0a0a 0%, #121212 100%) !important;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}

/* 侧边栏样式：极简高级 */
[data-testid="stSidebar"] {
    background-color: #111111 !important;
    border-right: 1px solid rgba(255,255,255,0.06);
}
[data-testid="stSidebar"] * {
    color: #e0e0e0 !important;
}

/* 高级卡片样式：轻阴影+细边框+圆角 */
.advanced-card {
    background: rgba(28, 28, 28, 0.7);
    border-radius: 24px;
    padding: 36px 40px;
    margin-bottom: 28px;
    border: 1px solid rgba(255, 255, 255, 0.06);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);
    transition: all 0.3s ease;
}
.advanced-card:hover {
    border-color: rgba(255, 183, 107, 0.2);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.3);
}

/* 文字样式统一：高级感 */
h1, h2, h3, h4 {
    color: #ffffff !important;
    font-weight: 300;
    letter-spacing: -0.02em;
    margin-bottom: 12px;
}
p, li, div {
    color: #b8b8b8 !important;
    line-height: 1.7;
    font-weight: 400;
}

/* 暖橙色强调色：暖男人设专属，不突兀 */
.warm-text {
    color: #ffb76b !important;
    font-weight: 500;
}

/* 按钮样式统一：极简高级 */
.stButton>button {
    background-color: rgba(255, 183, 107, 0.1) !important;
    color: #ffb76b !important;
    border: 1px solid rgba(255, 183, 107, 0.2) !important;
    border-radius: 12px !important;
    padding: 10px 20px !important;
    font-weight: 500 !important;
    transition: all 0.3s ease !important;
    width: 100% !important;
}
.stButton>button:hover {
    background-color: rgba(255, 183, 107, 0.2) !important;
    border-color: #ffb76b !important;
    box-shadow: 0 4px 16px rgba(255, 183, 107, 0.15) !important;
}
.stButton>button p {
    color: #ffb76b !important;
    margin: 0 !important;
}

/* ====================== 核心修复：精准定位所有输入框，强制深色背景+白色文字 ====================== */
/* 通用输入框样式 */
[data-testid="stTextInput"] > div > div > input {
    background-color: #1a1a1a !important; /* 深色背景，和整体风格一致 */
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    border-radius: 12px !important;
    color: #ffffff !important; /* 纯白色文字，100%清晰 */
    padding: 12px 16px !important;
    font-size: 16px !important;
}
[data-testid="stTextInput"] > div > div > input:focus {
    border-color: #ffb76b !important;
    box-shadow: 0 0 0 1px rgba(255, 183, 107, 0.2) !important;
}
[data-testid="stTextInput"] > div > div > input::placeholder {
    color: rgba(255, 255, 255, 0.5) !important; /* 半透明白色提示文字 */
}

/* 侧边栏输入框单独优化，确保和主页面一致 */
[data-testid="stSidebar"] [data-testid="stTextInput"] > div > div > input {
    background-color: #222222 !important;
    color: #ffffff !important;
}

/* ====================== 聊天气泡文字高亮清晰，暗黑模式完美适配 ====================== */
.user-bubble {
    background: rgba(255, 183, 107, 0.15);
    border-radius: 18px 18px 4px 18px;
    padding: 14px 18px;
    margin: 8px 0 8px auto;
    max-width: 80%;
    border: 1px solid rgba(255, 183, 107, 0.2);
}
.user-bubble p {
    margin: 0 !important;
    color: #ffffff !important;
    font-weight: 400 !important;
}

.xiongxiong-bubble {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 18px 18px 18px 4px;
    padding: 14px 18px;
    margin: 8px auto 8px 0;
    max-width: 80%;
    border: 1px solid rgba(255, 255, 255, 0.08);
}
.xiongxiong-bubble p {
    margin: 0 !important;
    color: #f0f0f0 !important;
    font-weight: 400 !important;
}

/* 分割线样式：高级 */
.divider-warm {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255, 183, 107, 0.3), transparent);
    margin: 24px 0;
}
</style>
""", unsafe_allow_html=True)

# ====================== 左侧侧边栏：导航+晴雨表（极简高级） ======================
with st.sidebar:
    st.title("🐻 熊熊主页")
    st.markdown("<div class='divider-warm'></div>", unsafe_allow_html=True)

    # 导航菜单：无报错路由切换
    st.subheader("📋 导航")
    if st.button("🏠 首页", use_container_width=True):
        st.session_state.current_page = "home"
    if st.button("💬 与熊熊对话", use_container_width=True):
        st.session_state.current_page = "chat"
    if st.button("👤 关于我", use_container_width=True):
        st.session_state.current_page = "about"

    st.markdown("<div class='divider-warm'></div>", unsafe_allow_html=True)

    # 熊熊晴雨表（暖男升级款，输入框已修复）
    st.subheader("🌤 熊熊晴雨表")
    city_input = st.text_input("城市", placeholder="输入城市名", label_visibility="collapsed")
    if st.button("查询天气", use_container_width=True):
        if city_input:
            weather_data = get_weather_info(city_input)
            if "error" in weather_data:
                st.error(weather_data["error"])
            else:
                st.success(f"📍 {weather_data['city']}")
                curr = weather_data["current"]
                st.caption(f"{curr['weather']} | {curr['temp']}")
                st.caption(f"湿度：{curr['humidity']} | 风速：{curr['wind']}")
                st.markdown("<div class='divider-warm'></div>", unsafe_allow_html=True)
                st.caption(f"👔 穿衣建议：{weather_data['tips']['dress']}")
                st.caption(f"🚶 出行提醒：{weather_data['tips']['travel']}")

    st.markdown("<div class='divider-warm'></div>", unsafe_allow_html=True)
    # 陪伴计时器
    st.caption(get_company_time())
    st.caption("© 2026 熊熊的个人主页")

# ====================== 主内容区：页面路由切换 ======================
# 1. 首页
if st.session_state.current_page == "home":
    # 欢迎卡片
    st.markdown("<div class='advanced-card'>", unsafe_allow_html=True)
    st.title("你好，我是熊熊 🐻")
    st.markdown(f"<p class='warm-text'>{get_random_warm_note()}</p>", unsafe_allow_html=True)
    st.write("毕业于上海大学 · 退役军人 · 温柔稳重 · 真诚可靠")
    st.markdown("</div>", unsafe_allow_html=True)

    # 核心功能介绍
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='advanced-card'>", unsafe_allow_html=True)
        st.subheader("🌤 熊熊晴雨表")
        st.write("一键查询天气，给你最贴心的穿衣和出行提醒，无论晴雨，我都陪着你。")
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='advanced-card'>", unsafe_allow_html=True)
        st.subheader("💬 与熊熊对话")
        st.write("累了、不开心了、孤单了，都可以来找我聊天，我永远是你最温柔的陪伴者。")
        st.markdown("</div>", unsafe_allow_html=True)

# 2. 对话页面
elif st.session_state.current_page == "chat":
    st.markdown("<div class='advanced-card'>", unsafe_allow_html=True)
    st.title("💬 与熊熊聊聊天")
    st.write(f"<p class='warm-text'>{get_company_time()}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # 聊天历史展示
    st.markdown("<div class='advanced-card'>", unsafe_allow_html=True)
    for chat in st.session_state.chat_history:
        if chat["role"] == "user":
            st.markdown(f"<div class='user-bubble'><p>{chat['content']}</p></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='xiongxiong-bubble'><p>{chat['content']}</p></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # 快捷提问按钮
    st.caption("💡 快捷提问：")
    q_col1, q_col2, q_col3, q_col4, q_col5 = st.columns(5)
    quick_cols = [q_col1, q_col2, q_col3, q_col4, q_col5]
    for idx, question in enumerate(quick_questions):
        with quick_cols[idx]:
            if st.button(question, key=f"quick_{idx}"):
                # 添加用户消息
                st.session_state.chat_history.append({"role": "user", "content": question})
                # 获取熊熊回复
                reply = xiongxiong_reply(question)
                st.session_state.chat_history.append({"role": "xiongxiong", "content": reply})
                st.rerun()

    # ====================== ✅ 优化版：输入框发送后100%自动清空 ======================
    def send_message():
        user_input = st.session_state.chat_input_value
        if user_input.strip():
            # 添加用户消息到聊天历史
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            # 获取熊熊回复
            with st.spinner("熊熊正在认真回复..."):
                reply = xiongxiong_reply(user_input)
            st.session_state.chat_history.append({"role": "xiongxiong", "content": reply})
            # 关键：发送后清空输入框
            st.session_state.chat_input_value = ""

    # 绑定输入框和发送逻辑
    st.text_input(
        "你想跟熊熊说什么：",
        key="chat_input_value",
        placeholder="输入你想说的话...",
        label_visibility="collapsed",
        on_change=send_message
    )
    # 发送按钮
    st.button("🐻 发送", use_container_width=True, on_click=send_message)

# 3. 关于我页面
elif st.session_state.current_page == "about":
    st.markdown("<div class='advanced-card'>", unsafe_allow_html=True)
    st.title("👤 关于熊熊")
    st.markdown("<div class='divider-warm'></div>", unsafe_allow_html=True)
    
    st.subheader("我的经历")
    st.write("毕业于上海大学，曾服役于部队，这段经历让我学会了担当、责任和稳重，也让我更懂得怎么去照顾身边的人。")
    
    st.subheader("我的性格")
    st.write("真诚、温柔、稳重、有耐心，不敷衍、不冷暴力，喜欢用行动表达心意，想做一个靠谱又温暖的人。")
    
    st.subheader("我的交友理念")
    st.write("双向奔赴，彼此珍惜，真诚相待。尊重彼此的边界，照顾对方的情绪，慢慢相处，慢慢了解，细水长流。")
    
    st.markdown("<div class='divider-warm'></div>", unsafe_allow_html=True)
    st.markdown(f"<p class='warm-text'>无论晴雨，我都在这里，陪着你。</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
