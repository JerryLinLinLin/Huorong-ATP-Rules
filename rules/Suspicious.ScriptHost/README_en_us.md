



Contents
========

* [Suspicious.ScriptHost](#suspiciousscripthost)
	* [Suspicious.ScriptHost.A](#suspiciousscripthosta)
	* [Suspicious.ScriptHost.B](#suspiciousscripthostb)

# Suspicious.ScriptHost

## Suspicious.ScriptHost.A
  
Status: Enabled

Behavioral Description:   
When the source process`*\?script.exe`initializes the following actions, HIPS module should let the user decide them.
- `Execute` the program under the path `*\Windows\Sys?????\*.exe`
- `Create` the file under the path `*.exe`
- `Create` the file under the path `*.dll`
- `Execute` the program under the path `*\Users\*\AppData\*`

## Suspicious.ScriptHost.B
  
Status: Enabled

Behavioral Description:   
When the source process`*\Windows\Sys?????\*.exe`initializes the following actions, HIPS module should let the user decide them.
- `Execute` the program under the path `*\?script.exe`
  
***rule.json hash: 7692734f67bdef45c360f5d4b04da6d64141543e16f47214a7b005f3094a3fe9***