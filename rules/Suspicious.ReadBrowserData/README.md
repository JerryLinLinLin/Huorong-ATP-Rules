



目录
==

* [Suspicious.ReadBrowserData](#suspiciousreadbrowserdata)
	* [Suspicious.ReadBrowserData.A](#suspiciousreadbrowserdataa)

# Suspicious.ReadBrowserData

## Suspicious.ReadBrowserData.A
  
状态：未启用

行为描述：源程序`*`做出以下操作时，自动阻止
- 对路径为`*\Users\*\AppData\Local\*\User Data\Default\*`的文件进行**读取**操作
- 对路径为`*\Users\*\AppData\Roaming\Mozilla\Firefox\Profiles\*`的文件进行**读取**操作
  
***rule.json hash: f9af5aadaebe552fe3df866cf91edf2744eaea4da3fd2f29dba025b48996d057***