


  
[简体中文](README.md) | English  
  

Contents
========

* [Telemetry.PowerShell](#telemetrypowershell)
	* [Telemetry.PowerShell.A](#telemetrypowershella)
	* [Telemetry.PowerShell.B](#telemetrypowershellb)
	* [Telemetry.PowerShell.C](#telemetrypowershellc)

# Telemetry.PowerShell

## Telemetry.PowerShell.A
  
Status: Disabled

Behavioral Description:   
When the source process`*\powershell.exe`initializes the following actions, HIPS module should let the user decide them.
- `Create` the file under the path `*.exe`

## Telemetry.PowerShell.B
  
Status: Disabled

Behavioral Description:   
When the source process`*\powershell.exe`initializes the following actions, HIPS module should let the user decide them.
- `Create` the registry under the path `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\*`

## Telemetry.PowerShell.C
  
Status: Disabled

Behavioral Description:   
When the source process`*\powershell.exe`initializes the following actions, HIPS module should let the user decide them.
- `Write` the registry under the path `\SOFTWARE\Policies\Microsoft\Windows\PowerShell\ExecutionPolicy`
  
***rule.json hash: 6176d464860dad2aa05aac6d1bdd4d556618cc1fa09a68bc9aba16208d464613***