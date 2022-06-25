



目录
==

* [Suspicious.ReadBrowserData 规则组](#suspiciousreadbrowserdata-)
	* [规则：Suspicious.ReadBrowserData](#suspiciousreadbrowserdata)

# Suspicious.ReadBrowserData 规则组

## 规则：Suspicious.ReadBrowserData
  
状态：未启用

源程序`*`做出以下操作时，自动阻止
- 对路径为`*\Users\*\AppData\Local\*\User Data\Default\*`的文件进行读操作
- 对路径为`*\Users\*\AppData\Roaming\Mozilla\Firefox\Profiles\*`的文件进行读操作
  
***rule.json hash: ba1741093a8cab0b165da7ff972ca3fee71478259430ce3d544ac122c6fe87e4***