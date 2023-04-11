


  
[简体中文](README.md) | 繁體中文 | [English](README_en_us.md)  
  

目錄
==

* [Ransom.CreateRansomNote](#ransomcreateransomnote)
	* [Ransom.CreateRansomNote.A](#ransomcreateransomnotea)

# Ransom.CreateRansomNote

## Ransom.CreateRansomNote.A
  
狀態：啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`>\ProgramData\>.txt`的文件進行`创建`操作
- 對路徑為`>\Program Files (x86)\>.txt`的文件進行`创建`操作
- 對路徑為`>\Users\*\AppData\Local\>.txt`的文件進行`创建`操作
- 對路徑為`>\Users\*\AppData\>.txt`的文件進行`创建`操作
- 對路徑為`>\Program Files\>.txt`的文件進行`创建`操作
  
***rule.json hash: c2c8db5cd47d81f8a5f0d961cc8c86cd9bf327106b678a8370b38d6e50963444***