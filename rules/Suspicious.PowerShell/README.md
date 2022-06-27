



目录
==

* [Suspicious.PowerShell](#suspiciouspowershell)
	* [Suspicious.PowerShell.A](#suspiciouspowershella)
	* [Suspicious.PowerShell.B](#suspiciouspowershellb)

# Suspicious.PowerShell

## Suspicious.PowerShell.A
  
状态：未启用

行为描述：源程序`*\Windows\Sys?????\*.exe`做出以下操作时，自动阻止
- 对路径为`*\powershell.exe`的程序进行**执行**操作

## Suspicious.PowerShell.B
  
状态：启用

行为描述：源程序`*\powershell.exe`做出以下操作时，提示用户处理
- 对路径为`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\*`的注册表进行**创建**操作
- 对路径为`*.exe`的文件进行**创建**操作
- 对路径为`*\Users\*\AppData\*`的程序进行**执行**操作
  
***rule.json hash: b8719134d7772aa185965fa0b3f36db165a1ce1c5dd8533e41bbfe674f5f3437***