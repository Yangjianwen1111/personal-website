# ====================== 极简华丽个人主页 | 侧边栏缩进/弹出完美修复版 ======================
import streamlit as st
from datetime import datetime

# ====================== 页面配置 ======================
st.set_page_config(
    page_title="我的主页",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ====================== 状态 ======================
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"
if "guestbook" not in st.session_state:
    st.session_state.guestbook = []

# ====================== 超级CSS：侧边栏按钮可用 + 华丽界面 ======================
st.markdown("""
<style>
/* 全局样式 */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0a0a0f 0%, #121218 100%) !important;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
[data-testid="stHeader"] {
    display: none !important;
}

/* 侧边栏强制可见 */
[data-testid="stSidebar"] {
    background: rgba(15,15,25,0.9) !important;
    backdrop-filter: blur(10px);
    border-right: 1px solid rgba(255,255,255,0.06);

}

/* 侧边栏开关按钮 白色高亮 绝对可用 */
button[data-testid="stSidebarCollapseButton"] {
    background: #8278ff !important;
    color: white !important;
    border-radius: 6px !important;
    padding: 6px 10px !important;

    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
}
button[data-testid="stSidebarCollapseButton"] svg {
    fill: white !important;
}

/* 玻璃卡片 */
.glass-card {
    background: rgba(25,25,35,0.6);
    border-radius: 24px;
    padding: 40px 44px;
    margin-bottom: 24px;
    border: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    transition: all 0.3s ease;
}
.glass-card:hover {
    transform: translateY(-4px);
    border-color: rgba(130,120,255,0.3);
}

/* 渐变标题 */
.gradient-title {
    background: linear-gradient(90deg, #8278ff 0%, #ff7eb3 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 700;
}

/* 按钮 */
.stButton>button {
    background: rgba(130,120,255,0.1) !important;
    color: white !important;
    border: 1px solid rgba(130,120,255,0.3) !important;
    border-radius: 12px !important;
    padding: 10px 24px !important;
    transition: all 0.3s;
}
.stButton>button:hover {
    background: rgba(130,120,255,0.2) !important;
    border-color: #8278ff !important;
}

/* 技能标签 */
.skill-tag {
    display: inline-block;
    background: rgba(130,120,255,0.1);
    border: 1px solid rgba(130,120,255,0.2);
    border-radius: 20px;
    padding: 6px 14px;
    margin: 4px 6px 4px 0;
    color: white !important;
}

/* 分割线 */
.gradient-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(130,120,255,0.4), transparent);
    margin: 24px 0;
}
</style>
""", unsafe_allow_html=True)


# ====================== 侧边栏 ======================
with st.sidebar:
    st.markdown("<h1 class='gradient-title' style='font-size:26px;'>✨ 我的主页</h1>", unsafe_allow_html=True)
    st.markdown("<div class='gradient-divider'></div>", unsafe_allow_html=True)

    st.subheader("📋 导航")

    if st.button("🏠 首页", use_container_width=True):
        st.session_state.current_page = "home"
        st.rerun()
    if st.button("👤 关于我", use_container_width=True):
        st.session_state.current_page = "about"
        st.rerun()
    if st.button("💼 项目", use_container_width=True):
        st.session_state.current_page = "projects"
        st.rerun()
    if st.button("📝 留言板", use_container_width=True):
        st.session_state.current_page = "guestbook"
        st.rerun()
    if st.button("📞 联系我", use_container_width=True):
        st.session_state.current_page = "contact"
        st.rerun()

    st.markdown("<div class='gradient-divider'></div>", unsafe_allow_html=True)
    st.caption(f"© {datetime.now().year} 个人主页")

# ====================== 页面内容 ======================
if st.session_state.current_page == "home":
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<h1 class='gradient-title' style='font-size:52px;'>你好，我是 XXX</h1>", unsafe_allow_html=True)
    st.markdown("<h3>极简风格 · 华丽界面 · 稳定不崩</h3>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("💡 关于我")
        st.write("温柔、稳重、热爱技术")
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("🚀 技能")
        st.write("Python / Streamlit / AI 应用")
        st.markdown("</div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("🌱 风格")
        st.write("极简、高级、质感")
        st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.current_page == "about":
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<h1 class='gradient-title'>关于我</h1>", unsafe_allow_html=True)
    st.write("这里填写你的个人介绍")
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.current_page == "projects":
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<h1 class='gradient-title'>我的项目</h1>", unsafe_allow_html=True)
    st.write("展示你的作品")
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.current_page == "guestbook":
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<h1 class='gradient-title'>留言板</h1>", unsafe_allow_html=True)
    st.text_input("昵称")
    st.text_area("留言")
    st.button("提交")
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.current_page == "contact":
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<h1 class='gradient-title'>联系我</h1>", unsafe_allow_html=True)
    st.write("📮 邮箱：xxx@xxx.com")
    st.markdown("</div>", unsafe_allow_html=True)
