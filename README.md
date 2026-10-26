# Patent Disclosure Drafting Skill

[![Validation](https://img.shields.io/github/actions/workflow/status/PDBen-Auto/patent-disclosure-drafting-skill/validate.yml?branch=main&style=flat-square&label=validation)](https://github.com/PDBen-Auto/patent-disclosure-drafting-skill/actions/workflows/validate.yml)
[![License](https://img.shields.io/badge/license-source--available-59636e?style=flat-square)](LICENSE)

把产品图片、结构说明、草图、CAD视图或访谈笔记整理成可供专利代理师审查的技术交底包。

## 解决什么问题

专利起草前最容易出现的断点不是“不会写句子”，而是：

- 外观设计和结构方案混在一份叙述里，保护路线不清；
- 部件、连接关系和附图编号不稳定，代理师需要反复返工；
- 方案里的推测被写成事实，尺寸、材料、测试结果和技术效果缺少证据；
- 内部案例直接拿去公开，泄露真实产品、文件名、人员、供应商或未公开策略。

这个 Skill 把输入资料变成证据台账、技术交底、外观设计交底、附图目录、部件编号表、开放问题和代理师交接清单，并提供公开合成案例工作流。

## 和普通模板的差异

| 普通做法 | 常见问题 | 本 Skill 的处理 |
| --- | --- | --- |
| 直接让 AI 写一篇“专利说明书” | 事实、推测和拟议保护范围混在一起 | 先建证据台账，再分路线起草 |
| 只列产品功能 | 没有可复核的连接关系和附图覆盖 | 部件编号、连接、图号和文字交叉校验 |
| 只写外观或只写结构 | 组合产品容易漏掉另一条保护路线 | 外观设计与实用新型/实用专利分流 |
| 用原始项目做公开演示 | 泄露项目、公司、人员或未公开策略 | 新建完全虚构的合成案例并做发布审计 |
| 把结果当成“可直接申请” | 可能造成法律和商业误判 | 明确是代理师审查前的技术交底草案 |

## 适合谁

产品经理、工业设计师、研发工程师、供应链团队、创业者，以及需要把产品资料交给专利代理师的项目负责人。

## 安装

```bash
npx skills add PDBen-Auto/patent-disclosure-drafting-skill --skill patent-disclosure-drafting
```

也可以从 [GitHub Releases](https://github.com/PDBen-Auto/patent-disclosure-drafting-skill/releases/latest) 下载 ZIP，解压后将 `patent-disclosure-drafting` 目录放入 Codex 用户 Skill 目录。

显式调用：

```text
$patent-disclosure-drafting
```

## 使用方式

### 外观设计 + 实用新型组合交底

```text
请根据产品图片、结构说明和装配关系，分别整理外观设计交底书与实用新型技术交底书。请先建立证据台账，再给出部件编号、附图目录、连接关系、可选实施方式、缺失信息和代理师审查问题。所有不确定内容标为 unknown 或待确认。
```

### 附图和编号复核

```text
请检查这组专利附图的 Fig. 1-Fig. 6、部件编号和文字说明是否一致，列出冲突、缺失视图和需要代理师决定的线型问题，不要替我判断是否授权。
```

### 公开合成案例

```text
请把这个内部专利起草流程提炼成公开案例，但不要使用原项目名称、文件、图片、尺寸、人员、公司、供应商或真实专利策略。请改成一个完全虚构的类似产品，并附上脱敏审计记录。
```

## 输出内容

- 起草状态与范围说明；
- 证据台账；
- 技术问题、方案、部件、连接、动作和技术效果；
- 外观设计的整体视觉和视图清单；
- Fig. 1 起的附图目录和来源；
- 部件参考编号表；
- 非最终的保护重点和代理师问题；
- 缺失信息、矛盾信息和下一步验证；
- 公开模式下的合成案例和脱敏审计。

## 合成案例

仓库中的案例是“模块化桌面灯壳体”，产品、部件、数字和文字均为虚构，仅用于演示如何把外观设计与技术结构分开、如何组织附图和参考编号，以及如何保留代理师审查边界。案例不对应真实品牌、供应商、专利或历史项目。

## 重要边界

本项目输出的是技术交底和代理师审查前的整理材料，不是律师意见、正式 FTO、授权保证、侵权结论或自动提交服务。最终的保护范围、新颖性/创造性判断、发明人和申请人确认、附图合规、翻译和递交必须由有资质的专利代理师或律师审查。

## 公开发布边界

不要把真实客户、供应商、未公开申请、平台投诉、原始 CAD、PPT、工程图、账号信息或凭据放进公开仓库。来源证明文件只用于版本和作者核验，不包含隐藏指令、追踪回调或影响 Skill 行为的后门。

## Search terms

`patent disclosure drafting`, `patent technical disclosure`, `design patent disclosure`, `utility model disclosure`, `utility patent invention disclosure`, `patent figure numbering`, `reference numeral table`, `patent agent handoff`, `anonymized patent case`, `专利技术交底书`, `专利文件起草`, `外观设计交底`, `实用新型交底`, `专利附图编号`, `部件编号`, `代理师交接`, `专利案例脱敏`

## Related skill

如果任务重点是寻找已有外观设计、解释设计权范围或生成设计规避方向，请使用 [design-patent-search-and-design-around](https://github.com/PDBen-Auto/design-patent-design-around-skill)。本仓库负责“把产品资料整理成专利交底”，不负责替代检索和正式法律意见。

## Validation

```powershell
python tests/test_skill_structure.py
python tests/test_anonymized_example.py
python -X utf8 <path-to-skill-creator>/scripts/quick_validate.py .
```

## License

见 [LICENSE](LICENSE)。默认是保留所有权利的 source-available 发布。若需要开放修改和再发布，请在发布前替换为明确的开源许可证。
