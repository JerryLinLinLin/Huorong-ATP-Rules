



Contents
========

* [Suspicious.ReadBrowserData](#suspiciousreadbrowserdata)
	* [Suspicious.ReadBrowserData.A](#suspiciousreadbrowserdataa)

# Suspicious.ReadBrowserData

## Suspicious.ReadBrowserData.A
  
Status: Disabled

Behavioral Description: When the source process`*`initializes the following actions, HIPS module should automatically block.
- `Read` the file under the path `*\Users\*\AppData\Local\*\User Data\Default\*`
- `Read` the file under the path `*\Users\*\AppData\Roaming\Mozilla\Firefox\Profiles\*`
  
***rule.json hash: f9af5aadaebe552fe3df866cf91edf2744eaea4da3fd2f29dba025b48996d057***