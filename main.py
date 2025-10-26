# coding: utf-8

import random
import time
import nltk
import argparse
import hashlib
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
mode = args.mode

def wait_cartoon(head: str, content: str, min_time=0.001, max_time=0.2):
    times = random.randint(1, 8)
    ascii_cartoon_char = ["|", "/", "_", "\\"]
    for i in range(1, 3):
        for j in range(1, 5):
            if i*j >= times:
                print(f"\r{head} {content} success.")
                return
            print(f"\r{head} {content} {ascii_cartoon_char[j-1]}", end='')
            time.sleep(random.uniform(min_time, max_time))

# 输出字符串
while True:
    try:
        if mode == 0:
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
        elif mode == 1:
            input_str = ''
            input_mode = random.randint(1, 4)

            for _ in range(random.randint(50, 200)):
                if input_mode == 1:
                    wait_cartoon("Download:", word_list[random.randint(0, len(word_list) - 1)])
                elif input_mode == 2:
                    wait_cartoon("Update", word_list[random.randint(0, len(word_list) - 1)])
                elif input_mode == 3:
                    print(f"Delete: sha256:{''.join(random.choice('0123456789abcdef') for _ in range(64))}")
                elif input_mode == 4:
                    mid = random.randint(1, 3)
                    if mid == 1:
                        wait_cartoon("Download:", word_list[random.randint(0, len(word_list) - 1)])
                    elif mid == 2:
                        wait_cartoon("Update", word_list[random.randint(0, len(word_list) - 1)])
                    elif mid == 3:
                        print(f"Delete: sha256:{''.join(random.choice('0123456789abcdef') for _ in range(64))}")

                time.sleep(random.uniform(0.02, 0.5))

    except KeyboardInterrupt:
        break
