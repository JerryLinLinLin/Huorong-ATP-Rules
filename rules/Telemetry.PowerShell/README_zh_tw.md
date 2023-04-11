


  
[简体中文](README.md) | 繁體中文 | [English](README_en_us.md)  
  

目錄
==

* [Telemetry.PowerShell](#telemetrypowershell)
	* [Telemetry.PowerShell.A](#telemetrypowershella)
	* [Telemetry.PowerShell.B](#telemetrypowershellb)
	* [Telemetry.PowerShell.C](#telemetrypowershellc)

# Telemetry.PowerShell

## Telemetry.PowerShell.A
  
狀態：未啟用

行為描述：源程式`*\powershell.exe`做出以下操作時，提示使用者處理
- 對路徑為`*.exe`的文件進行`创建`操作

## Telemetry.PowerShell.B
  
狀態：未啟用

行為描述：源程式`*\powershell.exe`做出以下操作時，提示使用者處理
- 對路徑為`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\*`的注册表進行`创建`操作

## Telemetry.PowerShell.C
  
狀態：未啟用

行為描述：源程式`*\powershell.exe`做出以下操作時，提示使用者處理
- 對路徑為`\SOFTWARE\Policies\Microsoft\Windows\PowerShell\ExecutionPolicy`的注册表進行`写入`操作
  
***rule.json hash: 29f6108776c83ada5ba0762361814e853353ce651363a49dbbd469df11219859***