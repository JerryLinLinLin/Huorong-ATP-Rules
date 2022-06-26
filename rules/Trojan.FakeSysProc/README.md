



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
  
***rule.json hash: 5d9ecb177de9dbf727527545e505b234f0b67bd84ba9626eccbfb5e5167e7a0a***