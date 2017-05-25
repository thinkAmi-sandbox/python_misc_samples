from urllib.parse import quote, quote_plus

WHITE_SPACE = '\x20'  # 半角スペース
ALPHABET = 'aA'
DIGIT = '0'
JAPANESE = 'あ'

# RFC3986の「2.2.  Reserved Characters」や「2.3.  Unreserved Characters」より
# https://tools.ietf.org/html/rfc3986
RFC3986_RESERVED = (
    ":/?#[]@"  # gen-delims
    "!$&'()"   # sub-delims 1行目
    "*+,;="    # sub-delims 2行目
)
RFC3986_UNRESERVED = '-._~'

# w3cの「HTML5 4.10.22.6 URL-encoded form data」より
# https://www.w3.org/TR/html5/forms.html#url-encoded-form-data
HTML5_ENABLE_OCTET = (
    '*'  # x2a
    '-'  # x2d
    '.'  # x2e
         # x30 ~ x39は0-9なので省略
         # x41 ~ x5aはA-Zなので省略
    '_'  # x5f
         # x61 ~ x7aはa-zなので省略
)

# RFC6265の「4.1.1.  Syntax」より
# https://tools.ietf.org/html/rfc6265
COOKIE_DISABLE_OCTET = (
    '\t'    # 水平タブ (x09)
    '\n'    # LF(改行) (x0a)
    '\r'    # CR (x0d)
    '"'     # ダブルクォート(x22)
    ','     # カンマ(x2c)
    ';'     # セミコロン(x3b)
    '\\'    # バックスラッシュ(x5c)
    '\x20'  # whitespace
)

def main(func):
    print(func.__name__)
    print('-'*20)
    print('[WHITE_SPACE]')
    percent_encode(func, WHITE_SPACE)
    print('[ALPHABET]')
    percent_encode(func, ALPHABET)
    print('[DIGIT]')
    percent_encode(func, DIGIT)
    print('[JAPANESE]')
    percent_encode(func, JAPANESE)

    # RFC3986に関するURLエンコード
    print('[RFC3986_RESERVED]')
    percent_encode(func, RFC3986_RESERVED)
    print('[RFC3986_UNRESERVED]')
    percent_encode(func, RFC3986_UNRESERVED)

    # HTML5に関するURLエンコード
    print('[HTML5_ENABLE_OCTET]')
    percent_encode(func, HTML5_ENABLE_OCTET)

    # COOKIEで使えない文字に関するURLエンコード
    print('[COOKIE_DISABLE_OCTET]')
    percent_encode(func, COOKIE_DISABLE_OCTET)

def percent_encode(func, characters):
    for c in characters:
        print(f'{c}: {func(c)}')

def quote_rfc3986_strictly(character):
    # 半角スペースと/は%エンコードするが、チルダはそのまま
    return quote(character, safe='~')

def quote_html5_strictly(character):
    # *はそのまま、スペースは+にする
    return quote_plus(character, safe='*')


if __name__ == '__main__':
    # quote()やquote_plus()の挙動確認
    print('-'*20)
    main(quote)
    print('-'*20)
    main(quote_plus)
    print('-'*20)
    main(quote_rfc3986_strictly)
    print('-'*20)
    main(quote_html5_strictly)
