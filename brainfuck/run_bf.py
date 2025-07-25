def run_brainfuck(code, input_stream=''):
    tape = [0] * 30000
    ptr = 0
    output = ''
    input_ptr = 0
    code_ptr = 0
    bracket_map = {}

    # ブラケット対応を事前に構築
    temp_stack = []
    for i, c in enumerate(code):
        if c == '[':
            temp_stack.append(i)
        elif c == ']':
            start = temp_stack.pop()
            bracket_map[start] = i
            bracket_map[i] = start

    while code_ptr < len(code):
        cmd = code[code_ptr]
        if cmd == '>':
            ptr += 1
        elif cmd == '<':
            ptr -= 1
        elif cmd == '+':
            tape[ptr] = (tape[ptr] + 1) % 256
        elif cmd == '-':
            tape[ptr] = (tape[ptr] - 1) % 256
        elif cmd == '.':
            output += chr(tape[ptr])
        elif cmd == ',':
            if input_ptr < len(input_stream):
                tape[ptr] = ord(input_stream[input_ptr])
                input_ptr += 1
            else:
                tape[ptr] = 0
        elif cmd == '[' and tape[ptr] == 0:
            code_ptr = bracket_map[code_ptr]
        elif cmd == ']' and tape[ptr] != 0:
            code_ptr = bracket_map[code_ptr]
        code_ptr += 1
    return output