# 导入streamlit库，用于快速搭建网页
import streamlit as st

# ======================================
# 【1】页面基础配置（网站标题、图标、布局）
# ======================================
st.set_page_config(
    page_title="我的个人博客",    # 浏览器标签标题
    page_icon="📝",              # 浏览器标签图标
    layout="wide"                # 宽屏模式（看起来更大气）
)

# ======================================
# 【2】网站样式：苹果风 + 暗黑高级感
# 你可以在这里改颜色、圆角、阴影、字体
# ======================================
st.markdown("""
<style>
/* 全局字体：苹果系统字体 */
* {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}

/* 背景：深色渐变（苹果暗黑风格） */
.main {
    background: linear-gradient(135deg, #121212, #1c1c1e);
    padding: 2rem 1rem;
}

/* 卡片样式：苹果毛玻璃效果 */
.apple-dark-card {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 22px;       /* 圆角：苹果风格 */
    padding: 30px;             /* 内边距 */
    box-shadow: 0 10px 40px rgba(0,0,0,0.3); /* 阴影 */
    margin-bottom: 22px;       /* 卡片间距 */
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.1);
}

/* 标题样式 */
h1 {
    font-size: 46px;
    font-weight: 700;
    color: #f9f9f9;
    margin-bottom: 10px;
}

/* 二级标题 */
h2 {
    font-size: 28px;
    font-weight: 600;
    color: #e6e6e6;
}

/* 正文文字 */
p, li {
    font-size: 17px;
    color: #d1d1d6;
    line-height: 1.7;
}

/* 链接颜色 */
a {
    color: #0a84ff;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)

# ======================================
# 【3】顶部区域：博客标题 + 简介
# ======================================
st.markdown("<div class='apple-dark-card'>", unsafe_allow_html=True)

st.title("📝 我的个人博客")
st.subheader("分享技术、生活、思考与成长")
st.write("""
这里是我的专属小空间，专注于编程学习、AI知识库建设、自动化工具开发与极简风格设计。
保持简洁，保持高级，持续更新，持续进步。
""")

st.markdown("</div>", unsafe_allow_html=True)

# ======================================
# 【4】文章列表区域（博客核心）
# ======================================
st.markdown("<div class='apple-dark-card'>", unsafe_allow_html=True)
st.subheader("✍️ 最新文章")
st.write("### 1. 从零搭建个人知识库全过程")
st.write("---")
st.write("### 2. 苹果风界面设计心得")
st.write("圆角、阴影、毛玻璃、极简排版，这就是高级感的秘密。")
st.write("---")
st.write("### 3. 我的AI知识库建设计划")
st.write("目标：打造一个能上传文档、智能问答的私人AI系统。")
st.markdown("</div>", unsafe_allow_html=True)

# ======================================
# 【5】关于我（个人介绍）
# ======================================
st.markdown("<div class='apple-dark-card'>", unsafe_allow_html=True)
st.subheader("👤 关于我")
st.write("""
- 热爱技术与设计
- 正在建设个人AI知识库
- 魔术爱好者
- 持续学习，持续输出
""")
st.markdown("</div>", unsafe_allow_html=True)

# ======================================
# 【6】技能标签（丰富页面效果）
# ======================================
st.markdown("<div class='apple-dark-card'>", unsafe_allow_html=True)
st.subheader("💡 学习技能")
st.write("Python | 网页开发 | AI大模型 | 知识库搭建 | Langchain | LangGraphe | YOLO ")
st.markdown("</div>", unsafe_allow_html=True)

# ======================================
# 【7】联系方式
# ======================================
st.markdown("<div class='apple-dark-card'>", unsafe_allow_html=True)
st.subheader("📮 联系我")
st.code("2423038671@qq.com")
st.markdown("</div>", unsafe_allow_html=True)

# ======================================
# 【8】底部版权（更像真实博客）
# ======================================
st.write("")
st.caption("© 2025 我的个人博客 | 持续建设中")
