



Contents
========

* [Suspicious.AppCertDLLs](#suspiciousappcertdlls)
	* [Suspicious.AppCertDLLs.A](#suspiciousappcertdllsa)

# Suspicious.AppCertDLLs

## Suspicious.AppCertDLLs.A
  
Status: Disabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*\System\CurrentControlSet\Control\Session Manager\AppCertDLLs\*`
  
***rule.json hash: dfdff9349d60a3a7d57355d0e0a7e20b7da9997568cf228a647f1a94f2db6ec0***  
[简体中文](/README.md) | English