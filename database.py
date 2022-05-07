from importlib.resources import as_file
import sqlite3
# from tabulate import tabulate
def startpy():
    conn = sqlite3.connect('bts.db')
    member_list = ['RM','jin','J-hope', 'Jungkook', 'Jimin', 'V','suga']
    print ("Opened database successfully")

    # conn.execute('''CREATE TABLE BTS_BIAS
    #          (NAME           TEXT    NOT NULL,
    #           ABOUT          CHAR(50)   NOT NULL);''')
    for member in member_list:
        with open(f'{member}.txt') as f:
            lines = f.readlines()
        for line in lines:
            line = line.replace('\n','')
            conn.execute(f"INSERT INTO BTS_BIAS (NAME,ABOUT) VALUES ('{member}','{line}')")
    conn.commit()
    print('values added')
    conn.close()
if __name__ == '__main__':
    startpy()