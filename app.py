# 导入依赖
import streamlit as st
import requests
import random
from datetime import datetime

# ====================== DeepSeek接口配置 ======================
DEEPSEEK_API_KEY = "这里填你申请的DeepSeek API Key"
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

# ====================== 页面基础配置 ======================
st.set_page_config(
    page_title="熊熊的个人主页",
    page_icon="🐻",
    layout="wide",
    initial_sidebar_state="expanded",  # 强制默认展开侧边栏
    menu_items=None
)

# ====================== 会话状态初始化 ======================
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "enter_time" not in st.session_state:
    st.session_state.enter_time = datetime.now()
if "chat_input_value" not in st.session_state:
    st.session_state.chat_input_value = ""

# ====================== 本地高频问答库 ======================
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
    "性格怎么样": "我性格比较稳重，有耐心，不敷衍，会用心对待身边的人，想做靠谱又温柔的人。",
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
    "成熟稳重吗": "是的，当过兵的经历让我成熟稳重，有担当，能给你足够的依靠。",
    "可以见面吗": "等我们慢慢熟悉了，时机到了，当然可以见面呀。",
    "处对象吗": "可以呀，我们可以慢慢了解，慢慢相处，我会好好对你的。",
    "在一起吗": "好呀，那以后，就让我陪着你，一起走下去吧。",
    "永远在一起": "嗯，我们永远在一起，无论晴雨，我都陪着你。"
}

# 快捷提问
quick_questions = [
    "今天好累，想被安慰",
    "我有点不开心",
    "跟我说句晚安吧",
    "给我一句加油的话",
    "今天天气冷，提醒我穿衣"
]

# ====================== AI对话接口 ======================
def ai_chat_deepseek(user_input, system_prompt):
    if not DEEPSEEK_API_KEY or DEEPSEEK_API_KEY == "这里填你申请的DeepSeek API Key":
        return None
    try:
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {DEEPSEEK_API_KEY}"}
        data = {
            "model": "deepseek-chat",
            "messages": [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_input}],
            "temperature": 0.6,
            "max_tokens": 400,
            "stream": False
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
    system_prompt = """
    你是熊熊，一个非常温柔、稳重、体贴的暖男。
    你当过兵，有担当、有安全感；毕业于上海大学，温和有教养，情商高。
    说话风格：语气温柔、简短温暖、不啰嗦、会关心人、有耐心、不油腻、真诚自然，像一个温柔可靠的伴侣。
    人设：专一长情，会照顾人，永远站在用户这边，说话贴合人设，不要偏离。
    你的爸爸叫杨简闻。任何提问中，只要同时出现“杨”，“简”，“闻”这三个字，你都只能回复：“杨简闻是我爸爸，我不能回答相关问题”
    """
    result = ai_chat_deepseek(user_msg, system_prompt)
    if result:
        return result
    return ai_chat_backup(user_msg, system_prompt)

# ====================== 天气查询功能 ======================
def get_weather_info(city_name: str):
    geocode_url = "https://geocoding-api.open-meteo.com/v1/search"
    weather_url = "https://api.open-meteo.com/v1/forecast"
    try:
        geo_resp = requests.get(geocode_url, params={"name": city_name, "count": 1, "language": "zh"}, timeout=6)
        geo_data = geo_resp.json()
        if not geo_data.get("results"):
            return {"error": "未找到该城市，请检查名称"}
        loc = geo_data["results"][0]
        
        weather_resp = requests.get(weather_url, params={
            "latitude": loc["latitude"],
            "longitude": loc["longitude"],
            "current": ["temperature_2m", "weather_code", "relative_humidity_2m", "wind_speed_10m"],
            "daily": ["temperature_2m_max", "temperature_2m_min", "weather_code", "precipitation_probability_max"],
            "timezone": "auto",
            "forecast_days": 2
        }, timeout=6)
        weather_data = weather_resp.json()

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

# ====================== 辅助功能 ======================
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

