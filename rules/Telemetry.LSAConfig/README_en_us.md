


  
[简体中文](README.md) | [繁體中文](README_zh_tw.md) | English  
  

Contents
========

* [Telemetry.LSAConfig](#telemetrylsaconfig)
	* [Telemetry.LSAConfig.A](#telemetrylsaconfiga)

# Telemetry.LSAConfig

## Telemetry.LSAConfig.A
  
Status: Disabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*\Control\Lsa`
- `Create, Write` the registry under the path `*\Control\Lsa*`
  
***rule.json hash: f94511a7d03f0b57a291761d410b84c4f5376efd0bb7fe56ba9e06d3ebe09bf7***