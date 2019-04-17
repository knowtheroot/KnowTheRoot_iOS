# ReactNative技术详解：React-Naitve框架概要

## 一、简介

React-Native 是FaceBook在2015年开源的，一个基于 JavaScript，具备动态配置能力（**针对原生热更新而言，不只是动态更改配置信息，也能动态更新执行逻辑**），面向前端开发者的移动端开发框架。  
React-Native和 React的编程思路有些不同，React是以WebView（浏览器）为后端，操作Virtual DOM进行视图渲染的，而React-Native是**以ios或者anroid原生控件为后端，但以React component 的方式Expose出来进行视图渲染的**。

## 二、React-Native的框架

![avatar](https://github.com/knowtheroot/KnowTheRoot_iOS/blob/master/Resources/Imgs/react-native01.png)

