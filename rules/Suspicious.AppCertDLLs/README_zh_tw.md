


  
[简体中文](README.md) | 繁體中文 | [English](README_en_us.md)  
  

目錄
==

* [Suspicious.AppCertDLLs](#suspiciousappcertdlls)
	* [Suspicious.AppCertDLLs.A](#suspiciousappcertdllsa)

# Suspicious.AppCertDLLs

## Suspicious.AppCertDLLs.A
  
狀態：未啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*\System\CurrentControlSet\Control\Session Manager\AppCertDLLs\*`的注册表進行`建立、寫入`操作
  
***rule.json hash: dfdff9349d60a3a7d57355d0e0a7e20b7da9997568cf228a647f1a94f2db6ec0***