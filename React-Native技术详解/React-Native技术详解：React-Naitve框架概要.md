# ReactNative技术详解：React-Naitve框架概要

## 一、简介

React-Native 是FaceBook在2015年开源的，一个基于 JavaScript，具备动态配置能力（**针对原生热更新而言，不只是动态更改配置信息，也能动态更新执行逻辑**），面向前端开发者的移动端开发框架。  
React-Native和 React的编程思路有些不同，React是以WebView（浏览器）为后端，操作Virtual DOM进行视图渲染的，而React-Native是**以ios或者anroid原生控件为后端，但以React component 的方式Expose出来进行视图渲染的**。

## 二、React-Native的框架概要

![avatar](https://github.com/knowtheroot/KnowTheRoot_iOS/blob/master/Resources/Imgs/react-native01.png)

### 1.React

React 是FaceBook在2013年开源的，基于JavaScript的，可以用简洁的语法高效绘制DOM，进而构建“可预期的”、“声明式的”Web用户界面的UI框架（库）。

### 2.Virtual DOM

既虚拟DOM，相对Browser环境下的DOM而言，Virtual DOM是DOM在内存中的一种轻量级表达方式（lightweight representation of the document），可以通过不同的渲染引擎生成不同平台下的UI，**JS和Native之间通过Bridge通信**。

## 三、React-Naitve的优势

### 1.渲染
React-Native在JavaScript中抽象操作系统原生的UI组件，**使用的是Android或iOS的本地控代替DOM元素来渲染**，所以在UI渲染上已经非常接近Native App了。

### 2.编译
虽然业务逻辑代码使用JavaScript，但由于JavaScript是**即时编译**的，也就是第一次使用时会将JavaScript代码编译成二进制文件，所以JavaScript得运行效率比较高。因此，React Native的运行效率要比基于HTML5、CSS等技术的PhoneGap、AppCan高很多，因为这些技术直接使用HTML5进行渲染，而HTML5会大量使用DOM技术，**DOM的操作是很消耗性能的**。