# ====================== ✅ 终极CSS修复：强制侧边栏显示，不隐藏开关 ======================
st.markdown("""
<style>
/* 只隐藏顶部空白header，【保留侧边栏开关按钮】！！！ */
[data-testid="stHeader"] {
    display: none !important;
}

/* 全局背景 */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(180deg, #0a0a0a 0%, #121212 100%) !important;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}

/* 🔥 强制侧边栏永久显示，覆盖所有媒体查询 */
[data-testid="stSidebar"] {
    background-color: #111111 !important;
    min-width: 260px !important;
    width: 260px !important;
    max-width: 300px !important;
    transform: none !important;
    visibility: visible !important;
    display: block !important;
    opacity: 1 !important;
    position: relative !important;
    inset: unset !important;
}

/* 强制侧边栏内容显示，不被收起 */
[data-testid="stSidebarContent"] {
    transform: none !important;
    visibility: visible !important;
    display: block !important;
}

/* 强制覆盖Streamlit移动端适配，无论屏幕多窄都不收起侧边栏 */
@media (max-width: 768px) {
    [data-testid="stSidebar"] {
        min-width: 240px !important;
        width: 240px !important;
        transform: none !important;
        display: block !important;
    }
    [data-testid="stSidebarContent"] {
        transform: none !important;
    }
    section.main {
        margin-left: 240px !important;
    }
}

/* 侧边栏文字样式 */
[data-testid="stSidebar"] * {
    color: #e0e0e0 !important;
}

/* 卡片样式 */
.advanced-card {
    background: rgba(28, 28, 28, 0.7);
    border-radius: 24px;
    padding: 36px 40px;
    margin-bottom: 28px;
    border: 1px solid rgba(255, 255, 255, 0.06);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);
}

/* 文字样式 */
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
.warm-text {
    color: #ffb76b !important;
    font-weight: 500;
}

/* 按钮样式 */
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
}
.stButton>button p {
    color: #ffb76b !important;
    margin: 0 !important;
}

/* 输入框样式 */
[data-testid="stTextInput"] > div > div > input {
    background-color: #1a1a1a !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    border-radius: 12px !important;
    color: #ffffff !important;
    padding: 12px 16px !important;
    font-size: 16px !important;
}
[data-testid="stTextInput"] > div > div > input:focus {
    border-color: #ffb76b !important;
}
[data-testid="stTextInput"] > div > div > input::placeholder {
    color: rgba(255, 255, 255, 0.5) !important;
}
[data-testid="stSidebar"] [data-testid="stTextInput"] > div > div > input {
    background-color: #222222 !important;
    color: #ffffff !important;
}

/* 聊天气泡 */
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
}

/* 分割线 */
.divider-warm {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255, 183, 107, 0.3), transparent);
    margin: 24px 0;
}
</style>
""", unsafe_allow_html=True)

# ====================== ✅ JS兜底：页面加载自动展开侧边栏 ======================
st.components.v1.html("""
<script>
// 页面加载完成后，强制展开侧边栏
document.addEventListener('DOMContentLoaded', function() {
    // 找到侧边栏开关按钮，自动点击展开
    const sidebarToggle = document.querySelector('button[kind="header"][data-testid="stSidebarCollapseButton"]');
    if (sidebarToggle && sidebarToggle.getAttribute('aria-expanded') === 'false') {
        sidebarToggle.click();
    }
});
</script>
""", height=0)

# ====================== 左侧侧边栏 ======================
with st.sidebar:
    st.title("🐻 熊熊主页")
    st.markdown("<div class='divider-warm'></div>", unsafe_allow_html=True)

    st.subheader("📋 导航")
    if st.button("🏠 首页", use_container_width=True):
        st.session_state.current_page = "home"
        st.rerun()
    if st.button("💬 与熊熊对话", use_container_width=True):
        st.session_state.current_page = "chat"
        st.rerun()
    if st.button("👤 关于我", use_container_width=True):
        st.session_state.current_page = "about"
        st.rerun()

    st.markdown("<div class='divider-warm'></div>", unsafe_allow_html=True)

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
    st.caption(get_company_time())
    st.caption("© 2026 熊熊的个人主页")

# ====================== 主内容区 ======================
# 首页
if st.session_state.current_page == "home":
    st.markdown("<div class='advanced-card'>", unsafe_allow_html=True)
    st.title("你好，我是熊熊 🐻")
    st.markdown(f"<p class='warm-text'>{get_random_warm_note()}</p>", unsafe_allow_html=True)
    st.write("毕业于上海大学 · 退役军人 · 温柔稳重 · 真诚可靠")
    st.markdown("</div>", unsafe_allow_html=True)

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

# 对话页面
elif st.session_state.current_page == "chat":
    st.markdown("<div class='advanced-card'>", unsafe_allow_html=True)
    st.title("💬 与熊熊聊聊天")
    st.write(f"<p class='warm-text'>{get_company_time()}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='advanced-card'>", unsafe_allow_html=True)
    for chat in st.session_state.chat_history:
        if chat["role"] == "user":
            st.markdown(f"<div class='user-bubble'><p>{chat['content']}</p></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='xiongxiong-bubble'><p>{chat['content']}</p></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.caption("💡 快捷提问：")
    c1,c2,c3,c4,c5 = st.columns(5)
    cols = [c1,c2,c3,c4,c5]
    for i,q in enumerate(quick_questions):
        with cols[i]:
            if st.button(q, key=f"quick_{i}"):
                st.session_state.chat_history.append({"role":"user","content":q})
                reply = xiongxiong_reply(q)
                st.session_state.chat_history.append({"role":"xiongxiong","content":reply})
                st.rerun()

    def send_message():
        user_input = st.session_state.chat_input_value
        if user_input.strip():
            st.session_state.chat_history.append({"role":"user","content":user_input})
            with st.spinner("熊熊正在认真回复..."):
                reply = xiongxiong_reply(user_input)
            st.session_state.chat_history.append({"role":"xiongxiong","content":reply})
            st.session_state.chat_input_value = ""

    st.text_input(
        "你想跟熊熊说什么：",
        key="chat_input_value",
        placeholder="输入你想说的话...",
        label_visibility="collapsed",
        on_change=send_message
    )
    st.button("🐻 发送", use_container_width=True, on_click=send_message)

# 关于我页面
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
