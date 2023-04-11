


  
[简体中文](README.md) | [繁體中文](README_zh_tw.md) | English  
  

Contents
========

* [Telemetry.CredentialProviders](#telemetrycredentialproviders)
	* [Telemetry.CredentialProviders.A](#telemetrycredentialprovidersa)

# Telemetry.CredentialProviders

## Telemetry.CredentialProviders.A
  
Status: Disabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create, Write` the registry under the path `*\Software\Microsoft\Windows\CurrentVersion\Authentication\PLAP Provider*`
- `Create, Write` the registry under the path `*\Software\Microsoft\Windows\CurrentVersion\Authentication\Credential Provider*`
  
***rule.json hash: 495c7c42f579fcc2a45efdd8c22bcee72c3bd88964ebf0c1714c7c7c4c32062d***