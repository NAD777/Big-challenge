import sys
import sqlite3


# Функция открытия изображения в бинарном режиме
def img_to_bin(filename):
    try:
        fin = open(filename, "rb")
        img = fin.read()
        return sqlite3.Binary(img)
    except IOError:
        print("Error")
        sys.exit(1)
    finally:
        if fin:
            fin.close()


def bin_to_img(data, name_of_file):
    try:
        fout = open(name_of_file, 'wb')
        fout.write(data)

    except IOError:
        print('Error while writing')
        sys.exit(1)
    finally:
        if fout:
            fout.close()

"""
guide http://python-3.ru/page/sqlite-blob-to-image-example
http://python-3.ru/page/sqlite-upload-image-in-database
"""