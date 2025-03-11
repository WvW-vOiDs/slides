个人 Slides 仓库. - Supported by [Slidev](https://cn.sli.dev/)

## Beamer to Slidev

1. 安装依赖.

```bash
pip3 install PyMuPDF
```
2. 复制 main.pdf 文件到 项目根目录.

3. 执行 `./utils/beamer2slidev/create_project.sh`.

```bash
./utils/beamer2slidev/create_project.sh
```

4. 根据 beamer 修改 title, colorSchema 和 aspectRatio 等参数.