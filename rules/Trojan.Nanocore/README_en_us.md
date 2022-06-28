



Contents
========

* [Trojan.Nanocore](#trojannanocore)
	* [Trojan.Nanocore](#trojannanocore)

# Trojan.Nanocore

## Trojan.Nanocore
  
Status: Disabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should automatically block them.
- `Create` the file under the path `*\Users\*\AppData\Roaming\>\run.dat`
  
***rule.json hash: 8e0a16afc7e1b262b59238b529e2188d8bb0750bf737f2b2f764683394bd005d***