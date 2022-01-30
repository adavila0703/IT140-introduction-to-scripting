'''
"Simon Says" is a memory game where "Simon" outputs a sequence of 10 
characters (R, G, B, Y) and the user must repeat the sequence.
 Create a for loop that compares the two strings. For each match, 
 add one point to user_score. Upon a mismatch, end the game.

Sample output with inputs: 'RRGBRYYBGY' 'RRGBBRYBGY'
User score: 4
'''


user_score = 0
simon_pattern = input()
user_pattern = input()


for num in range(len(simon_pattern)):
    if simon_pattern[num] != user_pattern[num]:
        break
    user_score += 1

print('User score:', user_score)
