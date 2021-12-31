


def read_file(filename):

    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    # print(lines)
    return lines

def get_content(singer_name):
    if (singer_name == "jin"):
        print('worldwide handsome')
        read_file('jin.txt')

    elif(singer_name == 'suga'):
        print('meow-meow')
        read_file('suga.txt')

def get_players():
    return read_file('players.txt')


if __name__== "__main__":
    print('bts')
    get_content('suga')
