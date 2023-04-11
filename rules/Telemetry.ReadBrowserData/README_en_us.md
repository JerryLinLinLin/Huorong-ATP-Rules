


  
[简体中文](README.md) | [繁體中文](README_zh_tw.md) | English  
  

Contents
========

* [Telemetry.ReadBrowserData](#telemetryreadbrowserdata)
	* [Telemetry.ReadBrowserData.A](#telemetryreadbrowserdataa)

# Telemetry.ReadBrowserData

## Telemetry.ReadBrowserData.A
  
Status: Disabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Read` the file under the path `*\Users\*\AppData\Local\*\User Data\Default\*`
- `Read` the file under the path `*\Users\*\AppData\Roaming\Mozilla\Firefox\Profiles\*`
  
***rule.json hash: 4d1a67a222e18c1250786e431e7c774fe73a254ee6de8d5e12b893eb310bd32b***