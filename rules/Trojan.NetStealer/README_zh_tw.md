


  
[简体中文](README.md) | 繁體中文 | [English](README_en_us.md)  
  

目錄
==

* [Trojan.NetStealer](#trojannetstealer)
	* [Trojan.NetStealer.A](#trojannetstealera)
	* [Trojan.NetStealer.B](#trojannetstealerb)

# Trojan.NetStealer

## Trojan.NetStealer.A
  
狀態：啟用

行為描述：源程式`*\Windows\Microsoft.NET\Framework\>\>`做出以下操作時，提示使用者處理
- 對路徑為`*.txt`的文件進行`创建`操作
- 對路徑為`*\Users\*\AppData\Roaming\>\>.ini`的文件進行`创建`操作
- 對路徑為`*\Software\Microsoft\Windows\CurrentVersion\Run*`的注册表進行`创建、写入`操作
- 對路徑為`*\Users\*\AppData\Local\*\User Data\Default\*`的文件進行`读取`操作
- 對路徑為`*\Users\*\AppData\Roaming\Mozilla\Firefox\Profiles\*`的文件進行`读取`操作

## Trojan.NetStealer.B
  
狀態：啟用

行為描述：源程式`*\Windows\>`做出以下操作時，提示使用者處理
- 對路徑為`*\Users\*\AppData\Roaming\>\>.ini`的文件進行`创建`操作
  
***rule.json hash: 5454ed890ae1d2bf443eeabd5100e1df7a4fb650d290265e5879bb4eba62bbad***