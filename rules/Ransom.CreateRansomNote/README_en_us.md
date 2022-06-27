



Contents
========

* [Ransom.CreateRansomNote](#ransomcreateransomnote)
	* [Ransom.CreateRansomNote.A](#ransomcreateransomnotea)

# Ransom.CreateRansomNote

## Ransom.CreateRansomNote.A
  
Status: Enabled  
Behavioral Description: 

When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create` the file under the path `>\ProgramData\>.txt`
- `Create` the file under the path `>\Program Files (x86)\>.txt`
- `Create` the file under the path `>\Users\*\AppData\Local\>.txt`
- `Create` the file under the path `>\Users\*\AppData\>.txt`
- `Create` the file under the path `>\Program Files\>.txt`
  
***rule.json hash: c2c8db5cd47d81f8a5f0d961cc8c86cd9bf327106b678a8370b38d6e50963444***