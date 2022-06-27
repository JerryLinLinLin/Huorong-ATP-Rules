



Contents
========

* [Suspicious.SysProcAddAutoRun](#suspicioussysprocaddautorun)
	* [Suspicious.SysProcAddAutoRun.A](#suspicioussysprocaddautoruna)

# Suspicious.SysProcAddAutoRun

## Suspicious.SysProcAddAutoRun.A
  
Status: Enabled

Behavioral Description:   
When the source process`*\Windows\*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*\Software\Microsoft\Windows\CurrentVersion\Run*`
- `Create` the file under the path `*\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\*`
  
***rule.json hash: b616ca54c5a8095a7189004d17c0fce2bdc47ead11d3a7151d6658b00a431fcf***