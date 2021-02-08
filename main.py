#This is text to Morse Code converter
import winsound
import time

mc_dict = {}
mc_dict['a'] = '*-'
mc_dict['b'] = '-***'
mc_dict['c'] = '-*-*'
mc_dict['d'] = '-**'
mc_dict['e'] = '*'
mc_dict['f'] = '**-*'
mc_dict['g'] = '--*'
mc_dict['h'] = '****'
mc_dict['i'] = '**'
mc_dict['j'] = '*---'
mc_dict['k'] = '-*-'
mc_dict['l'] = '*-**'
mc_dict['m'] = '--'
mc_dict['n'] = '-*'
mc_dict['o'] = '---'
mc_dict['p'] = '*--*'
mc_dict['q'] = '--*-'
mc_dict['r'] = '*-*'
mc_dict['s'] = '***'
mc_dict['t'] = '-'
mc_dict['u'] = '**-'
mc_dict['v'] = '***-'
mc_dict['w'] = '*--'
mc_dict['x'] = '-**-'
mc_dict['y'] = '-*--'
mc_dict['z'] = '--**'
mc_dict['0'] = '-----'
mc_dict['1'] = '*----'
mc_dict['2'] = '**---'
mc_dict['3'] = '***--'
mc_dict['4'] = '****-'
mc_dict['5'] = '*****'
mc_dict['6'] = '-****'
mc_dict['7'] = '--***'
mc_dict['8'] = '---**'
mc_dict['9'] = '----*'

# The space between symbols(dots and dashes) of the same letter is 1 time unit. 
# The space between letters is 3 time units. 
# The space between words is 7 time units.
# A dash is the length of 3 dots

dot = 150
dash = 450
wait_unit = 0.15
freq = 1700

# winsound.Beep(1700, dot)
# time.sleep(wait_unit)
# winsound.Beep(1700, dash)

def play_function(input_string):
    for char in input_string:
        if (char == '*'):
            winsound.Beep(freq,dot)
        else:
            winsound.Beep(freq,dash)
        time.sleep(wait_unit)


text_to_convert = input('Hi there! \n Please input your word: ')
words_to_play = text_to_convert.split()

for item in words_to_play:
    for char in item:
        play_function(mc_dict[char])
        time.sleep(wait_unit*2)
    time.sleep(wait_unit*4)
    print('END OF WORD')

