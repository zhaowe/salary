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

接下来有两项工作，一是了解老婆的工作规则，譬如Excel公式；二是学习
tkinter相关知识。

## Pandas ##

Pandas用于读写Excel。

## Tkinter ##

python 2.x和3.x的tkinter不兼容。老婆单位用的电脑是xp，只能安装3.4以下
的版本，加上Mac也对python3兼容不好，决定用python2开发。
	
UI设计决定是左边一个Treeview，右边一个table。但tkinter没有自带但table
widget。一是用自定义widget简单实现，二是安装tktable扩展。都快速尝试一
下吧。
	
### 自定义widget ###

最简单都就是用message widget显示多行文本.

### tktable ###

在xp虚拟机里安装

## 工作规则 ##

 
## Emacs ##

Emacs自带python-mode。C-c C-c可以将运行buffer的代码，dedicated选n就不
会有python编译器的buffer。

用git管理文件版本。C-x v v是check in。在comment编辑里，C-c C-c就可以结
束编辑。
