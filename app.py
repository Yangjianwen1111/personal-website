# ====================== 仅依赖streamlit，零额外安装，100%稳定 ======================
import streamlit as st
from datetime import datetime

# ====================== 页面基础配置（原生写法，零hack） ======================
st.set_page_config(
    page_title="我的个人主页",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None
)

# ====================== 会话状态初始化（极简，无冲突） ======================
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"
if "guestbook" not in st.session_state:
    st.session_state.guestbook = []

# ====================== 安全CSS美化（只改视觉，不动布局，绝对不崩） ======================
st.markdown("""
<style>
/* 全局背景：极简暗黑渐变 */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0a0a0f 0%, #121218 100%) !important;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}

/* 隐藏顶部空白，保留侧边栏开关（绝对不碰侧边栏布局） */
[data-testid="stHeader"] {
    display: none !important;
}

/* 侧边栏：玻璃态极简设计 */
[data-testid="stSidebar"] {
    background: rgba(15, 15, 25, 0.8) !important;
    border-right: 1px solid rgba(255,255,255,0.06);
    backdrop-filter: blur(10px);
}
[data-testid="stSidebar"] * {
    color: #f0f0f0 !important;
}

/* 玻璃态卡片：核心华丽效果，极简结构 */
.glass-card {
    background: rgba(25, 25, 35, 0.6);
    border-radius: 24px;
    padding: 40px 44px;
    margin-bottom: 24px;
    border: 1px solid rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(12px);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
/* 卡片hover微动效：华丽但不突兀 */
.glass-card:hover {
    transform: translateY(-4px);
    border-color: rgba(130, 120, 255, 0.3);
    box-shadow: 0 12px 40px rgba(130, 120, 255, 0.15);
}

/* 渐变标题：极简华丽 */
.gradient-title {
    background: linear-gradient(90deg, #8278ff 0%, #ff7eb3 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-weight: 700;
    letter-spacing: -0.03em;
}

/* 文字样式统一 */
h1, h2, h3, h4 {
    color: #ffffff !important;
    font-weight: 600;
    letter-spacing: -0.02em;
    margin-bottom: 12px;
}
p, li, div {
    color: #c0c0c8 !important;
    line-height: 1.7;
    font-weight: 400;
}

/* 高亮文字 */
.highlight-text {
    color: #8278ff !important;
    font-weight: 500;
}

/* 按钮样式：极简华丽，微动效 */
.stButton>button {
    background: rgba(130, 120, 255, 0.1) !important;
    color: #ffffff !important;
    border: 1px solid rgba(130, 120, 255, 0.3) !important;
    border-radius: 12px !important;
    padding: 10px 24px !important;
    font-weight: 500 !important;
    transition: all 0.3s ease !important;
    width: 100% !important;
}
.stButton>button:hover {
    background: rgba(130, 120, 255, 0.2) !important;
    border-color: #8278ff !important;
    transform: translateY(-2px);
    box-shadow: 0 4px 16px rgba(130, 120, 255, 0.2) !important;
}
.stButton>button p {
    margin: 0 !important;
}

/* 输入框样式 */
[data-testid="stTextInput"] > div > div > input,
[data-testid="stTextArea"] > div > div > textarea {
    background: rgba(25, 25, 35, 0.6) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 12px !important;
    color: #ffffff !important;
    padding: 12px 16px !important;
    font-size: 15px !important;
    backdrop-filter: blur(10px);
}
[data-testid="stTextInput"] > div > div > input:focus,
[data-testid="stTextArea"] > div > div > textarea:focus {
    border-color: #8278ff !important;
    box-shadow: 0 0 0 1px rgba(130, 120, 255, 0.2) !important;
}
[data-testid="stTextInput"] > div > div > input::placeholder,
[data-testid="stTextArea"] > div > div > textarea::placeholder {
    color: rgba(255, 255, 255, 0.4) !important;
}

/* 技能标签 */
.skill-tag {
    display: inline-block;
    background: rgba(130, 120, 255, 0.1);
    border: 1px solid rgba(130, 120, 255, 0.2);
    border-radius: 20px;
    padding: 6px 14px;
    margin: 4px 6px 4px 0;
    font-size: 14px;
    color: #ffffff !important;
}

/* 渐变分割线 */
.gradient-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(130, 120, 255, 0.4), transparent);
    margin: 32px 0;
}
</style>
""", unsafe_allow_html=True)

