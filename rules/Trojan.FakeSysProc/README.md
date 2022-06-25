



目录
==

* [Trojan.FakeSysProc 规则组](#trojanfakesysproc-)
	* [规则：Trojan.FakeSysProc.A](#trojanfakesysproca)

# Trojan.FakeSysProc 规则组

## 规则：Trojan.FakeSysProc.A
  
状态：未启用

行为描述：源程序`*`做出以下操作时，自动阻止
- 对路径为`*\svchost.exe`的程序进行执行操作
- 对路径为`*\lsass.exe`的程序进行执行操作
- 对路径为`*\services.exe`的程序进行执行操作
- 对路径为`*\winlogon.exe`的程序进行执行操作
- 对路径为`*\csrss.exe`的程序进行执行操作
- 对路径为`*\smss.exe`的程序进行执行操作
  
***rule.json hash: 11379f4626e28e779f0a4c030f0aecd2c7ba07b3eb000f11f8b2b5a1be13d6f5***