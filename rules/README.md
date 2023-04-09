


  
简体中文 | [English](rules/README_en_us)  
  

目录
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
  
状态：启用

行为描述：源程序`*\EXCEL.EXE`做出以下操作时，提示用户处理
- 对路径为`*.exe`的文件进行**创建、写入**操作
- 对路径为`*.scr`的文件进行**创建、写入**操作
- 对路径为`*\Windows\Sys?????\*.exe`的程序进行**执行**操作

## Exploit.MSOffice.B
  
状态：启用

行为描述：源程序`*\EXCEL.EXE`做出以下操作时，提示用户处理
- 对路径为`*\Software\Microsoft\Windows\CurrentVersion\Run*`的注册表进行**创建、写入**操作

## Exploit.MSOffice.C
  
状态：启用

行为描述：源程序`*\POWERPNT.EXE`做出以下操作时，提示用户处理
- 对路径为`*.exe`的文件进行**创建、写入**操作
- 对路径为`*.scr`的文件进行**创建、写入**操作
- 对路径为`*\Windows\Sys?????\*.exe`的程序进行**执行**操作

## Exploit.MSOffice.D
  
状态：启用

行为描述：源程序`*\POWERPNT.EXE`做出以下操作时，提示用户处理
- 对路径为`*\Software\Microsoft\Windows\CurrentVersion\Run*`的注册表进行**创建、写入**操作

## Exploit.MSOffice.E
  
状态：启用

行为描述：源程序`*\WINWORD.EXE`做出以下操作时，提示用户处理
- 对路径为`*.exe`的文件进行**创建、写入**操作
- 对路径为`*.scr`的文件进行**创建、写入**操作
- 对路径为`*\Windows\Sys?????\*.exe`的程序进行**执行**操作

## Exploit.MSOffice.F
  
状态：启用

行为描述：源程序`*\WINWORD.EXE`做出以下操作时，提示用户处理
- 对路径为`*\Software\Microsoft\Windows\CurrentVersion\Run*`的注册表进行**创建、写入**操作

## Exploit.MSOffice.G
  
状态：启用

行为描述：源程序`*\EQNEDT32.EXE`做出以下操作时，提示用户处理
- 对路径为`*.exe`的文件进行**创建、写入**操作
- 对路径为`*.scr`的文件进行**创建、写入**操作
- 对路径为`*\Windows\Sys?????\*.exe`的程序进行**执行**操作

## Exploit.MSOffice.H
  
状态：启用

行为描述：源程序`*\EQNEDT32.EXE`做出以下操作时，提示用户处理
- 对路径为`*\Software\Microsoft\Windows\CurrentVersion\Run*`的注册表进行**创建、写入**操作
  
***rule.json hash: 11a6f7f126334cff29ddfdc485905a1c4ba3aec0f7f911e203980f34cb4ce62c***
# Ransom.CreateRansomNote

## Ransom.CreateRansomNote.A
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`>\ProgramData\>.txt`的文件进行**创建**操作
- 对路径为`>\Program Files (x86)\>.txt`的文件进行**创建**操作
- 对路径为`>\Users\*\AppData\Local\>.txt`的文件进行**创建**操作
- 对路径为`>\Users\*\AppData\>.txt`的文件进行**创建**操作
- 对路径为`>\Program Files\>.txt`的文件进行**创建**操作
  
***rule.json hash: 92dea9dc04af20406512baf6d17bf9ffc4c27911257403682db3b4bccd2b9bf3***
# Ransom.DoubleExt

