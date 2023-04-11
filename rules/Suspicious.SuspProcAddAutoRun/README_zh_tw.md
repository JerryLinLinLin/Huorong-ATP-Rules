


  
[简体中文](README.md) | 繁體中文 | [English](README_en_us.md)  
  

目錄
==

* [Suspicious.SuspProcAddAutoRun](#suspicioussuspprocaddautorun)
	* [Suspicious.SuspProcAddAutoRun.A](#suspicioussuspprocaddautoruna)

# Suspicious.SuspProcAddAutoRun

## Suspicious.SuspProcAddAutoRun.A
  
狀態：啟用

行為描述：源程式`*\Users\*\AppData\>\>\>`做出以下操作時，提示使用者處理
- 對路徑為`*\Software\Microsoft\Windows\CurrentVersion\Run*`的注册表進行`创建、写入`操作
- 對路徑為`*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*`的文件進行`创建`操作
  
***rule.json hash: 44c2865460b206ad160babc1a7db46f5150601c4b4f3ac30fadb8598e27ad1ad***