


  
[简体中文](README.md) | 繁體中文 | [English](README_en_us.md)  
  

目錄
==

* [Trojan.Spy](#trojanspy)
	* [Trojan.Spy.A](#trojanspya)

# Trojan.Spy

## Trojan.Spy.A
  
狀態：啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*\ProgramData\*Cookie*.txt`的文件進行`建立`操作
- 對路徑為`*\Users\*\AppData\Local\Temp\*Cookie*txt`的文件進行`建立`操作
- 對路徑為`*\Users\*\AppData\Local\>\>\>Cookie>txt`的文件進行`建立`操作
- 對路徑為`*\Users\*\AppData\Local\>\>screen*png`的文件進行`建立`操作
- 對路徑為`*\Users\*\AppData\Local\Temp\*cookie*txt`的文件進行`讀取`操作
- 對路徑為`*\Users\*\AppData\Local\Temp\*passowrd*txt`的文件進行`讀取`操作
- 對路徑為`*\Users\*\AppData\Roaming\>\>.jpeg`的文件進行`建立`操作
  
***rule.json hash: 007f1ee31843571162c95ca83eb42cbc192ccdfe1268363c1a4cd4c96955b914***