



Contents
========

* [Suspicious.NetDebugger](#suspiciousnetdebugger)
	* [Suspicious.NetDebugger.A](#suspiciousnetdebuggera)

# Suspicious.NetDebugger

## Suspicious.NetDebugger.A
  
Status: Disabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*\SOFTWARE*Microsoft\.NETFramework\DbgManagedDebugge*`
  
***rule.json hash: 04ca56b228447f507b7f8e4bc012dfee5c97828c916b7513db6b61c24d14ed14***