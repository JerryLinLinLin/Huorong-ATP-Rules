



Contents
========

* [Trojan.Spy](#trojanspy)
	* [Trojan.Spy.A](#trojanspya)
* [Template](#template)
* [Ransom.CreateRansomNote](#ransomcreateransomnote)
	* [Ransom.CreateRansomNote.A](#ransomcreateransomnotea)
* [Trojan.StartupFolderMalDropper](#trojanstartupfoldermaldropper)
	* [Trojan.StartupFolderMalDropper.A](#trojanstartupfoldermaldroppera)
* [Suspicious.ScriptHost](#suspiciousscripthost)
	* [Suspicious.ScriptHost.A](#suspiciousscripthosta)
	* [Suspicious.ScriptHost.B](#suspiciousscripthostb)
* [Suspicious.SuspProcCallSysProc](#suspicioussuspproccallsysproc)
	* [Suspicious.SuspProcCallSysProc.A](#suspicioussuspproccallsysproca)
* [Trojan.FakeSysProc](#trojanfakesysproc)
	* [Trojan.FakeSysProc.A](#trojanfakesysproca)
* [Trojan.CmstpDownloader](#trojancmstpdownloader)
	* [Trojan.CmstpDownloader.A](#trojancmstpdownloadera)
* [Trojan.Remcos](#trojanremcos)
	* [Trojan.Remcos.A](#trojanremcosa)
* [Trojan.NetStealer](#trojannetstealer)
	* [Trojan.NetStealer.A](#trojannetstealera)
	* [Trojan.NetStealer.B](#trojannetstealerb)
* [Suspicious.SuspProcAddAutoRun](#suspicioussuspprocaddautorun)
	* [Suspicious.SuspProcAddAutoRun.A](#suspicioussuspprocaddautoruna)
* [Suspicious.RunFromSusPath](#suspiciousrunfromsuspath)
	* [Suspicious.RunFromSusPath.A](#suspiciousrunfromsuspatha)
	* [Suspicious.RunFromSusPath.B](#suspiciousrunfromsuspathb)
	* [Suspicious.RunFromSusPath.C](#suspiciousrunfromsuspathc)
	* [Suspicious.RunFromSusPath.D](#suspiciousrunfromsuspathd)
	* [Suspicious.RunFromSusPath.E](#suspiciousrunfromsuspathe)
* [Trojan.MshtaDownloader](#trojanmshtadownloader)
	* [Trojan.MshtaDownloader.A](#trojanmshtadownloadera)
* [Suspicious.SysProcAddAutoRun](#suspicioussysprocaddautorun)
	* [Suspicious.SysProcAddAutoRun.A](#suspicioussysprocaddautoruna)
* [Ransom.DoubleExt](#ransomdoubleext)
	* [Ransom.DoubleExt.A](#ransomdoubleexta)
	* [Ransom.DoubleExt.B](#ransomdoubleextb)
* [Exploit.MSOffice](#exploitmsoffice)
	* [Exploit.MSOffice.A](#exploitmsofficea)
	* [Exploit.MSOffice.B](#exploitmsofficeb)
	* [Exploit.MSOffice.C](#exploitmsofficec)
	* [Exploit.MSOffice.D](#exploitmsofficed)
	* [Exploit.MSOffice.E](#exploitmsofficee)
	* [Exploit.MSOffice.F](#exploitmsofficef)
	* [Exploit.MSOffice.G](#exploitmsofficeg)
	* [Exploit.MSOffice.H](#exploitmsofficeh)
* [Suspicious.PowerShell](#suspiciouspowershell)
	* [Suspicious.PowerShell.A](#suspiciouspowershella)
	* [Suspicious.PowerShell.B](#suspiciouspowershellb)
* [Suspicious.CommandPrompt](#suspiciouscommandprompt)
	* [Suspicious.CommandPrompt.A](#suspiciouscommandprompta)
* [Suspicious.ReadBrowserData](#suspiciousreadbrowserdata)
	* [Suspicious.ReadBrowserData.A](#suspiciousreadbrowserdataa)

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
# Template
  
***rule.json hash: 26c5a555c2ccb94877985ee87cda3a1f44578de3e71abb672b5b822639f95416***
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
# Trojan.StartupFolderMalDropper

## Trojan.StartupFolderMalDropper.A
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the file under the path `*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.js`
- `Create, Write` the file under the path `*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.vb?`
- `Create, Write` the file under the path `*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.exe`
  
***rule.json hash: abc72d6bff17530a9ffc16e62214150baea2002eb8d6ce764865666d600313b9***
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
# Suspicious.SuspProcCallSysProc

## Suspicious.SuspProcCallSysProc.A
  
Status: Enabled

Behavioral Description:   
When the source process`*\Users\*\AppData\>\>\>`initializes the following actions, HIPS module should let the user decide them.
- `Execute` the program under the path `*\Windows\Sys?????\*.exe`
  
***rule.json hash: e89457383d24e328b7690300d5f3bf253909e57adf4cce5d0069c637a708ad35***
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
# Trojan.CmstpDownloader

## Trojan.CmstpDownloader.A
  
Status: Enabled

Behavioral Description:   
When the source process`*\cmstp.exe`initializes the following actions, HIPS module should let the user decide them.
- `Create` the file under the path `*.exe`
- `Create` the file under the path `*.dll`
  
***rule.json hash: 7a61cc7f5c4d7b6726f51cfc9110e44425f219f4b2165f38c3c959691bce9627***
# Trojan.Remcos

## Trojan.Remcos.A
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*Remcos*`
  
***rule.json hash: 9356fc082479626e97c5c8a06fec3876eb7860531d87b548b6a0897598921edb***
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
# Suspicious.SuspProcAddAutoRun

## Suspicious.SuspProcAddAutoRun.A
  
Status: Enabled

Behavioral Description:   
When the source process`*\Users\*\AppData\>\>\>`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*\Software\Microsoft\Windows\CurrentVersion\Run*`
- `Create` the file under the path `*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*`
  
***rule.json hash: 4aa4a4bcd0c6ecdd91d95954e534c4cd844dcde11960cdfcafb4d6169b081ca2***
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
  
Status: Disabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should automatically block them.
- `Execute` the program under the path `*\ProgramData\>\>.exe`

## Suspicious.RunFromSusPath.D
  
Status: Enabled

Behavioral Description:   
When the source process`*\Windows\Sys?????\>`initializes the following actions, HIPS module should let the user decide them.
- `Execute` the program under the path `*\Users\*\AppData\Roaming\>\>.exe`

## Suspicious.RunFromSusPath.E
  
Status: Disabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should automatically block them.
- `Execute` the program under the path `*\Users\*\AppData\Roaming\>\>.exe`
  
***rule.json hash: 08f7e3dc7ada40ee0b6cce1ef341404eb3de0be6da37d852a0549a1c049944c2***
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
# Suspicious.SysProcAddAutoRun

## Suspicious.SysProcAddAutoRun.A
  
Status: Enabled

Behavioral Description:   
When the source process`*\Windows\*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*\Software\Microsoft\Windows\CurrentVersion\Run*`
- `Create` the file under the path `*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*`
  
***rule.json hash: b57855ef08d403a05d0d219b948fd32048c5f38ff07da0155ac2719ed510c2e9***
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
  
***rule.json hash: b8719134d7772aa185965fa0b3f36db165a1ce1c5dd8533e41bbfe674f5f3437***
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
# Suspicious.ReadBrowserData

## Suspicious.ReadBrowserData.A
  
Status: Disabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should automatically block them.
- `Read` the file under the path `*\Users\*\AppData\Local\*\User Data\Default\*`
- `Read` the file under the path `*\Users\*\AppData\Roaming\Mozilla\Firefox\Profiles\*`
  
***rule.json hash: d13b8a311d712501d84b1645052ed84e506624c200a1f8a05ae649e07d258e76***