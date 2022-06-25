



目录
==

* [Suspicious.ScriptHost](#suspiciousscripthost)
	* [Suspicious.ScriptHost.A](#suspiciousscripthosta)
	* [Suspicious.ScriptHost.B](#suspiciousscripthostb)

# Suspicious.ScriptHost

## Suspicious.ScriptHost.A
  
状态：启用

行为描述：源程序`*\?script.exe`做出以下操作时，提示用户处理
- 对路径为`*\Windows\Sys?????\*.exe`的程序进行**执行**操作
- 对路径为`*.exe`的文件进行**创建**操作
- 对路径为`*.dll`的文件进行**创建**操作
- 对路径为`*\Users\*\AppData\*`的程序进行**执行**操作

## Suspicious.ScriptHost.B
  
状态：启用

行为描述：源程序`*\Windows\Sys?????\*.exe`做出以下操作时，提示用户处理
- 对路径为`*\?script.exe`的程序进行**执行**操作
  
***rule.json hash: d2705aeab053e2c7a8fb7a2a57bd21c0378b71cce1c8b9403b89c3e7941abf12***