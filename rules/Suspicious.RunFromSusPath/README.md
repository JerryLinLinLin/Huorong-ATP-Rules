


  
简体中文 | [English](README_en_us.md)  
  

目录
==

* [Suspicious.RunFromSusPath](#suspiciousrunfromsuspath)
	* [Suspicious.RunFromSusPath.A](#suspiciousrunfromsuspatha)
	* [Suspicious.RunFromSusPath.B](#suspiciousrunfromsuspathb)
	* [Suspicious.RunFromSusPath.C](#suspiciousrunfromsuspathc)
	* [Suspicious.RunFromSusPath.D](#suspiciousrunfromsuspathd)

# Suspicious.RunFromSusPath

## Suspicious.RunFromSusPath.A
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\Users\*\AppData\Roaming\>`的程序进行`执行`操作
- 对路径为`*\Users\*\AppData\>`的程序进行`执行`操作
- 对路径为`*\Users\>\>`的程序进行`执行`操作
- 对路径为`*\ProgramData\>`的程序进行`执行`操作
- 对路径为`*\Program Files\>`的程序进行`执行`操作
- 对路径为`*\Program Files (x86)\>`的程序进行`执行`操作
- 对路径为`*\Users\*\AppData\Local\>`的程序进行`执行`操作
- 对路径为`*\Users\>\Documents\>`的程序进行`执行`操作
- 对路径为`*\Users\>\Documents\>\>`的程序进行`执行`操作
- 对路径为`*\Users\Public\>.bat`的文件进行`读取`操作

## Suspicious.RunFromSusPath.B
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\Recycler\*`的程序进行`执行`操作
- 对路径为`*\$RECYCLE.BIN\*`的程序进行`执行`操作
- 对路径为`*\System Volume Information\*`的程序进行`执行`操作

## Suspicious.RunFromSusPath.C
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\ProgramData\>\>.exe`的程序进行`执行`操作

## Suspicious.RunFromSusPath.D
  
状态：启用

行为描述：源程序`*\Windows\Sys?????\>`做出以下操作时，提示用户处理
- 对路径为`*\Users\*\AppData\Roaming\>\>.exe`的程序进行`执行`操作
  
***rule.json hash: 0ce318e7bf946e22f9b9bc6bb13188f0e1fc43c42d10a7699f0d4a0c6af16cb7***