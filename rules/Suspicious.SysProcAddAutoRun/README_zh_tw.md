


  
[简体中文](README.md) | 繁體中文 | [English](README_en_us.md)  
  

目錄
==

* [Suspicious.SysProcAddAutoRun](#suspicioussysprocaddautorun)
	* [Suspicious.SysProcAddAutoRun.A](#suspicioussysprocaddautoruna)

# Suspicious.SysProcAddAutoRun

## Suspicious.SysProcAddAutoRun.A
  
狀態：啟用

行為描述：源程式`*\Windows\*`做出以下操作時，提示使用者處理
- 對路徑為`*\Software\Microsoft\Windows\CurrentVersion\Run*`的注册表進行`创建、写入`操作
- 對路徑為`*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*`的文件進行`创建`操作
  
***rule.json hash: b616ca54c5a8095a7189004d17c0fce2bdc47ead11d3a7151d6658b00a431fcf***