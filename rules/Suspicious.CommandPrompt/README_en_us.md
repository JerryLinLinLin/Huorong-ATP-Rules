


  
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
  
***rule.json hash: ac6da01e160cfb9848cec158ee41f935786a5413aadca2f4bb2c9ef66fcce2cd***