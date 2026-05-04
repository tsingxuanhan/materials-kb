# SFT数据集格式

## Alpaca格式

```json
{
  "instruction": "请介绍钙钛矿结构",
  "input": "",
  "output": "钙钛矿（Perovskite）是一种具有ABX₃化学式的晶体结构..."
}
```

字段：
- `instruction`(必填): 指令/问题
- `input`(可选): 附加上下文
- `output`(必填): 期望回答

## ShareGPT格式

```json
{
  "conversations": [
    {"from": "human", "value": "什么是固溶体？"},
    {"from": "gpt", "value": "固溶体（Solid Solution）是..."},
    {"from": "human", "value": "和化合物有什么区别？"},
    {"from": "gpt", "value": "区别在于..."}
  ]
}
```

## 质量检查

- [ ] output > 50字符
- [ ] 无重复instruction
- [ ] 无HTML标签
- [ ] 术语拼写正确
- [ ] 中英混排一致
