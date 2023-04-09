


  
简体中文 | [English](README_en_us.md)  
  

目录
==

* [Suspicious.SysProcAddAutoRun](#suspicioussysprocaddautorun)
	* [Suspicious.SysProcAddAutoRun.A](#suspicioussysprocaddautoruna)

# Suspicious.SysProcAddAutoRun

## Suspicious.SysProcAddAutoRun.A
  
状态：启用

行为描述：源程序`*\Windows\*`做出以下操作时，提示用户处理
- 对路径为`*\Software\Microsoft\Windows\CurrentVersion\Run*`的注册表进行`创建、写入`操作
- 对路径为`*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*`的文件进行`创建`操作
  
***rule.json hash: b57855ef08d403a05d0d219b948fd32048c5f38ff07da0155ac2719ed510c2e9***