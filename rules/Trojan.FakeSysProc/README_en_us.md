



Contents
========

* [Trojan.FakeSysProc](#trojanfakesysproc)
	* [Trojan.FakeSysProc.A](#trojanfakesysproca)

# Trojan.FakeSysProc

## Trojan.FakeSysProc.A
  
Status: Enabled

Behavioral Description: When the source process`*`initializes the following actions, HIPS module should let the user decide.
- `Execute` the program under the path `*\svchost.exe`
- `Execute` the program under the path `*\lsass.exe`
- `Execute` the program under the path `*\services.exe`
- `Execute` the program under the path `*\winlogon.exe`
- `Execute` the program under the path `*\csrss.exe`
- `Execute` the program under the path `*\smss.exe`
  
***rule.json hash: 5d9ecb177de9dbf727527545e505b234f0b67bd84ba9626eccbfb5e5167e7a0a***