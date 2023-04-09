


  
简体中文 | [English](README_en_us.md)  
  

目录
==

* [Suspicious.SuspProcAddAutoRun](#suspicioussuspprocaddautorun)
	* [Suspicious.SuspProcAddAutoRun.A](#suspicioussuspprocaddautoruna)

# Suspicious.SuspProcAddAutoRun

## Suspicious.SuspProcAddAutoRun.A
  
状态：启用

行为描述：源程序`*\Users\*\AppData\>\>\>`做出以下操作时，提示用户处理
- 对路径为`*\Software\Microsoft\Windows\CurrentVersion\Run*`的注册表进行**创建、写入**操作
- 对路径为`*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*`的文件进行**创建**操作
  
***rule.json hash: 4aa4a4bcd0c6ecdd91d95954e534c4cd844dcde11960cdfcafb4d6169b081ca2***