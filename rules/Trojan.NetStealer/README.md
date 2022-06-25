



目录
==

* [Trojan.NetStealer](#trojannetstealer)
	* [Trojan.NetStealer.A](#trojannetstealera)
	* [Trojan.NetStealer.B](#trojannetstealerb)

# Trojan.NetStealer

## Trojan.NetStealer.A
  
状态：启用

行为描述：源程序`*\Windows\Microsoft.NET\Framework\>\>`做出以下操作时，提示用户处理
- 对路径为`*.txt`的文件进行创建操作
- 对路径为`*\Users\*\AppData\Roaming\>\>.ini`的文件进行创建操作
- 对路径为`*\Software\Microsoft\Windows\CurrentVersion\Run*`的注册表进行创建、写入操作
- 对路径为`*\Users\*\AppData\Local\*\User Data\Default\*`的文件进行读取操作
- 对路径为`*\Users\*\AppData\Roaming\Mozilla\Firefox\Profiles\*`的文件进行读取操作

## Trojan.NetStealer.B
  
状态：启用

行为描述：源程序`*\Windows\>`做出以下操作时，提示用户处理
- 对路径为`*\Users\*\AppData\Roaming\>\>.ini`的文件进行创建操作
  
***rule.json hash: 5454ed890ae1d2bf443eeabd5100e1df7a4fb650d290265e5879bb4eba62bbad***