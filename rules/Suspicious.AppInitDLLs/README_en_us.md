


  
[简体中文](README.md) | [繁體中文](README_zh_tw.md) | English  
  

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
  
***rule.json hash: cba6993d469ccd5b83618066036bce299790aea826ebde01cdbc16efb862d101***