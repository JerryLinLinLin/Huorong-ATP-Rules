



Contents
========

* [Suspicious.NetWinAppXRT](#suspiciousnetwinappxrt)
	* [Suspicious.NetWinAppXRT.A](#suspiciousnetwinappxrta)

# Suspicious.NetWinAppXRT

## Suspicious.NetWinAppXRT.A
  
Status: Disabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the file under the path `*\WinAppXRT.dll`
  
***rule.json hash: e929a5393844223a858a2db1aec518991e2d30f560a952a4066a5f69352cdf47***