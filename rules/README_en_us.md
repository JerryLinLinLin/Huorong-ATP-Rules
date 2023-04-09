



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
  
***rule.json hash: 11a6f7f126334cff29ddfdc485905a1c4ba3aec0f7f911e203980f34cb4ce62c***
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
  
***rule.json hash: 92dea9dc04af20406512baf6d17bf9ffc4c27911257403682db3b4bccd2b9bf3***
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
  
***rule.json hash: 8afaf4ee0e8ea6328dd7102d76abcd442db651f497c2208e1e9e54e72bad7c4c***
# Suspicious.AppCertDLLs

## Suspicious.AppCertDLLs.A
  
Status: Disabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*\System\CurrentControlSet\Control\Session Manager\AppCertDLLs\*`
  
***rule.json hash: dfdff9349d60a3a7d57355d0e0a7e20b7da9997568cf228a647f1a94f2db6ec0***
# Suspicious.AppInitDLLs

## Suspicious.AppInitDLLs.A
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*\SOFTWARE*Microsoft\Windows NT\CurrentVersion\Windows\Appinit_Dll*`
  
***rule.json hash: 6fd0e8a0cc1edb410eaf010023f9d27aa7c7ff487492f67a7f92ccdbed6e8391***
# Suspicious.CommandPrompt

## Suspicious.CommandPrompt.A
  
Status: Enabled

Behavioral Description:   
When the source process`*\cmd.exe`initializes the following actions, HIPS module should let the user decide them.
- `Execute` the program under the path `*\?script.exe`
- `Create` the file under the path `*.exe`
- `Create` the file under the path `*.vb?`
- `Create` the file under the path `*.js`
  
***rule.json hash: ac6da01e160cfb9848cec158ee41f935786a5413aadca2f4bb2c9ef66fcce2cd***
# Suspicious.NetDebugger

## Suspicious.NetDebugger.A
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*\SOFTWARE*Microsoft\.NETFramework\DbgManagedDebugge*`
  
***rule.json hash: 69a78ae8fed5bc9bcbb68eae9c549fcf9ac68e5aaeb26a2a0639866dbaf5d8d6***
# Suspicious.NetWinAppXRT

## Suspicious.NetWinAppXRT.A
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the file under the path `*\WinAppXRT.dll`
  
***rule.json hash: f4ad1d9a4fc9506d43c0e802b323c39414a8599d5241095efeba91abffb9d1ea***
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
  
***rule.json hash: 8407b3ae9312f1ebc1145986020e3ff3cd72543e98e6ded29b064a7ccf875ea8***
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
  
***rule.json hash: 0ce318e7bf946e22f9b9bc6bb13188f0e1fc43c42d10a7699f0d4a0c6af16cb7***
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
# Suspicious.SuspProcAddAutoRun

## Suspicious.SuspProcAddAutoRun.A
  
Status: Enabled

Behavioral Description:   
When the source process`*\Users\*\AppData\>\>\>`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*\Software\Microsoft\Windows\CurrentVersion\Run*`
- `Create` the file under the path `*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*`
  
***rule.json hash: 4aa4a4bcd0c6ecdd91d95954e534c4cd844dcde11960cdfcafb4d6169b081ca2***
# Suspicious.SuspProcCallSysProc

## Suspicious.SuspProcCallSysProc.A
  
Status: Enabled

Behavioral Description:   
When the source process`*\Users\*\AppData\>\>\>`initializes the following actions, HIPS module should let the user decide them.
- `Execute` the program under the path `*\Windows\Sys?????\*.exe`
  
***rule.json hash: e89457383d24e328b7690300d5f3bf253909e57adf4cce5d0069c637a708ad35***
# Suspicious.SysProcAddAutoRun

## Suspicious.SysProcAddAutoRun.A
  
Status: Enabled

Behavioral Description:   
When the source process`*\Windows\*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*\Software\Microsoft\Windows\CurrentVersion\Run*`
- `Create` the file under the path `*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*`
  
***rule.json hash: b57855ef08d403a05d0d219b948fd32048c5f38ff07da0155ac2719ed510c2e9***
# Telemetry.ActiveSetup

## Telemetry.ActiveSetup.A
  
