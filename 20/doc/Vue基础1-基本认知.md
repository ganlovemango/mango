## 一、Vue官网
[Vue中文网](https://cn.vuejs.org/)


## 二、Vue简介
Vue是一个前端的双向绑定类的框架，新的Vue版本参考了React的部分设计，当然也有自己独特的地方，比如Vue的单文件组件开发方式都很有创新，另外Vue自身的一些绑定的语法、用法等都非常精炼，很容易上手，而且第三方的插件都非常丰富，社区非常活跃，最新的文档都有中文版本。而且Vue配合官方的和第三方的库可以实现单文件的组件化开发、SPA等现代化前端开发。
```
  - 是一个轻量级MVVM框架(大小只有18KB)
  - 数据驱动+组件化的前端开发
  - 社区完善
```

## 三、MVVM框架
- MVVM框架好处
    ```
    - 针对具有复杂交互逻辑的前端应用
    - 提供的结构抽象
    - 主要目的是为了解决应用程序展示结构、业务逻辑之间的紧耦合关系
    - 通过ajax数据持久化，保证前端用户体验(部分异步刷新)
    ```
    ![MVVM框架](http://upload-images.jianshu.io/upload_images/1801379-389ba972ad3c8191.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- MVC组成
    ```
    - 模型(Model): 处理数据和业务逻辑
    - 视图(View): 向用户展示数据的界面
    - 控制器(Controller): 组织调度相应的处理模型
    ```
    
## 四、Vue入门
Vue 可以直接把它当做一个js库使用，可以很简单的接入到你的项目中，或者你只需要使用双向数据绑定。
```
  需求: 网页中有个div标签，而需要有json对象存储数据，把json对象上的数据放到div。

  - 在页面中引入Vue库
  <script src="https://unpkg.com/vue/dist/vue.js"></script>

  - 在页面中div标签添加一个id，例如app
    <div id='app'></app>

  - 创建Vue的对象，并把数据绑定到上面创建好的div上去
```
```
<html>
	<head>
        <meta charset="utf8"/>
		<title>hello vue</title>
        <!--1、引入Vue库-->
        <script src="https://unpkg.com/vue/dist/vue.js"></script>
	</head>

	<body>
        <!-- 2、创建一个Div -->
		<div id="app">
            <!--Vue的模板的绑定数据的方法，可以用两对花括号进行绑定Vue中的数据对象的属性 -->
            {{message}}
        </div>
	</body>

    <!-- 3、创建Vue的对象，并把数据绑定到上面创建好的div上去 -->
    <script>
        // 创建Vue对象(Vue的核心对象)
        var app = new Vue({
            el: '#app', // el属性：把当前Vue对象挂载到 div标签上，#app是id选择器
            data: {     // data: 是Vue对象中绑定的数据
                message: 'hello Vue!'       // message 自定义的数据
            }
        });
    </script>
</html>
```


## 五、Vue核心思想
- 数据驱动(即是双向的数据绑定)
DOM是数据的一种自然映射。双向是指：HTML标签数据 绑定到 Vue对象，另外反方向数据也是绑定的。Vue对象的改变会直接影响到HTML的标签的变化，而且标签的变化也会反过来影响Vue对象的属性的变化。之前Dom驱动的开发方式尤其是以jQuery为主的开发时代，都是dom变化后，触发js事件，然后在事件中通过js代码取得标签的变化，再跟后台进行交互，然后根据后台返回的结果再更新HTML标签，异常的繁琐。有了Vue这种双向绑定，让开发人员只需要关心json数据的变化即可，Vue自动映射到HTML上，而且HTML的变化也会映射回js对象上，开发方式直接变革成了前端由数据驱动的开发时代。
![数据驱动](http://upload-images.jianshu.io/upload_images/1801379-c6dfee841d4d0174.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 组件化
扩展HTML元素，封装可重用的代码。
    ```
    组件设计原则:
        - 页面上每个独立的可视/可交互区域视为一个组件(例如头部尾部)；
        - 每个组件对应一个工程目录，组件所需要的各种资源在该目录下就近维护；
        - 页面不过是组件的容器，组件可以嵌套自由组合，形成完整的页面；
    ```