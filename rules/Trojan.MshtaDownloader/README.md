


  
简体中文 | [繁體中文](README_zh_tw.md) | [English](README_en_us.md)  
  

目录
==

* [Trojan.MshtaDownloader](#trojanmshtadownloader)
	* [Trojan.MshtaDownloader.A](#trojanmshtadownloadera)

# Trojan.MshtaDownloader

## Trojan.MshtaDownloader.A
  
状态：启用

行为描述：源程序`*\mshta.exe`做出以下操作时，提示用户处理
- 对路径为`*\Windows\Sys?????\*.exe`的程序进行`执行`操作
- 对路径为`*.exe`的文件进行`创建`操作
- 对路径为`*.dll`的文件进行`创建`操作
- 对路径为`*\Users\*\AppData\*`的程序进行`执行`操作
  
***rule.json hash: 892d5b0994e53705cef82d97b0724d4c867cd9b36181fdb896a680319342e388***