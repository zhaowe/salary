# Salary Report #

老婆需要一个薪酬计算器，减少操作Excel时发生的错误。当然是需要GUI的。给
她搭一个WebApp又似乎用不上，因为应该只有她一个人使用这个工具。写跨平台
GUI的开发语言有很多。脚本语言对比了tcl和python。第一反应就是用python写
GUI。因为python很火，特别以后向AI方向发展一定避不开它。看了一下python
的GUI框架，发现官方标准是tk。于是又看了一下tcl。因为Mac OS X自带tcl/tk，
而OSX自带的python跑tkinter经常崩溃。但发现实在接受不来tcl的语法，还是
在python官网下载了安装器安装全新的python3。试跑了一下测试代码，GUI出现
了。
	
安装python时要选上‘Add python.exe to PATH’

现打算用Excel文件做数据持久化保存格式。每个月独立保存一个文件。管理器
能设置文件保存路径，并按年、月规则在Treeview里显示数据入口。然后在类
table的widget里显示具体数据。

把Mac里的idle和pip都找出来了。试了一下，Mac的idle不能输入中文，还是用
Emacs。Emacs也越用越顺手，基本上可以在Emacs里完成所有操作。估计逐渐连
xp的虚拟机都可以很少打开。

## Github ##

打算暂停本项目，将代码上传到GitHub保存。

## TODO ##

- 公共列表变量保存workbook对象

## Python ##

interactive很好用，原型验证和查看帮助就用它。用help()和dir()能看到基本
的帮助内容。这就是它越来越火的原因。

type()可以返回变量的类型。切片（slice）返回类型是list。

## pyinstaller ##

用pyinstaller制作可独立运行都最终产品。估计这要在xp上执行。

## pypi ##

模块安装工具。python2.7在xp环境运行pip存在字符集不兼容问题。在
Lib/site-packages文件夹增加sitecustomize.py文件，如下

`import sys
sys.setdefaultencoding('gbk')`

## xlutils ##

用xlrd、xlwt和xlutils读写Excel文件。老婆用的Excel是2010版，xlrd和xlwt
都不支持2010。

`pip install xlutils`

## openpyxl ##

这是python-excel.org推荐的2010读写包。

读取文件用load_workbook。

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

`pip install paphra-tktable`

## 工作规则 ##

 
## Emacs ##

Emacs自带python-mode。C-c C-c可以将运行buffer的代码，dedicated选n就不
会有python编译器的buffer。

用git管理文件版本。C-x v v是check in。在comment编辑里，C-c C-c就可以结
束编辑。
