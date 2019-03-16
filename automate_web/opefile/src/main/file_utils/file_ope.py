# ファイル移動に関するモジュール

import logging
import os
import shutil
import send2trash

# TODO:処理がごちゃってる・・・

# TODO:デスクトップのファイルを指定したフォルダパスに移動
# 用途：デスクトップクリーン

# パスがファルダかどうか返します
def is_folder_path(dst):
    return os.path.isdir(dst)

# デスクトップ上のファイルを指定のフォルダに移動
def move_file_on_desktop(dst):
    """
    デスクトップ上のファイルを指定のフォルダに移動
    :param dst:
    :return:
    """
    if not is_folder_path(dst):
        logging.warnning('>>> Parameter error not folder')
        raise SyntaxError('引数がフォルダではありません')

    desktop_path = get_desktop_path()

    # ファイル名の抽出
    file_list = get_file_list_except_hide_file(desktop_path)
    if len(file_list) == 0:
        logging.warning('>>> There is not file on desktop')
        raise FileNotFoundError('デスクトップにファイルがありません')

    for f in file_list:
        desktop_file_path = os.path.join(desktop_path,f)
        # ファイルを移動
        shutil.move(desktop_file_path,dst)
        logging.info('>>> File move completed to specified folder')

# デスクトップ上のファイルを削除します
def delete_file_on_desktop():
    """
    デスクトップ上のファイルを削除
    :return:
    """
    desktop_path = get_desktop_path()
    # ファイル名の抽出
    file_list = get_file_list_except_hide_file(desktop_path)
    if len(file_list) == 0:
        logging.warning('>>> There is not file on desktop')
        raise FileNotFoundError('デスクトップにファイルがありません')

    # ファイル削除処理(ゴミ箱に移動します)
    for f in file_list:
        desktop_file_path = os.path.join(desktop_path, f)
        send2trash.send2trash(desktop_file_path)
        logging.info('>>> File delete completed to specified folder')

# デスクトップ上に存在するファイル取得する
def get_desktop_file_list():
    """
    デスクトップ上に存在するファイルを取得
    :return: デスクトップ上のファイル一覧 [f1,f2,f3]
    """
    return get_file_list_except_hide_file(get_desktop_path())


# 共通的な関数
def get_desktop_path():
    """
    OS間に依存しないデスクトップの絶対パスを取得
    :return: デスクトップの絶対パス
    """
    return os.path.join(os.path.expanduser('~'),'Desktop')

def get_file_list(path):
    """
    指定したファルダ内のファイルリストを取得
    :param path:
    :return:[f1,f2,f3]
    """
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]

def get_file_list_except_hide_file(path):
    """
    指定したファルダ内のファイルリストを取得(隠しファイルは除く)
    :param path:
    :return:[f1,f2,f3]
    """
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and not f.startswith('.')]