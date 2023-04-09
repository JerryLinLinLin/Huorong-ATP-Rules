



目录
==

* [Telemetry.PowerShell](#telemetrypowershell)
	* [Telemetry.PowerShell.A](#telemetrypowershella)
	* [Telemetry.PowerShell.B](#telemetrypowershellb)
	* [Telemetry.PowerShell.C](#telemetrypowershellc)

# Telemetry.PowerShell

## Telemetry.PowerShell.A
  
状态：未启用

行为描述：源程序`*\powershell.exe`做出以下操作时，提示用户处理
- 对路径为`*.exe`的文件进行**创建**操作

## Telemetry.PowerShell.B
  
状态：未启用

行为描述：源程序`*\powershell.exe`做出以下操作时，提示用户处理
- 对路径为`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\*`的注册表进行**创建**操作

## Telemetry.PowerShell.C
  
状态：未启用

行为描述：源程序`*\powershell.exe`做出以下操作时，提示用户处理
- 对路径为`\SOFTWARE\Policies\Microsoft\Windows\PowerShell\ExecutionPolicy`的注册表进行**写入**操作
  
***rule.json hash: 6176d464860dad2aa05aac6d1bdd4d556618cc1fa09a68bc9aba16208d464613***  
简体中文 | [English](/README_en_us.md)