#前言
今天逛博客园看到一篇好玩的文章，于是玩了玩。  

题目是分析下面代码的结果  
def multipliers():  
&emsp;&emsp;return [lambda x: i * x for i in range(4)]  
print([m(2) for m in multipliers()])  

结果是：  
[6, 6, 6, 6]
