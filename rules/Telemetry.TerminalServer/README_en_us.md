


  
[简体中文](README.md) | English  
  

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
  
***rule.json hash: 1b245341cbd4dc6c3457fef43ee9ab8ffc96738ea578ed2bda9981f86819490e***