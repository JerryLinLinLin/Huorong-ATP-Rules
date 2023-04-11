


  
简体中文 | [繁體中文](README_zh_tw.md) | [English](README_en_us.md)  
  

目录
==

* [Suspicious.AppInitDLLs](#suspiciousappinitdlls)
	* [Suspicious.AppInitDLLs.A](#suspiciousappinitdllsa)

# Suspicious.AppInitDLLs

## Suspicious.AppInitDLLs.A
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\SOFTWARE*Microsoft\Windows NT\CurrentVersion\Windows\Appinit_Dll*`的注册表进行`创建、写入`操作
  
***rule.json hash: cba6993d469ccd5b83618066036bce299790aea826ebde01cdbc16efb862d101***