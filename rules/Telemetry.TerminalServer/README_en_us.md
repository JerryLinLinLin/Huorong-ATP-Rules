


  
[简体中文](README.md) | [繁體中文](README_zh_tw.md) | English  
  

Contents
========

* [Telemetry.TerminalServer](#telemetryterminalserver)
	* [Telemetry.TerminalServer.A](#telemetryterminalservera)

# Telemetry.TerminalServer

## Telemetry.TerminalServer.A
  
Status: Disabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Write` the registry under the path `*\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp\InitialProgram`
  
***rule.json hash: b8410efc74805550bfd35e4030951b048c8cc9d8af0698e999d36cfe5425d2a4***