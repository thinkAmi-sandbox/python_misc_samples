# 参考
# https://blog.luminoso.com/2012/08/20/fix-unicode-mistakes-with-python/
# http://graphemica.com/%E3%81%82
# http://stackoverflow.com/questions/6539881/python-converting-from-iso-8859-1-latin1-to-utf-8
# Octal Escape Sequence
escaped_literal = '\343\201\202'
print(escaped_literal)
#=> ã

# 「あ」にするため、まずはlatin1でencodeし、バイト文字列にする
encoded = escaped_literal.encode('latin1')
print(encoded)
#=> b'\xe3\x81\x82'

# 最後にutf-8でdecodeし、unicode文字にする
decoded = encoded.decode('utf-8')
print(decoded)
#=> あ