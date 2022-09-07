



Contents
========

* [Suspicious.AppCertDLLs](#suspiciousappcertdlls)
	* [Suspicious.AppCertDLLs.A](#suspiciousappcertdllsa)

# Suspicious.AppCertDLLs

## Suspicious.AppCertDLLs.A
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*\System\CurrentControlSet\Control\Session Manager\AppCertDLLs\*`
  
***rule.json hash: ca1f6ff9981726324e729b6e012c879a6f839b30a95eebb4f756792da9773ccd***