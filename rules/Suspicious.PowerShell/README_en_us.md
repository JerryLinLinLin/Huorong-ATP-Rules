



Contents
========

* [Suspicious.PowerShell](#suspiciouspowershell)
	* [Suspicious.PowerShell.A](#suspiciouspowershella)
	* [Suspicious.PowerShell.B](#suspiciouspowershellb)

# Suspicious.PowerShell

## Suspicious.PowerShell.A
  
Status: Disabled  
Behavioral Description: 

When the source process`*\Windows\Sys?????\*.exe`initializes the following actions, HIPS module should automatically block them.
- `Execute` the program under the path `*\powershell.exe`

## Suspicious.PowerShell.B
  
Status: Enabled  
Behavioral Description: 

When the source process`*\powershell.exe`initializes the following actions, HIPS module should let the user decide them.
- `Create` the registry under the path `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\*`
- `Create` the file under the path `*.exe`
- `Execute` the program under the path `*\Users\*\AppData\*`
  
***rule.json hash: a07c32503aed526ce12772851f805a467b3155bdb1cc30e7e84fe2d9fdbdaa4b***