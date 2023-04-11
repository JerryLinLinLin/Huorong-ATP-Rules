


  
[简体中文](README.md) | 繁體中文 | [English](README_en_us.md)  
  

目錄
==

* [Suspicious.ScriptHost](#suspiciousscripthost)
	* [Suspicious.ScriptHost.A](#suspiciousscripthosta)
	* [Suspicious.ScriptHost.B](#suspiciousscripthostb)

# Suspicious.ScriptHost

## Suspicious.ScriptHost.A
  
狀態：啟用

行為描述：源程式`*\?script.exe`做出以下操作時，提示使用者處理
- 對路徑為`*\Windows\Sys?????\*.exe`的程序進行`執行`操作
- 對路徑為`*.exe`的文件進行`建立`操作
- 對路徑為`*.dll`的文件進行`建立`操作
- 對路徑為`*\Users\*\AppData\*`的程序進行`執行`操作

## Suspicious.ScriptHost.B
  
狀態：啟用

行為描述：源程式`*\Windows\Sys?????\*.exe`做出以下操作時，提示使用者處理
- 對路徑為`*\?script.exe`的程序進行`執行`操作
  
***rule.json hash: 7692734f67bdef45c360f5d4b04da6d64141543e16f47214a7b005f3094a3fe9***