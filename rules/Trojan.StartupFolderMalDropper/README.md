


  
简体中文 | [繁體中文](README_zh_tw.md) | [English](README_en_us.md)  
  

目录
==

* [Trojan.StartupFolderMalDropper](#trojanstartupfoldermaldropper)
	* [Trojan.StartupFolderMalDropper.A](#trojanstartupfoldermaldroppera)

# Trojan.StartupFolderMalDropper

## Trojan.StartupFolderMalDropper.A
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.j>`的文件进行`创建、写入`操作
- 对路径为`*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.vb?`的文件进行`创建、写入`操作
- 对路径为`*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.exe`的文件进行`创建、写入`操作
  
***rule.json hash: 08785f08a7b5db2ca1868486ad734c2bad1e7158a9e5047480a1e397af621d0f***