



Contents
========

* [Trojan.NetStealer](#trojannetstealer)
	* [Trojan.NetStealer.A](#trojannetstealera)
	* [Trojan.NetStealer.B](#trojannetstealerb)

# Trojan.NetStealer

## Trojan.NetStealer.A
  
Status: Enabled

Behavioral Description:   
When the source process`*\Windows\Microsoft.NET\Framework\>\>`initializes the following actions, HIPS module should let the user decide them.
- `Create` the file under the path `*.txt`
- `Create` the file under the path `*\Users\*\AppData\Roaming\>\>.ini`
- `Create, Write` the registry under the path `*\Software\Microsoft\Windows\CurrentVersion\Run*`
- `Read` the file under the path `*\Users\*\AppData\Local\*\User Data\Default\*`
- `Read` the file under the path `*\Users\*\AppData\Roaming\Mozilla\Firefox\Profiles\*`

## Trojan.NetStealer.B
  
Status: Enabled

Behavioral Description:   
When the source process`*\Windows\>`initializes the following actions, HIPS module should let the user decide them.
- `Create` the file under the path `*\Users\*\AppData\Roaming\>\>.ini`
  
***rule.json hash: a1dc27a7fe9ba237485ee9bff7e5d1a72d413649aaf9cd82a43b5819c1ff1468***