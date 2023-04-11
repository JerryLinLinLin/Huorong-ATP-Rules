


  
[简体中文](README.md) | [繁體中文](README_zh_tw.md) | English  
  

Contents
========

* [Suspicious.RunFromSusPath](#suspiciousrunfromsuspath)
	* [Suspicious.RunFromSusPath.A](#suspiciousrunfromsuspatha)
	* [Suspicious.RunFromSusPath.B](#suspiciousrunfromsuspathb)
	* [Suspicious.RunFromSusPath.C](#suspiciousrunfromsuspathc)
	* [Suspicious.RunFromSusPath.D](#suspiciousrunfromsuspathd)

# Suspicious.RunFromSusPath

## Suspicious.RunFromSusPath.A
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Execute` the program under the path `*\Users\*\AppData\Roaming\>`
- `Execute` the program under the path `*\Users\*\AppData\>`
- `Execute` the program under the path `*\Users\>\>`
- `Execute` the program under the path `*\ProgramData\>`
- `Execute` the program under the path `*\Program Files\>`
- `Execute` the program under the path `*\Program Files (x86)\>`
- `Execute` the program under the path `*\Users\*\AppData\Local\>`
- `Execute` the program under the path `*\Users\>\Documents\>`
- `Execute` the program under the path `*\Users\>\Documents\>\>`
- `Read` the file under the path `*\Users\Public\>.bat`

## Suspicious.RunFromSusPath.B
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Execute` the program under the path `*\Recycler\*`
- `Execute` the program under the path `*\$RECYCLE.BIN\*`
- `Execute` the program under the path `*\System Volume Information\*`

## Suspicious.RunFromSusPath.C
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Execute` the program under the path `*\ProgramData\>\>.exe`

## Suspicious.RunFromSusPath.D
  
Status: Enabled

Behavioral Description:   
When the source process`*\Windows\Sys?????\>`initializes the following actions, HIPS module should let the user decide them.
- `Execute` the program under the path `*\Users\*\AppData\Roaming\>\>.exe`
  
***rule.json hash: 365f46a07ea3328aabbec53fbbd02ca27418a21bd8c4b5ac36535f678d509940***