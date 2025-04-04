"""
文件名: init_slides.py
作者: [WvW-vOiDs](https://WvW-vOiDs.github.io)
描述: 将 PDF 文件转换为 PNG 图像并生成相应的 Markdown 文件
"""

import fitz  # PyMuPDF
from pathlib import Path
from typing import Union

def pdf_to_png(pdf_path: Union[str, Path], dpi: int = 300) -> None:
    """
    将 PDF 每一页转换为 PNG 图像
    参数:
        pdf_path: 输入的PDF文件路径
        dpi: 输出图像分辨率（默认为300）
    """
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF文件不存在: {pdf_path}")

    base_name = pdf_path.stem
    script_dir = Path(__file__).parent
    output_dir = script_dir / "public" / base_name
    output_dir.mkdir(parents=True, exist_ok=True)

    pdf_doc = fitz.open(pdf_path)
    num_pages = len(pdf_doc)
    num_digits = len(str(num_pages))  # 计算页数的位数

    for page_num in range(num_pages):
        page = pdf_doc.load_page(page_num)
        matrix = fitz.Matrix(dpi / 72, dpi / 72)
        pix = page.get_pixmap(matrix=matrix, alpha=False)

        output_name = f"{base_name}-{page_num + 1:0{num_digits}d}.png"
        output_path = output_dir / output_name
        pix.save(output_path)
        print(f"已保存: {output_path}")

    pdf_doc.close()
    create_slides_md(base_name, num_pages)
    create_package_json(base_name)

