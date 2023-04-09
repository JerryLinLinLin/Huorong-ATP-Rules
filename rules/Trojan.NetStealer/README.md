


  
简体中文 | [English](README_en_us.md)  
  

目录
==

* [Trojan.NetStealer](#trojannetstealer)
	* [Trojan.NetStealer.A](#trojannetstealera)
	* [Trojan.NetStealer.B](#trojannetstealerb)

# Trojan.NetStealer

## Trojan.NetStealer.A
  
状态：启用

行为描述：源程序`*\Windows\Microsoft.NET\Framework\>\>`做出以下操作时，提示用户处理
- 对路径为`*.txt`的文件进行**创建**操作
- 对路径为`*\Users\*\AppData\Roaming\>\>.ini`的文件进行**创建**操作
- 对路径为`*\Software\Microsoft\Windows\CurrentVersion\Run*`的注册表进行**创建、写入**操作
- 对路径为`*\Users\*\AppData\Local\*\User Data\Default\*`的文件进行**读取**操作
- 对路径为`*\Users\*\AppData\Roaming\Mozilla\Firefox\Profiles\*`的文件进行**读取**操作

## Trojan.NetStealer.B
  
状态：启用

行为描述：源程序`*\Windows\>`做出以下操作时，提示用户处理
- 对路径为`*\Users\*\AppData\Roaming\>\>.ini`的文件进行**创建**操作
  
***rule.json hash: a1dc27a7fe9ba237485ee9bff7e5d1a72d413649aaf9cd82a43b5819c1ff1468***