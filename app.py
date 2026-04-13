# 导入库
import streamlit as st

# 1. 用官方配置强制锁定深色主题
st.set_page_config(
    page_title="熊熊的主页",
    page_icon="🐻",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items=None
)

# 2. 强制覆盖 Streamlit 默认样式 + 暗黑风格
st.markdown("""
<style>
    /* 覆盖 Streamlit 根容器，确保暗黑背景 */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(180deg, #0a0a0a 0%, #121212 100%) !important;
    }
    [data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stSidebar"] {
        background-color: #0a0a0a !important;
    }

    /* 玻璃态卡片系统 */
    .card {
        background: rgba(30, 30, 30, 0.6);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 24px;
        padding: 45px;
        margin-bottom: 50px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3), 
                    inset 0 1px 0 rgba(255, 255, 255, 0.05);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }

    .card:hover {
        transform: translateY(-4px);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5), 
                    0 0 40px rgba(255, 255, 255, 0.03),
                    inset 0 1px 0 rgba(255, 255, 255, 0.1);
        border-color: rgba(255, 255, 255, 0.15);
    }

    /* 主标题 */
    h1 {
        color: #ffffff !important;
        font-size: 56px;
        font-weight: 300;
        letter-spacing: -1.5px;
        margin-bottom: 15px;
        background: linear-gradient(135deg, #ffffff 0%, #a0a0a0 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    /* 副标题 */
    h3 {
        color: #f0f0f0 !important;
        font-size: 28px;
        font-weight: 400;
        letter-spacing: -0.5px;
        margin-bottom: 12px;
    }

    /* 正文 */
    p {
        color: #b0b0b0 !important;
        line-height: 1.8;
        font-size: 17px;
        font-weight: 350;
        letter-spacing: 0.2px;
    }

    /* 标签 */
    .tag {
        display: inline-block;
        background: rgba(255, 255, 255, 0.08);
        color: #d0d0d0;
        padding: 6px 16px;
        border-radius: 20px;
        font-size: 13px;
        margin-right: 8px;
        margin-top: 10px;
        border: 1px solid rgba(255, 255, 255, 0.06);
        transition: all 0.3s ease;
    }

    .tag:hover {
        background: rgba(255, 255, 255, 0.12);
        color: #ffffff;
    }

    /* 分隔线 */
    .divider {
        height: 1px;
        background: linear-gradient(90deg, 
            transparent 0%, 
            rgba(255, 255, 255, 0.08) 50%, 
            transparent 100%);
        margin: 30px 0;
    }

    /* 引用 */
    .quote {
        border-left: 3px solid rgba(255, 255, 255, 0.2);
        padding-left: 20px;
        margin: 20px 0;
        font-style: italic;
        color: #c0c0c0 !important;
    }

    /* 页脚 */
    .footer {
        text-align: center;
        color: #505050 !important;
        font-size: 14px;
        padding: 40px 0;
        letter-spacing: 0.5px;
    }

    /* 滚动条 */
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: #0a0a0a;
    }
    ::-webkit-scrollbar-thumb {
        background: rgba(255, 255, 255, 0.15);
        border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(255, 255, 255, 0.25);
    }
</style>
""", unsafe_allow_html=True)

# Hero 区域 - 个人介绍
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.title("🐻 熊熊的主页")
st.write("真诚交友 · 温暖陪伴 · 双向奔赴")
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
st.write("一个靠谱、有担当、热爱生活的人，期待与你相遇。")
st.markdown("</div>", unsafe_allow_html=True)

# 个人背景卡片
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("关于我")
st.write("你好，我是熊熊。")
st.write("毕业于上海大学，曾服役于部队，习惯了自律、守时和责任。")
st.write("性格稳重，待人真诚，喜欢在生活中发现温暖的瞬间。")
st.markdown("""
<div class='quote'>
"保持热爱，奔赴山海。愿我们都能被温柔以待。"
</div>
""", unsafe_allow_html=True)
st.markdown("<span class='tag'>上海</span><span class='tag'>上海大学</span><span class='tag'>退役军人</span><span class='tag'>真诚交友</span>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# 兴趣爱好卡片
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("我的日常")
st.write("喜欢健身、阅读和探索城市的角落。")
st.write("平时也会研究一些数码产品，偶尔打打游戏。")
st.write("更期待的是，能找到一个聊得来的人，一起分享生活中的小美好。")
st.markdown("</div>", unsafe_allow_html=True)

# 交友宣言卡片
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("交友宣言")
st.write("我期待的关系，是平等、尊重和互相支持。")
st.write("希望你也是一个真诚、有温度、对生活有热情的人。")
st.markdown("""
<div class='quote'>
"两个人在一起，是为了成为更好的彼此。"
</div>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# 页脚
st.markdown("<div class='footer'>© 2025 熊熊的主页 · 真诚交友</div>", unsafe_allow_html=True)
