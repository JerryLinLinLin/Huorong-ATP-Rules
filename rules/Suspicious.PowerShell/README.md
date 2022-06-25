



目录
==

* [Suspicious.PowerShell 规则组](#suspiciouspowershell-)
	* [规则：Suspicious.PowerShell.A](#suspiciouspowershella)
	* [规则：Suspicious.PowerShell.B](#suspiciouspowershellb)

# Suspicious.PowerShell 规则组

## 规则：Suspicious.PowerShell.A
  
状态：未启用

源程序`*\Windows\Sys?????\*.exe`做出以下操作时，自动阻止
- 对路径为*\powershell.exe的程序进行操作

## 规则：Suspicious.PowerShell.B
  
状态：启用

源程序`*\powershell.exe`做出以下操作时，提示用户处理
- 对路径为HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\*的注册表进行创操作
- 对路径为*.exe的文件进行创操作
- 对路径为*\Users\*\AppData\*的程序进行操作
  
***rule.json hash: a07c32503aed526ce12772851f805a467b3155bdb1cc30e7e84fe2d9fdbdaa4b***