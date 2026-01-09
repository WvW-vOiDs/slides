---
# **************************************************************************** #
#                                     Info                                     #
# **************************************************************************** #

# 幻灯片的总标题，如果没有指定，那么将以第一张拥有标题的幻灯片的标题作为总标题。
title: {title}
# subtitle: subtitle

# 网页的标题模板，`%s` 会被页面的标题替换。
titleTemplate: '%s - WvW-vOiDs'

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
aspectRatio: 16/9

# favicon 可以是本地文件路径，也可以是一个 URL
favicon: "https://wvw-voids.github.io/icon/favicon.ico"

# 定义幻灯片与下一张幻灯片之间的过渡
# 了解更多： https://cn.sli.dev/guide/animations.html#slide-transitions
transition: slide-left

# **************************************************************************** #
#                                   Exporting                                  #
# **************************************************************************** #

# 要导出文件的文件名称
exportFilename: {base_name}-exported

# 导出的 PDF 或 PPTX 文件中的作者字段。
author: WvW-vOiDs

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

# 从何处加载 monaco 的类型，可以是 'cdn'，'local' 或 'none'
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
record: dev

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
| <kbd>o</kbd>                                                       | Toggle Quick Overview          |
| <kbd>g</kbd>                                                       | Show goto...                   |

<div class="abs-br m-6 text-xl">
  <a href="https://wvw-voids.github.io" target="_blank" class="slidev-icon-btn">
    <carbon:logo-github />
  </a>
</div>