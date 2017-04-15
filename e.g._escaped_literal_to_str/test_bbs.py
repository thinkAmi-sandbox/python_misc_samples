import os
import requests
from wsgi_intercept.interceptor import RequestsInterceptor
import bottle
import pytest
from bbs_app.bbs import app


class TestRequest(object):
    def get_app(self):
        return app

    @classmethod
    def setup_class(cls):
        """Bottleのviewテンプレートを認識させる"""
        current_dir = os.path.abspath(os.path.dirname(__file__))
        template_dir = os.path.join(current_dir, 'bbs_app/views')
        bottle.TEMPLATE_PATH.insert(0, template_dir)

    def teardown_method(self):
        """テストごとにpickleファイルができるため、お互いに影響を与えないよう削除する"""
        if os.path.exists('bbs.pickle'):
            os.remove('bbs.pickle')

    def run_assertion(self):
        form = {
            'title': 'タイトル',
            'handle': 'あ',
            'message': 'メッセージ',
        }
        with RequestsInterceptor(self.get_app, host='localhost', port=8081) as url:
            actual = requests.post(url, data=form, allow_redirects=False)

        assert actual.status_code == 302
        assert len(actual.cookies) == 1

        handle = actual.cookies['handle']
        print(handle)
        #=> "\343\201\202"
        print(type(handle))
        #=> <class 'str'>

        return handle


    @pytest.mark.xfail
    def test_cookie(self):
        handle = self.run_assertion()

        encoded = handle.encode('latin1')
        print(encoded)
        #=> b'"\\343\\201\\202"'

        decoded = encoded.decode('utf-8')
        print(decoded)
        #=> "\343\201\202"

        assert decoded == 'あ'


    @pytest.mark.xfail
    def test_cookie_using_strip(self):
        handle = self.run_assertion()

        replaced = handle.strip('"').strip()
        print(replaced)
        #=> \343\201\202
        print(type(replaced))
        #=> <class 'str'>

        encoded = replaced.encode('latin1')
        print(encoded)
        #=> b'\\343\\201\\202'

        decoded = encoded.decode('utf-8')
        print(decoded)
        #=> \343\201\202

        assert decoded == 'あ'


    def test_cookie_using_codecs(self):
        handle = self.run_assertion()

        import codecs
        decoder_func = codecs.getdecoder('unicode_escape')
        print(decoder_func)
        #=> <built-in function unicode_escape_decode>

        after_codecs_tuple = decoder_func(handle)
        print(after_codecs_tuple)
        #=> ('"ã\x81\x82"', 14)

        after_codecs = after_codecs_tuple[0]
        print(after_codecs)
        #=> "ã"
        print(type(after_codecs))
        #=> <class 'str'>

        encoded = after_codecs.encode('latin1')
        print(encoded)
        #=> b'"\xe3\x81\x82"'

        decoded = encoded.decode('utf-8')
        print(decoded)
        #=> "あ"

        stripped = decoded.strip('"')
        print(stripped)
        #=> あ

        assert stripped == 'あ'


    def test_cookie_using_ast_module(self):
        handle = self.run_assertion()

        import ast
        after_literal_eval = ast.literal_eval(handle)
        print(type(after_literal_eval))
        #=> <class 'str'>
        print(after_literal_eval)
        #=> ã

        encoded = after_literal_eval.encode('latin1')
        print(encoded)
        #=> b'\xe3\x81\x82'

        decoded = encoded.decode('utf-8')
        print(decoded)
        #=> あ
        
        assert decoded == 'あ'
