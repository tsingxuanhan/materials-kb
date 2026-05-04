# 从KB提取QA对的方法

## 原理

知识库中每条论文/概念条目都可以转化为一个或多个QA对，用于SFT微调数据集构建。

## 提取策略

### 1. 概念类QA
```
KB条目: "梯度下降（Gradient Descent）是一种迭代优化算法..."
QA: Q="什么是梯度下降？" A="梯度下降（Gradient Descent）是..."
```

### 2. 论文类QA
```
KB条目: "CGCNN使用晶体图卷积网络预测材料性质..."
QA1: Q="CGCNN是什么？" A="CGCNN（Crystal Graph Convolutional Neural Network）..."
QA2: Q="CGCNN的核心创新是什么？" A="CGCNN的核心创新是..."
```

### 3. 对比类QA
```
QA: Q="CGCNN和MEGNet有什么区别？"
A: "CGCNN基于晶体图卷积，MEGNet引入全局状态向量..."
```

## 批量提取流程

```python
import re

def extract_qa_from_kb(kb_file):
    qa_pairs = []
    with open(kb_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 按 ### 分割条目
    entries = content.split('\n### ')
    for entry in entries[1:]:  # 跳过文件头
        title = entry.split('\n')[0].strip()
        body = '\n'.join(entry.split('\n')[1:])

        # 生成QA对
        qa_pairs.append({
            'instruction': f'请介绍{title}',
            'output': body
        })

        # 如果包含"核心创新"，生成对比类QA
        if '核心' in body or '创新' in body:
            qa_pairs.append({
                'instruction': f'{title}的核心创新是什么？',
                'output': extract_innovation(body)
            })

    return qa_pairs
```

## 质量要求

- 每条QA的output ≥ 50字符
- 不生成"What is X?"类过于简单的QA
- 优先提取材料科学特有的概念和方法
- 术语保持中英对照
