#This is text to Morse Code converter

# Morse Code rules:
# The space between symbols(dots and dashes) of the same letter is 1 time unit.
# The space between letters is 3 time units.
# The space between words is 7 time units.
# A dash is the length of 3 dots

import winsound
import time

# Specifying time lengths and beep frequency
dot = 150 #in milliseconds
dash = 450 #in milliseconds
wait_time_unit = 0.15 #in seconds
freq = 1700 #in HZ

# Morse Code dictionary
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
mc_dict['.'] = '*-*-*-'
mc_dict[','] = '--**--'
mc_dict['!'] = '-*-*--'
mc_dict['?'] = '**--**'

#function that plays one character
def play_function(input_string):
    for char in input_string:
        if (char == '*'):
            winsound.Beep(freq,dot)
        else:
            winsound.Beep(freq,dash)
        time.sleep(wait_time_unit)


text_to_convert = input('Hi there! \n Welcome to Greg\'s Morse Code encoder \n Please input your text: ')
words_to_play = text_to_convert.lower().split()

for item in words_to_play:
    for char in item:
        try:
            play_function(mc_dict[char])
            time.sleep(wait_time_unit*2)
        except: # this is in case we don't have a character in our Morse Code dictionary
            print(f'Character {char} doesn\'t exist')
            pass
    time.sleep(wait_time_unit*4)
    print('END OF WORD')
print('END OF TEXT')
