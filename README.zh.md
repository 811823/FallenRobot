# FallenRobot

## 项目简介
FallenRobot 是一个基于 Python 的多功能 Telegram 群组管理机器人，支持丰富的管理、娱乐和工具功能，适合自动化群组管理和互动。

- [English README](README.en.md)

## 主要功能
- 群组管理（踢人、禁言、黑名单、警告等）
- 娱乐互动（真心话大冒险、表情包、情侣配对等）
- 工具服务（翻译、维基百科、谷歌搜索、汇率转换等）
- 支持多种用户分级和权限管理
- 插件化模块扩展

## 快速开始
### 依赖安装
```bash
pip install -r requirements.txt
# 开发环境依赖
pip install -r requirements-dev.txt
```

### 配置
1. 复制 `.env.example` 为 `.env`，并根据实际情况填写：
```
API_ID=xxxx
API_HASH=xxxx
TOKEN=xxxx
OWNER_ID=xxxx
DATABASE_URL=xxxx
...
```
2. 或直接设置环境变量。

### 启动
```bash
python -m FallenRobot
```

## 使用示例
- 在群组中添加机器人，发送 `/help` 查看所有命令
- 管理员可使用 `/ban` `/mute` `/warn` 等命令管理成员
- 普通成员可使用 `/truth` `/dare` `/meme` `/translate` 等娱乐和工具命令

## 常见问题 FAQ
**Q: 如何获取 API_ID 和 API_HASH?**  
A: 访问 [my.telegram.org](https://my.telegram.org/apps) 注册应用获取。

**Q: 启动时报错 TOKEN 无效？**  
A: 请确认 `.env` 文件中的 TOKEN 填写为 @BotFather 获取的 Bot Token。

**Q: 如何自定义模块？**  
A: 在 `FallenRobot/modules/` 目录下新增 Python 文件，参考现有模块实现。

## 贡献指南
1. Fork 本仓库并新建分支
2. 保持代码风格一致，建议使用 `black`、`flake8` 检查
3. 补充必要的类型注解和文档
4. 提交 PR 前请确保通过 pytest 测试
5. 欢迎补充文档、修复 bug、添加新功能

## 安全建议
- 请勿泄露 `.env` 文件和 Bot Token
- 建议为机器人账号开启两步验证
- 定期更新依赖，修复安全漏洞
- 仅添加信任的用户为管理员

## 社区与支持
- Telegram 支持群：[点击加入](https://t.me/DevilsHeavenMF)
- 提交 Issue 或 PR 参与开发

## 多语言
- [English README](README.en.md)

---
如有更多问题，欢迎在 Issue 区留言或加入支持群交流。