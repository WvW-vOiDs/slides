#!/bin/bash
set -euo pipefail  # 启用严格模式：自动报错、未定义变量报错、管道报错

# 检查 main.pdf 是否存在
if [[ ! -f "./main.pdf" ]]; then
  echo "错误：当前目录下未找到 main.pdf 文件！"
  exit 1
fi

# 提示用户输入项目名称
read -p "请输入项目名称: " project_name

# 检查输入非空
if [[ -z "$project_name" ]]; then
  echo "错误：项目名称不能为空！"
  exit 1
fi

# 验证项目名称合法性（仅允许字母、数字、下划线、连字符）
if [[ ! "$project_name" =~ ^[a-zA-Z0-9_-]+$ ]]; then
  echo "错误：项目名称只能包含字母、数字、下划线和连字符！"
  exit 1
fi

# 检查目录是否已存在
target_dir="./${project_name}"
if [[ -d "$target_dir" ]]; then
  echo "错误：目录 '${target_dir}' 已存在！"
  exit 1
fi

# 创建目录
mkdir -p "${target_dir}/src" || {
  echo "错误：目录创建失败！"
  exit 1
}

# 复制文件（逐个检查）
cp "./main.pdf" "${target_dir}/src/${project_name}.pdf" || {
  echo "错误：复制 main.pdf 失败！"
  rm -rf "$target_dir"
  exit 1
}

cp "./utils/beamer2slidev/init_slides.py" "${target_dir}/src/init_slides.py" || {
  echo "错误：复制 init_slides.py 失败！"
  rm -rf "$target_dir"
  exit 1
}

# 执行 Python 脚本（跨平台兼容）
python_cmd="python3"
if command -v python3 &>/dev/null; then
  python_cmd="python3"
fi

"$python_cmd" "${target_dir}/src/init_slides.py" || {
  echo "错误：项目初始化程序执行失败！"
  rm -rf "$target_dir"
  exit 1
}

mv "${target_dir}/src/${project_name}.pdf" "${target_dir}/${project_name}-origin.pdf" || {
  echo "错误：项目初始化成功，但移动原始pdf文件失败！"
  exit 1
}

# 清理文件（按需取消注释）
rm -f "./main.pdf" "${target_dir}/src/init_slides.py" || {
  echo "错误：项目初始化成功，但删除脚本和根目录文件失败！"
  exit 1
}

echo "操作成功完成！"