import os

cates = ['quiz', 'enroll', 'vote', 'light', 'swipe',
         'show', 'game', 'poster', 'lottery', 'wheel', 'rush']
for cate in cates:
    os.system(f"ls | grep {cate} | wc -l")
