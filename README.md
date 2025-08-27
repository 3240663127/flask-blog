# Flask 个人博客

一个使用 Python 的 Flask 框架开发的轻量级、简洁的个人博客网站。

## 功能特性

-   **文章管理**: 发布、编辑、删除和查看博客文章。
-   **Markdown 支持**: 使用 Markdown 语法编写富文本文章。
-   **分类与标签**: 对文章进行组织和分类。
-   **评论功能**: 访客可以对文章发表评论（需审核/直接发布）。
-   **响应式设计**: 适配桌面和移动设备。
-   **管理后台**: 简单的后台管理界面用于内容管理（可选，可通过 `FLASK_ADMIN` 配置）。

## 技术栈

-   **后端框架**: Flask 2.3.x
-   **前端模板**: Jinja2
-   **数据库**: SQLite (开发) / PostgreSQL 或 MySQL (生产环境推荐)
-   **ORM**: SQLAlchemy + Flask-SQLAlchemy
-   **表单处理**: WTForms + Flask-WTF
-   **Markdown 解析**: Mistune 或 Markdown2
-   **身份验证**: Flask-Login
-   **管理后台**: Flask-Admin (可选)


## 项目文件结构
flask-personal-blog/
├── app.py                 # 应用主入口/工厂函数
├── requirements.txt       # 项目依赖列表
├── .flaskenv             # Flask 开发环境变量配置
├── venv/                 # Python 虚拟环境 (忽略)
├── instance/             # 实例文件夹 (存放数据库、配置)
│   └── blog.db          # SQLite 数据库文件 (自动生成)
├── static/               # 静态文件 (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
└── templates/            # Jinja2 HTML 模板
    ├── base.html        # 基础模板
    ├── index.html       # 首页
    ├── post.html        # 文章详情页
    ├── create_edit_post.html # 创建/编辑文章页
    └── ...              # 其他模板

## 开发环境设置 (Windows 10)

### 1.  prerequisites

确保您的系统已安装：
-   Python (3.8 或更高版本)
-   pip (Python 包管理器)
-   Git (可选，用于版本控制)

### 2. 克隆项目

```bash
git clone <your-repository-url>
cd flask-personal-blog