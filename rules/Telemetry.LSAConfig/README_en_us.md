


  
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
  
***rule.json hash: 1e2d9f278a99ba6eba9d9c27f5ea5ab9a386228c74964f0290559a1256166d9d***