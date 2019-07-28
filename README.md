# Salary Report #

老婆需要一个薪酬计算器，减少操作Excel时发生的错误。当然是需要GUI的。给
她搭一个WebApp又似乎用不上，因为应该只有她一个人使用这个工具。写跨平台
GUI的开发语言有很多。脚本语言对比了tcl和python。第一反应就是用python写
GUI。因为python很火，特别以后向AI方向发展一定避不开它。看了一下python
的GUI框架，发现官方标准是tk。于是又看了一下tcl。因为Mac OS X自带tcl/tk，
而OSX自带的python跑tkinter经常崩溃。但发现实在接受不来tcl的语法，还是
在python官网下载了安装器安装全新的python3。试跑了一下测试代码，GUI出现
了。
	
现打算用Excel文件做数据持久化保存格式。每个月独立保存一个文件。管理器
能设置文件保存路径，并按年、月规则在Treeview里显示数据入口。然后在类
table的widget里显示具体数据。

