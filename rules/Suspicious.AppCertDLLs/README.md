



目录
==

* [Suspicious.AppCertDLLs](#suspiciousappcertdlls)
	* [Suspicious.AppCertDLLs.A](#suspiciousappcertdllsa)

# Suspicious.AppCertDLLs

## Suspicious.AppCertDLLs.A
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\System\CurrentControlSet\Control\Session Manager\AppCertDLLs\*`的注册表进行**创建、写入**操作
  
***rule.json hash: ca1f6ff9981726324e729b6e012c879a6f839b30a95eebb4f756792da9773ccd***