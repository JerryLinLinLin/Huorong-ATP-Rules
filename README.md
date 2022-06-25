[English](/README_en_us.md)

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/JerryLinLinLin/Huorong-ATP-Rules)](https://github.com/JerryLinLinLin/Huorong-ATP-Rules/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/JerryLinLinLin/Huorong-ATP-Rules)](https://github.com/JerryLinLinLin/Huorong-ATP-Rules/pulls)
[![License](https://img.shields.io/github/license/JerryLinLinLin/Huorong-ATP-Rules)](/LICENSE)

# 火绒高级威胁防护规则

基于 [MITRE ATT&CK™](https://attack.mitre.org/) 和恶意软件行为特征编写而成的火绒自定义防护规则，能够检测，阻止，拦截各类恶意软件，[高级持续性威胁（APT）](https://zh.m.wikipedia.org/zh-hans/%E9%AB%98%E7%BA%A7%E9%95%BF%E6%9C%9F%E5%A8%81%E8%83%81)的攻击载体和攻击途径，典型的如无文件攻击，漏洞攻击，加密勒索等。

## 安装/导入规则

下载[最新规则版本](https://github.com/JerryLinLinLin/Huorong-ATP-Rules/releases/latest)，解压文件可得`Rule.json`, `Auto.json`。打开火绒主界面->防护中心->高级防护->自定义规则，点击开关启用，点击项目->进入高级防护设置项，在自定义规则设置界面->导入->选择`Rule.json`，在自动处理设置页面->导入->选择`Auto.json`。版本更新时请手动删除旧规则然后重新导入。

## 规则内容

- Office 漏洞攻击防护
- 勒索防护
- 无文件攻击防护
- 流行恶意软件家族防护
- [...](/rule/)

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo.

## 🔧 Running the tests <a name = "tests"></a>

Explain how to run the automated tests for this system.

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## 🎈 Usage <a name="usage"></a>

Add notes about how to use the system.

## 🚀 Deployment <a name = "deployment"></a>

Add additional notes about how to deploy this on a live system.

## ⛏️ Built Using <a name = "built_using"></a>

- [MongoDB](https://www.mongodb.com/) - Database
- [Express](https://expressjs.com/) - Server Framework
- [VueJs](https://vuejs.org/) - Web Framework
- [NodeJs](https://nodejs.org/en/) - Server Environment

## ✍️ Authors <a name = "authors"></a>

- [@kylelobo](https://github.com/kylelobo) - Idea & Initial work

See also the list of [contributors](https://github.com/kylelobo/The-Documentation-Compendium/contributors) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References
