


  
简体中文 | [English](README_en_us.md)  
  

目录
==

* [Telemetry.CredentialProviders](#telemetrycredentialproviders)
	* [Telemetry.CredentialProviders.A](#telemetrycredentialprovidersa)

# Telemetry.CredentialProviders

## Telemetry.CredentialProviders.A
  
状态：未启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\Software\Microsoft\Windows\CurrentVersion\Authentication\PLAP Provider*`的注册表进行`创建、写入`操作
- 对路径为`*\Software\Microsoft\Windows\CurrentVersion\Authentication\Credential Provider*`的注册表进行`创建、写入`操作
  
***rule.json hash: 495c7c42f579fcc2a45efdd8c22bcee72c3bd88964ebf0c1714c7c7c4c32062d***