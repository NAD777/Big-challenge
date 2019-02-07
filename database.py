import sqlite3, sys


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


class db:
    def __init__(self, name):
        self.connection = sqlite3.connect('{}.db'.format(name), check_same_thread=True)
        self.cursor = self.connection.cursor()

    def create_new_table(self, name_of_table='images'):
        self.cursor.execute("""CREATE TABLE {} (description text,img text)""".format(name_of_table))

    def get_date(self, column, key, name_of_table='images', fetch="all"):
        self.cursor.execute("SELECT * FROM {} WHERE {} = '{}'".format(name_of_table, column, key))
        if fetch == 'all':
            return self.cursor.fetchall()
        elif fetch == 'one':
            return self.cursor.fetchone()
        elif fetch == 'many':
            return self.cursor.fetchmany()

    def commit(self, description, img, name_of_table='images'):
        # self.cursor.execute("INSERT INTO {} VALUES ({},{})".format(name_of_table, description, img))
        self.cursor.execute(
            "INSERT INTO " + name_of_table + " VALUES (:description,:img)",
            {'description': description, 'img': img})
        self.connection.commit()

    def close_connection(self):
        self.connection.close()


if __name__ == '__main__':
    database = db('data')
    # database.create_new_table('images')
    # database.commit('description', img_to_bin('dog.jpg'))
    bin_to_img(database.get_date('description', 'dog')[0][1], 'dodo.jpg')
