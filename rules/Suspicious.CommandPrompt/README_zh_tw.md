


  
[简体中文](README.md) | 繁體中文 | [English](README_en_us.md)  
  

目錄
==

* [Suspicious.CommandPrompt](#suspiciouscommandprompt)
	* [Suspicious.CommandPrompt.A](#suspiciouscommandprompta)

# Suspicious.CommandPrompt

## Suspicious.CommandPrompt.A
  
狀態：啟用

行為描述：源程式`*\cmd.exe`做出以下操作時，提示使用者處理
- 對路徑為`*\?script.exe`的程序進行`執行`操作
- 對路徑為`*.exe`的文件進行`建立`操作
- 對路徑為`*.vb?`的文件進行`建立`操作
- 對路徑為`*.js`的文件進行`建立`操作
  
***rule.json hash: ac6da01e160cfb9848cec158ee41f935786a5413aadca2f4bb2c9ef66fcce2cd***