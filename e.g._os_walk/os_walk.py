import os
import sys


def print_out(root, dirs, files):
    print('-'*10)
    print('root:{}'.format(root))
    print('dirs:{}'.format(dirs))
    print('files:{}'.format(files))


def print_os_walk_all(root_dir):
    print(sys._getframe().f_code.co_name)

    for root, dirs, files in os.walk(root_dir):
        print_out(root, dirs, files)


def print_os_walk_using_slice_dirs(root_dir):
    print(sys._getframe().f_code.co_name)

    target_files = []
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if 'hoge' not in os.path.join(root, d)]
        print_out(root, dirs, files)

        targets = [os.path.join(root, f) for f in files]
        target_files.extend(targets)


def print_os_walk_using_variable_assignments(root_dir):
    """変数代入を使って、hogeディレクトリを除くファイル一覧は作成できない"""
    print(sys._getframe().f_code.co_name)

    target_files = []
    for root, dirs, files in os.walk(root_dir):
        dirs = [d for d in dirs if 'hoge' not in os.path.join(root, d)]
        print_out(root, dirs, files)

        targets = [os.path.join(root, f) for f in files]
        target_files.extend(targets)

    for f in target_files:
        print(f)


def os_walk_all(root_dir):
    """ファイル一覧の作成"""
    print(sys._getframe().f_code.co_name)

    target_files = []
    for root, dirs, files in os.walk(root_dir):
        targets = [os.path.join(root, f) for f in files]
        target_files.extend(targets)

    for f in target_files:
        print(f)


def os_walk_using_slice_dirs(root_dir):
    """スライスを使って、hogeディレクトリを除くファイル一覧を作成"""
    print(sys._getframe().f_code.co_name)

    target_files = []
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if 'hoge' not in os.path.join(root, d)]
        targets = [os.path.join(root, f) for f in files]
        target_files.extend(targets)

    for f in target_files:
        print(f)


def os_walk_using_remove_dirs(root_dir):
    """removeを使って、hogeディレクトリを除くファイル一覧を作成"""
    print(sys._getframe().f_code.co_name)

    target_files = []
    for root, dirs, files in os.walk(root_dir):
        try:
            dirs.remove('hoge')
        except:
            pass

        targets = [os.path.join(root, f) for f in files]
        target_files.extend(targets)

    for f in target_files:
        print(f)



if __name__ == '__main__':
    root_dir = os.path.abspath(os.path.dirname(__file__))

    print_os_walk_all(root_dir)
    print('='*30)
    print_os_walk_using_slice_dirs(root_dir)
    print('='*30)
    print_os_walk_using_variable_assignments(root_dir)
    print('='*30)
    os_walk_all(root_dir)
    print('='*30)
    os_walk_using_slice_dirs(root_dir)
    print('='*30)
    os_walk_using_remove_dirs(root_dir)