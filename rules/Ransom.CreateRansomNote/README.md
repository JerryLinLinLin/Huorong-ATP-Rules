


  
简体中文 | [繁體中文](README_zh_tw.md) | [English](README_en_us.md)  
  

目录
==

* [Ransom.CreateRansomNote](#ransomcreateransomnote)
	* [Ransom.CreateRansomNote.A](#ransomcreateransomnotea)

# Ransom.CreateRansomNote

## Ransom.CreateRansomNote.A
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`>\ProgramData\>.txt`的文件进行`创建`操作
- 对路径为`>\Program Files (x86)\>.txt`的文件进行`创建`操作
- 对路径为`>\Users\*\AppData\Local\>.txt`的文件进行`创建`操作
- 对路径为`>\Users\*\AppData\>.txt`的文件进行`创建`操作
- 对路径为`>\Program Files\>.txt`的文件进行`创建`操作
  
***rule.json hash: c2c8db5cd47d81f8a5f0d961cc8c86cd9bf327106b678a8370b38d6e50963444***