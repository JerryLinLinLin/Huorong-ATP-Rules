- [开发/添加新规则](#开发添加新规则)
- [Development/Adding New Rules](#development-adding-new-rules)

# 开发/添加新规则

- 在`rules/`下有子文件夹`Template`，以此为模板添加新规则组。

- 使用此 [Json Schema](https://github.com/JerryLinLinLin/Huorong-HIPS-Rule-Schema) 确保规则文件格式正确

- 规则组命名方式为`威胁类别.行为描述/病毒家族`。目前的威胁类别可分为：
    
    - `Backdoor`
    - `Exploit`
    - `Ransom`
    - `Suspicious`
    - `Trojan`
    - `Telmetry`
    - ...

- 当规则组有针对的恶意软件家族时，优先使用恶意软件家族名命名，例如`Trojan.Remcos`代表针对Remcos家族的规则。使用行为描述时，以下词语需要缩写以避免名字过长：
    
    - `System` -> `Sys`
    - `Process` -> `Proc`
    - `Suspicious` -> `Susp`
    - `Malicious` -> `Mal`
    - ...

- 每条规则的命名方式为`规则组名.[A-Z]`。

- 例外项/自动处理规则请添加在对应的`auto.json`文件内。

- Telemetry 为遥测组别，默认不开启。

- 添加完新规则组后请运行Github Actions `Generate Documentation` 生成对应规则文档。

# Development/Adding New Rules

- Under `rules/` there is a subfolder `Template`, use this as a template to add new rule groups.

- Use this [Json Schema](https://github.com/JerryLinLinLin/Huorong-HIPS-Rule-Schema) to ensure that rule files are properly formatted

- The rule group naming scheme is `Threat Category. Behavior description/virus family`. The current threat categories can be classified as

  - `Backdoor`
  - `Exploit`
  - `Ransom`
  - `Suspicious`
  - `Trojan`
  - `Telmetry`
  - ...

- When a rule group has a malware family to target, the name of the malware family is preferred, e.g. `Trojan.Remcos` stands for a rule targeting the Remcos family. When using behavior descriptions, the following terms need to be abbreviated to avoid long names.

  - `System` -> `Sys`
  - `Process` -> `Proc`
  - `Suspicious` -> `Susp`
  - `Malicious` -> `Mal`
  - ...

- Each rule is named by the `rule group name. [A-Z]`.

- Exceptions/automatic rules should be added in the corresponding `auto.json` file.

- Telemetry rule group is not enabled by default.

- After adding the new rule group, please run Github Actions `Generate Documentation` to generate the corresponding rule file. 

