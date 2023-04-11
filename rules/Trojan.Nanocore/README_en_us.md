


  
[简体中文](README.md) | [繁體中文](README_zh_tw.md) | English  
  

Contents
========

* [Trojan.Nanocore](#trojannanocore)
	* [Trojan.Nanocore.A](#trojannanocorea)

# Trojan.Nanocore

## Trojan.Nanocore.A
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create` the file under the path `*\Users\*\AppData\Roaming\>\run.dat`
  
***rule.json hash: 7b2e1d410b22e9086de4bfa8882b43796c60fbe5efb2bd8af010d7fafd0893ca***