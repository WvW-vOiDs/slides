---
# **************************************************************************** #
#                                     Info                                     #
# **************************************************************************** #

# 幻灯片的总标题，如果没有指定，那么将以第一张拥有标题的幻灯片的标题作为总标题。
title: The Beamer Class For LaTeX
subtitle: A Tutorial

# 网页的标题模板，`%s` 会被页面的标题替换。
titleTemplate: '%s - A Tutorial'

# 幻灯片信息，可以是一个 markdown 字符串。
info: false

# **************************************************************************** #
#                                 Configurition                                #
# **************************************************************************** #

# 主题 id 或 主题包名称
# 了解更多：https://cn.sli.dev/guide/theme-addon#use-theme
theme: default

# 附加组件, 一个可以含包名或本地路径的数组。
# 了解更多： https://cn.sli.dev/guide/theme-addon#use-addon
# addons: []

# 幻灯片的配色方案，可以使用 'auto'，'light' 或者 'dark'
colorSchema: light

# 幻灯片的长宽比
aspectRatio: 4/3

# favicon 可以是本地文件路径，也可以是一个 URL
favicon: "https://wvw-voids.github.io/icon/favicon.ico"

# 定义幻灯片与下一张幻灯片之间的过渡
# 了解更多： https://cn.sli.dev/guide/animations.html#slide-transitions
transition: slide-left

# **************************************************************************** #
#                                   Exporting                                  #
# **************************************************************************** #

# 要导出文件的文件名称
exportFilename: The-beamer-class-for-LATEX-exported

# 导出的 PDF 或 PPTX 文件中的作者字段。
author: Kathrin Wünsch

# 导出选项
# 使用驼峰命名法的导出 CLI 选项
# 了解更多： https://cn.sli.dev/guide/exporting
export:
  format: pdf
  timeout: 30000
  dark: false
  withClicks: false
  withToc: false

# **************************************************************************** #
#                                     Other                                    #
# **************************************************************************** #


# 导出的 PDF 文件中的关键字，以逗号分割。
# keywords: keyword1,keyword2

# 启用演讲者模式，可以是一个 boolean 值、'dev' 或 'build'
# presenter: true

# 在单页（SPA）构建中启用 pdf 下载，也可以指定一个自定义 url
# download: false


# 语法高亮设置，可以使用 'shiki' 或 'prism'(已弃用) 方案
# highlighter: shiki

# 启用 twoslash, 可以是一个 boolean 值，'dev' 或 'build'
# twoslash: true

# 在代码块中显示行号
# lineNumbers: false

# 启用 monaco 编辑器，可以是一个 boolean 值，'dev' 或 'build'
monaco: true

# 从何处加载 monaco 的类型，可以是 'cdn'，'local' 或 ‘none’
# monacoTypesSource: cdn
# 指定额外的本地包以导入 monaco 类型
# monacoTypesAdditionalPackages: []
# 指定额外的本地模块作为 monaco 可运行的依赖项
# monacoRunAdditionalDeps: []

# 使用 vite-plugin-remote-assets 在本地下载远程资源，可以是一个 boolean 值，'dev' 或者 'build'
# remoteAssets: false

# 控制幻灯片中的文本是否可以被选择
# selectable: true

# 启用幻灯片录制，可以是一个 boolean 值，'dev' 或者 'build'
record: false

# 启用 Slidev 的前后文菜单，可以是一个 boolean 值，'dev' 或者 'build'
# contextMenu: true

# 防止休眠，可以是一个 boolean 值，'dev' 或者 'build'
# wakeLock: true

# vue-router 模式，可以使用 'history' 或 'hash' 模式
routerMode: hash

# canvas 的真实宽度，单位为 px
# canvasWidth: 980

# 用于主题定制，会将属性 `x` 注入根样式 `--slidev-theme-x`
# themeConfig:
#   primary: '#5d8392'

# 用于渲染图表的 PlantUML 服务器的 URL
# 了解更多： https://cn.sli.dev/features/plantuml.html
# plantUmlServer: https://www.plantuml.com/plantuml

# 字体将从 Google 字体自动导入
# 了解更多： https://cn.sli.dev/custom/config-fonts
# fonts:
#   sans: Roboto
#   serif: Roboto Slab
#   mono: Fira Code

# 为所有幻灯片添加默认的 frontmatter
# defaults:
#   layout: default
# ...

# 绘制选项
# 了解更多：https://cn.sli.dev/features/drawing
drawings:
  enabled: true
  persist: false
  # presenterOnly: false
  # syncAll: true

  # HTML 标签属性
  # htmlAttrs:
  #   dir: ltr
  #   lang: en
---

## The Beginning of the Slide

