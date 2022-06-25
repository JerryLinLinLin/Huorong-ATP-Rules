



目录
==

* [Suspicious.SuspProcAddAutoRun 规则组](#suspicioussuspprocaddautorun-)
	* [规则：Suspicious.SuspProcAddAutoRun.A](#suspicioussuspprocaddautoruna)

# Suspicious.SuspProcAddAutoRun 规则组

## 规则：Suspicious.SuspProcAddAutoRun.A
  
状态：启用

源程序`*\Users\*\AppData\>\>\>`做出以下操作时，提示用户处理
- 对路径为`*\Software\Microsoft\Windows\CurrentVersion\Run*`的注册表进行创建、写操作
- 对路径为`*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*`的文件进行创操作
  
***rule.json hash: 44c2865460b206ad160babc1a7db46f5150601c4b4f3ac30fadb8598e27ad1ad***