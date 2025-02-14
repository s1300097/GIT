from flask import Flask, redirect ,request,render_template,jsonify
nc = Flask(__name__)

def expectation(card:list):
    height = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    count = sum(card)
    all_sum = sum([x * y for x, y in zip(card, height)])
    expected = all_sum /count

    p_list = [100 *x /count for x in card]
    p_list.insert(10, sum(p_list[10:]))
    p_list = p_list[1:11]

    return p_list, expected

def fist_select():
    print("Input num by round\n5 round -> 1\n10 round -> 2")
    a = int(input())
    if a == 1:
        n = 3
    elif a == 2:
        n = 5
    else:
        exit()
    return n

def run_command():
    n = fist_select()
    cards = [0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
    card = [x *n for x in cards]

    while(True):
        print("supported command")
        print("add, com(compere by carrent score]), print, reset, q(quit)")
        command = input().split()

        match command[0]:
            case "add":
                for i in map(int, command[1:]):
                    card[i] = int(card[i]) -1
                probality, expected = expectation(card)
                print(f'期待値: {expected:.3f}')
                for i, pro in enumerate(probality, 1):
                    print(f'{i}:  {pro:.2f} %')
                print()

            case "com":
                num = 21 -int(command[1])
                for i, pro in enumerate(probality[:num], 1):
                    print(f'{i}:  {pro:.2f} %')
                print(f'sum: {sum(probality[:num]):.2f}%')

            case "reset":
                card = [x *n for x in cards]

            case "print":
                for i, j in enumerate(card[1:], 1):
                    print(f'{i}:  {j}枚')
                print()

            case "q":
                exit()
                
if __name__ == "__main__":
    try:
        run_command()
    except Exception as e:
        print(e)
    
