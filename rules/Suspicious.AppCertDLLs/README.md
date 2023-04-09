


  
简体中文 | [English](README_en_us.md)  
  

目录
==

* [Suspicious.AppCertDLLs](#suspiciousappcertdlls)
	* [Suspicious.AppCertDLLs.A](#suspiciousappcertdllsa)

# Suspicious.AppCertDLLs

## Suspicious.AppCertDLLs.A
  
状态：未启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\System\CurrentControlSet\Control\Session Manager\AppCertDLLs\*`的注册表进行**创建、写入**操作
  
***rule.json hash: dfdff9349d60a3a7d57355d0e0a7e20b7da9997568cf228a647f1a94f2db6ec0***