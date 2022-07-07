



目录
==

* [Suspicious.AppCertDLLs](#suspiciousappcertdlls)
	* [Suspicious.AppCertDLLs.A](#suspiciousappcertdllsa)

# Suspicious.AppCertDLLs

## Suspicious.AppCertDLLs.A
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\System\CurrentControlSet\Control\Session Manager\*`的注册表进行**创建、写入**操作
  
***rule.json hash: 5374f45048ea16f29e3ac22fc5e64ba6e5e655511033ac8d58ef78c8f8558e7e***