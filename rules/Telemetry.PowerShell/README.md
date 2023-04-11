


  
简体中文 | [繁體中文](README_zh_tw.md) | [English](README_en_us.md)  
  

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
- 对路径为`*.exe`的文件进行`创建`操作

## Telemetry.PowerShell.B
  
状态：未启用

行为描述：源程序`*\powershell.exe`做出以下操作时，提示用户处理
- 对路径为`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\*`的注册表进行`创建`操作

## Telemetry.PowerShell.C
  
状态：未启用

行为描述：源程序`*\powershell.exe`做出以下操作时，提示用户处理
- 对路径为`\SOFTWARE\Policies\Microsoft\Windows\PowerShell\ExecutionPolicy`的注册表进行`写入`操作
  
***rule.json hash: 29f6108776c83ada5ba0762361814e853353ce651363a49dbbd469df11219859***