


  
[简体中文](README.md) | 繁體中文 | [English](README_en_us.md)  
  

目錄
==

* [Trojan.StartupFolderMalDropper](#trojanstartupfoldermaldropper)
	* [Trojan.StartupFolderMalDropper.A](#trojanstartupfoldermaldroppera)

# Trojan.StartupFolderMalDropper

## Trojan.StartupFolderMalDropper.A
  
狀態：啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.j>`的文件進行`创建、写入`操作
- 對路徑為`*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.vb?`的文件進行`创建、写入`操作
- 對路徑為`*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.exe`的文件進行`创建、写入`操作
  
***rule.json hash: 08785f08a7b5db2ca1868486ad734c2bad1e7158a9e5047480a1e397af621d0f***