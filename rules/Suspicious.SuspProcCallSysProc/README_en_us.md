



Contents
========

* [Suspicious.SuspProcCallSysProc](#suspicioussuspproccallsysproc)
	* [Suspicious.SuspProcCallSysProc.A](#suspicioussuspproccallsysproca)

# Suspicious.SuspProcCallSysProc

## Suspicious.SuspProcCallSysProc.A
  
Status: Enabled  
Behavioral Description: 

When the source process`*\Users\*\AppData\>\>\>`initializes the following actions, HIPS module should let the user decide them.
- `Execute` the program under the path `*\Windows\Sys?????\*.exe`
  
***rule.json hash: 8976ebf9e98afb7f6c1285c15f2a65f5a5a6bfe826f1818fda1b0929cf0a9a47***