
---

## 2. plan.md (开发计划)

```markdown
# Flask 个人博客开发计划

## 阶段一：项目初始化与基础设置 (预计: 0.5 天)

-   [ ] 创建项目根目录 `flask-personal-blog`。
-   [ ] 初始化 Git 仓库，创建 `.gitignore` 文件（忽略 `venv/`, `instance/`, `__pycache__/` 等）。
-   [ ] 创建 Python 虚拟环境 `venv` 并激活。
-   [ ] 安装核心 Flask 库：`pip install flask`。
-   [ ] 创建基础文件结构：`app.py`, `static/`, `templates/`。
-   [ ] 创建 `.flaskenv` 文件并配置基础环境变量 (`FLASK_APP`, `FLASK_ENV`, `SECRET_KEY`)。
-   [ ] 编写 `README.md` 和 `plan.md`。

## 阶段二：数据库模型设计 (预计: 0.5 天)

-   [ ] 安装数据库相关库：`pip install flask-sqlalchemy`。
-   [ ] 在 `app.py` 中配置数据库 URI（使用 SQLite）。
-   [ ] 定义数据模型（Model）:
    -   [ ] `User` 模型（用于未来扩展，暂时主要用于作者）。
    -   [ ] `Post` 模型（文章：id, title, content, created_date, author_id 等）。
    -   [ ] `Category` 模型（分类：id, name）。
    -   [ ] `Tag` 模型（标签：id, name）。(可选，或使用分类代替)
    -   [ ] `Comment` 模型（评论：id, post_id, author, content, created_date）。(Phase 3)
-   [ ] 初始化数据库，使用 `db.create_all()` 创建表。

## 阶段三：核心功能开发 (预计: 2-3 天)

### 1. 视图与路由 (Routes/Views)
-   [ ] 首页 (`/`): 显示文章列表（最新优先）。
-   [ ] 文章详情页 (`/post/<int:post_id>`): 显示单篇文章全文。
-   [ ] 关于页面 (`/about`): 静态页面。

### 2. 模板渲染 (Templates)
-   [ ] 创建基础模板 `base.html`，包含共用的 HTML 结构、CSS/JS 引用、导航栏。
-   [ ] 创建 `index.html` 模板，继承 `base.html`，循环显示文章列表。
-   [ ] 创建 `post.html` 模板，显示单篇文章。
-   [ ] 创建 `about.html` 模板。

### 3. 前端样式 (Static Files)
-   [ ] 添加简单的 CSS 样式（或使用 Bootstrap/Tailwind CSS 等框架）到 `static/css/style.css`。
-   [ ] 确保基础布局和导航栏样式完成。

## 阶段四：内容管理功能 (预计: 1-2 天)

-   [ ] 安装表单相关库：`pip install flask-wtf`。
-   [ ] 创建文章表单 `PostForm` (使用 WTForms)。
-   [ ] 创建路由和模板用于发布新文章 (`/create`)。
-   [ ] 创建路由和模板用于编辑已有文章 (`/edit/<int:post_id>`)。
-   [ ] 创建路由用于删除文章 (`/delete/<int:post_id>`, POST 方法)。
-   [ ] 在文章详情页添加“编辑”按钮（链接到编辑页面）。

## 阶段五：高级功能与优化 (预计: 1-2 天)

-   [ ] **Markdown 支持**:
    -   [ ] 安装 Markdown 解析库（如 `pip install mistune`）。
    -   [ ] 在 `Post` 模型中存储原始 Markdown 内容。
    -   [ ] 在显示文章时，将 Markdown 内容转换为 HTML 再渲染。
-   [ ] **分类/标签功能**:
    -   [ ] 在 `Post` 模型中建立与 `Category`/`Tag` 的关系。
    -   [ ] 在发布/编辑文章的表单中添加分类/标签选择/输入字段。
    -   [ ] 创建页面按分类/标签筛选文章。
-   [ ] **评论功能**:
    -   [ ] 在文章详情页下方显示评论列表。
    -   [ ] 添加表单供访客提交评论。
    -   [ ] 实现评论提交的逻辑（存储到 `Comment` 表）。

## 阶段六：最终打磨与部署准备 (预计: 1 天)

-   [ ] 代码整理与注释。
-   [ ] 全面测试所有功能。
-   [ ] 生成 `requirements.txt` 文件：`pip freeze > requirements.txt`。
-   [ ] 更新 `README.md`，补充部署章节。
-   [ ] 研究并选择部署平台（Heroku, PythonAnywhere 等）。
-   [ ] **(可选)** 编写简单的单元测试。

---

## 可能的功能扩展 (未来版本)

-   **用户认证 (Flask-Login)**: 实现作者登录功能，保护管理页面。
-   **管理后台 (Flask-Admin)**: 集成 Flask-Admin 进行更便捷的内容管理。
-   **分页功能**: 文章列表分页显示。
-   **全文搜索**: 实现简单的博客内容搜索。
-   **RSS 订阅**: 生成 RSS 源。
-   **文件上传**: 支持在文章中上传图片。