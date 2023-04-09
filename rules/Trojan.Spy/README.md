


  
简体中文 | [English](README_en_us.md)  
  

目录
==

* [Trojan.Spy](#trojanspy)
	* [Trojan.Spy.A](#trojanspya)

# Trojan.Spy

## Trojan.Spy.A
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\ProgramData\*Cookie*.txt`的文件进行**创建**操作
- 对路径为`*\Users\*\AppData\Local\Temp\*Cookie*txt`的文件进行**创建**操作
- 对路径为`*\Users\*\AppData\Local\>\>\>Cookie>txt`的文件进行**创建**操作
- 对路径为`*\Users\*\AppData\Local\>\>screen*png`的文件进行**创建**操作
- 对路径为`*\Users\*\AppData\Local\Temp\*cookie*txt`的文件进行**读取**操作
- 对路径为`*\Users\*\AppData\Local\Temp\*passowrd*txt`的文件进行**读取**操作
- 对路径为`*\Users\*\AppData\Roaming\>\>.jpeg`的文件进行**创建**操作
  
***rule.json hash: 007f1ee31843571162c95ca83eb42cbc192ccdfe1268363c1a4cd4c96955b914***