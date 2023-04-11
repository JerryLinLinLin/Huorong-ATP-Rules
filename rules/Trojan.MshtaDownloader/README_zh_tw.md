


  
[简体中文](README.md) | 繁體中文 | [English](README_en_us.md)  
  

目錄
==

* [Trojan.MshtaDownloader](#trojanmshtadownloader)
	* [Trojan.MshtaDownloader.A](#trojanmshtadownloadera)

# Trojan.MshtaDownloader

## Trojan.MshtaDownloader.A
  
狀態：啟用

行為描述：源程式`*\mshta.exe`做出以下操作時，提示使用者處理
- 對路徑為`*\Windows\Sys?????\*.exe`的程序進行`執行`操作
- 對路徑為`*.exe`的文件進行`建立`操作
- 對路徑為`*.dll`的文件進行`建立`操作
- 對路徑為`*\Users\*\AppData\*`的程序進行`執行`操作
  
***rule.json hash: 9af5a10aba8688c0759a59db43479ddd32558715cf3b6905531d9ef484e924a7***