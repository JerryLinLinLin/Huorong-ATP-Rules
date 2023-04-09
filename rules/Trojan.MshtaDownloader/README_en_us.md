



Contents
========

* [Trojan.MshtaDownloader](#trojanmshtadownloader)
	* [Trojan.MshtaDownloader.A](#trojanmshtadownloadera)

# Trojan.MshtaDownloader

## Trojan.MshtaDownloader.A
  
Status: Enabled

Behavioral Description:   
When the source process`*\mshta.exe`initializes the following actions, HIPS module should let the user decide them.
- `Execute` the program under the path `*\Windows\Sys?????\*.exe`
- `Create` the file under the path `*.exe`
- `Create` the file under the path `*.dll`
- `Execute` the program under the path `*\Users\*\AppData\*`
  
***rule.json hash: 9af5a10aba8688c0759a59db43479ddd32558715cf3b6905531d9ef484e924a7***  
[简体中文](/README.md) | English