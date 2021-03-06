import random

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # TODO: name, character

    # TODO: 

class Space:
    def __init__(self, width, height):
        self.space = []

        for i in range(height):
            row = ['.'] * width
            self.space.append(row)

        for i in range(11):
            rowNum = random.randint(0, height - 1)
            colNum = random.randint(0, width - 1)

            self.space[rowNum][colNum] = '*'

    def print_map(self, player):
        print(f'Player is at {player.x}, {player.y}')
        for rowNum in range(len(self.space)):
            for colNum in range(len(self.space[rowNum])):
                if player.x == colNum and player.y == rowNum:
                    char = 'Y'
                else:
                    char = self.space[rowNum] [colNum]
                print(f'{char} ', end='')
            print()
        

    def __str__(self):
        s = ""

        for row in self.space:
            s += " ".join(row) + "\n"

        return s


s = Space(15, 10)
p = Player(15 // 2, 10 //2)
while True:
    s.print_map(p)
    
    dir = input(">> ")

    if dir == 'n':
        p.y -= 1
    if dir == 's':
        p.y += 1
    if dir == 'w':
        p.x -= 1
    if dir == 'e':
        p.x += 1