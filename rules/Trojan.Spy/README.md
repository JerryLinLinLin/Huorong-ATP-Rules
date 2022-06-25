



目录
==

* [Trojan.Spy 规则组](#trojanspy-)
	* [规则：Trojan.Spy.A](#trojanspya)

# Trojan.Spy 规则组

## 规则：Trojan.Spy.A
  
状态：启用

源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\ProgramData\*Cookie*.txt`的文件进行创建操作
- 对路径为`*\Users\*\AppData\Local\Temp\*Cookie*txt`的文件进行创建操作
- 对路径为`*\Users\*\AppData\Local\>\>\>Cookie>txt`的文件进行创建操作
- 对路径为`*\Users\*\AppData\Local\>\>screen*png`的文件进行创建操作
- 对路径为`*\Users\*\AppData\Local\Temp\*cookie*txt`的文件进行读取操作
- 对路径为`*\Users\*\AppData\Local\Temp\*passowrd*txt`的文件进行读取操作
- 对路径为`*\Users\*\AppData\Roaming\>\>.jpeg`的文件进行创建操作
  
***rule.json hash: 710be4af7b3f126da4f46688eb30715dc581c9cb4416124b73b0475acb7feb83***