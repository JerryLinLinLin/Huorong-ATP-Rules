



Contents
========

* [Trojan.FakeSysProc](#trojanfakesysproc)
	* [Trojan.FakeSysProc.A](#trojanfakesysproca)

# Trojan.FakeSysProc

## Trojan.FakeSysProc.A
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Execute` the program under the path `*\svchost.exe`
- `Execute` the program under the path `*\lsass.exe`
- `Execute` the program under the path `*\services.exe`
- `Execute` the program under the path `*\winlogon.exe`
- `Execute` the program under the path `*\csrss.exe`
- `Execute` the program under the path `*\smss.exe`
  
***rule.json hash: 050c9912a384d8858c1f745894d9172ff45ef8a04c03a3fa7b57f02c8a0634da***  
[简体中文](/README.md) | English