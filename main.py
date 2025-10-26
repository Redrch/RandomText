# coding: utf-8

import random
import time
import nltk
import argparse
from nltk.corpus import words

# 添加nltk词库地址
nltk.data.path.append("nltk")
# 获取英文词库
word_list = words.words()
# ANSI转义码
ansi_colors = [
    "\033[38;2;255;0;0m",  # Red
    "\033[38;2;255;255;255m",  # White
    "\033[38;2;0;128;0m",  # Green
    ""
]

# 参数处理
parser = argparse.ArgumentParser(description="参数处理")
parser.add_argument('--mode', '-m', type=int, default=0, help="运行模式")

args = parser.parse_args()

# 输出字符串
while True:
    try:
        if args.mode == 0:
            sentence = ''
            # 生成句子
            for _ in range(random.randint(3, 8)):
                word = word_list[random.randint(0, len(word_list) - 1)]
                sentence += word + ' '
            sentence = sentence.strip()
            # 添加句号
            sentence += "."
            # 首字母大写
            sentence = sentence[0].upper() + sentence[1:]
            # 添加ANSI转义字符
            sentence = f'{ansi_colors[random.randint(0, len(ansi_colors) - 1)]}{sentence}'
            # 输出
            print(sentence)
            # 等待
            time.sleep(random.uniform(0.02, 0.8))
        elif args.mode == 1:
            pass
    except KeyboardInterrupt:
        break
