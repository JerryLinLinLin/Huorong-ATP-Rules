



Contents
========

* [Suspicious.ScriptHost](#suspiciousscripthost)
	* [Suspicious.ScriptHost.A](#suspiciousscripthosta)
	* [Suspicious.ScriptHost.B](#suspiciousscripthostb)

# Suspicious.ScriptHost

## Suspicious.ScriptHost.A
  
Status: Enabled

Behavioral Description: When the source process`*\?script.exe`initializes the following actions, HIPS module should let the user decide.
- `Execute` the program under the path `*\Windows\Sys?????\*.exe`
- `Create` the file under the path `*.exe`
- `Create` the file under the path `*.dll`
- `Execute` the program under the path `*\Users\*\AppData\*`

## Suspicious.ScriptHost.B
  
Status: Enabled

Behavioral Description: When the source process`*\Windows\Sys?????\*.exe`initializes the following actions, HIPS module should let the user decide.
- `Execute` the program under the path `*\?script.exe`
  
***rule.json hash: d2705aeab053e2c7a8fb7a2a57bd21c0378b71cce1c8b9403b89c3e7941abf12***