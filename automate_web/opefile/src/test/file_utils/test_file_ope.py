import os
import unittest

import automate_web.opefile.src.main.file_utils.file_ope as file_ope


class TestFileOpe(unittest.TestCase):
    """
    test module of file_ope
    """

    # デスクトップ上のファイルを指定のフォルダに移動する
    # def test_move_file_on_desktop_success(self):
    #     dst = '/Users/matsukado/Desktop/test'
    #     expected = '/Users/matsukado/Desktop/test/hello_world.txt'
    #     file_ope.move_file_on_desktop(dst)
    #     self.assertTrue(os.path.isfile(expected))

    def test_delete_file_on_desktop_success(self):
        desktop_path = '/Users/matsukado/Desktop/hello_world.txt'
        expected = False
        self.assertTrue(os.path.isfile(desktop_path))
        file_ope.delete_file_on_desktop()
        actual = os.path.isfile(desktop_path)
        self.assertEquals(expected,actual)



    def test_get_desktop_path_success(self):
        if os.name == 'posix':
            # Linux OS系
            expected = '/Users/matsukado/Desktop'
        else :
            # windowsのパス
            expected = '/Users/matsukado/Desktop'
        actual = file_ope.get_desktop_path()
        self.assertEquals(expected, actual)
    #
    # def test_get_file_list_success(self):
    #     expected = ['test_file_ope.py']
    #     actual = file_ope.get_file_list('/Users/matsukado/PycharmProjects/automate/test/file_utils')
    #     self.assertEquals(expected, actual)
    #
    # def test_get_file_list_except_hide_file_success(self):
    #     expected = ['test_file_ope.py']
    #     actual = file_ope.get_file_list_except_hide_file('/Users/matsukado/PycharmProjects/automate/test/file_utils')
    #     self.assertEquals(expected, actual)

    def test_is_is_folder_paht_success(self):
        # 正しいパス
        expected = True
        actual = file_ope.is_folder_path('/Users/matsukado/Desktop/test')
        self.assertEquals(expected,actual)

        # パスが空白
        expected = False
        actual = file_ope.is_folder_path('')
        self.assertEquals(expected, actual)


# テスト実行
if __name__ == "__main__":
    unittest.main()