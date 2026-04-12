import streamlit as st

# 1. 用官方配置强制锁定深色主题（最关键！）
st.set_page_config(
    page_title="我的博客",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items=None
)

# 2. 用 config.toml 配置强制深色主题（Streamlit 会优先读取）
st.markdown("""
<style>
    /* 第一步：强制覆盖所有 Streamlit 默认样式 */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(180deg, #0a0a0a 0%, #121212 100%) !important;
    }
    [data-testid="stHeader"] {
        background-color: #0a0a0a !important;
    }
    [data-testid="stToolbar"] {
        background-color: #0a0a0a !important;
    }
    [data-testid="stSidebar"] {
        background-color: #0a0a0a !important;
    }
    [data-testid="stMarkdown"] {
        color: #ffffff !important;
    }
    .stText {
        color: #b0b0b0 !important;
    }

    /* 第二步：你的自定义深色样式 */
    /* 玻璃态卡片系统 - 参考苹果macOS Big Sur设计 */
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

    /* 卡片悬停动效 - 特斯拉官网交互风格 */
    .card:hover {
        transform: translateY(-4px);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5), 
                    0 0 40px rgba(255, 255, 255, 0.03),
                    inset 0 1px 0 rgba(255, 255, 255, 0.1);
        border-color: rgba(255, 255, 255, 0.15);
    }

    /* 卡片光晕效果 - 微妙的渐变叠加 */
    .card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: linear-gradient(90deg, 
            transparent 0%, 
            rgba(255, 255, 255, 0.1) 50%, 
            transparent 100%);
    }

    /* 主标题 - 大号细体字,苹果风格 */
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

    /* 副标题 - 次级信息层级 */
    h3 {
        color: #f0f0f0 !important;
        font-size: 28px;
        font-weight: 400;
        letter-spacing: -0.5px;
        margin-bottom: 12px;
    }

    /* 正文文本 - 高可读性灰度 */
    p {
        color: #b0b0b0 !important;
        line-height: 1.8;
        font-size: 17px;
        font-weight: 350;
        letter-spacing: 0.2px;
    }

    /* 标签徽章 - Pill形状设计 */
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

    /* 分隔线 - 极细分隔 */
    .divider {
        height: 1px;
        background: linear-gradient(90deg, 
            transparent 0%, 
            rgba(255, 255, 255, 0.08) 50%, 
            transparent 100%);
        margin: 30px 0;
    }

    /* 引用块 - 强调内容 */
    .quote {
        border-left: 3px solid rgba(255, 255, 255, 0.2);
        padding-left: 20px;
        margin: 20px 0;
        font-style: italic;
        color: #c0c0c0 !important;
    }

    /* 底部版权 - 低调处理 */
    .footer {
        text-align: center;
        color: #505050 !important;
        font-size: 14px;
        padding: 40px 0;
        letter-spacing: 0.5px;
    }

    /* 滚动条美化 - Webkit浏览器 */
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

# Hero区域 - 大标题展示区
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.title("📝 我的个人博客")
st.write("极简主义 · 深度思考 · 持续进化")
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
st.write("记录技术探索与认知升级的每一步")
st.markdown("</div>", unsafe_allow_html=True)

# 文章卡片1 - 带标签系统
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("第一篇博客：启程")
st.write("这是我的第一篇博客，记录学习与成长的起点。在这里，我将分享技术心得、项目实践以及对未来的思考。")
st.markdown("""
<div class='quote'>
"千里之行，始于足下。每一次记录，都是对思维的梳理与升华。"
</div>
""", unsafe_allow_html=True)
st.markdown("<span class='tag'>成长</span><span class='tag'>随笔</span>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# 文章卡片2 - 项目展示
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("网站搭建实战")
st.write("从零开始搭建个人网站，探索现代Web开发的最佳实践。采用Streamlit框架，融合极简美学与功能性。")
st.markdown("""
<div class='quote'>
"优秀的设计是尽可能少的设计。" —— Dieter Rams
</div>
""", unsafe_allow_html=True)
st.markdown("<span class='tag'>Web开发</span><span class='tag'>Streamlit</span><span class='tag'>UI设计</span>",
            unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# 关于我 - 个人信息卡片
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("关于我")
st.write("热爱技术美学，追求极简主义生活方式。目前正在构建AI知识库，探索人工智能与人类认知的边界。")
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
st.write("🎯 专注领域：Python开发 | AI应用 | 产品设计")
st.write("🌱 当前目标：打造高质量技术内容平台")
st.markdown("</div>", unsafe_allow_html=True)

# 底部版权信息
st.markdown("<div class='footer'>© 2025 我的极简博客 · Designed with Precision</div>", unsafe_allow_html=True)
