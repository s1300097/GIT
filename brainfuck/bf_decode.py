
sentence = '''
I'm crazy!!
'''

def sentence2ascii(sentence):
    return [ord(c) for c in sentence]

def bf_decoder(code_list):
    bf = '++++++++++[>+++>+++++>+++++++>++++++++++>+<<<<<-]>++'
    cell_map = {
        'symbol': 0,
        'digit': 1,
        'upper': 2,
        'lower': 3,
        'newline': 4,
    }
    prev_val = {
        'symbol': 32,
        'digit': 50,
        'upper': 70,
        'lower': 100,
        'newline': 10,
    }
    current_cell = 0  # 初期位置は cell #0

    for code in code_list:
        if 32 <= code <= 47 or 58 <= code <= 64:
            category = 'symbol'
        elif 48 <= code <= 57:
            category = 'digit'
        elif 65 <= code <= 90:
            category = 'upper'
        elif 97 <= code <= 122:
            category = 'lower'
        elif code == 10:
            category = 'newline'
        else:
            raise ValueError(f"対応していない文字です: {code} (ASCII={code})")

        target_cell = cell_map[category]
        move = target_cell - current_cell
        bf += '>' * move if move > 0 else '<' * (-move)
        current_cell = target_cell

        diff = code - prev_val[category]
        bf += '+' * diff if diff > 0 else '-' * (-diff)
        prev_val[category] = code

        bf += '.'

    return bf

if __name__ == "__main__":
    code = sentence2ascii(sentence)
    code = code[1:]  # 最初の改行は無視
    bf_output = bf_decoder(code)
    print(bf_output)
    