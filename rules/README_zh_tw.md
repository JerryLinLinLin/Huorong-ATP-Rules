


  
[简体中文](README.md) | 繁體中文 | [English](README_en_us.md)  
  

目錄
==

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
  
狀態：啟用

行為描述：源程式`*\EXCEL.EXE`做出以下操作時，提示使用者處理
- 對路徑為`*.exe`的文件進行`创建、写入`操作
- 對路徑為`*.scr`的文件進行`创建、写入`操作
- 對路徑為`*\Windows\Sys?????\*.exe`的程序進行`执行`操作

## Exploit.MSOffice.B
  
狀態：啟用

行為描述：源程式`*\EXCEL.EXE`做出以下操作時，提示使用者處理
- 對路徑為`*\Software\Microsoft\Windows\CurrentVersion\Run*`的注册表進行`创建、写入`操作

## Exploit.MSOffice.C
  
狀態：啟用

行為描述：源程式`*\POWERPNT.EXE`做出以下操作時，提示使用者處理
- 對路徑為`*.exe`的文件進行`创建、写入`操作
- 對路徑為`*.scr`的文件進行`创建、写入`操作
- 對路徑為`*\Windows\Sys?????\*.exe`的程序進行`执行`操作

## Exploit.MSOffice.D
  
狀態：啟用

行為描述：源程式`*\POWERPNT.EXE`做出以下操作時，提示使用者處理
- 對路徑為`*\Software\Microsoft\Windows\CurrentVersion\Run*`的注册表進行`创建、写入`操作

## Exploit.MSOffice.E
  
狀態：啟用

行為描述：源程式`*\WINWORD.EXE`做出以下操作時，提示使用者處理
- 對路徑為`*.exe`的文件進行`创建、写入`操作
- 對路徑為`*.scr`的文件進行`创建、写入`操作
- 對路徑為`*\Windows\Sys?????\*.exe`的程序進行`执行`操作

## Exploit.MSOffice.F
  
狀態：啟用

行為描述：源程式`*\WINWORD.EXE`做出以下操作時，提示使用者處理
- 對路徑為`*\Software\Microsoft\Windows\CurrentVersion\Run*`的注册表進行`创建、写入`操作

## Exploit.MSOffice.G
  
狀態：啟用

行為描述：源程式`*\EQNEDT32.EXE`做出以下操作時，提示使用者處理
- 對路徑為`*.exe`的文件進行`创建、写入`操作
- 對路徑為`*.scr`的文件進行`创建、写入`操作
- 對路徑為`*\Windows\Sys?????\*.exe`的程序進行`执行`操作

## Exploit.MSOffice.H
  
狀態：啟用

行為描述：源程式`*\EQNEDT32.EXE`做出以下操作時，提示使用者處理
- 對路徑為`*\Software\Microsoft\Windows\CurrentVersion\Run*`的注册表進行`创建、写入`操作
  
***rule.json hash: 0b95bbddefa3f3c899c788551a690bee3417d706ccb99d71c30931b82532d141***
# Ransom.CreateRansomNote

## Ransom.CreateRansomNote.A
  
狀態：啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`>\ProgramData\>.txt`的文件進行`创建`操作
- 對路徑為`>\Program Files (x86)\>.txt`的文件進行`创建`操作
- 對路徑為`>\Users\*\AppData\Local\>.txt`的文件進行`创建`操作
- 對路徑為`>\Users\*\AppData\>.txt`的文件進行`创建`操作
- 對路徑為`>\Program Files\>.txt`的文件進行`创建`操作
  
***rule.json hash: c2c8db5cd47d81f8a5f0d961cc8c86cd9bf327106b678a8370b38d6e50963444***
# Ransom.DoubleExt

## Ransom.DoubleExt.A
  
