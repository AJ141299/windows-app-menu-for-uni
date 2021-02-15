import os
import sys
import random

for i in range(0, 150, 2):
    if random.choice([True, False]):
        d = str(i) + ' days ago'
        with open(os.path.join(sys.path[0], "main.txt"), 'a') as file:
            file.write(d + '\n')
        os.system('git add main.txt')
        os.system('git commit --date="' + d + '" -m time"')

os.system('git push -u origin master')
