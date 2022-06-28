



Contents
========

* [Suspicious.ReadBrowserData](#suspiciousreadbrowserdata)
	* [Suspicious.ReadBrowserData.A](#suspiciousreadbrowserdataa)

# Suspicious.ReadBrowserData

## Suspicious.ReadBrowserData.A
  
Status: Disabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Read` the file under the path `*\Users\*\AppData\Local\*\User Data\Default\*`
- `Read` the file under the path `*\Users\*\AppData\Roaming\Mozilla\Firefox\Profiles\*`
  
***rule.json hash: d13b8a311d712501d84b1645052ed84e506624c200a1f8a05ae649e07d258e76***