# ====================== 侧边栏导航（原生写法，绝对稳定） ======================
with st.sidebar:
    st.markdown("<h1 class='gradient-title' style='font-size: 28px;'>✨ 我的主页</h1>", unsafe_allow_html=True)
    st.markdown("<div class='gradient-divider'></div>", unsafe_allow_html=True)

    # 导航菜单
    st.subheader("📋 导航栏")
    if st.button("🏠 首页", use_container_width=True):
        st.session_state.current_page = "home"
        st.rerun()
    if st.button("👤 关于我", use_container_width=True):
        st.session_state.current_page = "about"
        st.rerun()
    if st.button("💼 我的项目", use_container_width=True):
        st.session_state.current_page = "projects"
        st.rerun()
    if st.button("📝 留言板", use_container_width=True):
        st.session_state.current_page = "guestbook"
        st.rerun()
    if st.button("📞 联系我", use_container_width=True):
        st.session_state.current_page = "contact"
        st.rerun()

    st.markdown("<div class='gradient-divider'></div>", unsafe_allow_html=True)
    st.caption(f"© {datetime.now().year} 我的个人主页")
    st.caption("Built with Streamlit")

# ====================== 页面内容区 ======================
# 1. 首页
if st.session_state.current_page == "home":
    # 主视觉卡片
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<h1 class='gradient-title' style='font-size: 56px; margin-bottom: 20px;'>你好，我是XXX</h1>",
                unsafe_allow_html=True)
    st.markdown(
        "<h3 style='color: #c0c0c8; font-weight: 400; margin-bottom: 30px;'>一个专注于XX领域的创作者 / 开发者 / 设计师</h3>",
        unsafe_allow_html=True)
    st.markdown("<p class='highlight-text' style='font-size: 18px;'>热爱创作，专注细节，用代码/设计创造有温度的作品</p>",
                unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # 核心亮点卡片
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("💡 专业能力")
        st.write("深耕XX领域，拥有XX年实战经验，擅长从0到1打造完整作品")
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("🚀 作品理念")
        st.write("极简至上，拒绝冗余，每一个作品都追求实用与美感的平衡")
        st.markdown("</div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("🌱 成长态度")
        st.write("保持好奇，持续学习，在热爱的领域里稳步前行，永远对世界充满热情")
        st.markdown("</div>", unsafe_allow_html=True)

# 2. 关于我
elif st.session_state.current_page == "about":
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<h1 class='gradient-title'>关于我</h1>", unsafe_allow_html=True)
    st.markdown("<div class='gradient-divider'></div>", unsafe_allow_html=True)

    st.subheader("👋 个人介绍")
    st.write("""
    你好，我是XXX，现居XX城市。
    毕业于XX大学XX专业，目前从事XX行业/职业，拥有XX年相关经验。
    我始终相信，把热爱的事情做到极致，便有了价值。
    """)

    st.markdown("<div class='gradient-divider'></div>", unsafe_allow_html=True)

    st.subheader("🛠 我的技能栈")
    st.markdown("""
    <span class='skill-tag'>Python</span>
    <span class='skill-tag'>Streamlit</span>
    <span class='skill-tag'>数据分析</span>
    <span class='skill-tag'>AI应用开发</span>
    <span class='skill-tag'>UI/UX设计</span>
    <span class='skill-tag'>项目管理</span>
    """, unsafe_allow_html=True)

    st.markdown("<div class='gradient-divider'></div>", unsafe_allow_html=True)

    st.subheader("🎯 我的热爱")
    st.write("📚 喜欢阅读，尤其偏爱科技、人文类书籍")
    st.write("✍️ 坚持创作，定期分享自己的技术/行业思考")
    st.write("🌍 热爱旅行，喜欢用镜头记录不同的风景")
    st.write("💻 沉迷代码，享受用技术解决实际问题的成就感")

    st.markdown("</div>", unsafe_allow_html=True)

# 3. 我的项目
elif st.session_state.current_page == "projects":
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<h1 class='gradient-title'>我的项目</h1>", unsafe_allow_html=True)
    st.write("这里记录了我做过的一些有意思的项目，每一个都倾注了我的心血")
    st.markdown("</div>", unsafe_allow_html=True)

    # 项目卡片
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("🔥 项目一：熊熊AI陪伴主页")
        st.write("基于Streamlit开发的AI陪伴个人主页，支持实时对话、天气查询、暖心提醒等功能，暗黑极简设计，部署即用。")
        st.markdown("<p class='highlight-text'>技术栈：Python · Streamlit · 大模型API</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("📊 项目二：数据分析可视化平台")
        st.write("一站式数据分析工具，支持数据上传、清洗、可视化分析，自动生成分析报告，零代码也能轻松上手。")
        st.markdown("<p class='highlight-text'>技术栈：Python · Pandas · Streamlit · Plotly</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("🤖 项目三：AI大模型应用开发")
        st.write("基于开源大模型开发的垂直领域应用，支持知识库问答、内容生成、多轮对话，适配多种部署环境。")
        st.markdown("<p class='highlight-text'>技术栈：Python · LangChain · FastAPI · Streamlit</p>",
                    unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("🎨 项目四：个人设计作品集")
        st.write("个人UI/UX设计作品集，涵盖APP、网页、品牌设计等多个领域，主打极简实用的设计风格。")
        st.markdown("<p class='highlight-text'>设计工具：Figma · PS · AI</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# 4. 留言板
elif st.session_state.current_page == "guestbook":
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<h1 class='gradient-title'>留言板</h1>", unsafe_allow_html=True)
    st.write("有什么想对我说的，都可以在这里留下痕迹～")
    st.markdown("<div class='gradient-divider'></div>", unsafe_allow_html=True)

    # 留言输入
    nickname = st.text_input("你的昵称", placeholder="怎么称呼你呢？")
    message = st.text_area("你的留言", placeholder="想对我说点什么...", height=120)
    if st.button("💌 提交留言", use_container_width=True):
        if nickname.strip() and message.strip():
            st.session_state.guestbook.insert(0, {
                "nickname": nickname,
                "message": message,
                "time": datetime.now().strftime("%Y-%m-%d %H:%M")
            })
            st.success("留言提交成功！谢谢你的到访～")
            st.rerun()
        else:
            st.warning("昵称和留言都不能为空哦")

    st.markdown("<div class='gradient-divider'></div>", unsafe_allow_html=True)

    # 留言展示
    st.subheader("📋 大家的留言")
    if len(st.session_state.guestbook) == 0:
        st.write("还没有留言，快来抢沙发吧～")
    else:
        for item in st.session_state.guestbook:
            st.markdown(f"""
            <div style='background: rgba(25,25,35,0.4); border-radius: 12px; padding: 16px 20px; margin-bottom: 12px; border: 1px solid rgba(255,255,255,0.05);'>
                <div style='display: flex; justify-content: space-between; margin-bottom: 8px;'>
                    <span style='color: #8278ff; font-weight: 600;'>{item['nickname']}</span>
                    <span style='color: rgba(255,255,255,0.4); font-size: 13px;'>{item['time']}</span>
                </div>
                <p style='margin: 0; color: #e0e0e0;'>{item['message']}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# 5. 联系我
elif st.session_state.current_page == "contact":
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<h1 class='gradient-title'>联系我</h1>", unsafe_allow_html=True)
    st.write("很高兴你能看到这里，如果你想和我交流、合作，都可以通过下面的方式找到我")
    st.markdown("<div class='gradient-divider'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("📱 社交平台")
        st.write("📮 邮箱：xxx@xxx.com")
        st.write("💬 微信：xxxxxx")
        st.write("📖 知乎：@xxx")
        st.write("🐱 GitHub：@xxx")
        st.write("📷 小红书：@xxx")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("💼 工作合作")
        st.write("如果你有项目合作、技术咨询、设计委托等需求，欢迎随时联系我")
        st.write("工作日24小时内必回，非工作日48小时内回复")
        st.markdown("<p class='highlight-text'>合作理念：真诚相待，双向奔赴，共同做好每一件事</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>✨ 感谢你的到访，期待与你相遇 ✨</h3>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
