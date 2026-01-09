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

    # Check if output directory already exists and has content
    if output_dir.exists() and list(output_dir.iterdir()):
        confirm = input(f"目录 {output_dir} 已存在且非空，是否覆盖内容？(y/N): ")
        if confirm.lower() != 'y':
            print("操作已取消")
            return

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
    templates_dir = script_dir / "templates"

    # 确保模板目录存在
    templates_dir.mkdir(exist_ok=True)

    if slides_md_path.exists():
        confirm = input(f"{slides_md_path} 已存在，是否覆盖？(y/N): ")
        if confirm.lower() != 'y':
            print("操作已取消")
            return

    # 读取主模板文件
    try:
        with open(templates_dir / "slides_template.md", 'r', encoding='utf-8') as template_file:
            slides_template = template_file.read()
    except FileNotFoundError:
        # 如果模板文件不存在，使用默认内置模板
        print("警告: 模板文件不存在，使用内置模板")
        # 这里你可以使用一个简化版的模板作为备用
        slides_template = "---\ntitle: {title}\nexportFilename: {base_name}-exported\n---\n\n## The Beginning of the Slide\n\n"

    # 读取页面模板文件
    try:
        with open(templates_dir / "page_template.md", 'r', encoding='utf-8') as page_template_file:
            page_template = page_template_file.read()
    except FileNotFoundError:
        # 如果页面模板文件不存在，使用默认内置模板
        print("警告: 页面模板文件不存在，使用内置模板")
        page_template = "---\nlayout: image\nimage: /{base_name}/{file_name}\nbackgroundSize: contain\n---\n\n<!-- 第 {page_num} 页批注:\n\n-->\n\n"

    # 填充模板变量
    title = base_name.replace('-', ' ').replace('_', ' ').title()
    slides_content = slides_template.format(title=title, base_name=base_name)

    num_digits = len(str(num_pages))  # 计算页数的位数

    # 为每一页生成内容
    page_contents = []
    for page_num in range(1, num_pages + 1):
        file_name = f"{base_name}-{page_num:0{num_digits}d}.png"
        page_content = page_template.format(
            base_name=base_name,
            file_name=file_name,
            page_num=f"{page_num:0{num_digits}d}"
        )
        page_contents.append(page_content)

    # 写入最终文件
    with slides_md_path.open('w', encoding='utf-8') as f:
        f.write(slides_content)
        f.write("\n".join(page_contents))

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
        confirm = input(f"{package_json_path} 已存在，是否覆盖？(y/N): ")
        if confirm.lower() != 'y':
            print("操作已取消")
            return

    with package_json_path.open('w', encoding='utf-8') as f:
        f.write(
            '{\n'
            f'  "name": "{base_name.lower()}",\n'
            '  "type": "module",\n'
            '  "private": true,\n'
            '  "scripts": {\n'
            '    "dev": "slidev",\n'
            f'    "build": "slidev build --base /slides/{base_name}/ --out ../../dist/{base_name}/",\n'
            f'    "export": "slidev export --dark --with-clicks --output ../{base_name}.pdf"\n'
            '  },\n'
            '  "dependencies": {\n'
            '    "@slidev/cli": "catalog:",\n'
            '    "@slidev/theme-default": "catalog:"\n'
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