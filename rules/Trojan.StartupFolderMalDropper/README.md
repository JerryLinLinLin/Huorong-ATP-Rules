



目录
==

* [Trojan.StartupFolderMalDropper 规则组](#trojanstartupfoldermaldropper-)
	* [规则：Trojan.StartupFolderMalDropper.A](#trojanstartupfoldermaldroppera)

# Trojan.StartupFolderMalDropper 规则组

## 规则：Trojan.StartupFolderMalDropper.A
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.js`的文件进行创建、写入操作
- 对路径为`*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.vb?`的文件进行创建、写入操作
- 对路径为`*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.exe`的文件进行创建、写入操作
  
***rule.json hash: 06703f7a24b2689c55038114daefd0625f1e163ee0cc847cdd74383fde1b78f7***