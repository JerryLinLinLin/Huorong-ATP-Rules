


  
[简体中文](README.md) | 繁體中文 | [English](README_en_us.md)  
  

目錄
==

* [Suspicious.PowerShell](#suspiciouspowershell)
	* [Suspicious.PowerShell.A](#suspiciouspowershella)
	* [Suspicious.PowerShell.B](#suspiciouspowershellb)
	* [Suspicious.PowerShell.C](#suspiciouspowershellc)

# Suspicious.PowerShell

## Suspicious.PowerShell.A
  
狀態：啟用

行為描述：源程式`*\Windows\Sys?????\*.exe`做出以下操作時，提示使用者處理
- 對路徑為`*\powershell.exe`的程序進行`执行`操作

## Suspicious.PowerShell.B
  
狀態：啟用

行為描述：源程式`*\powershell.exe`做出以下操作時，提示使用者處理
- 對路徑為`*\Users\*\AppData\*`的程序進行`执行`操作

## Suspicious.PowerShell.C
  
狀態：啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*\WindowsPowerShell\v1.0\profile.ps1`的文件進行`写入`操作
- 對路徑為`*\WindowsPowerShell\v1.0\Microsoft.PowerShell*profile.ps1`的文件進行`写入`操作
- 對路徑為`*\Documents\profile.ps1`的文件進行`写入`操作
  
***rule.json hash: 1768d205c6d4a0c6794d1933f20f5b43f306159d13c799fb8b7360c91372757a***