狀態：啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*.docx.>`的文件進行`创建`操作
- 對路徑為`*.xlsx.>`的文件進行`创建`操作
- 對路徑為`*.pptx.>`的文件進行`创建`操作
- 對路徑為`*.doc.>`的文件進行`创建`操作
- 對路徑為`*.xls.>`的文件進行`创建`操作
- 對路徑為`*.ppt.>`的文件進行`创建`操作

## Ransom.DoubleExt.B
  
狀態：啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`>\Users\>\Pictures\*.jpg.>`的文件進行`创建`操作
- 對路徑為`>\Users\>\Pictures\*.png.>`的文件進行`创建`操作
- 對路徑為`>\Users\>\Desktop\*.jpg.>`的文件進行`创建`操作
- 對路徑為`>\Users\>\Desktop\*.png.>`的文件進行`创建`操作
  
***rule.json hash: e5f5fd0249fcb5415f8445a356cf9b8d1b081981b6bbe3ce8d4e7b3052fd799a***
# Suspicious.AppCertDLLs

## Suspicious.AppCertDLLs.A
  
狀態：未啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*\System\CurrentControlSet\Control\Session Manager\AppCertDLLs\*`的注册表進行`创建、写入`操作
  
***rule.json hash: b7bddf3cc616ddeef545ba031f67f4e660eeee8f8baf211ed058c51d5b5ddb27***
# Suspicious.AppInitDLLs

## Suspicious.AppInitDLLs.A
  
狀態：啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*\SOFTWARE*Microsoft\Windows NT\CurrentVersion\Windows\Appinit_Dll*`的注册表進行`创建、写入`操作
  
***rule.json hash: cba6993d469ccd5b83618066036bce299790aea826ebde01cdbc16efb862d101***
# Suspicious.CommandPrompt

## Suspicious.CommandPrompt.A
  
狀態：啟用

行為描述：源程式`*\cmd.exe`做出以下操作時，提示使用者處理
- 對路徑為`*\?script.exe`的程序進行`执行`操作
- 對路徑為`*.exe`的文件進行`创建`操作
- 對路徑為`*.vb?`的文件進行`创建`操作
- 對路徑為`*.js`的文件進行`创建`操作
  
***rule.json hash: e62bc0757952c536054b872cac6a0ab7773edb697cd0a32dc824ab4246d53190***
# Suspicious.NetDebugger

## Suspicious.NetDebugger.A
  
狀態：啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*\SOFTWARE*Microsoft\.NETFramework\DbgManagedDebugge*`的注册表進行`创建、写入`操作
  
***rule.json hash: 8dafeaa565c7c02bff7bc9dd9a27155f95ad5958d3259a576797ea797fafb0c8***
# Suspicious.NetWinAppXRT

## Suspicious.NetWinAppXRT.A
  
狀態：啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*\WinAppXRT.dll`的文件進行`创建、写入`操作
  
***rule.json hash: 854d05545961e7d83d1f1d74614dae0589255c0542306eb3f4716647665ab8aa***
# Suspicious.PowerShell

## Suspicious.PowerShell.A
  
狀態：啟用

行為描述：源程式`*\Windows\Sys?????\*.exe`做出以下操作時，提示使用者處理
- 對路徑為`*\powershell.exe`的程序進行`执行`操作

## Suspicious.PowerShell.B
  
狀態：啟用

行為描述：源程式`*\powershell.exe`做出以下操作時，提示使用者處理
- 對路徑為`*\Users\*\AppData\*`的程序進行`执行`操作

## Suspicious.PowerShell.C
  
狀態：啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*\WindowsPowerShell\v1.0\profile.ps1`的文件進行`写入`操作
- 對路徑為`*\WindowsPowerShell\v1.0\Microsoft.PowerShell*profile.ps1`的文件進行`写入`操作
- 對路徑為`*\Documents\profile.ps1`的文件進行`写入`操作
  
***rule.json hash: 1768d205c6d4a0c6794d1933f20f5b43f306159d13c799fb8b7360c91372757a***
# Suspicious.RunFromSusPath

## Suspicious.RunFromSusPath.A
  
