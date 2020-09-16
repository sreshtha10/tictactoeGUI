# Tic tac toe
import  sys

board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
         'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
         'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def checkWin():
    if (board['top-L'] == board['top-M'] and board['top-M'] == board['top-R'] and board['top-R'] != ' '):
        print(board['top-R'] + ' won.')
        return 1

    if (board['mid-L'] == board['mid-M'] and board['mid-M'] == board['mid-R'] and board['mid-M'] != ' '):
        print(board['mid-R'] + ' won.')
        return 1

    if (board['low-L'] == board['low-M'] and board['low-M'] == board['low-R'] and board['low-R'] != ' '):
        print(board['low-R'] + ' won.')
        return 1

    if (board['top-R'] == board['mid-M'] and board['mid-M'] == board['low-L'] and board['mid-M'] != ' '):
        print(board['top-R'] + ' won.')
        return 1

    if (board['top-L'] == board['mid-M'] and board['mid-M'] == board['low-R'] and board['top-L'] != ' '):
        print(board['top-R'] + ' won.')
        return 1
    if (board['top-L'] == board['mid-L'] and board['mid-L'] == board['low-L'] and board['top-L'] != ' '):
        print(board['top-L'] + ' won.')
        return 1
    if (board['top-M'] == board['mid-M'] and board['mid-M'] == board['low-M'] and board['top-M'] != ' '):
        print(board['top-M'] + ' won.')
        return 1
    if (board['top-R'] == board['mid-R'] and board['mid-R'] == board['low-R'] and board['top-R'] != ' '):
        print(board['top-R'] + ' won.')
        return 1
    return 0

def printBoard(board: object) -> object:
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('+-+-+')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('+-+-+')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'

for i in range(9):
    printBoard(board)
    print('Turn for '+turn+'. Move on which space')
    move = input()
    board[move] = turn
    if(checkWin()):
        sys.exit()
        
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

print('Match Drawn')
