# coding: utf-8

import random
import time
import nltk
from nltk.corpus import words

nltk.data.path.append("nltk")
word_list = words.words()
ansi_colors = [
    "\033[38;2;255;0;0m",  # Red
    "\033[38;2;255;255;255m",  # White
    "\033[38;2;0;128;0m",  # Green
    ""
]

while True:
    try:
        word_str = ''
        for _ in range(random.randint(3, 8)):
            word = word_list[random.randint(0, len(word_list) - 1)]
            word_str += word + ' '
        word_str = word_str.strip()
        word_str += "."
        word_str = word_str[0].upper() + word_str[1:]
        word_str = f'{ansi_colors[random.randint(0, len(ansi_colors) - 1)]}{word_str}'
        print(word_str)
        time.sleep(random.uniform(0.02, 0.8))
    except KeyboardInterrupt:
        break