def create_slides_md(base_name: str, num_pages: int) -> None:
    """
    生成 slides.md 文件:
    参数:
        base_name: PDF文件的基础名称
        num_pages: PDF文件的页数
    """
    script_dir = Path(__file__).parent
    slides_md_path = script_dir / "slides.md"

    if slides_md_path.exists():
        confirm = input(f"{slides_md_path} 已存在，是否覆盖？(y/n): ")
        if confirm.lower() != 'y':
            print("操作已取消")
            return

    num_digits = len(str(num_pages))  # 计算页数的位数
    with slides_md_path.open('w', encoding='utf-8') as f:
        title = base_name.replace('-', ' ').replace('_', ' ').title()
        f.write(
            "---\n"
            "# **************************************************************************** #\n"
            "#                                     Info                                     #\n"
            "# **************************************************************************** #\n"
            "\n"
            "# 幻灯片的总标题，如果没有指定，那么将以第一张拥有标题的幻灯片的标题作为总标题。\n"
            f"title: {title}\n"
            "# subtitle: subtitle\n"
            "\n"
            "# 网页的标题模板，`%s` 会被页面的标题替换。\n"
            "titleTemplate: '%s - WvW-vOiDs'\n"
            "\n"
            "# 幻灯片信息，可以是一个 markdown 字符串。\n"
            "info: false\n"
            "\n"
            "# **************************************************************************** #\n"
            "#                                 Configurition                                #\n"
            "# **************************************************************************** #\n"
            "\n"
            "# 主题 id 或 主题包名称\n"
            "# 了解更多：https://cn.sli.dev/guide/theme-addon#use-theme\n"
            "theme: default\n"
            "\n"
            "# 附加组件, 一个可以含包名或本地路径的数组。\n"
            "# 了解更多： https://cn.sli.dev/guide/theme-addon#use-addon\n"
            "# addons: []\n"
            "\n"
            "# 幻灯片的配色方案，可以使用 'auto'，'light' 或者 'dark'\n"
            "colorSchema: light\n"
            "\n"
            "# 幻灯片的长宽比\n"
            "aspectRatio: 16/9\n"
            "\n"
            "# favicon 可以是本地文件路径，也可以是一个 URL\n"
            "favicon: \"https://wvw-voids.github.io/icon/favicon.ico\"\n"
            "\n"
            "# 定义幻灯片与下一张幻灯片之间的过渡\n"
            "# 了解更多： https://cn.sli.dev/guide/animations.html#slide-transitions\n"
            "transition: slide-left\n"
            "\n"
            "# **************************************************************************** #\n"
            "#                                   Exporting                                  #\n"
            "# **************************************************************************** #\n"
            "\n"
            "# 要导出文件的文件名称\n"
            f"exportFilename: {base_name}-exported\n"
            "\n"
            "# 导出的 PDF 或 PPTX 文件中的作者字段。\n"
            "author: WvW-vOiDs\n"
            "\n"
            "# 导出选项\n"
            "# 使用驼峰命名法的导出 CLI 选项\n"
            "# 了解更多： https://cn.sli.dev/guide/exporting\n"
            "export:\n"
            "  format: pdf\n"
            "  timeout: 30000\n"
            "  dark: false\n"
            "  withClicks: false\n"
            "  withToc: false\n"
            "\n"
            "# **************************************************************************** #\n"
            "#                                     Other                                    #\n"
            "# **************************************************************************** #\n"
            "\n"
            "\n"
            "# 导出的 PDF 文件中的关键字，以逗号分割。\n"
            "# keywords: keyword1,keyword2\n"
            "\n"
            "# 启用演讲者模式，可以是一个 boolean 值、'dev' 或 'build'\n"
            "# presenter: true\n"
            "\n"
            "# 在单页（SPA）构建中启用 pdf 下载，也可以指定一个自定义 url\n"
            "# download: false\n"
            "\n"
            "\n"
            "# 语法高亮设置，可以使用 'shiki' 或 'prism'(已弃用) 方案\n"
            "# highlighter: shiki\n"
            "\n"
            "# 启用 twoslash, 可以是一个 boolean 值，'dev' 或 'build'\n"
            "# twoslash: true\n"
            "\n"
            "# 在代码块中显示行号\n"
            "# lineNumbers: false\n"
            "\n"
            "# 启用 monaco 编辑器，可以是一个 boolean 值，'dev' 或 'build'\n"
            "monaco: true\n"
            "\n"
            "# 从何处加载 monaco 的类型，可以是 'cdn'，'local' 或 ‘none’\n"
            "# monacoTypesSource: cdn\n"
            "# 指定额外的本地包以导入 monaco 类型\n"
            "# monacoTypesAdditionalPackages: []\n"
            "# 指定额外的本地模块作为 monaco 可运行的依赖项\n"
            "# monacoRunAdditionalDeps: []\n"
            "\n"
            "# 使用 vite-plugin-remote-assets 在本地下载远程资源，可以是一个 boolean 值，'dev' 或者 'build'\n"
            "# remoteAssets: false\n"
            "\n"
            "# 控制幻灯片中的文本是否可以被选择\n"
            "# selectable: true\n"
            "\n"
            "# 启用幻灯片录制，可以是一个 boolean 值，'dev' 或者 'build'\n"
            "record: false\n"
            "\n"
            "# 启用 Slidev 的前后文菜单，可以是一个 boolean 值，'dev' 或者 'build'\n"
            "# contextMenu: true\n"
            "\n"
            "# 防止休眠，可以是一个 boolean 值，'dev' 或者 'build'\n"
            "# wakeLock: true\n"
            "\n"
            "# vue-router 模式，可以使用 'history' 或 'hash' 模式\n"
            "# routerMode: history\n"
            "\n"
            "# canvas 的真实宽度，单位为 px\n"
            "# canvasWidth: 980\n"
            "\n"
            "# 用于主题定制，会将属性 `x` 注入根样式 `--slidev-theme-x`\n"
            "# themeConfig:\n"
            "#   primary: '#5d8392'\n"
            "\n"
            "# 用于渲染图表的 PlantUML 服务器的 URL\n"
            "# 了解更多： https://cn.sli.dev/features/plantuml.html\n"
            "# plantUmlServer: https://www.plantuml.com/plantuml\n"
            "\n"
            "# 字体将从 Google 字体自动导入\n"
            "# 了解更多： https://cn.sli.dev/custom/config-fonts\n"
            "# fonts:\n"
            "#   sans: Roboto\n"
            "#   serif: Roboto Slab\n"
            "#   mono: Fira Code\n"
            "\n"
            "# 为所有幻灯片添加默认的 frontmatter\n"
            "# defaults:\n"
            "#   layout: default\n"
            "# ...\n"
            "\n"
            "# 绘制选项\n"
            "# 了解更多：https://cn.sli.dev/features/drawing\n"
            "drawings:\n"
            "  enabled: true\n"
            "  persist: false\n"
            "  # presenterOnly: false\n"
            "  # syncAll: true\n"
            "\n"
            "# HTML 标签属性\n"
            "# htmlAttrs:\n"
            "#   dir: ltr\n"
            "#   lang: en\n"
            "---\n\n"
            "## The Beginning of the Slide\n\n"
            "| Keyboard Shortcut                                                  | Description                    |\n"
            "|--------------------------------------------------------------------|--------------------------------|\n"
            "| <kbd>right</kbd> / <kbd>down</kbd> / <kbd>space</kbd>              | next animation or slide        |\n"
            "| <kbd>left</kbd> / <kbd>up</kbd> / <kbd>shift</kbd><kbd>space</kbd> | previous animation or slide    |\n"
            "| <kbd>f</kbd>                                                       | Toggle fullscreen              |\n"
            "| <kbd>o</kbd>                                                       | Toggle Quick Overview          |\n"
            "| <kbd>g</kbd>                                                       | Show goto...                   |\n\n"
            "<div class=\"abs-br m-6 text-xl\">\n"
            "  <a href=\"https://wvw-voids.github.io\" target=\"_blank\" class=\"slidev-icon-btn\">\n"
            "    <carbon:logo-github />\n"
            "  </a>\n"
            "</div>\n\n"
        )
        for page_num in range(1, num_pages + 1):
            f.write(
                "---\n"
                "layout: image\n"
                f"image: /{base_name}/{base_name}-{page_num:0{num_digits}d}.png\n"
                "backgroundSize: contain\n"
                "---\n\n"
            )
            f.write(f"<!-- 第 {page_num:0{num_digits}d} 页批注:\n\n-->\n\n")
    print(f"已生成: {slides_md_path}")

