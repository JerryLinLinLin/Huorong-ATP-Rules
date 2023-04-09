



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
  
***rule.json hash: ac6da01e160cfb9848cec158ee41f935786a5413aadca2f4bb2c9ef66fcce2cd***  
简体中文 | [English](/README_en_us.md)