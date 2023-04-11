


  
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
  
***rule.json hash: 8dafeaa565c7c02bff7bc9dd9a27155f95ad5958d3259a576797ea797fafb0c8***