def create_package_json(base_name: str) -> None:
    """
    生成 package.json 文件:
    参数:
        base_name: PDF文件的基础名称
    """
    script_dir = Path(__file__).parent
    package_json_path = script_dir / "package.json"

    if package_json_path.exists():
        confirm = input(f"{package_json_path} 已存在，是否覆盖？(y/n): ")
        if confirm.lower() != 'y':
            print("操作已取消")
            return

    with package_json_path.open('w', encoding='utf-8') as f:
        f.write(
            '{\n'
            f'  "name": "{base_name.lower()}",\n'
            '  "private": true,\n'
            '  "scripts": {\n'
            '    "dev": "slidev",\n'
            f'    "build": "slidev build --base /slides/{base_name}/ --out ../../dist/{base_name}/",\n'
            f'    "export": "slidev export --dark --with-clicks --output ../{base_name}.pdf"\n'
            '  },\n'
            '  "dependencies": {\n'
            '    "@slidev/cli": "^51.5.0",\n'
            '    "@slidev/theme-default": "latest"\n'
            '  }\n'
            '}'
        )
    print(f"已生成: {package_json_path}")

def main() -> None:
    script_dir = Path(__file__).parent
    pdf_files = [f for f in script_dir.iterdir() if f.suffix.lower() == '.pdf']

    if len(pdf_files) == 0:
        raise FileNotFoundError("当前目录没有找到PDF文件")
    elif len(pdf_files) > 1:
        raise RuntimeError("当前目录存在多个PDF文件，请确保只有一个PDF文件")

    pdf_to_png(pdf_files[0], dpi=300)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"发生错误: {e}")