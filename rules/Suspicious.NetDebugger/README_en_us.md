


  
[简体中文](README.md) | [繁體中文](README_zh_tw.md) | English  
  

Contents
========

* [Suspicious.NetDebugger](#suspiciousnetdebugger)
	* [Suspicious.NetDebugger.A](#suspiciousnetdebuggera)

# Suspicious.NetDebugger

## Suspicious.NetDebugger.A
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*\SOFTWARE*Microsoft\.NETFramework\DbgManagedDebugge*`
  
***rule.json hash: 69a78ae8fed5bc9bcbb68eae9c549fcf9ac68e5aaeb26a2a0639866dbaf5d8d6***