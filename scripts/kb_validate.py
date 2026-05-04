#!/usr/bin/env python3
"""KB格式校验脚本 — 检查知识库文件格式是否规范"""
import os
import sys
import re
from pathlib import Path

KB_DIR = Path(__file__).parent.parent

def check_file(filepath):
    """检查单个KB文件"""
    errors = []
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')

    # 检查空文件
    if len(content.strip()) == 0:
        errors.append("空文件")
        return errors

    # 检查是否有标题
    if not re.search(r'^#+\s', content, re.MULTILINE):
        errors.append("缺少Markdown标题")

    # 检查常见格式问题
    for i, line in enumerate(lines, 1):
        if '\t' in line:
            errors.append(f"L{i}: 含Tab缩进，应用空格")
        if line.rstrip() != line:
            if line.strip() != '':
                errors.append(f"L{i}: 行尾多余空格")

    return errors

def main():
    md_files = list(KB_DIR.glob("**/*.md"))
    total_errors = 0

    for f in sorted(md_files):
        rel = f.relative_to(KB_DIR)
        errs = check_file(f)
        if errs:
            print(f"❌ {rel}")
            for e in errs:
                print(f"   {e}")
            total_errors += len(errs)
        else:
            print(f"✅ {rel}")

    print(f"\n检查完成: {len(md_files)}文件, {total_errors}错误")
    sys.exit(1 if total_errors > 0 else 0)

if __name__ == '__main__':
    main()
