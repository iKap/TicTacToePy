'''
Program of the game TicTacToe
'''
from random import *
import sys
import pickle
class TicTacToe:
    '''
    Field for the game, 2 players: 'x' and 'o'.
    The program enables them to play,
    checks and says who win or give up, when it's a draw.
    Says when the game is over, who's turn is now.
    '''
    def __init__(self):
        '''
        Initialisation of the class.
        There are 9 turns in the game, this shows self.turn_num.
        The self.field[0] shows who's turn will be next,
        the self.last_turn shows who's turn was previous.
        '''
        self.field = ['.']*10
        self.turn_num = 9
        self.field[0] = 'x'
        self.win = False
        self.last_turn = 'o'        
        
    def __str__(self):
        '''
        Field for the game in str.
        '''
        f = self.field
        s  = f'{f[7]} {f[8]} {f[9]}\n'
        s += f'{f[4]} {f[5]} {f[6]}\n'
        s += f'{f[1]} {f[2]} {f[3]}\n'
        return s
    
    def turn(self,idx):
        '''
        One turn. It counts only if player write the correct index,
        and it's not occupied. Correct indexes:
                7 8 9
                4 5 6
                1 2 3
        When the turn ends, the player in the self.field[0] and self.last_turn changes,
        and the number of turns is fewer by 1.
        '''
        if idx != 0:
            if self.field[idx] == '.':
                self.field[idx] = self.field[0]
                self.turn_num -= 1
                self.last_turn = self.field[0]
                if self.field[0] == 'o':
                    self.field[0] = 'x'
                elif self.field[0] == 'x':
                    self.field[0] = 'o'
            else:
                raise ImportError(f'cell {idx} is already occupied')
    def check(self):
        '''
        Checking the winner. Program checks if the last player moves.
        Player wins only if he moved 3 marks in a row, column or diagonal.
        '''
        if not self.win:
            result = False
            player = self.last_turn
            if self.field[7] == player and self.field[8] == player and self.field[9] == player:
                result = True
            elif self.field[9] == player and self.field[6] == player and self.field[3] == player:
                result = True
            elif self.field[1] == player and self.field[2] == player and self.field[3] == player:
                result = True
            elif self.field[7] == player and self.field[4] == player and self.field[1] == player:
                result = True
            elif self.field[5] == player:
              if self.field[7] == player and self.field[3] == player:
                  result = True
              elif self.field[9] == player and self.field[1] == player:
                  result = True
              elif self.field[8] == player and self.field[2] == player:
                  result = True
              elif self.field[4] == player and self.field[6] == player:
                  result = True
            self.win = result      

    def autoTurn(self):
        '''
        Computer's turn. In the game first player is human, and second is computer.
        Program defines this turn by using random int number.
        The turn also counts only if computer write correct index, and it's not occupied.
        Watch method "turn" to see it. Random number can be wrong many times,
        so tryCount variable counts that numbers, and write them after index.
        '''
        print(f'Now turn Player \"{self.field[0].upper()}\"(Computer)')
        tryInput = True
        tryCount = 0
        while tryInput:
            ind = randint(1, 9)
            if self.field[ind] == '.':
                tryInput = False
            else:
                tryCount += 1
        print(f'{ind}:{tryCount}')        
        return ind
    
def player_input(t):
    '''
    The number that player write to move on field.
    Player can only write a number from 1 to 9.
    Program enables player to move marks on the field.
    The player(human)can give up by writing '-',
    the program will say about it.
    '''
    print(f'Now turn Player \"{t.field[0].upper()}\"')
    doing_input = True
    while doing_input:
        try:
            pturn = input()
            if pturn == '-':
                print(f'Player \"{t.field[0].upper()}\" gives up')
                t.win = True
                idx = 0
                break
            if pturn == 's':
                file = open('ttt_save.bin', 'wb')
                pickle.dump(t, file)
                file.close()
                print('Game is saved at this stage')
                exit()
            idx = int(pturn)
            if idx < 1 or idx > 9:
                raise ValueError
            else:
                doing_input = False
        except ValueError:
            print('Invalid input. Please write a number from 1 to 9')
    return idx
    
def Run(t):
    '''
    Program defines who's turn is now: human's or computer's,
    checks the winner, say when someone wins, when the game is over,
    and when it's draw, says when player moves in occupied cell.
    And that can only happen if there are turns left.  
    '''
    while t.turn_num:
        print(t)
        try:
            if t.field[0] == 'x':
                t.turn(player_input(t))
            else:
                t.turn(t.autoTurn())
            t.check()
        except ImportError as ie:   
            print(ie)
        if t.win:
            break
    print('Game over.')
    print(t)
    if t.turn_num == 0 and t.win is False:
        print('Win-Win.')
    else:
        print(f'Player \"{t.last_turn.upper()}\" win the game.')
        
def main(argv):
    '''
    The main program fo the game.
    '''
    t = None
    print(argv)
    print(__doc__)
    argc = len(argv)
 
    if argc > 1:
        print(f'Loading from {argv[1]}')
        try:
            file = open(argv[1], 'rb')
            t = pickle.load(file)
            file.close()
        except Exception as exc:
            print(exc)
            
    if t is None:
        t = TicTacToe()        

    try:        
        Run(t)
    except Exception as exc:
        print(exc)
def test():
    '''
    Test your program, if you added changes.
    '''
    main(sys.argv + ['ttt_save.bin','asjfiejf'])
    
if __name__ == '__main__':
    test()
#    main(sys.argv)
    
