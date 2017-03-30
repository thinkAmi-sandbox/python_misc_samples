from pathlib import Path


"""テスト向けのディレクトリを作成するスクリプト"""


# parents=Trueとして、親ディレクトリがない場合は同時に作成
Path('foo/hoge').mkdir(parents=True, exist_ok=True)
Path('foo/foo.txt').touch()
Path('foo/hoge/spam.txt').touch()
Path('foo/hoge/ham.txt').touch()
Path('bar/hoge').mkdir(parents=True, exist_ok=True)
Path('bar/fuga').mkdir(parents=True, exist_ok=True)
Path('bar/foo.txt').touch()
Path('bar/hoge/spam.txt').touch()
Path('bar/hoge/ham.txt').touch()
Path('bar/fuga/spam.txt').touch()
Path('bar/fuga/ham.txt').touch()
Path('baz/hoge').mkdir(parents=True, exist_ok=True)
Path('baz/fuga').mkdir(parents=True, exist_ok=True)

"""
$ tree
.
├── bar
│   ├── foo.txt
│   ├── fuga
│   │   ├── ham.txt
│   │   └── spam.txt
│   └── hoge
│       ├── ham.txt
│       └── spam.txt
├── baz
│   ├── fuga
│   └── hoge
├── foo
│   ├── foo.txt
│   └── hoge
│       ├── ham.txt
│       └── spam.txt
├── make_file.py
└── os_walk.py
"""

