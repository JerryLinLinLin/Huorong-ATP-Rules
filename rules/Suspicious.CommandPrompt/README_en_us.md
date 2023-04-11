


  
[简体中文](README.md) | [繁體中文](README_zh_tw.md) | English  
  

Contents
========

* [Suspicious.CommandPrompt](#suspiciouscommandprompt)
	* [Suspicious.CommandPrompt.A](#suspiciouscommandprompta)

# Suspicious.CommandPrompt

## Suspicious.CommandPrompt.A
  
Status: Enabled

Behavioral Description:   
When the source process`*\cmd.exe`initializes the following actions, HIPS module should let the user decide them.
- `Execute` the program under the path `*\?script.exe`
- `Create` the file under the path `*.exe`
- `Create` the file under the path `*.vb?`
- `Create` the file under the path `*.js`
  
***rule.json hash: e62bc0757952c536054b872cac6a0ab7773edb697cd0a32dc824ab4246d53190***