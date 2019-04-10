# Flutter技术概览

## 前言

目前hybrid开发模式：

1.通过WebView来进行原生和web交互

2.为了解决WebView性能差的问题，以React Native为代表的一类框架将最终渲染工作交还给了系统，虽然同样使用类HTML+JS的UI构建逻辑，但是最终会生成对应的自定义原生控件，以充分利用原生控件相对于WebView的较高的绘制效率。