## Ransom.DoubleExt.A
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*.docx.>`的文件进行**创建**操作
- 对路径为`*.xlsx.>`的文件进行**创建**操作
- 对路径为`*.pptx.>`的文件进行**创建**操作
- 对路径为`*.doc.>`的文件进行**创建**操作
- 对路径为`*.xls.>`的文件进行**创建**操作
- 对路径为`*.ppt.>`的文件进行**创建**操作

## Ransom.DoubleExt.B
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`>\Users\>\Pictures\*.jpg.>`的文件进行**创建**操作
- 对路径为`>\Users\>\Pictures\*.png.>`的文件进行**创建**操作
- 对路径为`>\Users\>\Desktop\*.jpg.>`的文件进行**创建**操作
- 对路径为`>\Users\>\Desktop\*.png.>`的文件进行**创建**操作
  
***rule.json hash: 8afaf4ee0e8ea6328dd7102d76abcd442db651f497c2208e1e9e54e72bad7c4c***
# Suspicious.AppCertDLLs

## Suspicious.AppCertDLLs.A
  
状态：未启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\System\CurrentControlSet\Control\Session Manager\AppCertDLLs\*`的注册表进行**创建、写入**操作
  
***rule.json hash: dfdff9349d60a3a7d57355d0e0a7e20b7da9997568cf228a647f1a94f2db6ec0***
# Suspicious.AppInitDLLs

## Suspicious.AppInitDLLs.A
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\SOFTWARE*Microsoft\Windows NT\CurrentVersion\Windows\Appinit_Dll*`的注册表进行**创建、写入**操作
  
***rule.json hash: 6fd0e8a0cc1edb410eaf010023f9d27aa7c7ff487492f67a7f92ccdbed6e8391***
# Suspicious.CommandPrompt

## Suspicious.CommandPrompt.A
  
状态：启用

行为描述：源程序`*\cmd.exe`做出以下操作时，提示用户处理
- 对路径为`*\?script.exe`的程序进行**执行**操作
- 对路径为`*.exe`的文件进行**创建**操作
- 对路径为`*.vb?`的文件进行**创建**操作
- 对路径为`*.js`的文件进行**创建**操作
  
***rule.json hash: ac6da01e160cfb9848cec158ee41f935786a5413aadca2f4bb2c9ef66fcce2cd***
# Suspicious.NetDebugger

## Suspicious.NetDebugger.A
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\SOFTWARE*Microsoft\.NETFramework\DbgManagedDebugge*`的注册表进行**创建、写入**操作
  
***rule.json hash: 69a78ae8fed5bc9bcbb68eae9c549fcf9ac68e5aaeb26a2a0639866dbaf5d8d6***
# Suspicious.NetWinAppXRT

## Suspicious.NetWinAppXRT.A
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\WinAppXRT.dll`的文件进行**创建、写入**操作
  
***rule.json hash: f4ad1d9a4fc9506d43c0e802b323c39414a8599d5241095efeba91abffb9d1ea***
# Suspicious.PowerShell

## Suspicious.PowerShell.A
  
状态：启用

行为描述：源程序`*\Windows\Sys?????\*.exe`做出以下操作时，提示用户处理
- 对路径为`*\powershell.exe`的程序进行**执行**操作

## Suspicious.PowerShell.B
  
状态：启用

行为描述：源程序`*\powershell.exe`做出以下操作时，提示用户处理
- 对路径为`*\Users\*\AppData\*`的程序进行**执行**操作

## Suspicious.PowerShell.C
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\WindowsPowerShell\v1.0\profile.ps1`的文件进行**写入**操作
- 对路径为`*\WindowsPowerShell\v1.0\Microsoft.PowerShell*profile.ps1`的文件进行**写入**操作
- 对路径为`*\Documents\profile.ps1`的文件进行**写入**操作
  
***rule.json hash: 8407b3ae9312f1ebc1145986020e3ff3cd72543e98e6ded29b064a7ccf875ea8***
# Suspicious.RunFromSusPath

