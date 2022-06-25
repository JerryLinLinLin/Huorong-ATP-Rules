



目录
==

* [Trojan.MshtaDownloader 规则组](#trojanmshtadownloader-)
	* [规则：Trojan.MshtaDownloader.A](#trojanmshtadownloadera)

# Trojan.MshtaDownloader 规则组

## 规则：Trojan.MshtaDownloader.A
  
状态：启用

源程序`*\mshta.exe`做出以下操作时，提示用户处理
- 对路径为`*\Windows\Sys?????\*.exe`的程序进行执行操作
- 对路径为`*.exe`的文件进行创建操作
- 对路径为`*.dll`的文件进行创建操作
- 对路径为`*\Users\*\AppData\*`的程序进行执行操作
  
***rule.json hash: 892d5b0994e53705cef82d97b0724d4c867cd9b36181fdb896a680319342e388***