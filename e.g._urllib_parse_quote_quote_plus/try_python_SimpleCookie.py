from http.cookies import SimpleCookie
import binascii

# RFC6265 4.1.1.Syntax のcookie-octetより
# https://tools.ietf.org/html/rfc6265#section-4.1.1
ENABLE_OCTET = {
    'x21': '!',
    'x23': '#',
    'x24': '$',
    'x25': '%',
    'x26': '&',
    'x27': "'",
    'x28': '(',
    'x29': ')',
    'x2a': '*',
    'x2b': '+',
    'x2d': '-',
    'x2e': '.',
    'x2f': '/',
    # x30 ~ x39は0-9なので省略
    'x3a': ':',
    'x3c': '<',
    'x3d': '=',
    'x3e': '>',
    'x3f': '?',
    'x40': '@',
    # x41 ~ x5aはA-Zなので省略
    'x5b': '[',
    'x5d': ']',
    'x5e': '^',
    'x5f': '_',
    'x60': '`',
    # x61 ~ x7aはa-zなので省略
    'x7b': '{',
    'x7c': '|',
    'x7d': '}',
    'x7e': '~',
}

DISABLE_OCTET = {
    'x09': '\t', # 水平タブ
    'x0a': '\n', # LF(改行)
    'x0d': '\r', # CR
    'x22': '"',
    'x2c': ',',
    'x3b': ';',
    'x5c': '\\',
    'whitespace': '\x20'  # 半角スペース
}

STRINGS = ['a', 'あ', 'a,a', 'a;a', 'a a', 'a あ',]


def print_cookie_header_from_list(characters):
    for c in characters:
        try:
            cookie = SimpleCookie(f'key={c}')
            print(f'{c}: {type(cookie)} -> {cookie}')
        except Exception as ex_info:
            print(f'{c}: {ex_info}')


def print_cookie_header_from_dict(char_dict):
    for key, value in char_dict.items():
        # http://qiita.com/atsaki/items/6120cad2e3c448d774bf
        h = binascii.hexlify(value.encode('utf-8'))
        try:
            cookie = SimpleCookie(f'{key}={value}')
            print(f'{value} ({key}), hex:{h}, {type(cookie)} -> {cookie}')
        except Exception as ex_info:
            print(f'{key}: {ex_info}')


if __name__ == '__main__':
    print_cookie_header_from_dict(ENABLE_OCTET)
    print('-'*20)
    print_cookie_header_from_dict(DISABLE_OCTET)
    print('-'*20)
    print_cookie_header_from_list(STRINGS)