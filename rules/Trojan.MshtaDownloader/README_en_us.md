



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
  
***rule.json hash: 892d5b0994e53705cef82d97b0724d4c867cd9b36181fdb896a680319342e388***