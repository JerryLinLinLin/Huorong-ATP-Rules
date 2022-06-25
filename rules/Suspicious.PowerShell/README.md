



目录
==

* [Suspicious.PowerShell](#suspiciouspowershell)
	* [Suspicious.PowerShell.A](#suspiciouspowershella)
	* [Suspicious.PowerShell.B](#suspiciouspowershellb)

# Suspicious.PowerShell

## Suspicious.PowerShell.A
  
状态：未启用

行为描述：源程序`*\Windows\Sys?????\*.exe`做出以下操作时，自动阻止
- 对路径为`*\powershell.exe`的程序进行执行操作

## Suspicious.PowerShell.B
  
状态：启用

行为描述：源程序`*\powershell.exe`做出以下操作时，提示用户处理
- 对路径为`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\*`的注册表进行创建操作
- 对路径为`*.exe`的文件进行创建操作
- 对路径为`*\Users\*\AppData\*`的程序进行执行操作
  
***rule.json hash: a07c32503aed526ce12772851f805a467b3155bdb1cc30e7e84fe2d9fdbdaa4b***