Status: Disabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create` the registry under the path `*\SOFTWARE*Microsoft\Active Setup\Installed Components*`
  
***rule.json hash: 25f31e649b656ea0a57e2bcf47eb507ac362fd3b168aeeeed1cbf6dd0fbeaeb9***
# Telemetry.CredentialProviders

## Telemetry.CredentialProviders.A
  
Status: Disabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*\Software\Microsoft\Windows\CurrentVersion\Authentication\PLAP Provider*`
- `Create, Write` the registry under the path `*\Software\Microsoft\Windows\CurrentVersion\Authentication\Credential Provider*`
  
***rule.json hash: 495c7c42f579fcc2a45efdd8c22bcee72c3bd88964ebf0c1714c7c7c4c32062d***
# Telemetry.LSAConfig

## Telemetry.LSAConfig.A
  
Status: Disabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*\Control\Lsa`
- `Create, Write` the registry under the path `*\Control\Lsa*`
  
***rule.json hash: f94511a7d03f0b57a291761d410b84c4f5376efd0bb7fe56ba9e06d3ebe09bf7***
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
# Telemetry.ReadBrowserData

## Telemetry.ReadBrowserData.A
  
Status: Disabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Read` the file under the path `*\Users\*\AppData\Local\*\User Data\Default\*`
- `Read` the file under the path `*\Users\*\AppData\Roaming\Mozilla\Firefox\Profiles\*`
  
***rule.json hash: 04c8f6e13bbfc0027141f86bf678a2573bfd46326051c1753b2930bfdc2d1d7a***
# Telemetry.RunFromSusPath

## Telemetry.RunFromSusPath.A
  
Status: Disabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Execute` the program under the path `*\Users\*\AppData\Roaming\>\>.exe`
  
***rule.json hash: 8e649f1c95f70ea514564927537534ec4e4d61a9dc322d163fff85aab12fd612***
# Telemetry.TerminalServer

## Telemetry.TerminalServer.A
  
Status: Disabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Write` the registry under the path `*\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp\InitialProgram`
  
***rule.json hash: 1b245341cbd4dc6c3457fef43ee9ab8ffc96738ea578ed2bda9981f86819490e***
# Template
  
***rule.json hash: 26c5a555c2ccb94877985ee87cda3a1f44578de3e71abb672b5b822639f95416***
# Trojan.CmstpDownloader

## Trojan.CmstpDownloader.A
  
Status: Enabled

Behavioral Description:   
When the source process`*\cmstp.exe`initializes the following actions, HIPS module should let the user decide them.
- `Create` the file under the path `*.exe`
- `Create` the file under the path `*.dll`
  
***rule.json hash: 7a61cc7f5c4d7b6726f51cfc9110e44425f219f4b2165f38c3c959691bce9627***
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
# Trojan.MshtaDownloader

## Trojan.MshtaDownloader.A
  
Status: Enabled

Behavioral Description:   
When the source process`*\mshta.exe`initializes the following actions, HIPS module should let the user decide them.
- `Execute` the program under the path `*\Windows\Sys?????\*.exe`
- `Create` the file under the path `*.exe`
- `Create` the file under the path `*.dll`
- `Execute` the program under the path `*\Users\*\AppData\*`
  
***rule.json hash: 9af5a10aba8688c0759a59db43479ddd32558715cf3b6905531d9ef484e924a7***
# Trojan.Nanocore

## Trojan.Nanocore.A
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create` the file under the path `*\Users\*\AppData\Roaming\>\run.dat`
  
***rule.json hash: dfee1a531ec4660d2f369489bf185f6d24a448670867d2e1d2f62ff86d4aefd3***
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
  
***rule.json hash: a1dc27a7fe9ba237485ee9bff7e5d1a72d413649aaf9cd82a43b5819c1ff1468***
# Trojan.Remcos

## Trojan.Remcos.A
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*Remcos*`
  
***rule.json hash: 9356fc082479626e97c5c8a06fec3876eb7860531d87b548b6a0897598921edb***
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
  
***rule.json hash: 007f1ee31843571162c95ca83eb42cbc192ccdfe1268363c1a4cd4c96955b914***
# Trojan.StartupFolderMalDropper

## Trojan.StartupFolderMalDropper.A
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the file under the path `*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.j>`
- `Create, Write` the file under the path `*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.vb?`
- `Create, Write` the file under the path `*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.exe`
  
***rule.json hash: d5498c78b6062c8e4a7376af6eb2cd2e5455102de2d1a404c65b6c8493f72ea0***  
[简体中文](/README.md) | English