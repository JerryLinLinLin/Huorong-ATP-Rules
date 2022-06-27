



Contents
========

* [Ransom.DoubleExt](#ransomdoubleext)
	* [Ransom.DoubleExt.A](#ransomdoubleexta)
	* [Ransom.DoubleExt.B](#ransomdoubleextb)

# Ransom.DoubleExt

## Ransom.DoubleExt.A
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create` the file under the path `*.docx.>`
- `Create` the file under the path `*.xlsx.>`
- `Create` the file under the path `*.pptx.>`
- `Create` the file under the path `*.doc.>`
- `Create` the file under the path `*.xls.>`
- `Create` the file under the path `*.ppt.>`

## Ransom.DoubleExt.B
  
Status: Enabled

Behavioral Description:   
When the source process`*`initializes the following actions, HIPS module should let the user decide them.
- `Create` the file under the path `>\Users\>\Pictures\*.jpg.>`
- `Create` the file under the path `>\Users\>\Pictures\*.png.>`
- `Create` the file under the path `>\Users\>\Desktop\*.jpg.>`
- `Create` the file under the path `>\Users\>\Desktop\*.png.>`
  
***rule.json hash: e5f5fd0249fcb5415f8445a356cf9b8d1b081981b6bbe3ce8d4e7b3052fd799a***