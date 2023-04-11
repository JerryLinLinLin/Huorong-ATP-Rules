


  
[简体中文](README.md) | 繁體中文 | [English](README_en_us.md)  
  

目錄
==

* [Trojan.FakeSysProc](#trojanfakesysproc)
	* [Trojan.FakeSysProc.A](#trojanfakesysproca)

# Trojan.FakeSysProc

## Trojan.FakeSysProc.A
  
狀態：啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*\svchost.exe`的程序進行`执行`操作
- 對路徑為`*\lsass.exe`的程序進行`执行`操作
- 對路徑為`*\services.exe`的程序進行`执行`操作
- 對路徑為`*\winlogon.exe`的程序進行`执行`操作
- 對路徑為`*\csrss.exe`的程序進行`执行`操作
- 對路徑為`*\smss.exe`的程序進行`执行`操作
  
***rule.json hash: 5d9ecb177de9dbf727527545e505b234f0b67bd84ba9626eccbfb5e5167e7a0a***