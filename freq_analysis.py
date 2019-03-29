from os.path import exists
from collections import OrderedDict


def char_frequency(file_path, char_count=1):
    f_handler = open(file_path, "r")
    cipher_text = f_handler.read()
    cipher_text = "".join(cipher_text.split())
    text_len = len(cipher_text)
    char_count_dict = {}
    for i in range(text_len):
        if i > 1:
            i += char_count
        if i + char_count >= text_len:
            break
        keys = char_count_dict.keys()

        if char_count > 1:
            chars = ""
            for c in range(char_count):
                chars += cipher_text[i]
                i += 1
        else:
            chars = cipher_text[i]
        if chars in keys:
            char_count_dict[chars] += 1
        else:
            char_count_dict[chars] = 1

    # order the count by desc
    sort_char_dict = OrderedDict(sorted(char_count_dict.items(), key=lambda kv: kv[1], reverse=True))

    for key in sort_char_dict:
        print('[ ' + key + ' ] - '
              + str(sort_char_dict[key]) + ' - '
              + str(round((sort_char_dict[key] * 100) / (text_len * char_count), 1)))


if __name__ == '__main__':
    cipher_text_path = './ciphertext.txt'
    if exists(cipher_text_path):
        char_frequency(cipher_text_path, 1)
