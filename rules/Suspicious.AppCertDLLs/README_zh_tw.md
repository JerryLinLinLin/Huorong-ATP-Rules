


  
[简体中文](README.md) | 繁體中文 | [English](README_en_us.md)  
  

目錄
==

* [Suspicious.AppCertDLLs](#suspiciousappcertdlls)
	* [Suspicious.AppCertDLLs.A](#suspiciousappcertdllsa)

# Suspicious.AppCertDLLs

## Suspicious.AppCertDLLs.A
  
狀態：未啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*\System\CurrentControlSet\Control\Session Manager\AppCertDLLs\*`的注册表進行`创建、写入`操作
  
***rule.json hash: b7bddf3cc616ddeef545ba031f67f4e660eeee8f8baf211ed058c51d5b5ddb27***