狀態：啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*\Users\*\AppData\Roaming\>`的程序進行`执行`操作
- 對路徑為`*\Users\*\AppData\>`的程序進行`执行`操作
- 對路徑為`*\Users\>\>`的程序進行`执行`操作
- 對路徑為`*\ProgramData\>`的程序進行`执行`操作
- 對路徑為`*\Program Files\>`的程序進行`执行`操作
- 對路徑為`*\Program Files (x86)\>`的程序進行`执行`操作
- 對路徑為`*\Users\*\AppData\Local\>`的程序進行`执行`操作
- 對路徑為`*\Users\>\Documents\>`的程序進行`执行`操作
- 對路徑為`*\Users\>\Documents\>\>`的程序進行`执行`操作
- 對路徑為`*\Users\Public\>.bat`的文件進行`读取`操作

## Suspicious.RunFromSusPath.B
  
狀態：啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*\Recycler\*`的程序進行`执行`操作
- 對路徑為`*\$RECYCLE.BIN\*`的程序進行`执行`操作
- 對路徑為`*\System Volume Information\*`的程序進行`执行`操作

## Suspicious.RunFromSusPath.C
  
狀態：啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*\ProgramData\>\>.exe`的程序進行`执行`操作

## Suspicious.RunFromSusPath.D
  
狀態：啟用

行為描述：源程式`*\Windows\Sys?????\>`做出以下操作時，提示使用者處理
- 對路徑為`*\Users\*\AppData\Roaming\>\>.exe`的程序進行`执行`操作
  
***rule.json hash: 365f46a07ea3328aabbec53fbbd02ca27418a21bd8c4b5ac36535f678d509940***
# Suspicious.ScriptHost

## Suspicious.ScriptHost.A
  
狀態：啟用

行為描述：源程式`*\?script.exe`做出以下操作時，提示使用者處理
- 對路徑為`*\Windows\Sys?????\*.exe`的程序進行`执行`操作
- 對路徑為`*.exe`的文件進行`创建`操作
- 對路徑為`*.dll`的文件進行`创建`操作
- 對路徑為`*\Users\*\AppData\*`的程序進行`执行`操作

## Suspicious.ScriptHost.B
  
狀態：啟用

行為描述：源程式`*\Windows\Sys?????\*.exe`做出以下操作時，提示使用者處理
- 對路徑為`*\?script.exe`的程序進行`执行`操作
  
***rule.json hash: d2705aeab053e2c7a8fb7a2a57bd21c0378b71cce1c8b9403b89c3e7941abf12***
# Suspicious.SuspProcAddAutoRun

## Suspicious.SuspProcAddAutoRun.A
  
狀態：啟用

行為描述：源程式`*\Users\*\AppData\>\>\>`做出以下操作時，提示使用者處理
- 對路徑為`*\Software\Microsoft\Windows\CurrentVersion\Run*`的注册表進行`创建、写入`操作
- 對路徑為`*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*`的文件進行`创建`操作
  
***rule.json hash: 44c2865460b206ad160babc1a7db46f5150601c4b4f3ac30fadb8598e27ad1ad***
# Suspicious.SuspProcCallSysProc

## Suspicious.SuspProcCallSysProc.A
  
狀態：啟用

行為描述：源程式`*\Users\*\AppData\>\>\>`做出以下操作時，提示使用者處理
- 對路徑為`*\Windows\Sys?????\*.exe`的程序進行`执行`操作
  
***rule.json hash: 8976ebf9e98afb7f6c1285c15f2a65f5a5a6bfe826f1818fda1b0929cf0a9a47***
# Suspicious.SysProcAddAutoRun

## Suspicious.SysProcAddAutoRun.A
  
狀態：啟用

行為描述：源程式`*\Windows\*`做出以下操作時，提示使用者處理
- 對路徑為`*\Software\Microsoft\Windows\CurrentVersion\Run*`的注册表進行`创建、写入`操作
- 對路徑為`*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*`的文件進行`创建`操作
  
***rule.json hash: b616ca54c5a8095a7189004d17c0fce2bdc47ead11d3a7151d6658b00a431fcf***
# Telemetry.ActiveSetup

## Telemetry.ActiveSetup.A
  
狀態：未啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*\SOFTWARE*Microsoft\Active Setup\Installed Components*`的注册表進行`创建`操作
  
