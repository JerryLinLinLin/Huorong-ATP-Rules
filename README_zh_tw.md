[简体中文](/README.md) | 繁體中文 | [English](/README_en_us.md)

<h1 align="center">火絨高階威脅防護規則</h1>

<div align="center">
  
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/JerryLinLinLin/Huorong-ATP-Rules)](https://github.com/JerryLinLinLin/Huorong-ATP-Rules/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/JerryLinLinLin/Huorong-ATP-Rules)](https://github.com/JerryLinLinLin/Huorong-ATP-Rules/pulls)
[![License](https://img.shields.io/github/license/JerryLinLinLin/Huorong-ATP-Rules)](/LICENSE)

</div>

基於 [MITRE ATT&CK™](https://attack.mitre.org/) 和惡意軟體行為特徵編寫而成的火絨自定義防護規則，能夠檢測，阻止，攔截各類惡意軟體，[高階持續性威脅（APT）](https://zh.m.wikipedia.org/zh-hans/%E9%AB%98%E7%BA%A7%E9%95%BF%E6%9C%9F%E5%A8%81%E8%83%81)的攻擊載體和攻擊途徑，典型的如無檔案攻擊，漏洞攻擊，加密勒索等。同時具有較高的可擴充套件性和可維護性，對社群開發者友好。

- [安裝/匯入規則](#安裝匯入規則)
- [新手上路](#新手上路)
- [規則內容](#規則內容)
- [規則目錄](#規則目錄)
- [自動化指令碼](#自動化指令碼)
- [更新日誌](#更新日誌)
- [反饋/貢獻](#反饋貢獻)

## 安裝/匯入規則

下載[最新規則版本](https://github.com/JerryLinLinLin/Huorong-ATP-Rules/releases/latest)，解壓檔案可得`Rule.json`, `Auto.json`。開啟火絨主介面->防護中心->高階防護->自定義規則，點選開關啟用，點選專案->進入高階防護設定項，在自定義規則設定介面->匯入->選擇`Rule.json`，在自動處理設定頁面->匯入->選擇`Auto.json`。

版本更新時請手動刪除舊規則然後重新匯入。

## 新手上路

按照[此圖](images/import_rules.jpg)所示匯入規則。

為防止誤報，部分規則預設未啟用，請在閱讀規則文件後再選擇開啟。

## 規則內容

- Office 漏洞攻擊防護
- 勒索防護
- 無檔案攻擊防護
- 流行惡意軟體家族防護
- [...詳見規則文件](/rules/README.md)

## 規則目錄

所有規則位於`rules/`目錄下，子資料夾代表不同規則組，以`威脅類別.行為描述/病毒家族`命名，例如`Exploit.MSOffice`。

每個子目錄下含有規則檔案`rule.json`、`auto.json`，為當前規則組的規則檔案和對應的自動處理檔案。每項規則以`當前規則組名稱+字母`命名，例如`Exploit.MSOffice`。

每條規則的具體用途可在各規則組資料夾下`README.md`找到，或在`Rules`根目錄下找到。

目錄結構如下

```
.
├── Classification.Description1
├── Classification.Description2
│   ├── rule.json
│   ├── auto.json
│   └── README.md
└── README.md
```

## 自動化指令碼

位於`scripts/`目錄下，用於自動檢查規則檔案格式、匯出/合併所有規則組，生成規則說明文件等，僅限於此規則目錄結構。

- `validate_rules.py` - 驗證規則檔案，基於此[schema](https://github.com/JerryLinLinLin/Huorong-HIPS-Rule-Schema)

```
usage: validate_rules.py [-h] --path PATH

optional arguments:
  -h, --help   show this help message and exit
  --path PATH  folder path to check
```

- `merge_rules.py` - 將規則組合併為一個檔案，方便匯入。

```
usage: merge_rules.py [-h] --path PATH --output OUTPUT

optional arguments:
  -h, --help       show this help message and exit
  --path PATH      rule folder path to merge
  --output OUTPUT  output folder path
```

- `md_parser.py` - 生成規則文件。

```
usage: md_parser.py [-h] --path PATH

optional arguments:
  -h, --help   show this help message and exit
  --path PATH  rule folder path to generate markdown
```

## 更新日誌

詳見每次[釋出日誌](https://github.com/JerryLinLinLin/Huorong-ATP-Rules/releases/latest)

TO-DO: Add changelog.md

## 反饋/貢獻

在開Issues或者PR前，請確保閱讀[contributing guidelines](/CONTRIBUTING.md)。
