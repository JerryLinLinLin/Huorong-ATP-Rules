



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
* [Suspicious.CommandPrompt](#suspiciouscommandprompt)
	* [Suspicious.CommandPrompt.A](#suspiciouscommandprompta)
* [Suspicious.PowerShell](#suspiciouspowershell)
	* [Suspicious.PowerShell.A](#suspiciouspowershella)
	* [Suspicious.PowerShell.B](#suspiciouspowershellb)
* [Suspicious.ReadBrowserData](#suspiciousreadbrowserdata)
	* [Suspicious.ReadBrowserData](#suspiciousreadbrowserdata)
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
  
状态：启用

行为描述：源程序`*\EXCEL.EXE`做出以下操作时，提示用户处理
- 对路径为`*.exe`的文件进行创建、写入操作
- 对路径为`*.scr`的文件进行创建、写入操作
- 对路径为`*\Windows\Sys?????\*.exe`的程序进行执行操作

## Exploit.MSOffice.B
  
状态：启用

行为描述：源程序`*\EXCEL.EXE`做出以下操作时，提示用户处理
- 对路径为`*\Software\Microsoft\Windows\CurrentVersion\Run*`的注册表进行创建、写入操作

## Exploit.MSOffice.C
  
状态：启用

行为描述：源程序`*\POWERPNT.EXE`做出以下操作时，提示用户处理
- 对路径为`*.exe`的文件进行创建、写入操作
- 对路径为`*.scr`的文件进行创建、写入操作
- 对路径为`*\Windows\Sys?????\*.exe`的程序进行执行操作

## Exploit.MSOffice.D
  
状态：启用

行为描述：源程序`*\POWERPNT.EXE`做出以下操作时，提示用户处理
- 对路径为`*\Software\Microsoft\Windows\CurrentVersion\Run*`的注册表进行创建、写入操作

## Exploit.MSOffice.E
  
状态：启用

行为描述：源程序`*\WINWORD.EXE`做出以下操作时，提示用户处理
- 对路径为`*.exe`的文件进行创建、写入操作
- 对路径为`*.scr`的文件进行创建、写入操作
- 对路径为`*\Windows\Sys?????\*.exe`的程序进行执行操作

## Exploit.MSOffice.F
  
状态：启用

行为描述：源程序`*\WINWORD.EXE`做出以下操作时，提示用户处理
- 对路径为`*\Software\Microsoft\Windows\CurrentVersion\Run*`的注册表进行创建、写入操作

## Exploit.MSOffice.G
  
状态：启用

行为描述：源程序`*\EQNEDT32.EXE`做出以下操作时，提示用户处理
- 对路径为`*.exe`的文件进行创建、写入操作
- 对路径为`*.scr`的文件进行创建、写入操作
- 对路径为`*\Windows\Sys?????\*.exe`的程序进行执行操作

## Exploit.MSOffice.H
  
状态：启用

行为描述：源程序`*\EQNEDT32.EXE`做出以下操作时，提示用户处理
- 对路径为`*\Software\Microsoft\Windows\CurrentVersion\Run*`的注册表进行创建、写入操作
  
***rule.json hash: 0b95bbddefa3f3c899c788551a690bee3417d706ccb99d71c30931b82532d141***
# Ransom.CreateRansomNote

## Ransom.CreateRansomNote.A
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`>\ProgramData\>.txt`的文件进行创建操作
- 对路径为`>\Program Files (x86)\>.txt`的文件进行创建操作
- 对路径为`>\Users\*\AppData\Local\>.txt`的文件进行创建操作
- 对路径为`>\Users\*\AppData\>.txt`的文件进行创建操作
- 对路径为`>\Program Files\>.txt`的文件进行创建操作
  
***rule.json hash: c2c8db5cd47d81f8a5f0d961cc8c86cd9bf327106b678a8370b38d6e50963444***
# Ransom.DoubleExt

## Ransom.DoubleExt.A
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*.docx.>`的文件进行创建操作
- 对路径为`*.xlsx.>`的文件进行创建操作
- 对路径为`*.pptx.>`的文件进行创建操作
- 对路径为`*.doc.>`的文件进行创建操作
- 对路径为`*.xls.>`的文件进行创建操作
- 对路径为`*.ppt.>`的文件进行创建操作

## Ransom.DoubleExt.B
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`>\Users\>\Pictures\*.jpg.>`的文件进行创建操作
- 对路径为`>\Users\>\Pictures\*.png.>`的文件进行创建操作
- 对路径为`>\Users\>\Desktop\*.jpg.>`的文件进行创建操作
- 对路径为`>\Users\>\Desktop\*.png.>`的文件进行创建操作
  
***rule.json hash: e5f5fd0249fcb5415f8445a356cf9b8d1b081981b6bbe3ce8d4e7b3052fd799a***
# Suspicious.CommandPrompt

## Suspicious.CommandPrompt.A
  
状态：启用

行为描述：源程序`*\cmd.exe`做出以下操作时，提示用户处理
- 对路径为`*\?script.exe`的程序进行执行操作
- 对路径为`*.exe`的文件进行创建操作
- 对路径为`*.vb?`的文件进行创建操作
- 对路径为`*.js`的文件进行创建操作
  
***rule.json hash: e62bc0757952c536054b872cac6a0ab7773edb697cd0a32dc824ab4246d53190***
# Suspicious.PowerShell

## Suspicious.PowerShell.A
  
状态：未启用

行为描述：源程序`*\Windows\Sys?????\*.exe`做出以下操作时，自动阻止
- 对路径为`*\powershell.exe`的程序进行执行操作

## Suspicious.PowerShell.B
  
状态：启用

行为描述：源程序`*\powershell.exe`做出以下操作时，提示用户处理
- 对路径为`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\*`的注册表进行创建操作
- 对路径为`*.exe`的文件进行创建操作
- 对路径为`*\Users\*\AppData\*`的程序进行执行操作
  
***rule.json hash: a07c32503aed526ce12772851f805a467b3155bdb1cc30e7e84fe2d9fdbdaa4b***
# Suspicious.ReadBrowserData

## Suspicious.ReadBrowserData
  
状态：未启用

行为描述：源程序`*`做出以下操作时，自动阻止
- 对路径为`*\Users\*\AppData\Local\*\User Data\Default\*`的文件进行读取操作
- 对路径为`*\Users\*\AppData\Roaming\Mozilla\Firefox\Profiles\*`的文件进行读取操作
  
***rule.json hash: ba1741093a8cab0b165da7ff972ca3fee71478259430ce3d544ac122c6fe87e4***
# Suspicious.RunFromSusPath

## Suspicious.RunFromSusPath.A
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\Users\*\AppData\Roaming\>`的程序进行执行操作
- 对路径为`*\Users\*\AppData\>`的程序进行执行操作
- 对路径为`*\Users\>\>`的程序进行执行操作
- 对路径为`*\ProgramData\>`的程序进行执行操作
- 对路径为`*\Program Files\>`的程序进行执行操作
- 对路径为`*\Program Files (x86)\>`的程序进行执行操作
- 对路径为`*\Users\*\AppData\Local\>`的程序进行执行操作
- 对路径为`*\Users\>\Documents\>`的程序进行执行操作
- 对路径为`*\Users\>\Documents\>\>`的程序进行执行操作
- 对路径为`*\Users\Public\>.bat`的文件进行读取操作

## Suspicious.RunFromSusPath.B
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\Recycler\*`的程序进行执行操作
- 对路径为`*\$RECYCLE.BIN\*`的程序进行执行操作
- 对路径为`*\System Volume Information\*`的程序进行执行操作

## Suspicious.RunFromSusPath.C
  
状态：未启用

行为描述：源程序`*`做出以下操作时，自动阻止
- 对路径为`*\ProgramData\>\>.exe`的程序进行执行操作

## Suspicious.RunFromSusPath.D
  
状态：启用

行为描述：源程序`*\Windows\Sys?????\>`做出以下操作时，提示用户处理
- 对路径为`*\Users\*\AppData\Roaming\>\>.exe`的程序进行执行操作

## Suspicious.RunFromSusPath.E
  
状态：未启用

行为描述：源程序`*`做出以下操作时，自动阻止
- 对路径为`*\Users\*\AppData\Roaming\>\>.exe`的程序进行执行操作
  
***rule.json hash: 3997ac4b56fb80d81d036c3beabcb423cfd73598afa0d93b5861c6523f10ac81***
# Suspicious.ScriptHost

## Suspicious.ScriptHost.A
  
状态：启用

行为描述：源程序`*\?script.exe`做出以下操作时，提示用户处理
- 对路径为`*\Windows\Sys?????\*.exe`的程序进行执行操作
- 对路径为`*.exe`的文件进行创建操作
- 对路径为`*.dll`的文件进行创建操作
- 对路径为`*\Users\*\AppData\*`的程序进行执行操作

## Suspicious.ScriptHost.B
  
状态：启用

行为描述：源程序`*\Windows\Sys?????\*.exe`做出以下操作时，提示用户处理
- 对路径为`*\?script.exe`的程序进行执行操作
  
***rule.json hash: d2705aeab053e2c7a8fb7a2a57bd21c0378b71cce1c8b9403b89c3e7941abf12***
# Suspicious.SuspProcAddAutoRun

## Suspicious.SuspProcAddAutoRun.A
  
状态：启用

行为描述：源程序`*\Users\*\AppData\>\>\>`做出以下操作时，提示用户处理
- 对路径为`*\Software\Microsoft\Windows\CurrentVersion\Run*`的注册表进行创建、写入操作
- 对路径为`*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*`的文件进行创建操作
  
***rule.json hash: 44c2865460b206ad160babc1a7db46f5150601c4b4f3ac30fadb8598e27ad1ad***
# Suspicious.SuspProcCallSysProc

## Suspicious.SuspProcCallSysProc.A
  
状态：未启用

行为描述：源程序`*\Users\*\AppData\>\>\>`做出以下操作时，自动阻止
- 对路径为`*\Windows\Sys?????\*.exe`的程序进行执行操作
  
***rule.json hash: b5c263fe0f878536b37daa38d98e32f854431f75754a5b59ffd881b0d5f70ba3***
# Suspicious.SysProcAddAutoRun

## Suspicious.SysProcAddAutoRun.A
  
状态：启用

行为描述：源程序`*\Windows\*`做出以下操作时，提示用户处理
- 对路径为`*\Software\Microsoft\Windows\CurrentVersion\Run*`的注册表进行创建、写入操作
- 对路径为`*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*`的文件进行创建操作
  
***rule.json hash: b616ca54c5a8095a7189004d17c0fce2bdc47ead11d3a7151d6658b00a431fcf***
# Template
  
***rule.json hash: e499200d7c7647a852931381fcdc2a5b0dd532c593f4a44e58417f77f8f0b617***
# Trojan.CmstpDownloader

## Trojan.CmstpDownloader.A
  
状态：启用

行为描述：源程序`*\cmstp.exe`做出以下操作时，提示用户处理
- 对路径为`*.exe`的文件进行创建操作
- 对路径为`*.dll`的文件进行创建操作
  
***rule.json hash: 11ed30aa824e9ec8efb789c6cf1b0bc5d30030f3732b5b11e6663bb8ee92bf42***
# Trojan.FakeSysProc

## Trojan.FakeSysProc.A
  
状态：未启用

行为描述：源程序`*`做出以下操作时，自动阻止
- 对路径为`*\svchost.exe`的程序进行执行操作
- 对路径为`*\lsass.exe`的程序进行执行操作
- 对路径为`*\services.exe`的程序进行执行操作
- 对路径为`*\winlogon.exe`的程序进行执行操作
- 对路径为`*\csrss.exe`的程序进行执行操作
- 对路径为`*\smss.exe`的程序进行执行操作
  
***rule.json hash: 11379f4626e28e779f0a4c030f0aecd2c7ba07b3eb000f11f8b2b5a1be13d6f5***
# Trojan.MshtaDownloader

## Trojan.MshtaDownloader.A
  
状态：启用

行为描述：源程序`*\mshta.exe`做出以下操作时，提示用户处理
- 对路径为`*\Windows\Sys?????\*.exe`的程序进行执行操作
- 对路径为`*.exe`的文件进行创建操作
- 对路径为`*.dll`的文件进行创建操作
- 对路径为`*\Users\*\AppData\*`的程序进行执行操作
  
***rule.json hash: 892d5b0994e53705cef82d97b0724d4c867cd9b36181fdb896a680319342e388***
# Trojan.NetStealer

## Trojan.NetStealer.A
  
状态：启用

行为描述：源程序`*\Windows\Microsoft.NET\Framework\>\>`做出以下操作时，提示用户处理
- 对路径为`*.txt`的文件进行创建操作
- 对路径为`*\Users\*\AppData\Roaming\>\>.ini`的文件进行创建操作
- 对路径为`*\Software\Microsoft\Windows\CurrentVersion\Run*`的注册表进行创建、写入操作
- 对路径为`*\Users\*\AppData\Local\*\User Data\Default\*`的文件进行读取操作
- 对路径为`*\Users\*\AppData\Roaming\Mozilla\Firefox\Profiles\*`的文件进行读取操作

## Trojan.NetStealer.B
  
状态：启用

行为描述：源程序`*\Windows\>`做出以下操作时，提示用户处理
- 对路径为`*\Users\*\AppData\Roaming\>\>.ini`的文件进行创建操作
  
***rule.json hash: 5454ed890ae1d2bf443eeabd5100e1df7a4fb650d290265e5879bb4eba62bbad***
# Trojan.Remcos

## Trojan.Remcos.A
  
状态：未启用

行为描述：源程序`*`做出以下操作时，自动阻止
- 对路径为`*Remcos*`的注册表进行创建、写入操作
  
***rule.json hash: 08fba77bc21b0d6c3e5bd254ba34246352d3962013bb93d4f668ec4da8e0e60d***
# Trojan.Spy

## Trojan.Spy.A
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\ProgramData\*Cookie*.txt`的文件进行创建操作
- 对路径为`*\Users\*\AppData\Local\Temp\*Cookie*txt`的文件进行创建操作
- 对路径为`*\Users\*\AppData\Local\>\>\>Cookie>txt`的文件进行创建操作
- 对路径为`*\Users\*\AppData\Local\>\>screen*png`的文件进行创建操作
- 对路径为`*\Users\*\AppData\Local\Temp\*cookie*txt`的文件进行读取操作
- 对路径为`*\Users\*\AppData\Local\Temp\*passowrd*txt`的文件进行读取操作
- 对路径为`*\Users\*\AppData\Roaming\>\>.jpeg`的文件进行创建操作
  
***rule.json hash: 710be4af7b3f126da4f46688eb30715dc581c9cb4416124b73b0475acb7feb83***
# Trojan.StartupFolderMalDropper

## Trojan.StartupFolderMalDropper.A
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.js`的文件进行创建、写入操作
- 对路径为`*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.vb?`的文件进行创建、写入操作
- 对路径为`*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*.exe`的文件进行创建、写入操作
  
***rule.json hash: 06703f7a24b2689c55038114daefd0625f1e163ee0cc847cdd74383fde1b78f7***