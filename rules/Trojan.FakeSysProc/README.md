


  
简体中文 | [English](README_en_us.md)  
  

目录
==

* [Trojan.FakeSysProc](#trojanfakesysproc)
	* [Trojan.FakeSysProc.A](#trojanfakesysproca)

# Trojan.FakeSysProc

## Trojan.FakeSysProc.A
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\svchost.exe`的程序进行**执行**操作
- 对路径为`*\lsass.exe`的程序进行**执行**操作
- 对路径为`*\services.exe`的程序进行**执行**操作
- 对路径为`*\winlogon.exe`的程序进行**执行**操作
- 对路径为`*\csrss.exe`的程序进行**执行**操作
- 对路径为`*\smss.exe`的程序进行**执行**操作
  
***rule.json hash: 050c9912a384d8858c1f745894d9172ff45ef8a04c03a3fa7b57f02c8a0634da***