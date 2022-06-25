



目录
==

* [Ransom.DoubleExt 规则组](#ransomdoubleext-)
	* [规则：Ransom.DoubleExt.A](#ransomdoubleexta)
	* [规则：Ransom.DoubleExt.B](#ransomdoubleextb)

# Ransom.DoubleExt 规则组

## 规则：Ransom.DoubleExt.A
  
状态：启用

源程序`*`做出以下操作时，提示用户处理
- 对路径为`*.docx.>`的文件进行创建操作
- 对路径为`*.xlsx.>`的文件进行创建操作
- 对路径为`*.pptx.>`的文件进行创建操作
- 对路径为`*.doc.>`的文件进行创建操作
- 对路径为`*.xls.>`的文件进行创建操作
- 对路径为`*.ppt.>`的文件进行创建操作

## 规则：Ransom.DoubleExt.B
  
状态：启用

源程序`*`做出以下操作时，提示用户处理
- 对路径为`>\Users\>\Pictures\*.jpg.>`的文件进行创建操作
- 对路径为`>\Users\>\Pictures\*.png.>`的文件进行创建操作
- 对路径为`>\Users\>\Desktop\*.jpg.>`的文件进行创建操作
- 对路径为`>\Users\>\Desktop\*.png.>`的文件进行创建操作
  
***rule.json hash: e5f5fd0249fcb5415f8445a356cf9b8d1b081981b6bbe3ce8d4e7b3052fd799a***