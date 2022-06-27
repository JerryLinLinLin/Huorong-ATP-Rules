



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
* [Suspicious.CommandPrompt](#suspiciouscommandprompt)
	* [Suspicious.CommandPrompt.A](#suspiciouscommandprompta)
* [Suspicious.PowerShell](#suspiciouspowershell)
	* [Suspicious.PowerShell.A](#suspiciouspowershella)
	* [Suspicious.PowerShell.B](#suspiciouspowershellb)
* [Suspicious.ReadBrowserData](#suspiciousreadbrowserdata)
	* [Suspicious.ReadBrowserData.A](#suspiciousreadbrowserdataa)
* [Suspicious.RunFromSusPath](#suspiciousrunfromsuspath)
	* [Suspicious.RunFromSusPath.A](#suspiciousrunfromsuspatha)
	* [Suspicious.RunFromSusPath.B](#suspiciousrunfromsuspathb)
	* [Suspicious.RunFromSusPath.C](#suspiciousrunfromsuspathc)
	* [Suspicious.RunFromSusPath.D](#suspiciousrunfromsuspathd)
	* [Suspicious.RunFromSusPath.E](#suspiciousrunfromsuspathe)
* [Suspicious.ScriptHost](#suspiciousscripthost)
	* [Suspicious.ScriptHost.A](#suspiciousscripthosta)
	* [Suspicious.ScriptHost.B](#suspiciousscripthostb)
* [Suspicious.SuspProcAddAutoRun](#suspicioussuspprocaddautorun)
	* [Suspicious.SuspProcAddAutoRun.A](#suspicioussuspprocaddautoruna)
* [Suspicious.SuspProcCallSysProc](#suspicioussuspproccallsysproc)
	* [Suspicious.SuspProcCallSysProc.A](#suspicioussuspproccallsysproca)
* [Suspicious.SysProcAddAutoRun](#suspicioussysprocaddautorun)
	* [Suspicious.SysProcAddAutoRun.A](#suspicioussysprocaddautoruna)
* [Template](#template)
* [Trojan.CmstpDownloader](#trojancmstpdownloader)
	* [Trojan.CmstpDownloader.A](#trojancmstpdownloadera)
* [Trojan.FakeSysProc](#trojanfakesysproc)
	* [Trojan.FakeSysProc.A](#trojanfakesysproca)
* [Trojan.MshtaDownloader](#trojanmshtadownloader)
	* [Trojan.MshtaDownloader.A](#trojanmshtadownloadera)
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

Behavioral Description: When the source process`*\EXCEL.EXE`initializes the following actions, HIPS module should let the user decide.
- `Create, Write` the file under the path `*.exe`
- `Create, Write` the file under the path `*.scr`
- `Execute` the program under the path `*\Windows\Sys?????\*.exe`

## Exploit.MSOffice.B
  
Status: Enabled

Behavioral Description: When the source process`*\EXCEL.EXE`initializes the following actions, HIPS module should let the user decide.
- `Create, Write` the registry under the path `*\Software\Microsoft\Windows\CurrentVersion\Run*`

## Exploit.MSOffice.C
  
Status: Enabled

Behavioral Description: When the source process`*\POWERPNT.EXE`initializes the following actions, HIPS module should let the user decide.
- `Create, Write` the file under the path `*.exe`
- `Create, Write` the file under the path `*.scr`
- `Execute` the program under the path `*\Windows\Sys?????\*.exe`

## Exploit.MSOffice.D
  
Status: Enabled

Behavioral Description: When the source process`*\POWERPNT.EXE`initializes the following actions, HIPS module should let the user decide.
- `Create, Write` the registry under the path `*\Software\Microsoft\Windows\CurrentVersion\Run*`

## Exploit.MSOffice.E
  
Status: Enabled

Behavioral Description: When the source process`*\WINWORD.EXE`initializes the following actions, HIPS module should let the user decide.
- `Create, Write` the file under the path `*.exe`
- `Create, Write` the file under the path `*.scr`
- `Execute` the program under the path `*\Windows\Sys?????\*.exe`

## Exploit.MSOffice.F
  
Status: Enabled

Behavioral Description: When the source process`*\WINWORD.EXE`initializes the following actions, HIPS module should let the user decide.
- `Create, Write` the registry under the path `*\Software\Microsoft\Windows\CurrentVersion\Run*`

## Exploit.MSOffice.G
  
Status: Enabled

Behavioral Description: When the source process`*\EQNEDT32.EXE`initializes the following actions, HIPS module should let the user decide.
- `Create, Write` the file under the path `*.exe`
- `Create, Write` the file under the path `*.scr`
- `Execute` the program under the path `*\Windows\Sys?????\*.exe`

## Exploit.MSOffice.H
  
Status: Enabled

Behavioral Description: When the source process`*\EQNEDT32.EXE`initializes the following actions, HIPS module should let the user decide.
- `Create, Write` the registry under the path `*\Software\Microsoft\Windows\CurrentVersion\Run*`
  
***rule.json hash: 0b95bbddefa3f3c899c788551a690bee3417d706ccb99d71c30931b82532d141***
# Ransom.CreateRansomNote

## Ransom.CreateRansomNote.A
  
Status: Enabled

Behavioral Description: When the source process`*`initializes the following actions, HIPS module should let the user decide.
- `Create` the file under the path `>\ProgramData\>.txt`
- `Create` the file under the path `>\Program Files (x86)\>.txt`
- `Create` the file under the path `>\Users\*\AppData\Local\>.txt`
- `Create` the file under the path `>\Users\*\AppData\>.txt`
- `Create` the file under the path `>\Program Files\>.txt`
  
***rule.json hash: c2c8db5cd47d81f8a5f0d961cc8c86cd9bf327106b678a8370b38d6e50963444***
# Ransom.DoubleExt

## Ransom.DoubleExt.A
  
Status: Enabled

Behavioral Description: When the source process`*`initializes the following actions, HIPS module should let the user decide.
- `Create` the file under the path `*.docx.>`
- `Create` the file under the path `*.xlsx.>`
- `Create` the file under the path `*.pptx.>`
- `Create` the file under the path `*.doc.>`
- `Create` the file under the path `*.xls.>`
- `Create` the file under the path `*.ppt.>`

## Ransom.DoubleExt.B
  
Status: Enabled

Behavioral Description: When the source process`*`initializes the following actions, HIPS module should let the user decide.
- `Create` the file under the path `>\Users\>\Pictures\*.jpg.>`
- `Create` the file under the path `>\Users\>\Pictures\*.png.>`
- `Create` the file under the path `>\Users\>\Desktop\*.jpg.>`
- `Create` the file under the path `>\Users\>\Desktop\*.png.>`
  
***rule.json hash: e5f5fd0249fcb5415f8445a356cf9b8d1b081981b6bbe3ce8d4e7b3052fd799a***
# Suspicious.CommandPrompt

## Suspicious.CommandPrompt.A
  
Status: Enabled

Behavioral Description: When the source process`*\cmd.exe`initializes the following actions, HIPS module should let the user decide.
- `Execute` the program under the path `*\?script.exe`
- `Create` the file under the path `*.exe`
- `Create` the file under the path `*.vb?`
- `Create` the file under the path `*.js`
  
***rule.json hash: e62bc0757952c536054b872cac6a0ab7773edb697cd0a32dc824ab4246d53190***
# Suspicious.PowerShell

## Suspicious.PowerShell.A
  
Status: Disabled

Behavioral Description: When the source process`*\Windows\Sys?????\*.exe`initializes the following actions, HIPS module should automatically block.
- `Execute` the program under the path `*\powershell.exe`

## Suspicious.PowerShell.B
  
Status: Enabled

Behavioral Description: When the source process`*\powershell.exe`initializes the following actions, HIPS module should let the user decide.
- `Create` the registry under the path `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\*`
- `Create` the file under the path `*.exe`
- `Execute` the program under the path `*\Users\*\AppData\*`
  
***rule.json hash: a07c32503aed526ce12772851f805a467b3155bdb1cc30e7e84fe2d9fdbdaa4b***
# Suspicious.ReadBrowserData

## Suspicious.ReadBrowserData.A
  
Status: Disabled

Behavioral Description: When the source process`*`initializes the following actions, HIPS module should automatically block.
- `Read` the file under the path `*\Users\*\AppData\Local\*\User Data\Default\*`
- `Read` the file under the path `*\Users\*\AppData\Roaming\Mozilla\Firefox\Profiles\*`
  
***rule.json hash: f9af5aadaebe552fe3df866cf91edf2744eaea4da3fd2f29dba025b48996d057***
# Suspicious.RunFromSusPath

## Suspicious.RunFromSusPath.A
  
Status: Enabled

Behavioral Description: When the source process`*`initializes the following actions, HIPS module should let the user decide.
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

Behavioral Description: When the source process`*`initializes the following actions, HIPS module should let the user decide.
- `Execute` the program under the path `*\Recycler\*`
- `Execute` the program under the path `*\$RECYCLE.BIN\*`
- `Execute` the program under the path `*\System Volume Information\*`

## Suspicious.RunFromSusPath.C
  
Status: Disabled

Behavioral Description: When the source process`*`initializes the following actions, HIPS module should automatically block.
- `Execute` the program under the path `*\ProgramData\>\>.exe`

## Suspicious.RunFromSusPath.D
  
Status: Enabled

Behavioral Description: When the source process`*\Windows\Sys?????\>`initializes the following actions, HIPS module should let the user decide.
- `Execute` the program under the path `*\Users\*\AppData\Roaming\>\>.exe`

## Suspicious.RunFromSusPath.E
  
Status: Disabled

Behavioral Description: When the source process`*`initializes the following actions, HIPS module should automatically block.
- `Execute` the program under the path `*\Users\*\AppData\Roaming\>\>.exe`
  
***rule.json hash: 3997ac4b56fb80d81d036c3beabcb423cfd73598afa0d93b5861c6523f10ac81***
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
# Suspicious.SuspProcAddAutoRun

## Suspicious.SuspProcAddAutoRun.A
  
Status: Enabled

Behavioral Description: When the source process`*\Users\*\AppData\>\>\>`initializes the following actions, HIPS module should let the user decide.
- `Create, Write` the registry under the path `*\Software\Microsoft\Windows\CurrentVersion\Run*`
- `Create` the file under the path `*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*`
  
***rule.json hash: 44c2865460b206ad160babc1a7db46f5150601c4b4f3ac30fadb8598e27ad1ad***
# Suspicious.SuspProcCallSysProc

## Suspicious.SuspProcCallSysProc.A
  
Status: Enabled

Behavioral Description: When the source process`*\Users\*\AppData\>\>\>`initializes the following actions, HIPS module should let the user decide.
- `Execute` the program under the path `*\Windows\Sys?????\*.exe`
  
***rule.json hash: 8976ebf9e98afb7f6c1285c15f2a65f5a5a6bfe826f1818fda1b0929cf0a9a47***
# Suspicious.SysProcAddAutoRun

## Suspicious.SysProcAddAutoRun.A
  
Status: Enabled

Behavioral Description: When the source process`*\Windows\*`initializes the following actions, HIPS module should let the user decide.
- `Create, Write` the registry under the path `*\Software\Microsoft\Windows\CurrentVersion\Run*`
- `Create` the file under the path `*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*`
  
***rule.json hash: b616ca54c5a8095a7189004d17c0fce2bdc47ead11d3a7151d6658b00a431fcf***
# Template
  
***rule.json hash: e499200d7c7647a852931381fcdc2a5b0dd532c593f4a44e58417f77f8f0b617***
# Trojan.CmstpDownloader

## Trojan.CmstpDownloader.A
  
Status: Enabled

Behavioral Description: When the source process`*\cmstp.exe`initializes the following actions, HIPS module should let the user decide.
- `Create` the file under the path `*.exe`
- `Create` the file under the path `*.dll`
  
***rule.json hash: 11ed30aa824e9ec8efb789c6cf1b0bc5d30030f3732b5b11e6663bb8ee92bf42***
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
# Trojan.MshtaDownloader

## Trojan.MshtaDownloader.A
  
Status: Enabled

Behavioral Description: When the source process`*\mshta.exe`initializes the following actions, HIPS module should let the user decide.
- `Execute` the program under the path `*\Windows\Sys?????\*.exe`
- `Create` the file under the path `*.exe`
- `Create` the file under the path `*.dll`
- `Execute` the program under the path `*\Users\*\AppData\*`
  
***rule.json hash: 892d5b0994e53705cef82d97b0724d4c867cd9b36181fdb896a680319342e388***
# Trojan.NetStealer

## Trojan.NetStealer.A
  
Status: Enabled

Behavioral Description: When the source process`*\Windows\Microsoft.NET\Framework\>\>`initializes the following actions, HIPS module should let the user decide.
- `Create` the file under the path `*.txt`
- `Create` the file under the path `*\Users\*\AppData\Roaming\>\>.ini`
- `Create, Write` the registry under the path `*\Software\Microsoft\Windows\CurrentVersion\Run*`
- `Read` the file under the path `*\Users\*\AppData\Local\*\User Data\Default\*`
- `Read` the file under the path `*\Users\*\AppData\Roaming\Mozilla\Firefox\Profiles\*`

## Trojan.NetStealer.B
  
Status: Enabled

Behavioral Description: When the source process`*\Windows\>`initializes the following actions, HIPS module should let the user decide.
- `Create` the file under the path `*\Users\*\AppData\Roaming\>\>.ini`
  
***rule.json hash: 5454ed890ae1d2bf443eeabd5100e1df7a4fb650d290265e5879bb4eba62bbad***
# Trojan.Remcos

## Trojan.Remcos.A
  
Status: Enabled

Behavioral Description: When the source process`*`initializes the following actions, HIPS module should let the user decide.
- `Create, Write` the registry under the path `*Remcos*`
  
***rule.json hash: f0d47e95129efb91fd8909c6b9cf4dcedeb0105a461f646d1e1878f4413b59f2***
# Trojan.Spy

## Trojan.Spy.A
  
Status: Enabled

Behavioral Description: When the source process`*`initializes the following actions, HIPS module should let the user decide.
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

Behavioral Description: When the source process`*`initializes the following actions, HIPS module should let the user decide.
- `Create, Write` the file under the path `*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.js`
- `Create, Write` the file under the path `*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.vb?`
- `Create, Write` the file under the path `*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.exe`
  
***rule.json hash: 06703f7a24b2689c55038114daefd0625f1e163ee0cc847cdd74383fde1b78f7***