## Suspicious.RunFromSusPath.A
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\Users\*\AppData\Roaming\>`的程序进行**执行**操作
- 对路径为`*\Users\*\AppData\>`的程序进行**执行**操作
- 对路径为`*\Users\>\>`的程序进行**执行**操作
- 对路径为`*\ProgramData\>`的程序进行**执行**操作
- 对路径为`*\Program Files\>`的程序进行**执行**操作
- 对路径为`*\Program Files (x86)\>`的程序进行**执行**操作
- 对路径为`*\Users\*\AppData\Local\>`的程序进行**执行**操作
- 对路径为`*\Users\>\Documents\>`的程序进行**执行**操作
- 对路径为`*\Users\>\Documents\>\>`的程序进行**执行**操作
- 对路径为`*\Users\Public\>.bat`的文件进行**读取**操作

## Suspicious.RunFromSusPath.B
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\Recycler\*`的程序进行**执行**操作
- 对路径为`*\$RECYCLE.BIN\*`的程序进行**执行**操作
- 对路径为`*\System Volume Information\*`的程序进行**执行**操作

## Suspicious.RunFromSusPath.C
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\ProgramData\>\>.exe`的程序进行**执行**操作

## Suspicious.RunFromSusPath.D
  
状态：启用

行为描述：源程序`*\Windows\Sys?????\>`做出以下操作时，提示用户处理
- 对路径为`*\Users\*\AppData\Roaming\>\>.exe`的程序进行**执行**操作
  
***rule.json hash: 0ce318e7bf946e22f9b9bc6bb13188f0e1fc43c42d10a7699f0d4a0c6af16cb7***
# Suspicious.ScriptHost

## Suspicious.ScriptHost.A
  
状态：启用

行为描述：源程序`*\?script.exe`做出以下操作时，提示用户处理
- 对路径为`*\Windows\Sys?????\*.exe`的程序进行**执行**操作
- 对路径为`*.exe`的文件进行**创建**操作
- 对路径为`*.dll`的文件进行**创建**操作
- 对路径为`*\Users\*\AppData\*`的程序进行**执行**操作

## Suspicious.ScriptHost.B
  
状态：启用

行为描述：源程序`*\Windows\Sys?????\*.exe`做出以下操作时，提示用户处理
- 对路径为`*\?script.exe`的程序进行**执行**操作
  
***rule.json hash: 7692734f67bdef45c360f5d4b04da6d64141543e16f47214a7b005f3094a3fe9***
# Suspicious.SuspProcAddAutoRun

## Suspicious.SuspProcAddAutoRun.A
  
状态：启用

行为描述：源程序`*\Users\*\AppData\>\>\>`做出以下操作时，提示用户处理
- 对路径为`*\Software\Microsoft\Windows\CurrentVersion\Run*`的注册表进行**创建、写入**操作
- 对路径为`*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*`的文件进行**创建**操作
  
***rule.json hash: 4aa4a4bcd0c6ecdd91d95954e534c4cd844dcde11960cdfcafb4d6169b081ca2***
# Suspicious.SuspProcCallSysProc

## Suspicious.SuspProcCallSysProc.A
  
状态：启用

行为描述：源程序`*\Users\*\AppData\>\>\>`做出以下操作时，提示用户处理
- 对路径为`*\Windows\Sys?????\*.exe`的程序进行**执行**操作
  
***rule.json hash: e89457383d24e328b7690300d5f3bf253909e57adf4cce5d0069c637a708ad35***
# Suspicious.SysProcAddAutoRun

## Suspicious.SysProcAddAutoRun.A
  
状态：启用

行为描述：源程序`*\Windows\*`做出以下操作时，提示用户处理
- 对路径为`*\Software\Microsoft\Windows\CurrentVersion\Run*`的注册表进行**创建、写入**操作
- 对路径为`*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*`的文件进行**创建**操作
  
***rule.json hash: b57855ef08d403a05d0d219b948fd32048c5f38ff07da0155ac2719ed510c2e9***
# Telemetry.ActiveSetup

## Telemetry.ActiveSetup.A
  
状态：未启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\SOFTWARE*Microsoft\Active Setup\Installed Components*`的注册表进行**创建**操作
  
