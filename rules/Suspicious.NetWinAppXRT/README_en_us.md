


  
[简体中文](README.md) | [繁體中文](README_zh_tw.md) | English  
  

Contents
========

* [Suspicious.NetWinAppXRT](#suspiciousnetwinappxrt)
	* [Suspicious.NetWinAppXRT.A](#suspiciousnetwinappxrta)

# Suspicious.NetWinAppXRT

## Suspicious.NetWinAppXRT.A
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the file under the path `*\WinAppXRT.dll`
  
***rule.json hash: 854d05545961e7d83d1f1d74614dae0589255c0542306eb3f4716647665ab8aa***