


  
[简体中文](README.md) | 繁體中文 | [English](README_en_us.md)  
  

目錄
==

* [Suspicious.NetDebugger](#suspiciousnetdebugger)
	* [Suspicious.NetDebugger.A](#suspiciousnetdebuggera)

# Suspicious.NetDebugger

## Suspicious.NetDebugger.A
  
狀態：啟用

行為描述：源程式`*`做出以下操作時，提示使用者處理
- 對路徑為`*\SOFTWARE*Microsoft\.NETFramework\DbgManagedDebugge*`的注册表進行`创建、写入`操作
  
***rule.json hash: 8dafeaa565c7c02bff7bc9dd9a27155f95ad5958d3259a576797ea797fafb0c8***