***rule.json hash: 25f31e649b656ea0a57e2bcf47eb507ac362fd3b168aeeeed1cbf6dd0fbeaeb9***
# Telemetry.CredentialProviders

## Telemetry.CredentialProviders.A
  
状态：未启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\Software\Microsoft\Windows\CurrentVersion\Authentication\PLAP Provider*`的注册表进行**创建、写入**操作
- 对路径为`*\Software\Microsoft\Windows\CurrentVersion\Authentication\Credential Provider*`的注册表进行**创建、写入**操作
  
***rule.json hash: 495c7c42f579fcc2a45efdd8c22bcee72c3bd88964ebf0c1714c7c7c4c32062d***
# Telemetry.LSAConfig

## Telemetry.LSAConfig.A
  
状态：未启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\Control\Lsa`的注册表进行**创建、写入**操作
- 对路径为`*\Control\Lsa*`的注册表进行**创建、写入**操作
  
***rule.json hash: f94511a7d03f0b57a291761d410b84c4f5376efd0bb7fe56ba9e06d3ebe09bf7***
# Telemetry.PowerShell

## Telemetry.PowerShell.A
  
状态：未启用

行为描述：源程序`*\powershell.exe`做出以下操作时，提示用户处理
- 对路径为`*.exe`的文件进行**创建**操作

## Telemetry.PowerShell.B
  
状态：未启用

行为描述：源程序`*\powershell.exe`做出以下操作时，提示用户处理
- 对路径为`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\*`的注册表进行**创建**操作

## Telemetry.PowerShell.C
  
状态：未启用

行为描述：源程序`*\powershell.exe`做出以下操作时，提示用户处理
- 对路径为`\SOFTWARE\Policies\Microsoft\Windows\PowerShell\ExecutionPolicy`的注册表进行**写入**操作
  
***rule.json hash: 6176d464860dad2aa05aac6d1bdd4d556618cc1fa09a68bc9aba16208d464613***
# Telemetry.ReadBrowserData

## Telemetry.ReadBrowserData.A
  
状态：未启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\Users\*\AppData\Local\*\User Data\Default\*`的文件进行**读取**操作
- 对路径为`*\Users\*\AppData\Roaming\Mozilla\Firefox\Profiles\*`的文件进行**读取**操作
  
***rule.json hash: 04c8f6e13bbfc0027141f86bf678a2573bfd46326051c1753b2930bfdc2d1d7a***
# Telemetry.RunFromSusPath

## Telemetry.RunFromSusPath.A
  
状态：未启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\Users\*\AppData\Roaming\>\>.exe`的程序进行**执行**操作
  
***rule.json hash: 8e649f1c95f70ea514564927537534ec4e4d61a9dc322d163fff85aab12fd612***
# Telemetry.TerminalServer

## Telemetry.TerminalServer.A
  
状态：未启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp\InitialProgram`的注册表进行**写入**操作
  
***rule.json hash: 1b245341cbd4dc6c3457fef43ee9ab8ffc96738ea578ed2bda9981f86819490e***
# Template
  
***rule.json hash: 26c5a555c2ccb94877985ee87cda3a1f44578de3e71abb672b5b822639f95416***
# Trojan.CmstpDownloader

## Trojan.CmstpDownloader.A
  
状态：启用

行为描述：源程序`*\cmstp.exe`做出以下操作时，提示用户处理
- 对路径为`*.exe`的文件进行**创建**操作
- 对路径为`*.dll`的文件进行**创建**操作
  
***rule.json hash: 7a61cc7f5c4d7b6726f51cfc9110e44425f219f4b2165f38c3c959691bce9627***
# Trojan.FakeSysProc

## Trojan.FakeSysProc.A
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\svchost.exe`的程序进行**执行**操作
- 对路径为`*\lsass.exe`的程序进行**执行**操作
- 对路径为`*\services.exe`的程序进行**执行**操作
- 对路径为`*\winlogon.exe`的程序进行**执行**操作
- 对路径为`*\csrss.exe`的程序进行**执行**操作
- 对路径为`*\smss.exe`的程序进行**执行**操作
  
