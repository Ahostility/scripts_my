from pathlib import Path
from pathlib import *


DIR_DATA = Path(__file__).absolute().parent
DIR_DATA_INPUT = DIR_DATA / '_input'
DIR_DATA_OUTPUT = DIR_DATA / '_output'
DIR_DATA_INPUT.mkdir(parents=True,exist_ok=True)
DIR_DATA_OUTPUT.mkdir(parents=True,exist_ok=True)
print(DIR_DATA)


def iterfiles(directory:Path,include:callable = lambda x: True):
    for x in directory.iterdir():
        if x.is_file() and include(x):
            yield x
        else:
            yield from iterfiles(directory / x, include)
