



目录
==

* [Suspicious.RunFromSusPath 规则组](#suspiciousrunfromsuspath-)
	* [规则：Suspicious.RunFromSusPath.A](#suspiciousrunfromsuspatha)
	* [规则：Suspicious.RunFromSusPath.B](#suspiciousrunfromsuspathb)
	* [规则：Suspicious.RunFromSusPath.C](#suspiciousrunfromsuspathc)
	* [规则：Suspicious.RunFromSusPath.D](#suspiciousrunfromsuspathd)
	* [规则：Suspicious.RunFromSusPath.E](#suspiciousrunfromsuspathe)

# Suspicious.RunFromSusPath 规则组

## 规则：Suspicious.RunFromSusPath.A
  
状态：启用

源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\Users\*\AppData\Roaming\>`的程序进行执行操作
- 对路径为`*\Users\*\AppData\>`的程序进行执行操作
- 对路径为`*\Users\>\>`的程序进行执行操作
- 对路径为`*\ProgramData\>`的程序进行执行操作
- 对路径为`*\Program Files\>`的程序进行执行操作
- 对路径为`*\Program Files (x86)\>`的程序进行执行操作
- 对路径为`*\Users\*\AppData\Local\>`的程序进行执行操作
- 对路径为`*\Users\>\Documents\>`的程序进行执行操作
- 对路径为`*\Users\>\Documents\>\>`的程序进行执行操作
- 对路径为`*\Users\Public\>.bat`的文件进行读取操作

## 规则：Suspicious.RunFromSusPath.B
  
状态：启用

源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\Recycler\*`的程序进行执行操作
- 对路径为`*\$RECYCLE.BIN\*`的程序进行执行操作
- 对路径为`*\System Volume Information\*`的程序进行执行操作

## 规则：Suspicious.RunFromSusPath.C
  
状态：未启用

源程序`*`做出以下操作时，自动阻止
- 对路径为`*\ProgramData\>\>.exe`的程序进行执行操作

## 规则：Suspicious.RunFromSusPath.D
  
状态：启用

源程序`*\Windows\Sys?????\>`做出以下操作时，提示用户处理
- 对路径为`*\Users\*\AppData\Roaming\>\>.exe`的程序进行执行操作

## 规则：Suspicious.RunFromSusPath.E
  
状态：未启用

源程序`*`做出以下操作时，自动阻止
- 对路径为`*\Users\*\AppData\Roaming\>\>.exe`的程序进行执行操作
  
***rule.json hash: 3997ac4b56fb80d81d036c3beabcb423cfd73598afa0d93b5861c6523f10ac81***