


  
简体中文 | [繁體中文](README_zh_tw.md) | [English](README_en_us.md)  
  

目录
==

* [Suspicious.PowerShell](#suspiciouspowershell)
	* [Suspicious.PowerShell.A](#suspiciouspowershella)
	* [Suspicious.PowerShell.B](#suspiciouspowershellb)
	* [Suspicious.PowerShell.C](#suspiciouspowershellc)

# Suspicious.PowerShell

## Suspicious.PowerShell.A
  
状态：启用

行为描述：源程序`*\Windows\Sys?????\*.exe`做出以下操作时，提示用户处理
- 对路径为`*\powershell.exe`的程序进行`执行`操作

## Suspicious.PowerShell.B
  
状态：启用

行为描述：源程序`*\powershell.exe`做出以下操作时，提示用户处理
- 对路径为`*\Users\*\AppData\*`的程序进行`执行`操作

## Suspicious.PowerShell.C
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\WindowsPowerShell\v1.0\profile.ps1`的文件进行`写入`操作
- 对路径为`*\WindowsPowerShell\v1.0\Microsoft.PowerShell*profile.ps1`的文件进行`写入`操作
- 对路径为`*\Documents\profile.ps1`的文件进行`写入`操作
  
***rule.json hash: 1768d205c6d4a0c6794d1933f20f5b43f306159d13c799fb8b7360c91372757a***