# Flutter技术概览

## 前言

目前hybrid开发模式：

1.通过WebView来进行原生和web交互

2.为了解决WebView性能差的问题，以React Native为代表的一类框架将最终渲染工作交还给了系统，虽然同样使用类HTML+JS的UI构建逻辑，但是最终会生成对应的自定义原生控件，以充分利用原生控件相对于WebView的较高的绘制效率。

## 一、框架架构
Flutter的架构主要分成三层:
- Framework 
- Engine
- Embedder

### 1.Framework
**Framework使用dart实现**，包括:  
- Material Design风格的Widget,Cupertino(针对iOS)风格的Widgets
- 文本/图片/按钮等基础Widgets，渲染，动画，手势等，此部分的核心代码是:flutter仓库下的flutter package
- sky_engine仓库下的io,async,ui(dart:ui库提供了Flutter框架和引擎之间的接口)等package
> Widgets:可以理解为小部件或者小控件。

### 2.Engine
**Engine使用C++实现**，主要包括:
- Skia
- Dart
- Text
  
> Skia是开源的二维图形库，提供了适用于多种软硬件平台的通用API。

### 3.Embedder

Embedder是一个**嵌入层**。  
即把Flutter嵌入到各个平台上去，这里做的主要工作包括渲染Surface设置,线程设置，以及插件等。从这里可以看出，Flutter的平台相关层很低，平台(如iOS)只是提供一个画布，剩余的所有渲染相关的逻辑都在Flutter内部，这就使得它具有了很好的跨端一致性。
  
 从架构图可以看出，从头到尾重写一套跨平台的UI框架，包括UI控件、渲染逻辑甚至开发语言。  
 1.**渲染引擎依靠跨平台的Skia图形库来实现**，依赖系统的只有图形绘制相关的接口，可以在最大程度上保证不同平台、不同设备的体验一致性;  
 2.**逻辑处理使用支持AOT的Dart语言**，执行效率也比JavaScript高得多。
