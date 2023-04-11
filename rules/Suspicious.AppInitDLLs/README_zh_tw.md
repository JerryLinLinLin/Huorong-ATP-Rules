


  
[简体中文](README.md) | 繁體中文 | [English](README_en_us.md)  
  

目錄
==

* [Suspicious.AppInitDLLs](#suspiciousappinitdlls)
	* [Suspicious.AppInitDLLs.A](#suspiciousappinitdllsa)

# Suspicious.AppInitDLLs

## Suspicious.AppInitDLLs.A
  
狀態：啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*\SOFTWARE*Microsoft\Windows NT\CurrentVersion\Windows\Appinit_Dll*`的注册表進行`建立、寫入`操作
  
***rule.json hash: 6fd0e8a0cc1edb410eaf010023f9d27aa7c7ff487492f67a7f92ccdbed6e8391***