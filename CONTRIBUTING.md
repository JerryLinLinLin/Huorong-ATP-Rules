# Issues 模板

## 误报反馈

- Win 版本号
- 火绒版本号
- 火绒日志 （打开火绒日志界面，选择对应日志，导出/复制粘贴到此处）
- 截图 （可选）
- 触发场景描述 （可选）

## 功能建议

- 需要什么样的规则，能达到什么样的效果
- 参考链接

# 开发/添加新规则

- 在`rules/`下有子文件夹`Template`，以此为模板添加新规则组。

- 使用此 [Json Schema](https://github.com/JerryLinLinLin/Huorong-HIPS-Rule-Schema) 确保规则文件格式正确

- 规则组命名方式为`威胁类别.行为描述/病毒家族`。目前的威胁类别可分为：
    
    - `Backdoor`
    - `Exploit`
    - `Ransom`
    - `Suspicious`
    - `Trojan`
    - ...

- 当规则组有针对的恶意软件家族时，优先使用恶意软件家族名命名，例如`Trojan.Remcos`代表针对Remcos家族的规则。使用行为描述时，以下词语需要缩写以避免名字过长：
    
    - `System` -> `Sys`
    - `Process` -> `Proc`
    - `Suspicious` -> `Susp`
    - `Malicious` -> `Mal`
    - ...

- 每条规则的命名方式为`规则组名.[A-Z]`。

- 例外项/自动处理规则请添加在对应的`auto.json`文件内。

- 添加完新规则组后请运行`md_parser.py` 生成对应规则文档。TO-DO: Add to CI