***rule.json hash: 13861bde9ed981f5012cc0fbb6f4d28ac50163d296043697ccf800f8e1784ada***
# Telemetry.CredentialProviders

## Telemetry.CredentialProviders.A
  
狀態：未啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*\Software\Microsoft\Windows\CurrentVersion\Authentication\PLAP Provider*`的注册表進行`创建、写入`操作
- 對路徑為`*\Software\Microsoft\Windows\CurrentVersion\Authentication\Credential Provider*`的注册表進行`创建、写入`操作
  
***rule.json hash: 238b5043dfaecb9d08883698d3b66cffc5214e8381f9460cfa191963efbfb628***
# Telemetry.LSAConfig

## Telemetry.LSAConfig.A
  
狀態：未啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*\Control\Lsa`的注册表進行`创建、写入`操作
- 對路徑為`*\Control\Lsa*`的注册表進行`创建、写入`操作
  
***rule.json hash: 1e2d9f278a99ba6eba9d9c27f5ea5ab9a386228c74964f0290559a1256166d9d***
# Telemetry.PowerShell

## Telemetry.PowerShell.A
  
狀態：未啟用

行為描述：源程式`*\powershell.exe`做出以下操作時，提示使用者處理
- 對路徑為`*.exe`的文件進行`创建`操作

## Telemetry.PowerShell.B
  
狀態：未啟用

行為描述：源程式`*\powershell.exe`做出以下操作時，提示使用者處理
- 對路徑為`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\*`的注册表進行`创建`操作

## Telemetry.PowerShell.C
  
狀態：未啟用

行為描述：源程式`*\powershell.exe`做出以下操作時，提示使用者處理
- 對路徑為`\SOFTWARE\Policies\Microsoft\Windows\PowerShell\ExecutionPolicy`的注册表進行`写入`操作
  
***rule.json hash: 29f6108776c83ada5ba0762361814e853353ce651363a49dbbd469df11219859***
# Telemetry.ReadBrowserData

## Telemetry.ReadBrowserData.A
  
狀態：未啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*\Users\*\AppData\Local\*\User Data\Default\*`的文件進行`读取`操作
- 對路徑為`*\Users\*\AppData\Roaming\Mozilla\Firefox\Profiles\*`的文件進行`读取`操作
  
***rule.json hash: 4d1a67a222e18c1250786e431e7c774fe73a254ee6de8d5e12b893eb310bd32b***
# Telemetry.RunFromSusPath

## Telemetry.RunFromSusPath.A
  
狀態：未啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*\Users\*\AppData\Roaming\>\>.exe`的程序進行`执行`操作
  
***rule.json hash: 8b5b19e3835453960e36607f095ce6353fa52bd88044083277e2627f7174209a***
# Telemetry.TerminalServer

## Telemetry.TerminalServer.A
  
狀態：未啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp\InitialProgram`的注册表進行`写入`操作
  
***rule.json hash: b8410efc74805550bfd35e4030951b048c8cc9d8af0698e999d36cfe5425d2a4***
# Template
  
***rule.json hash: e499200d7c7647a852931381fcdc2a5b0dd532c593f4a44e58417f77f8f0b617***
# Trojan.CmstpDownloader

## Trojan.CmstpDownloader.A
  
狀態：啟用

行為描述：源程式`*\cmstp.exe`做出以下操作時，提示使用者處理
- 對路徑為`*.exe`的文件進行`创建`操作
- 對路徑為`*.dll`的文件進行`创建`操作
  
***rule.json hash: 11ed30aa824e9ec8efb789c6cf1b0bc5d30030f3732b5b11e6663bb8ee92bf42***
# Trojan.FakeSysProc

## Trojan.FakeSysProc.A
  
狀態：啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*\svchost.exe`的程序進行`执行`操作
- 對路徑為`*\lsass.exe`的程序進行`执行`操作
- 對路徑為`*\services.exe`的程序進行`执行`操作
- 對路徑為`*\winlogon.exe`的程序進行`执行`操作
- 對路徑為`*\csrss.exe`的程序進行`执行`操作
- 對路徑為`*\smss.exe`的程序進行`执行`操作
  
