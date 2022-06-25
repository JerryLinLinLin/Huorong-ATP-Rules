



目录
==

* [Suspicious.CommandPrompt 规则组](#suspiciouscommandprompt-)
	* [规则：Suspicious.CommandPrompt.A](#suspiciouscommandprompta)

# Suspicious.CommandPrompt 规则组

## 规则：Suspicious.CommandPrompt.A
  
状态：启用

源程序`*\cmd.exe`做出以下操作时，提示用户处理
- 对路径为`*\?script.exe`的程序进行执行操作
- 对路径为`*.exe`的文件进行创建操作
- 对路径为`*.vb?`的文件进行创建操作
- 对路径为`*.js`的文件进行创建操作
  
***rule.json hash: e62bc0757952c536054b872cac6a0ab7773edb697cd0a32dc824ab4246d53190***