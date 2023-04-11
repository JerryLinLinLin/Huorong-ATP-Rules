


  
[简体中文](README.md) | [繁體中文](README_zh_tw.md) | English  
  

Contents
========

* [Suspicious.PowerShell](#suspiciouspowershell)
	* [Suspicious.PowerShell.A](#suspiciouspowershella)
	* [Suspicious.PowerShell.B](#suspiciouspowershellb)
	* [Suspicious.PowerShell.C](#suspiciouspowershellc)

# Suspicious.PowerShell

## Suspicious.PowerShell.A
  
Status: Enabled

Behavioral Description:   
When the source process`*\Windows\Sys?????\*.exe`initializes the following actions, HIPS module should let the user decide them.
- `Execute` the program under the path `*\powershell.exe`

## Suspicious.PowerShell.B
  
Status: Enabled

Behavioral Description:   
When the source process`*\powershell.exe`initializes the following actions, HIPS module should let the user decide them.
- `Execute` the program under the path `*\Users\*\AppData\*`

## Suspicious.PowerShell.C
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Write` the file under the path `*\WindowsPowerShell\v1.0\profile.ps1`
- `Write` the file under the path `*\WindowsPowerShell\v1.0\Microsoft.PowerShell*profile.ps1`
- `Write` the file under the path `*\Documents\profile.ps1`
  
***rule.json hash: 1768d205c6d4a0c6794d1933f20f5b43f306159d13c799fb8b7360c91372757a***