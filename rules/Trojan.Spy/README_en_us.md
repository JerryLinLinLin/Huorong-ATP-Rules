



Contents
========

* [Trojan.Spy](#trojanspy)
	* [Trojan.Spy.A](#trojanspya)

# Trojan.Spy

## Trojan.Spy.A
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create` the file under the path `*\ProgramData\*Cookie*.txt`
- `Create` the file under the path `*\Users\*\AppData\Local\Temp\*Cookie*txt`
- `Create` the file under the path `*\Users\*\AppData\Local\>\>\>Cookie>txt`
- `Create` the file under the path `*\Users\*\AppData\Local\>\>screen*png`
- `Read` the file under the path `*\Users\*\AppData\Local\Temp\*cookie*txt`
- `Read` the file under the path `*\Users\*\AppData\Local\Temp\*passowrd*txt`
- `Create` the file under the path `*\Users\*\AppData\Roaming\>\>.jpeg`
  
***rule.json hash: 007f1ee31843571162c95ca83eb42cbc192ccdfe1268363c1a4cd4c96955b914***