***rule.json hash: 050c9912a384d8858c1f745894d9172ff45ef8a04c03a3fa7b57f02c8a0634da***
# Trojan.MshtaDownloader

## Trojan.MshtaDownloader.A
  
状态：启用

行为描述：源程序`*\mshta.exe`做出以下操作时，提示用户处理
- 对路径为`*\Windows\Sys?????\*.exe`的程序进行**执行**操作
- 对路径为`*.exe`的文件进行**创建**操作
- 对路径为`*.dll`的文件进行**创建**操作
- 对路径为`*\Users\*\AppData\*`的程序进行**执行**操作
  
***rule.json hash: 9af5a10aba8688c0759a59db43479ddd32558715cf3b6905531d9ef484e924a7***
# Trojan.Nanocore

## Trojan.Nanocore.A
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\Users\*\AppData\Roaming\>\run.dat`的文件进行**创建**操作
  
***rule.json hash: dfee1a531ec4660d2f369489bf185f6d24a448670867d2e1d2f62ff86d4aefd3***
# Trojan.NetStealer

## Trojan.NetStealer.A
  
状态：启用

行为描述：源程序`*\Windows\Microsoft.NET\Framework\>\>`做出以下操作时，提示用户处理
- 对路径为`*.txt`的文件进行**创建**操作
- 对路径为`*\Users\*\AppData\Roaming\>\>.ini`的文件进行**创建**操作
- 对路径为`*\Software\Microsoft\Windows\CurrentVersion\Run*`的注册表进行**创建、写入**操作
- 对路径为`*\Users\*\AppData\Local\*\User Data\Default\*`的文件进行**读取**操作
- 对路径为`*\Users\*\AppData\Roaming\Mozilla\Firefox\Profiles\*`的文件进行**读取**操作

## Trojan.NetStealer.B
  
状态：启用

行为描述：源程序`*\Windows\>`做出以下操作时，提示用户处理
- 对路径为`*\Users\*\AppData\Roaming\>\>.ini`的文件进行**创建**操作
  
***rule.json hash: a1dc27a7fe9ba237485ee9bff7e5d1a72d413649aaf9cd82a43b5819c1ff1468***
# Trojan.Remcos

## Trojan.Remcos.A
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*Remcos*`的注册表进行**创建、写入**操作
  
***rule.json hash: 9356fc082479626e97c5c8a06fec3876eb7860531d87b548b6a0897598921edb***
# Trojan.Spy

## Trojan.Spy.A
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\ProgramData\*Cookie*.txt`的文件进行**创建**操作
- 对路径为`*\Users\*\AppData\Local\Temp\*Cookie*txt`的文件进行**创建**操作
- 对路径为`*\Users\*\AppData\Local\>\>\>Cookie>txt`的文件进行**创建**操作
- 对路径为`*\Users\*\AppData\Local\>\>screen*png`的文件进行**创建**操作
- 对路径为`*\Users\*\AppData\Local\Temp\*cookie*txt`的文件进行**读取**操作
- 对路径为`*\Users\*\AppData\Local\Temp\*passowrd*txt`的文件进行**读取**操作
- 对路径为`*\Users\*\AppData\Roaming\>\>.jpeg`的文件进行**创建**操作
  
***rule.json hash: 007f1ee31843571162c95ca83eb42cbc192ccdfe1268363c1a4cd4c96955b914***
# Trojan.StartupFolderMalDropper

## Trojan.StartupFolderMalDropper.A
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.j>`的文件进行**创建、写入**操作
- 对路径为`*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.vb?`的文件进行**创建、写入**操作
- 对路径为`*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.exe`的文件进行**创建、写入**操作
  
***rule.json hash: d5498c78b6062c8e4a7376af6eb2cd2e5455102de2d1a404c65b6c8493f72ea0***