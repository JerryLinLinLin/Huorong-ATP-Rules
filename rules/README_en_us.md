


  
[简体中文](README.md) | [繁體中文](README_zh_tw.md) | English  
  

Contents
========

* [Exploit.MSOffice](#exploitmsoffice)
	* [Exploit.MSOffice.A](#exploitmsofficea)
	* [Exploit.MSOffice.B](#exploitmsofficeb)
	* [Exploit.MSOffice.C](#exploitmsofficec)
	* [Exploit.MSOffice.D](#exploitmsofficed)
	* [Exploit.MSOffice.E](#exploitmsofficee)
	* [Exploit.MSOffice.F](#exploitmsofficef)
	* [Exploit.MSOffice.G](#exploitmsofficeg)
	* [Exploit.MSOffice.H](#exploitmsofficeh)
* [Ransom.CreateRansomNote](#ransomcreateransomnote)
	* [Ransom.CreateRansomNote.A](#ransomcreateransomnotea)
* [Ransom.DoubleExt](#ransomdoubleext)
	* [Ransom.DoubleExt.A](#ransomdoubleexta)
	* [Ransom.DoubleExt.B](#ransomdoubleextb)
* [Suspicious.AppCertDLLs](#suspiciousappcertdlls)
	* [Suspicious.AppCertDLLs.A](#suspiciousappcertdllsa)
* [Suspicious.AppInitDLLs](#suspiciousappinitdlls)
	* [Suspicious.AppInitDLLs.A](#suspiciousappinitdllsa)
* [Suspicious.CommandPrompt](#suspiciouscommandprompt)
	* [Suspicious.CommandPrompt.A](#suspiciouscommandprompta)
* [Suspicious.NetDebugger](#suspiciousnetdebugger)
	* [Suspicious.NetDebugger.A](#suspiciousnetdebuggera)
* [Suspicious.NetWinAppXRT](#suspiciousnetwinappxrt)
	* [Suspicious.NetWinAppXRT.A](#suspiciousnetwinappxrta)
* [Suspicious.PowerShell](#suspiciouspowershell)
	* [Suspicious.PowerShell.A](#suspiciouspowershella)
	* [Suspicious.PowerShell.B](#suspiciouspowershellb)
	* [Suspicious.PowerShell.C](#suspiciouspowershellc)
* [Suspicious.RunFromSusPath](#suspiciousrunfromsuspath)
	* [Suspicious.RunFromSusPath.A](#suspiciousrunfromsuspatha)
	* [Suspicious.RunFromSusPath.B](#suspiciousrunfromsuspathb)
	* [Suspicious.RunFromSusPath.C](#suspiciousrunfromsuspathc)
	* [Suspicious.RunFromSusPath.D](#suspiciousrunfromsuspathd)
* [Suspicious.ScriptHost](#suspiciousscripthost)
	* [Suspicious.ScriptHost.A](#suspiciousscripthosta)
	* [Suspicious.ScriptHost.B](#suspiciousscripthostb)
* [Suspicious.SuspProcAddAutoRun](#suspicioussuspprocaddautorun)
	* [Suspicious.SuspProcAddAutoRun.A](#suspicioussuspprocaddautoruna)
* [Suspicious.SuspProcCallSysProc](#suspicioussuspproccallsysproc)
	* [Suspicious.SuspProcCallSysProc.A](#suspicioussuspproccallsysproca)
* [Suspicious.SysProcAddAutoRun](#suspicioussysprocaddautorun)
	* [Suspicious.SysProcAddAutoRun.A](#suspicioussysprocaddautoruna)
* [Telemetry.ActiveSetup](#telemetryactivesetup)
	* [Telemetry.ActiveSetup.A](#telemetryactivesetupa)
* [Telemetry.CredentialProviders](#telemetrycredentialproviders)
	* [Telemetry.CredentialProviders.A](#telemetrycredentialprovidersa)
* [Telemetry.LSAConfig](#telemetrylsaconfig)
	* [Telemetry.LSAConfig.A](#telemetrylsaconfiga)
* [Telemetry.PowerShell](#telemetrypowershell)
	* [Telemetry.PowerShell.A](#telemetrypowershella)
	* [Telemetry.PowerShell.B](#telemetrypowershellb)
	* [Telemetry.PowerShell.C](#telemetrypowershellc)
* [Telemetry.ReadBrowserData](#telemetryreadbrowserdata)
	* [Telemetry.ReadBrowserData.A](#telemetryreadbrowserdataa)
* [Telemetry.RunFromSusPath](#telemetryrunfromsuspath)
	* [Telemetry.RunFromSusPath.A](#telemetryrunfromsuspatha)
* [Telemetry.TerminalServer](#telemetryterminalserver)
	* [Telemetry.TerminalServer.A](#telemetryterminalservera)
* [Template](#template)
* [Trojan.CmstpDownloader](#trojancmstpdownloader)
	* [Trojan.CmstpDownloader.A](#trojancmstpdownloadera)
* [Trojan.FakeSysProc](#trojanfakesysproc)
	* [Trojan.FakeSysProc.A](#trojanfakesysproca)
* [Trojan.MshtaDownloader](#trojanmshtadownloader)
	* [Trojan.MshtaDownloader.A](#trojanmshtadownloadera)
* [Trojan.Nanocore](#trojannanocore)
	* [Trojan.Nanocore.A](#trojannanocorea)
* [Trojan.NetStealer](#trojannetstealer)
	* [Trojan.NetStealer.A](#trojannetstealera)
	* [Trojan.NetStealer.B](#trojannetstealerb)
* [Trojan.Remcos](#trojanremcos)
	* [Trojan.Remcos.A](#trojanremcosa)
* [Trojan.Spy](#trojanspy)
	* [Trojan.Spy.A](#trojanspya)
* [Trojan.StartupFolderMalDropper](#trojanstartupfoldermaldropper)
	* [Trojan.StartupFolderMalDropper.A](#trojanstartupfoldermaldroppera)

# Exploit.MSOffice

## Exploit.MSOffice.A
  
Status: Enabled

Behavioral Description:   
When the source process`*\EXCEL.EXE`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the file under the path `*.exe`
- `Create, Write` the file under the path `*.scr`
- `Execute` the program under the path `*\Windows\Sys?????\*.exe`

## Exploit.MSOffice.B
  
Status: Enabled

Behavioral Description:   
When the source process`*\EXCEL.EXE`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*\Software\Microsoft\Windows\CurrentVersion\Run*`

## Exploit.MSOffice.C
  
Status: Enabled

Behavioral Description:   
When the source process`*\POWERPNT.EXE`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the file under the path `*.exe`
- `Create, Write` the file under the path `*.scr`
- `Execute` the program under the path `*\Windows\Sys?????\*.exe`

## Exploit.MSOffice.D
  
Status: Enabled

Behavioral Description:   
When the source process`*\POWERPNT.EXE`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*\Software\Microsoft\Windows\CurrentVersion\Run*`

## Exploit.MSOffice.E
  
Status: Enabled

Behavioral Description:   
When the source process`*\WINWORD.EXE`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the file under the path `*.exe`
- `Create, Write` the file under the path `*.scr`
- `Execute` the program under the path `*\Windows\Sys?????\*.exe`

## Exploit.MSOffice.F
  
Status: Enabled

Behavioral Description:   
When the source process`*\WINWORD.EXE`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*\Software\Microsoft\Windows\CurrentVersion\Run*`

## Exploit.MSOffice.G
  
Status: Enabled

Behavioral Description:   
When the source process`*\EQNEDT32.EXE`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the file under the path `*.exe`
- `Create, Write` the file under the path `*.scr`
- `Execute` the program under the path `*\Windows\Sys?????\*.exe`

## Exploit.MSOffice.H
  
Status: Enabled

Behavioral Description:   
When the source process`*\EQNEDT32.EXE`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*\Software\Microsoft\Windows\CurrentVersion\Run*`
  
***rule.json hash: 0b95bbddefa3f3c899c788551a690bee3417d706ccb99d71c30931b82532d141***
# Ransom.CreateRansomNote

## Ransom.CreateRansomNote.A
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create` the file under the path `>\ProgramData\>.txt`
- `Create` the file under the path `>\Program Files (x86)\>.txt`
- `Create` the file under the path `>\Users\*\AppData\Local\>.txt`
- `Create` the file under the path `>\Users\*\AppData\>.txt`
- `Create` the file under the path `>\Program Files\>.txt`
  
***rule.json hash: c2c8db5cd47d81f8a5f0d961cc8c86cd9bf327106b678a8370b38d6e50963444***
# Ransom.DoubleExt

## Ransom.DoubleExt.A
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create` the file under the path `*.docx.>`
- `Create` the file under the path `*.xlsx.>`
- `Create` the file under the path `*.pptx.>`
- `Create` the file under the path `*.doc.>`
- `Create` the file under the path `*.xls.>`
- `Create` the file under the path `*.ppt.>`

## Ransom.DoubleExt.B
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create` the file under the path `>\Users\>\Pictures\*.jpg.>`
- `Create` the file under the path `>\Users\>\Pictures\*.png.>`
- `Create` the file under the path `>\Users\>\Desktop\*.jpg.>`
- `Create` the file under the path `>\Users\>\Desktop\*.png.>`
  
***rule.json hash: e5f5fd0249fcb5415f8445a356cf9b8d1b081981b6bbe3ce8d4e7b3052fd799a***
# Suspicious.AppCertDLLs

## Suspicious.AppCertDLLs.A
  
Status: Disabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*\System\CurrentControlSet\Control\Session Manager\AppCertDLLs\*`
  
***rule.json hash: b7bddf3cc616ddeef545ba031f67f4e660eeee8f8baf211ed058c51d5b5ddb27***
# Suspicious.AppInitDLLs

## Suspicious.AppInitDLLs.A
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*\SOFTWARE*Microsoft\Windows NT\CurrentVersion\Windows\Appinit_Dll*`
  
***rule.json hash: cba6993d469ccd5b83618066036bce299790aea826ebde01cdbc16efb862d101***
# Suspicious.CommandPrompt

## Suspicious.CommandPrompt.A
  
Status: Enabled

Behavioral Description:   
When the source process`*\cmd.exe`initializes the following actions, HIPS module should let the user decide them.
- `Execute` the program under the path `*\?script.exe`
- `Create` the file under the path `*.exe`
- `Create` the file under the path `*.vb?`
- `Create` the file under the path `*.js`
  
***rule.json hash: e62bc0757952c536054b872cac6a0ab7773edb697cd0a32dc824ab4246d53190***
# Suspicious.NetDebugger

## Suspicious.NetDebugger.A
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*\SOFTWARE*Microsoft\.NETFramework\DbgManagedDebugge*`
  
***rule.json hash: 8dafeaa565c7c02bff7bc9dd9a27155f95ad5958d3259a576797ea797fafb0c8***
# Suspicious.NetWinAppXRT

## Suspicious.NetWinAppXRT.A
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the file under the path `*\WinAppXRT.dll`
  
***rule.json hash: 854d05545961e7d83d1f1d74614dae0589255c0542306eb3f4716647665ab8aa***
# Suspicious.PowerShell

## Suspicious.PowerShell.A
  
Status: Enabled

Behavioral Description:   
When the source process`*\Windows\Sys?????\*.exe`initializes the following actions, HIPS module should let the user decide them.
- `Execute` the program under the path `*\powershell.exe`

## Suspicious.PowerShell.B
  
Status: Enabled

Behavioral Description:   
When the source process`*\powershell.exe`initializes the following actions, HIPS module should let the user decide them.
- `Execute` the program under the path `*\Users\*\AppData\*`

## Suspicious.PowerShell.C
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Write` the file under the path `*\WindowsPowerShell\v1.0\profile.ps1`
- `Write` the file under the path `*\WindowsPowerShell\v1.0\Microsoft.PowerShell*profile.ps1`
- `Write` the file under the path `*\Documents\profile.ps1`
  
***rule.json hash: 1768d205c6d4a0c6794d1933f20f5b43f306159d13c799fb8b7360c91372757a***
# Suspicious.RunFromSusPath

## Suspicious.RunFromSusPath.A
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Execute` the program under the path `*\Users\*\AppData\Roaming\>`
- `Execute` the program under the path `*\Users\*\AppData\>`
- `Execute` the program under the path `*\Users\>\>`
- `Execute` the program under the path `*\ProgramData\>`
- `Execute` the program under the path `*\Program Files\>`
- `Execute` the program under the path `*\Program Files (x86)\>`
- `Execute` the program under the path `*\Users\*\AppData\Local\>`
- `Execute` the program under the path `*\Users\>\Documents\>`
- `Execute` the program under the path `*\Users\>\Documents\>\>`
- `Read` the file under the path `*\Users\Public\>.bat`

## Suspicious.RunFromSusPath.B
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Execute` the program under the path `*\Recycler\*`
- `Execute` the program under the path `*\$RECYCLE.BIN\*`
- `Execute` the program under the path `*\System Volume Information\*`

## Suspicious.RunFromSusPath.C
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Execute` the program under the path `*\ProgramData\>\>.exe`

## Suspicious.RunFromSusPath.D
  
Status: Enabled

Behavioral Description:   
When the source process`*\Windows\Sys?????\>`initializes the following actions, HIPS module should let the user decide them.
- `Execute` the program under the path `*\Users\*\AppData\Roaming\>\>.exe`
  
***rule.json hash: 365f46a07ea3328aabbec53fbbd02ca27418a21bd8c4b5ac36535f678d509940***
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
  
***rule.json hash: d2705aeab053e2c7a8fb7a2a57bd21c0378b71cce1c8b9403b89c3e7941abf12***
# Suspicious.SuspProcAddAutoRun

## Suspicious.SuspProcAddAutoRun.A
  
Status: Enabled

Behavioral Description:   
When the source process`*\Users\*\AppData\>\>\>`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*\Software\Microsoft\Windows\CurrentVersion\Run*`
- `Create` the file under the path `*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*`
  
***rule.json hash: 44c2865460b206ad160babc1a7db46f5150601c4b4f3ac30fadb8598e27ad1ad***
# Suspicious.SuspProcCallSysProc

## Suspicious.SuspProcCallSysProc.A
  
Status: Enabled

Behavioral Description:   
When the source process`*\Users\*\AppData\>\>\>`initializes the following actions, HIPS module should let the user decide them.
- `Execute` the program under the path `*\Windows\Sys?????\*.exe`
  
***rule.json hash: 8976ebf9e98afb7f6c1285c15f2a65f5a5a6bfe826f1818fda1b0929cf0a9a47***
# Suspicious.SysProcAddAutoRun

## Suspicious.SysProcAddAutoRun.A
  
Status: Enabled

Behavioral Description:   
When the source process`*\Windows\*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*\Software\Microsoft\Windows\CurrentVersion\Run*`
- `Create` the file under the path `*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*`
  
***rule.json hash: b616ca54c5a8095a7189004d17c0fce2bdc47ead11d3a7151d6658b00a431fcf***
# Telemetry.ActiveSetup

## Telemetry.ActiveSetup.A
  
Status: Disabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create` the registry under the path `*\SOFTWARE*Microsoft\Active Setup\Installed Components*`
  
***rule.json hash: 13861bde9ed981f5012cc0fbb6f4d28ac50163d296043697ccf800f8e1784ada***
# Telemetry.CredentialProviders

## Telemetry.CredentialProviders.A
  
Status: Disabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*\Software\Microsoft\Windows\CurrentVersion\Authentication\PLAP Provider*`
- `Create, Write` the registry under the path `*\Software\Microsoft\Windows\CurrentVersion\Authentication\Credential Provider*`
  
***rule.json hash: 238b5043dfaecb9d08883698d3b66cffc5214e8381f9460cfa191963efbfb628***
# Telemetry.LSAConfig

## Telemetry.LSAConfig.A
  
Status: Disabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*\Control\Lsa`
- `Create, Write` the registry under the path `*\Control\Lsa*`
  
***rule.json hash: 1e2d9f278a99ba6eba9d9c27f5ea5ab9a386228c74964f0290559a1256166d9d***
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
  
***rule.json hash: 29f6108776c83ada5ba0762361814e853353ce651363a49dbbd469df11219859***
# Telemetry.ReadBrowserData

## Telemetry.ReadBrowserData.A
  
Status: Disabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Read` the file under the path `*\Users\*\AppData\Local\*\User Data\Default\*`
- `Read` the file under the path `*\Users\*\AppData\Roaming\Mozilla\Firefox\Profiles\*`
  
***rule.json hash: 4d1a67a222e18c1250786e431e7c774fe73a254ee6de8d5e12b893eb310bd32b***
# Telemetry.RunFromSusPath

## Telemetry.RunFromSusPath.A
  
Status: Disabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Execute` the program under the path `*\Users\*\AppData\Roaming\>\>.exe`
  
***rule.json hash: 8b5b19e3835453960e36607f095ce6353fa52bd88044083277e2627f7174209a***
# Telemetry.TerminalServer

## Telemetry.TerminalServer.A
  
Status: Disabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Write` the registry under the path `*\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp\InitialProgram`
  
***rule.json hash: b8410efc74805550bfd35e4030951b048c8cc9d8af0698e999d36cfe5425d2a4***
# Template
  
***rule.json hash: e499200d7c7647a852931381fcdc2a5b0dd532c593f4a44e58417f77f8f0b617***
# Trojan.CmstpDownloader

## Trojan.CmstpDownloader.A
  
Status: Enabled

Behavioral Description:   
When the source process`*\cmstp.exe`initializes the following actions, HIPS module should let the user decide them.
- `Create` the file under the path `*.exe`
- `Create` the file under the path `*.dll`
  
***rule.json hash: 11ed30aa824e9ec8efb789c6cf1b0bc5d30030f3732b5b11e6663bb8ee92bf42***
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
  
***rule.json hash: 5d9ecb177de9dbf727527545e505b234f0b67bd84ba9626eccbfb5e5167e7a0a***
# Trojan.MshtaDownloader

## Trojan.MshtaDownloader.A
  
Status: Enabled

Behavioral Description:   
When the source process`*\mshta.exe`initializes the following actions, HIPS module should let the user decide them.
- `Execute` the program under the path `*\Windows\Sys?????\*.exe`
- `Create` the file under the path `*.exe`
- `Create` the file under the path `*.dll`
- `Execute` the program under the path `*\Users\*\AppData\*`
  
***rule.json hash: 892d5b0994e53705cef82d97b0724d4c867cd9b36181fdb896a680319342e388***
# Trojan.Nanocore

## Trojan.Nanocore.A
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create` the file under the path `*\Users\*\AppData\Roaming\>\run.dat`
  
***rule.json hash: 7b2e1d410b22e9086de4bfa8882b43796c60fbe5efb2bd8af010d7fafd0893ca***
# Trojan.NetStealer

## Trojan.NetStealer.A
  
Status: Enabled

Behavioral Description:   
When the source process`*\Windows\Microsoft.NET\Framework\>\>`initializes the following actions, HIPS module should let the user decide them.
- `Create` the file under the path `*.txt`
- `Create` the file under the path `*\Users\*\AppData\Roaming\>\>.ini`
- `Create, Write` the registry under the path `*\Software\Microsoft\Windows\CurrentVersion\Run*`
- `Read` the file under the path `*\Users\*\AppData\Local\*\User Data\Default\*`
- `Read` the file under the path `*\Users\*\AppData\Roaming\Mozilla\Firefox\Profiles\*`

## Trojan.NetStealer.B
  
Status: Enabled

Behavioral Description:   
When the source process`*\Windows\>`initializes the following actions, HIPS module should let the user decide them.
- `Create` the file under the path `*\Users\*\AppData\Roaming\>\>.ini`
  
***rule.json hash: 5454ed890ae1d2bf443eeabd5100e1df7a4fb650d290265e5879bb4eba62bbad***
# Trojan.Remcos

## Trojan.Remcos.A
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*Remcos*`
  
***rule.json hash: f0d47e95129efb91fd8909c6b9cf4dcedeb0105a461f646d1e1878f4413b59f2***
# Trojan.Spy

## Trojan.Spy.A
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create` the file under the path `*\ProgramData\*Cookie*.txt`
- `Create` the file under the path `*\Users\*\AppData\Local\Temp\*Cookie*txt`
- `Create` the file under the path `*\Users\*\AppData\Local\>\>\>Cookie>txt`
- `Create` the file under the path `*\Users\*\AppData\Local\>\>screen*png`
- `Read` the file under the path `*\Users\*\AppData\Local\Temp\*cookie*txt`
- `Read` the file under the path `*\Users\*\AppData\Local\Temp\*passowrd*txt`
- `Create` the file under the path `*\Users\*\AppData\Roaming\>\>.jpeg`
  
***rule.json hash: 710be4af7b3f126da4f46688eb30715dc581c9cb4416124b73b0475acb7feb83***
# Trojan.StartupFolderMalDropper

## Trojan.StartupFolderMalDropper.A
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the file under the path `*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.j>`
- `Create, Write` the file under the path `*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.vb?`
- `Create, Write` the file under the path `*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.exe`
  
***rule.json hash: 08785f08a7b5db2ca1868486ad734c2bad1e7158a9e5047480a1e397af621d0f***