| Keyboard Shortcut                                                  | Description                    |
|--------------------------------------------------------------------|--------------------------------|
| <kbd>right</kbd> / <kbd>down</kbd> / <kbd>space</kbd>              | next animation or slide        |
| <kbd>left</kbd> / <kbd>up</kbd> / <kbd>shift</kbd><kbd>space</kbd> | previous animation or slide    |
| <kbd>f</kbd>                                                       | Toggle fullscreen              |
| <kbd>o</kbd> / <kbd> ` </kbd>                                      | Toggle Quick Overview          |
| <kbd>g</kbd>                                                       | Show goto...                   |

## Reference

- [Link to original document](https://warwick.ac.uk/fac/sci/physics/research/cfsa/people/pastmembers/wuensch/workshoplatex/beamertutorialkwuensch.pdf)

<div class="abs-br m-6 text-xl">
  <a href="https://wvw-voids.github.io" target="_blank" class="slidev-icon-btn">
    <carbon:logo-github />
  </a>
</div>

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-01.png
backgroundSize: contain
---

<!-- 第 01 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-02.png
backgroundSize: contain
---

<!-- 第 02 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-03.png
backgroundSize: contain
---

<!-- 第 03 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-04.png
backgroundSize: contain
---

<!-- 第 04 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-05.png
backgroundSize: contain
---

<!-- 第 05 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-06.png
backgroundSize: contain
---

<!-- 第 06 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-07.png
backgroundSize: contain
---

<!-- 第 07 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-08.png
backgroundSize: contain
---

<!-- 第 08 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-09.png
backgroundSize: contain
---

<!-- 第 09 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-10.png
backgroundSize: contain
---

<!-- 第 10 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-11.png
backgroundSize: contain
---

<!-- 第 11 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-12.png
backgroundSize: contain
---

<!-- 第 12 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-13.png
backgroundSize: contain
---

<!-- 第 13 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-14.png
backgroundSize: contain
---

<!-- 第 14 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-15.png
backgroundSize: contain
---

<!-- 第 15 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-16.png
backgroundSize: contain
---

<!-- 第 16 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-17.png
backgroundSize: contain
---

<!-- 第 17 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-18.png
backgroundSize: contain
---

<!-- 第 18 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-19.png
backgroundSize: contain
---

<!-- 第 19 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-20.png
backgroundSize: contain
---

<!-- 第 20 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-21.png
backgroundSize: contain
---

<!-- 第 21 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-22.png
backgroundSize: contain
---

<!-- 第 22 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-23.png
backgroundSize: contain
---

<!-- 第 23 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-24.png
backgroundSize: contain
---

<!-- 第 24 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-25.png
backgroundSize: contain
---

<!-- 第 25 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-26.png
backgroundSize: contain
---

<!-- 第 26 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-27.png
backgroundSize: contain
---

<!-- 第 27 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-28.png
backgroundSize: contain
---

<!-- 第 28 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-29.png
backgroundSize: contain
---

<!-- 第 29 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-30.png
backgroundSize: contain
---

<!-- 第 30 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-31.png
backgroundSize: contain
---

<!-- 第 31 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-32.png
backgroundSize: contain
---

<!-- 第 32 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-33.png
backgroundSize: contain
---

<!-- 第 33 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-34.png
backgroundSize: contain
---

<!-- 第 34 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-35.png
backgroundSize: contain
---

<!-- 第 35 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-36.png
backgroundSize: contain
---

<!-- 第 36 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-37.png
backgroundSize: contain
---

<!-- 第 37 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-38.png
backgroundSize: contain
---

<!-- 第 38 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-39.png
backgroundSize: contain
---

<!-- 第 39 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-40.png
backgroundSize: contain
---

<!-- 第 40 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-41.png
backgroundSize: contain
---

<!-- 第 41 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-42.png
backgroundSize: contain
---

<!-- 第 42 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-43.png
backgroundSize: contain
---

<!-- 第 43 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-44.png
backgroundSize: contain
---

<!-- 第 44 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-45.png
backgroundSize: contain
---

<!-- 第 45 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-46.png
backgroundSize: contain
---

<!-- 第 46 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-47.png
backgroundSize: contain
---

<!-- 第 47 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-48.png
backgroundSize: contain
---

<!-- 第 48 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-49.png
backgroundSize: contain
---

<!-- 第 49 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-50.png
backgroundSize: contain
---

<!-- 第 50 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-51.png
backgroundSize: contain
---

<!-- 第 51 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-52.png
backgroundSize: contain
---

<!-- 第 52 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-53.png
backgroundSize: contain
---

<!-- 第 53 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-54.png
backgroundSize: contain
---

<!-- 第 54 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-55.png
backgroundSize: contain
---

<!-- 第 55 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-56.png
backgroundSize: contain
---

<!-- 第 56 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-57.png
backgroundSize: contain
---

<!-- 第 57 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-58.png
backgroundSize: contain
---

<!-- 第 58 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-59.png
backgroundSize: contain
---

<!-- 第 59 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-60.png
backgroundSize: contain
---

<!-- 第 60 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-61.png
backgroundSize: contain
---

<!-- 第 61 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-62.png
backgroundSize: contain
---

<!-- 第 62 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-63.png
backgroundSize: contain
---

<!-- 第 63 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-64.png
backgroundSize: contain
---

<!-- 第 64 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-65.png
backgroundSize: contain
---

<!-- 第 65 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-66.png
backgroundSize: contain
---

<!-- 第 66 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-67.png
backgroundSize: contain
---

<!-- 第 67 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-68.png
backgroundSize: contain
---

<!-- 第 68 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-69.png
backgroundSize: contain
---

<!-- 第 69 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-70.png
backgroundSize: contain
---

<!-- 第 70 页批注:

-->

---
layout: image
image: /The-beamer-class-for-LATEX/The-beamer-class-for-LATEX-71.png
backgroundSize: contain
---

<!-- 第 71 页批注:

-->
