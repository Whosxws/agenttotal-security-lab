# 固定版本扫描入口

主样例内容固定提交：`0cb96a276cd2db39bd207adcb2fabaa61d40df26`。后续说明更新不会改变这些地址指向的实验材料。

## Skill：可直接提交的子目录地址

| 输入 | 固定地址 |
|---|---|
| S1 | https://github.com/Whosxws/agenttotal-security-lab/tree/0cb96a276cd2db39bd207adcb2fabaa61d40df26/skills/S1 |
| S2 | https://github.com/Whosxws/agenttotal-security-lab/tree/0cb96a276cd2db39bd207adcb2fabaa61d40df26/skills/S2 |
| S3 | https://github.com/Whosxws/agenttotal-security-lab/tree/0cb96a276cd2db39bd207adcb2fabaa61d40df26/skills/S3 |
| S4 仅说明 | https://github.com/Whosxws/agenttotal-security-lab/tree/0cb96a276cd2db39bd207adcb2fabaa61d40df26/skills/S4-description |
| S4 完整包 | https://github.com/Whosxws/agenttotal-security-lab/tree/0cb96a276cd2db39bd207adcb2fabaa61d40df26/skills/S4-package |
| R3 | https://github.com/Whosxws/agenttotal-security-lab/tree/0cb96a276cd2db39bd207adcb2fabaa61d40df26/real-skills/R3 |
| R4 | https://github.com/Whosxws/agenttotal-security-lab/tree/0cb96a276cd2db39bd207adcb2fabaa61d40df26/real-skills/R4 |

选择 Skill 仓库入口；本轮使用 Cisco Skill、AgentVerus、Caterpillar 静态模式。不要提交 main 整仓再把总告警数当成 S1 结果。

## MCP 源码：隔离分支

| 样例 | 分支 | 固定提交 | 来源 |
|---|---|---|---|
| M5 | sample-m5 | d118198525c61e9312b04b50e809674f90c9e0cb | 仅 mcp/source/M5 内容 |
| M6 | sample-m6 | 292015e19a6c0940a27cfdbe7fc95f896a823d90 | 仅 mcp/source/M6 内容 |
| R1 | sample-r1 | 3014afcb1360f8ed12c00f461444b29ec5efef2f | upstash/context7 b250c2515694eee4b6df4db82fa056df9ed3e306 文件内容 |
| R2 | sample-r2 | 65cbb2a0eb222596e4ca1eb2463ee694576a5e04 | microsoft/playwright-mcp 55679f5f3d4b4f3e2534ec0ce2fc5683ba2eaf3f 文件内容 |

R1/R2 分支是上游归档文件内容的重新提交，**本仓库提交 SHA 不等于上游提交 SHA**；内容逐文件核对，保留上游许可，未运行项目。Git 可执行位等元数据不用于声称完整 Git 历史等同。

本次平台 MCP 仓库入口只接受仓库根地址，不能直接指定分支/子目录。实验时逐个将本仓库默认分支设为目标分支，再提交根地址，等任务完成并核对 Item 中的 revision 后才切换下一分支。全部完成后默认分支恢复 main。每次只有目标材料进入源码扫描。

因此，**当前直接扫描本仓库根地址会扫描 main 的混合内容，并不重现 M5/M6/R1/R2 单样例实验**。后续可用 archives 中的单样例 ZIP（需平台上传流程可用），或按上述串行流程由仓库所有者切换默认分支。不要在任务仍排队时切换默认分支。

## MCP JSON

M1/M2/M3 使用 mcp/snapshots 中的 JSON 内容；M4 使用 mcp/configs/M4.json。JSON 模式与仓库源码模式检测对象不同，不以源码扫描替代描述/启动配置检查。
