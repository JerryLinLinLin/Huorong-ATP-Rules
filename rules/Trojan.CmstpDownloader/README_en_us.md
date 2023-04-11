


  
[简体中文](README.md) | [繁體中文](README_zh_tw.md) | English  
  

Contents
========

* [Trojan.CmstpDownloader](#trojancmstpdownloader)
	* [Trojan.CmstpDownloader.A](#trojancmstpdownloadera)

# Trojan.CmstpDownloader

## Trojan.CmstpDownloader.A
  
Status: Enabled

Behavioral Description:   
When the source process`*\cmstp.exe`initializes the following actions, HIPS module should let the user decide them.
- `Create` the file under the path `*.exe`
- `Create` the file under the path `*.dll`
  
***rule.json hash: 11ed30aa824e9ec8efb789c6cf1b0bc5d30030f3732b5b11e6663bb8ee92bf42***