***rule.json hash: 5d9ecb177de9dbf727527545e505b234f0b67bd84ba9626eccbfb5e5167e7a0a***
# Trojan.MshtaDownloader

## Trojan.MshtaDownloader.A
  
狀態：啟用

行為描述：源程式`*\mshta.exe`做出以下操作時，提示使用者處理
- 對路徑為`*\Windows\Sys?????\*.exe`的程序進行`执行`操作
- 對路徑為`*.exe`的文件進行`创建`操作
- 對路徑為`*.dll`的文件進行`创建`操作
- 對路徑為`*\Users\*\AppData\*`的程序進行`执行`操作
  
***rule.json hash: 892d5b0994e53705cef82d97b0724d4c867cd9b36181fdb896a680319342e388***
# Trojan.Nanocore

## Trojan.Nanocore.A
  
狀態：啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*\Users\*\AppData\Roaming\>\run.dat`的文件進行`创建`操作
  
***rule.json hash: 7b2e1d410b22e9086de4bfa8882b43796c60fbe5efb2bd8af010d7fafd0893ca***
# Trojan.NetStealer

## Trojan.NetStealer.A
  
狀態：啟用

行為描述：源程式`*\Windows\Microsoft.NET\Framework\>\>`做出以下操作時，提示使用者處理
- 對路徑為`*.txt`的文件進行`创建`操作
- 對路徑為`*\Users\*\AppData\Roaming\>\>.ini`的文件進行`创建`操作
- 對路徑為`*\Software\Microsoft\Windows\CurrentVersion\Run*`的注册表進行`创建、写入`操作
- 對路徑為`*\Users\*\AppData\Local\*\User Data\Default\*`的文件進行`读取`操作
- 對路徑為`*\Users\*\AppData\Roaming\Mozilla\Firefox\Profiles\*`的文件進行`读取`操作

## Trojan.NetStealer.B
  
狀態：啟用

行為描述：源程式`*\Windows\>`做出以下操作時，提示使用者處理
- 對路徑為`*\Users\*\AppData\Roaming\>\>.ini`的文件進行`创建`操作
  
***rule.json hash: 5454ed890ae1d2bf443eeabd5100e1df7a4fb650d290265e5879bb4eba62bbad***
# Trojan.Remcos

## Trojan.Remcos.A
  
狀態：啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*Remcos*`的注册表進行`创建、写入`操作
  
***rule.json hash: f0d47e95129efb91fd8909c6b9cf4dcedeb0105a461f646d1e1878f4413b59f2***
# Trojan.Spy

## Trojan.Spy.A
  
狀態：啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*\ProgramData\*Cookie*.txt`的文件進行`创建`操作
- 對路徑為`*\Users\*\AppData\Local\Temp\*Cookie*txt`的文件進行`创建`操作
- 對路徑為`*\Users\*\AppData\Local\>\>\>Cookie>txt`的文件進行`创建`操作
- 對路徑為`*\Users\*\AppData\Local\>\>screen*png`的文件進行`创建`操作
- 對路徑為`*\Users\*\AppData\Local\Temp\*cookie*txt`的文件進行`读取`操作
- 對路徑為`*\Users\*\AppData\Local\Temp\*passowrd*txt`的文件進行`读取`操作
- 對路徑為`*\Users\*\AppData\Roaming\>\>.jpeg`的文件進行`创建`操作
  
***rule.json hash: 710be4af7b3f126da4f46688eb30715dc581c9cb4416124b73b0475acb7feb83***
# Trojan.StartupFolderMalDropper

## Trojan.StartupFolderMalDropper.A
  
狀態：啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.j>`的文件進行`创建、写入`操作
- 對路徑為`*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.vb?`的文件進行`创建、写入`操作
- 對路徑為`*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.exe`的文件進行`创建、写入`操作
  
***rule.json hash: 08785f08a7b5db2ca1868486ad734c2bad1e7158a9e5047480a1e397af621d0f***