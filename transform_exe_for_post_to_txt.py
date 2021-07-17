import subprocess
import sys
from data.dirs import DIR_DATA_OUTPUT


# Преобразование .exe файла для отправки
def transform(path,arg): # '-c', '{1...n}','-b'
    return subprocess.call(['xxd','-p',path.parent / "_input" / arg, path / (arg[:-3] + "txt")])


if __name__ == "__main__":
    print(transform(DIR_DATA_OUTPUT, sys.argv[1]))
