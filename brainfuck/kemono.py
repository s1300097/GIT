import re
# from run_bf import run_brainfuck

#ここにプロンプト
kemono = '''
'''

bf = '''
+++++[>+++++>---<[>+++++>++++<<-]<-]>>++.>+.<++.>+.-.--.<++.<<++++++[>++++++<-]>---.<++++[>-----<-]>.---.
'''

def decoder(bf, kemono, run = False):
    programming = ["たのしー！","たーのしー！","すごーい！","すっごーい！","うわー！","わーい！","なにこれなにこれ！"]
    encode_list = ['>','+','<','-','[',']','.']
    encode_dict = dict(zip(programming, encode_list))
    decode_dict = dict(zip(encode_list, programming))


    bf = bf.strip().replace('\n', '')
    kemono = kemono.strip().replace('\n', '').replace(' ', '')

    bf_bool = bool(bf)
    kemono_bool = bool(kemono)


    if kemono_bool and not bf_bool:
        kemono_tokens = re.findall(r'.+?！', kemono)
        kemono = ''.join([encode_dict[c] for c in kemono_tokens])
        print(kemono)
    elif bf_bool and not kemono_bool:
        convert = ''.join([decode_dict[c] for c in bf])
        print(convert)
    else:
        print("Both kemono and bf are empty or both have content.")

    print()
    if run:
        if kemono_bool:
            print(run_brainfuck(kemono))
        if bf_bool:
            print(run_brainfuck(bf))

if __name__ == "__main__":
    decoder(bf, kemono)