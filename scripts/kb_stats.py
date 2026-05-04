#!/usr/bin/env python3
"""KB统计分析脚本 — 生成知识库统计报告"""
import os
import re
from pathlib import Path
from collections import defaultdict

KB_DIR = Path(__file__).parent.parent

def analyze_file(filepath):
    """分析单个KB文件"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')

    stats = {
        'lines': len(lines),
        'chars': len(content),
        'headings': len(re.findall(r'^#+\s', content, re.MULTILINE)),
        'paper_refs': len(re.findall(r'\[.*?\]\(https?://', content)),
        'code_blocks': len(re.findall(r'```', content)) // 2,
        'tables': len(re.findall(r'^\|.*\|$', content, re.MULTILINE)),
        'inline_code': len(re.findall(r'`[^`]+`', content)),
    }
    return stats

def main():
    kb_stats = defaultdict(lambda: {'files': 0, 'lines': 0, 'chars': 0, 'papers': 0})

    for md_file in sorted(KB_DIR.glob("**/*.md")):
        kb_name = md_file.parts[-2] if md_file.parts[-2] != 'scripts' and md_file.parts[-2] != 'fine-tune' else md_file.stem
        rel = str(md_file.relative_to(KB_DIR))
        s = analyze_file(md_file)

        kb_stats[kb_name]['files'] += 1
        kb_stats[kb_name]['lines'] += s['lines']
        kb_stats[kb_name]['chars'] += s['chars']
        kb_stats[kb_name]['papers'] += s['paper_refs']

    print("# 知识库统计报告\n")
    print("| KB | 文件数 | 总行数 | 总字符 | 论文引用 |")
    print("|-----|--------|--------|--------|----------|")

    total_files = total_lines = total_chars = total_papers = 0
    for kb_name in sorted(kb_stats.keys()):
        s = kb_stats[kb_name]
        print(f"| {kb_name} | {s['files']} | {s['lines']} | {s['chars']} | {s['papers']} |")
        total_files += s['files']
        total_lines += s['lines']
        total_chars += s['chars']
        total_papers += s['papers']

    print(f"| **总计** | **{total_files}** | **{total_lines}** | **{total_chars}** | **{total_papers}** |")

if __name__ == '__main__':
    main()
