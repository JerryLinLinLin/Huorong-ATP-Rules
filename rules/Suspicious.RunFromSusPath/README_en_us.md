



Contents
========

* [Suspicious.RunFromSusPath](#suspiciousrunfromsuspath)
	* [Telemetry.RunFromSusPath.E](#telemetryrunfromsuspathe)

# Suspicious.RunFromSusPath

## Telemetry.RunFromSusPath.E
  
Status: Disabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Execute` the program under the path `*\Users\*\AppData\Roaming\>\>.exe`
  
***rule.json hash: ae7bf2ac35fb32eee6f78358c21c58b8e16d1e3204d61c29e3504a940ca0b6a1***