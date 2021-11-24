#!/usr/bin/python3
'''Pycodestyle Unittests'''
import unittest
import pycodestyle
import os


class TestPycodestyle(unittest.TestCase):
    '''Tests over-arching things'''

    dirs = ('/',
            '/models/',
            '/models/engine/',
            '/tests/',
            '/tests/test_models/',
            '/tests/test_models/test_engine/'
            )

    cw_dir = os.getcwd()

    def test_pycodestyle(self):
        '''run pycodestyle against all .py files in app'''
        self.assertEqual(pycodestyle.StyleGuide(
            quiet=True).check_files('.').total_errors, 0)

    def test_shabang(self):
        '''open all .py files and confirm the first line is a shabang'''
        for fldr in self.dirs:
            for f in os.listdir(self.cw_dir + fldr):
                if ".py" in f:
                    with open(self.cw_dir + fldr + f) as fd:
                        self.assertEqual(fd.readline(), "#!/usr/bin/python3\n",
                                         "First line needs shebang in {}"
                                         .format(self.cw_dir + fldr + f))

    def test_readme(self):
        '''checks for non-empty README'''
        with open("README.md") as f:
            self.assertNotEqual(len(f.read()), 0, "README is empty")
        with open("tests/README.md") as f:
            self.assertNotEqual(len(f.read()), 0, "tests/README is empty")

    def test_exe(self):
        '''confirm all files are executable'''
        for fldr in self.dirs:
            for f in os.listdir(self.cw_dir + fldr):
                if ".py" in f:
                    self.assertTrue(os.access(self.cw_dir + fldr + f, os.X_OK),
                                    "File {} is not executable"
                                    .format(self.cw_dir + fldr + f))
