# File Manifest · 文件清单

[English](README.md) | 简体中文

交付前确认文件到底有哪些、哪些内容重复。选定本地目录下的文件，工具会记录大小、SHA-256 和重复分组，便于收件人核对。

[下载 v0.2.1](https://github.com/KarmenLoop/skill-file-manifest/releases/tag/v0.2.1) · [完整教程](docs/tutorial.zh-CN.md) · [输入参考](docs/input.zh-CN.md) · [反馈问题](https://github.com/KarmenLoop/skill-file-manifest/issues)

## 能做什么

brief.txt 与 copy.txt 的字节内容相同，因此样例会把两个路径放进同一重复分组。

文件只在本地读取，不会上传、重命名、删除或替你决定保留哪个副本；含符号链接的路径会被拒绝。

![文件清单 0.2.1 版本样例的真实 JSON 输出](docs/images/example-output-v0.2.1.svg)

*图片来自 v0.2.1 的真实本地输出，采用英文键名；[完整结果](examples/expected.json) · [图片来源记录](docs/images/provenance.json)。*

## 开始使用

在发行页下载 `karmen-file-manifest-v0.2.1.zip` 与对应 `.sha256` 文件，核对哈希后解压。在解压目录中使用 Python 3.9 或更新版本：

```sh
python3 scripts/run.py --version
python3 scripts/run.py --input examples/input.json
```

预期版本：`karmen-file-manifest 0.2.1`。brief.txt 与 copy.txt 的字节内容相同，因此样例会把两个路径放进同一重复分组。

如果宿主读取 `~/.agents/skills`，可安装完整技能：

```sh
python3 install.py --host agents
```

目标目录已存在时安装器会拒绝覆盖。宿主发现和调用方式可能不同，见[安装与实践教程](docs/tutorial.zh-CN.md)。不使用 AI 宿主也能直接运行本地工具。

## 用于自己的任务

root 填写要检查的目录，paths 明确列出目录内的相对文件路径；使用真实文件，不使用符号链接。

修改副本后重新生成清单，比较哈希，区分“只是换了名字”与“内容已改变”。任何手动清理前先审阅重复分组。

准备新输入前可查看[字段约定](docs/input.zh-CN.md)。工具只依赖 Python 标准库，本身不需要模型账号、API 密钥或网络。使用 AI 宿主时，宿主有自己的数据与权限设置。

## 常见问题

**哈希相同就说明下载可信吗？** 它只能证明字节与该哈希一致。预期哈希本身应来自可信来源，不能据此证明作者身份或安全性。

**结果保存在哪里？** 默认向终端输出 JSON；使用 `--output` 时只创建新文件，已有输出文件会保留。工具只读取提交的记录和输入约定中明确列出的本地路径。

## 文档与支持

- [下载、安装、配置、练习、升级与卸载](docs/tutorial.zh-CN.md)
- [输入输出约定](docs/input.zh-CN.md)与[兼容性说明](docs/COMPATIBILITY.md)（英文参考）
- [更新记录](CHANGELOG.md)、[参与贡献](CONTRIBUTING.md)、[支持](SUPPORT.md)和[安全反馈](SECURITY.md)

## 许可证

[MIT](LICENSE)。再分发时保留许可证和[声明](NOTICE.md)。由 [KarmenLoop](https://karmenloop.com) 维护。
