



目录
==

* [Suspicious.SysProcAddAutoRun 规则组](#suspicioussysprocaddautorun-)
	* [规则：Suspicious.SysProcAddAutoRun.A](#suspicioussysprocaddautoruna)

# Suspicious.SysProcAddAutoRun 规则组

## 规则：Suspicious.SysProcAddAutoRun.A
  
状态：启用

源程序`*\Windows\*`做出以下操作时，提示用户处理
- 对路径为`*\Software\Microsoft\Windows\CurrentVersion\Run*`的注册表进行创建、写操作
- 对路径为`*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*`的文件进行创操作
  
***rule.json hash: b616ca54c5a8095a7189004d17c0fce2bdc47ead11d3a7151d6658b00a431fcf***