
# 一级标题

## 二级标题

[toc]

这是用paste image 插件来的功能
![](2023-02-13-19-36-27.png)


Emmet插件: 自动生成HTML部分代码

```html
<!--this is a comment-->
```

## 标准的文档结构
```html
<！DOCTYPE> html>
```
文档声明，我使用的标准是HTML5
不写的话，将导致浏览器进入怪异渲染模式。

### Element html
根元素 一个页面就一个。HTML5中没有强制写这个元素

属性：
lang language 比如 lang="cmn-hans" zh-CN 已经过时了

head 和 body 元素都必须是 html 的子元素，虽然说html5可以省略
### head脑子
内容是不会显示的。 charset： 指定网页内部编码

中文汉字的编码表叫 GB2312，台湾 是GBK
UTF-8 是 unicode 的一个版本的编码

一般代码都是写入body元素内
### Element a 
attributes:
href 网址
title 标题

### 空元素
有些元素是没有结尾的 叫空元素
比如 img

关于元素嵌套
一些词：父元素，子元素，祖先元素ancestor，后代元素，兄弟元素

## 语义化是什么

每个html元素都有含义

a 超链接
p 段落
h1 一级标题

所有元素与展示效果无关，因为那是css的工作
不管把一级标题变得多小 他都是一级标题。由于浏览器是默认带有css样式的，所以每个元素都是有样式的

为什么要强调要按照每个元素含义来写html？
为了优化搜索引擎（SEO）。搜索引擎会从整个互联网抓取页面的源代码（html5） 所以要明确区分每个元素