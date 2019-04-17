![avatar](https://user-gold-cdn.xitu.io/2019/4/10/16a07199d04afb58?w=1600&h=586&f=png&s=41169)
#### 关于作者
```
E-moss，程序员，爱好阅读和撸狗，主要从事iOS开发工作，公众号：知本集。  
主要分享和编写技术方面文章，不定期分享读书笔记，亦可访问“知本集”Git地址：https://github.com/knowtheroot/KnowTheRoot_iOS，欢迎提出问题和讨论。
```
#### 文章目录
- Flutter框架架构
- Widget
- Flutter界面渲染简述
- 总结
## 前言

目前hybrid开发模式：

1.通过WebView来进行原生和web交互

2.为了解决WebView性能差的问题，以React Native为代表的一类框架将最终渲染工作交还给了系统，虽然同样使用类HTML+JS的UI构建逻辑，但是最终会生成对应的自定义原生控件，以充分利用原生控件相对于WebView的较高的绘制效率。

## 一、Flutter框架架构
Flutter的架构主要分成三层:
- Framework 
- Engine
- Embedder

### 1.Framework
**Framework使用dart实现**，包括:  
- Material Design风格的Widget,Cupertino(针对iOS)风格的Widgets
- 文本/图片/按钮等基础Widgets，渲染，动画，手势等，此部分的核心代码是:flutter仓库下的flutter package
- sky_engine仓库下的io,async,ui(dart:ui库提供了Flutter框架和引擎之间的接口)等package
> Widgets:可以理解为组件。

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
 
## 二、Widget
 
 目前上主流的思想，都希望将各个**ui控件解耦**，慢慢演变出组件化的思想。
   
   Flutter控件主要分为两大类:
   - **StatelessWidget**
   - **StatefulWidget**
 

#### StatelessWidget
顾名思义，StatelessWidget是状态不可变的widget。初始状态设置以后就不可再变化。如果需要变化需要重新创建。  
当传入数据改变时会重新渲染UI。  
StatelessWidget用来展示静态的文本或者图片。

#### StatefulWidget
当传入数据和本类数据改变时StatefulWidget都会重新渲染UI。  
如果控件需要根据外部数据或者用户操作来改变的话，就需要使用StatefulWidget。

#### 什么是State?
State的概念来源于Facebook的流行Web框架React，React风格的框架中使用控件树和各自的状态来构建界面，当某个控件的状态发生变化时由框架负责对比前后状态差异并且采取最小代价来更新渲染结果。

#### widget怎么保存状态的？
Flutter是**通过引入了State来保存状态**。  
当State的状态改变时，<u>能重新构建本节点以及孩子的Widget树来进行UI变化。</u>如果需要主动改变State的状态，需要通过**setState()方法**进行触发，单纯改变数据是不会引发UI改变的。

## 三、Flutter界面渲染简述
Flutter界面渲染过程分为三个阶段：
- 布局
- 绘制
- 合成

布局和绘制在**Flutter框架(Framework)**中完成，合成则交由**引擎(Engine)**负责。  
详细的渲染原理将在《Flutter技术原理详解》讲解。

## 四、总结
### Flutter与ReactNative的对比
RN的渲染机制是基于前端框架的考虑,复杂的UI渲染是**需要依赖多个view叠加**。  
例如渲染一个复杂的ListView,每一个小的控件,都是一个native的view,然后相互组合叠加，当每次滚到刷新时，性能都是一个巨大的考验。
#### ReactNative

- 采用Javascript开发，需学React，成本高
- 需要JavaScript桥接器，实现JS到Native转化，性能耗损
- 访问原生UI，频繁操作易出性能问题 
- 支持线上动态性，可有效避免频繁更新版本

#### Flutter

- 采用Dart开发,可直接编译成Native代码（易学）
- 自带UI组件和渲染器，仅依赖系统提供的Canvas（无桥接耗损）
- 暂不支持线上动态性，目前Android支持，iOS不支持
