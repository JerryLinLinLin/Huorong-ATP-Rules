简体中文 | [English](/README_en_us.md)

<h1 align="center">火绒高级威胁防护规则</h1>

<div align="center">
  
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/JerryLinLinLin/Huorong-ATP-Rules)](https://github.com/JerryLinLinLin/Huorong-ATP-Rules/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/JerryLinLinLin/Huorong-ATP-Rules)](https://github.com/JerryLinLinLin/Huorong-ATP-Rules/pulls)
[![License](https://img.shields.io/github/license/JerryLinLinLin/Huorong-ATP-Rules)](/LICENSE)

</div>

基于 [MITRE ATT&CK™](https://attack.mitre.org/) 和恶意软件行为特征编写而成的火绒自定义防护规则，能够检测，阻止，拦截各类恶意软件，[高级持续性威胁（APT）](https://zh.m.wikipedia.org/zh-hans/%E9%AB%98%E7%BA%A7%E9%95%BF%E6%9C%9F%E5%A8%81%E8%83%81)的攻击载体和攻击途径，典型的如无文件攻击，漏洞攻击，加密勒索等。同时具有较高的可扩展性和可维护性，对社区开发者友好。

- [安装/导入规则](#安装导入规则)
- [新手上路](#新手上路)
- [规则内容](#规则内容)
- [规则目录](#规则目录)
- [自动化脚本](#自动化脚本)
- [更新日志](#更新日志)
- [反馈/贡献](#反馈贡献)

## 安装/导入规则

下载[最新规则版本](https://github.com/JerryLinLinLin/Huorong-ATP-Rules/releases/latest)，解压文件可得`Rule.json`, `Auto.json`。打开火绒主界面->防护中心->高级防护->自定义规则，点击开关启用，点击项目->进入高级防护设置项，在自定义规则设置界面->导入->选择`Rule.json`，在自动处理设置页面->导入->选择`Auto.json`。

版本更新时请手动删除旧规则然后重新导入。

## 新手上路

按照[此图](images/import_rules.jpg)所示导入规则。

为防止误报，部分规则默认未启用，请在阅读规则文档后再选择开启。

## 规则内容

- Office 漏洞攻击防护
- 勒索防护
- 无文件攻击防护
- 流行恶意软件家族防护
- [...详见规则文档](/rules/README.md)

## 规则目录

所有规则位于`rules/`目录下，子文件夹代表不同规则组，以`威胁类别.行为描述/病毒家族`命名，例如`Exploit.MSOffice`。

每个子目录下含有规则文件`rule.json`、`auto.json`，为当前规则组的规则文件和对应的自动处理文件。每项规则以`当前规则组名称+字母`命名，例如`Exploit.MSOffice`。

每条规则的具体用途可在各规则组文件夹下`README.md`找到，或在`Rules`根目录下找到。

目录结构如下

```
.
├── Classification.Description1
├── Classification.Description2
│   ├── rule.json
│   ├── auto.json
│   └── README.md
└── README.md
```

## 自动化脚本

位于`scripts/`目录下，用于自动检查规则文件格式、导出/合并所有规则组，生成规则说明文档等，仅限于此规则目录结构。

- `validate_rules.py` - 验证规则文件，基于此[schema](https://github.com/JerryLinLinLin/Huorong-HIPS-Rule-Schema)

```
usage: validate_rules.py [-h] --path PATH

optional arguments:
  -h, --help   show this help message and exit
  --path PATH  folder path to check
```

- `merge_rules.py` - 将规则组合并为一个文件，方便导入。

```
usage: merge_rules.py [-h] --path PATH --output OUTPUT

optional arguments:
  -h, --help       show this help message and exit
  --path PATH      rule folder path to merge
  --output OUTPUT  output folder path
```

- `md_parser.py` - 生成规则文档。

```
usage: md_parser.py [-h] --path PATH

optional arguments:
  -h, --help   show this help message and exit
  --path PATH  rule folder path to generate markdown
```

## 更新日志

详见每次[发布日志](https://github.com/JerryLinLinLin/Huorong-ATP-Rules/releases/latest)

TO-DO: Add changelog.md

## 反馈/贡献

在开Issues或者PR前，请确保阅读[contributing guidelines](/CONTRIBUTING.md)。
