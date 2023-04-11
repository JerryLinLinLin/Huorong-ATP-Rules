


  
[简体中文](README.md) | 繁體中文 | [English](README_en_us.md)  
  

目錄
==

* [Suspicious.RunFromSusPath](#suspiciousrunfromsuspath)
	* [Suspicious.RunFromSusPath.A](#suspiciousrunfromsuspatha)
	* [Suspicious.RunFromSusPath.B](#suspiciousrunfromsuspathb)
	* [Suspicious.RunFromSusPath.C](#suspiciousrunfromsuspathc)
	* [Suspicious.RunFromSusPath.D](#suspiciousrunfromsuspathd)

# Suspicious.RunFromSusPath

## Suspicious.RunFromSusPath.A
  
狀態：啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*\Users\*\AppData\Roaming\>`的程序進行`執行`操作
- 對路徑為`*\Users\*\AppData\>`的程序進行`執行`操作
- 對路徑為`*\Users\>\>`的程序進行`執行`操作
- 對路徑為`*\ProgramData\>`的程序進行`執行`操作
- 對路徑為`*\Program Files\>`的程序進行`執行`操作
- 對路徑為`*\Program Files (x86)\>`的程序進行`執行`操作
- 對路徑為`*\Users\*\AppData\Local\>`的程序進行`執行`操作
- 對路徑為`*\Users\>\Documents\>`的程序進行`執行`操作
- 對路徑為`*\Users\>\Documents\>\>`的程序進行`執行`操作
- 對路徑為`*\Users\Public\>.bat`的文件進行`讀取`操作

## Suspicious.RunFromSusPath.B
  
狀態：啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*\Recycler\*`的程序進行`執行`操作
- 對路徑為`*\$RECYCLE.BIN\*`的程序進行`執行`操作
- 對路徑為`*\System Volume Information\*`的程序進行`執行`操作

## Suspicious.RunFromSusPath.C
  
狀態：啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*\ProgramData\>\>.exe`的程序進行`執行`操作

## Suspicious.RunFromSusPath.D
  
狀態：啟用

行為描述：源程式`*\Windows\Sys?????\>`做出以下操作時，提示使用者處理
- 對路徑為`*\Users\*\AppData\Roaming\>\>.exe`的程序進行`執行`操作
  
***rule.json hash: 0ce318e7bf946e22f9b9bc6bb13188f0e1fc43c42d10a7699f0d4a0c6af16cb7***