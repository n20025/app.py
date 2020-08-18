from itertools import count
import random

left = random.randint(1, 13)
count = 0
print('*'* 18)
print("*   High & Low   *")
print('*'* 18)
while True:
    lists = list(range(1,14))
    lists.remove(left)
    right = random.choice(lists)
    print("    [問題表示]    ")
    print("*******    *******")
    print("*     *    *  *  *")
    print(f'*  {left}  *    *  *  *')
    print("*     *    *  *  *")
    print("*******    *******")
    text = input('High  or  Low ?(h/l) >')
    if(text == 'h' and right > left) or (text == 'l' and right < left):
        count += 1
        print("    [結果表示]    ")
        print("*******    *******")
        print("*     *    *     *")
        print(f'*  {left}  *    *  {right}  *')
        print('*     *    *     *')
        print('*******    *******')
        print(" You Win!")
        left = right
    elif text not in ['h','l']:
        continue
    else:
        print("    [結果表示]    ")
        print("*******    *******")
        print("*     *    *     *")
        print(f'*  {left}  *    *  {right}  *')
        print("*     *    *     *")
        print("*******    *******")
        print(" You Lose..")
        print("ゲーム終了！！")
        print(f'{count}回正解')
        break
