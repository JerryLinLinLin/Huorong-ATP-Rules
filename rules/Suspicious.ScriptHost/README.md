



目录
==

* [Suspicious.ScriptHost 规则组](#suspiciousscripthost-)
	* [规则：Suspicious.ScriptHost.A](#suspiciousscripthosta)
	* [规则：Suspicious.ScriptHost.B](#suspiciousscripthostb)

# Suspicious.ScriptHost 规则组

## 规则：Suspicious.ScriptHost.A
  
状态：启用

源程序`*\?script.exe`做出以下操作时，提示用户处理
- 对路径为*\Windows\Sys?????\*.exe的程序进行操作
- 对路径为*.exe的文件进行创操作
- 对路径为*.dll的文件进行创操作
- 对路径为*\Users\*\AppData\*的程序进行操作

## 规则：Suspicious.ScriptHost.B
  
状态：启用

源程序`*\Windows\Sys?????\*.exe`做出以下操作时，提示用户处理
- 对路径为*\?script.exe的程序进行操作
  
***rule.json hash: d2705aeab053e2c7a8fb7a2a57bd21c0378b71cce1c8b9403b89c3e7941abf12***