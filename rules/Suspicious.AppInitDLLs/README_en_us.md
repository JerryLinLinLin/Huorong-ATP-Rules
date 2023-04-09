


  
[简体中文](README.md) | English  
  

Contents
========

* [Suspicious.AppInitDLLs](#suspiciousappinitdlls)
	* [Suspicious.AppInitDLLs.A](#suspiciousappinitdllsa)

# Suspicious.AppInitDLLs

## Suspicious.AppInitDLLs.A
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*\SOFTWARE*Microsoft\Windows NT\CurrentVersion\Windows\Appinit_Dll*`
  
***rule.json hash: 6fd0e8a0cc1edb410eaf010023f9d27aa7c7ff487492f67a7f92ccdbed6e8391***