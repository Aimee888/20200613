# CallEXEParaller.py
### 目的
并行调用两个或两个以上的EXE程序  
### 导入库
subprocess，threading  
### 方法
开启多线程运行调用exe的函数  
### 功能  
rose.exe 画一朵玫瑰花  
CPUUsage.exe 画一个CPU使用率的折线图
### Rose动画
![Rose](https://github.com/Aimee888/20200613/blob/master/20200613/%E5%B9%B6%E8%A1%8C%E8%B0%83%E7%94%A8%E4%B8%A4%E4%B8%AAEXE/img_folder/rose.gif)
### Usage动态折线图
![Usage](https://github.com/Aimee888/20200613/blob/master/20200613/%E5%B9%B6%E8%A1%8C%E8%B0%83%E7%94%A8%E4%B8%A4%E4%B8%AAEXE/img_folder/usage.gif)  

=================================History===============================  
V0.0.0.1 并行调用rose.exe和Usage.exe  
&emsp;&emsp;&emsp;可能出现的问题：1.py中会切换路径到exe的目录中，由于是并行执行，所以此时的路径并不一定是在exe所在的目录，
如果exe里面需要调用文件并且用的相对路径，可能会报错，这个程序之所以通过，可能是因为Rose.exe不需要用到文件，执行Usage.exe
的时候已经在Usage.exe的目录中了，这存在一个概率问题，当并行程序少时，刚好两个程序都执行到切换路径语句的概率是比较小的，
但是这也是个隐患。  
V0.0.0.2 并行调用rose.exe，Usage.exe，readini.exe  
&emsp;&emsp;&emsp;刚开始，出现了在V0.0.0.1中担心的问题，因为路径切换导致readini.exe找不到“TEST”这个Key。
后来发现subprocess函数里面有个参数cwd可以直接指定运行路径，完美解决问题。