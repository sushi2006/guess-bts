'''
Created on 
Course work: 
@author: 
Source:
    
'''

import sqlite3
# from tabulate import tabulate
def startpy():
    conn = sqlite3.connect('bts.db')

    print ("Opened database successfully")
    columns = conn.execute('''SELECT * from BTS_BIAS;''')
    # print (columns)
    # for row in columns:
    #     print ("NAME = ", row[0])
    #     print("ABOUT = ", row[1],"\n")
    for i in columns:
        print(i[0]+" "+str(i[1]))
    # conn.execute("UPDATE BTS_BIAS SET ABOUT = 'He likes bonsai trees' WHERE NAME = 'RM';")
    conn.execute("DELETE FROM BTS_BIAS WHERE NAME = 'V';")
    columns = conn.execute('''SELECT * from BTS_BIAS;''')
    # print (columns)
    # for row in columns:
    #     print ("NAME = ", row[0])
    #     print("ABOUT = ", row[1],"\n")
    for i in columns:
        print(i[0]+" "+str(i[1]))
    conn.commit()
    conn.close()
if __name__ == '__main__':
    startpy()