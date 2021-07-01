from os import scandir
import sys
from pathlib import Path
from subprocess import call

# pdf2txt.py のパス
py_path = "C:\\Users\\81803\\Documents\\ROX\\appenv\\Scripts\\pdf2txt.py"

# pdf2txt.py の呼び出し
#call(["py", str(py_path), "-o extract-sample.txt", "-p 1", "sample.pdf"])
call(["py", str(py_path), "sample.pdf"])