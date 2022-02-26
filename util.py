


from fileinput import filename


# Local import
from const import *

def read_file(filename):

    file1 = open(filename,'r')
    lines = file1.readlines()
    lines = [line.rstrip() for line in lines]

    print(lines)
    return lines

def get_content(singer_name):
    if (singer_name == "jin"):
        file_name = f"{BASE_DIR_PATH}jin.txt"
        print('worldwide handsome')
        read_file(file_name)

    elif(singer_name == "suga"):
        file_name = f"{BASE_DIR_PATH}suga.txt"
        print('meow-meow')
        read_file(file_name)

    elif(singer_name == "J-hope"):
        file_name = f"{BASE_DIR_PATH}j-hope.txt"
        print('Hope')
        read_file(file_name)

    elif(singer_name == "RM"):
        file_name = f"{BASE_DIR_PATH}RM.txt"
        print('Rap Monster')
        read_file(file_name)

    elif(singer_name == "Jimin"):
        file_name = f"{BASE_DIR_PATH}jimin.txt"
        print('chim chim')
        read_file(file_name)

    elif(singer_name == "V"):
        file_name = f"{BASE_DIR_PATH}V.txt"
        print('tae tae')
        read_file(file_name)

    elif(singer_name == "Jungkook"):
        file_name = f"{BASE_DIR_PATH}jungkook.txt"
        print('kookie')
        read_file(file_name)

def get_players():
    return read_file(f'{BASE_DIR_PATH}players.txt')


if __name__== "__main__":
    print('bts')
    
    get_content("jin")
   
    # read_file(file_name)

if __name__== "__main__":
    print('bts')
    file_name = "{BASE_DIR_PATH}suga.txt"
    get_content('suga')
    
if __name__== "__main__":
    print('bts')
    file_name = f"{BASE_DIR_PATH}j-hope.txt"
    get_content('J-hope')
    
if __name__== "__main__":
    print('bts')
    file_name = "{BASE_DIR_PATH}RM.txt"
    get_content('RM')
    
if __name__== "__main__":
    print('bts')
    file_name = f"{BASE_DIR_PATH}jimin.txt"
    get_content('Jimin')
    
if __name__== "__main__":
    print('bts')
    file_name = "{BASE_DIR_PATH}V.txt"
    get_content('V')
    
if __name__== "__main__":
    print('bts')
    file_name = f"{BASE_DIR_PATH}jungkook.txt"
    get_content('Jungkook')
    