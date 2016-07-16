# -*- coding:utf-8 -*-

from distutils.core import setup
import py2exe

setup(
    windows = [{"script":"pack\PythonVersionChange.py", "icon_resources":[(1, "pack\python.ico")]}],
    options = {"py2exe":{"dll_excludes":["MSVCP90.dll"]}}
    )