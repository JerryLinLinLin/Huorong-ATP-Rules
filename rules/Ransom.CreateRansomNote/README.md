



目录
==

* [Ransom.CreateRansomNote 规则组](#ransomcreateransomnote-)
	* [规则：Ransom.CreateRansomNote.A](#ransomcreateransomnotea)

# Ransom.CreateRansomNote 规则组

## 规则：Ransom.CreateRansomNote.A
  
状态：启用

源程序`*`做出以下操作时，提示用户处理
- 对路径为>\ProgramData\>.txt的文件进行创操作
- 对路径为>\Program Files (x86)\>.txt的文件进行创操作
- 对路径为>\Users\*\AppData\Local\>.txt的文件进行创操作
- 对路径为>\Users\*\AppData\>.txt的文件进行创操作
- 对路径为>\Program Files\>.txt的文件进行创操作
  
***rule.json hash: c2c8db5cd47d81f8a5f0d961cc8c86cd9bf327106b678a8370b38d6e50963444***