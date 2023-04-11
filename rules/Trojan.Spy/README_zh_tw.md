


  
[简体中文](README.md) | 繁體中文 | [English](README_en_us.md)  
  

目錄
==

* [Trojan.Spy](#trojanspy)
	* [Trojan.Spy.A](#trojanspya)

# Trojan.Spy

## Trojan.Spy.A
  
狀態：啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*\ProgramData\*Cookie*.txt`的文件進行`创建`操作
- 對路徑為`*\Users\*\AppData\Local\Temp\*Cookie*txt`的文件進行`创建`操作
- 對路徑為`*\Users\*\AppData\Local\>\>\>Cookie>txt`的文件進行`创建`操作
- 對路徑為`*\Users\*\AppData\Local\>\>screen*png`的文件進行`创建`操作
- 對路徑為`*\Users\*\AppData\Local\Temp\*cookie*txt`的文件進行`读取`操作
- 對路徑為`*\Users\*\AppData\Local\Temp\*passowrd*txt`的文件進行`读取`操作
- 對路徑為`*\Users\*\AppData\Roaming\>\>.jpeg`的文件進行`创建`操作
  
***rule.json hash: 710be4af7b3f126da4f46688eb30715dc581c9cb4416124b73b0475acb7feb83***