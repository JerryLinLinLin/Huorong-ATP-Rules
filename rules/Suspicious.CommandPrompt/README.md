



目录
==

* [Suspicious.CommandPrompt](#suspiciouscommandprompt)
	* [Suspicious.CommandPrompt.A](#suspiciouscommandprompta)

# Suspicious.CommandPrompt

## Suspicious.CommandPrompt.A
  
状态：启用

行为描述：源程序`*\cmd.exe`做出以下操作时，提示用户处理
- 对路径为`*\?script.exe`的程序进行**执行**操作
- 对路径为`*.exe`的文件进行**创建**操作
- 对路径为`*.vb?`的文件进行**创建**操作
- 对路径为`*.js`的文件进行**创建**操作
  
***rule.json hash: e62bc0757952c536054b872cac6a0ab7773edb697cd0a32dc824ab4246d53190***