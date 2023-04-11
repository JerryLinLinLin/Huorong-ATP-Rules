


  
简体中文 | [繁體中文](README_zh_tw.md) | [English](README_en_us.md)  
  

目录
==

* [Suspicious.AppCertDLLs](#suspiciousappcertdlls)
	* [Suspicious.AppCertDLLs.A](#suspiciousappcertdllsa)

# Suspicious.AppCertDLLs

## Suspicious.AppCertDLLs.A
  
状态：未启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\System\CurrentControlSet\Control\Session Manager\AppCertDLLs\*`的注册表进行`创建、写入`操作
  
***rule.json hash: b7bddf3cc616ddeef545ba031f67f4e660eeee8f8baf211ed058c51d5b5ddb27***