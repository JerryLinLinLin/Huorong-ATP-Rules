



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
  
***rule.json hash: e89457383d24e328b7690300d5f3bf253909e57adf4cce5d0069c637a708ad35***