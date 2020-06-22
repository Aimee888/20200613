# Markdown基本语法
## Markdown标题
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题
# Markdown块应用
> 第一层
>> 第二层
>>> 第三层
>>>> 第四层
## Markdown代码块
这是一小段`代码`。
常常可以用来描述某种快捷键，例如`Ctrl+F`。  
    function DeleteText()  
    {  
        string s = "示例文本";  
        ...  
        ClipBoard.Delete();  
    }
    function DeleteImage()  
    {  
        Image img = new Image();  
        ...  
        ClipBoard.Delete();  
    }  
## Markdown列表
- 无序列表
1. 有序列表1
1. 有序列表2
1. 有序列表3
+ 嵌套列表项1  
    + 嵌套列表项2  
+ 嵌套列表项3  
    + 嵌套列表项4  
        + 嵌套列表项5   
## Markdown链接
##### 文字超链接
[我的小窝](http://www.lunarsf.club "我的个人网站")
##### 图像超链接
![找不到图像文件时显示的文本](.\图片\girl.jpg)  
##### 索引超链接
[参见百度官网][1x]
[1x]:http://www.baidu.com
##### 自动链接
<http://www.baidu.com>  


