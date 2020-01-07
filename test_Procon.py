#Python 3.8.1 unittest
import unittest
import procon

class proconTest(unittest.TestCase):
    def test_Procon1(self):
        self.assertEqual(5,procon.procon.Procon(20,30))
        #互いの数字に約数が複数ある場合に正しく実行されるかどうかを確認するメソッド
    def test_Procon2(self):
        self.assertEqual(1, procon.procon.Procon(2, 2))
        #約数がその数字と１しかない場合に１が返されるかどうかを確認するメソッド
    def test_Procon3(self):
        self.assertEqual(4800, procon.procon.Procon(9600, 96000))
        #大きい数字のの場合に正しく実行されるかを確認するメソッド
    def test_Procon4(self):
        self.assertEqual(6, procon.procon.Procon(96, 12))
        #引数の大小が入れ替わっても正しく動くか確認するメソッド


