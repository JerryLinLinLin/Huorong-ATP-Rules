


  
简体中文 | [繁體中文](README_zh_tw.md) | [English](README_en_us.md)  
  

目录
==

* [Suspicious.NetDebugger](#suspiciousnetdebugger)
	* [Suspicious.NetDebugger.A](#suspiciousnetdebuggera)

# Suspicious.NetDebugger

## Suspicious.NetDebugger.A
  
状态：启用

行为描述：源程序`*`做出以下操作时，提示用户处理
- 对路径为`*\SOFTWARE*Microsoft\.NETFramework\DbgManagedDebugge*`的注册表进行`创建、写入`操作
  
***rule.json hash: 8dafeaa565c7c02bff7bc9dd9a27155f95ad5958d3259a576797ea797fafb0c8***