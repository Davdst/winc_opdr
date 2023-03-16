# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer_name0 = 'Ruud Gullit'
scorer_name1 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

scorers = scorer_name0 + ' '+str(goal_0)+ ', '+ scorer_name1 +' ' +str(goal_1)

report = scorer_name0 +' '+ f'scored in the {goal_0}nd minute\n'+(scorer_name1 +' '+ f'scored in the {goal_1}th minute')


player = 'Frank Rijkaard'

first_name = player [:5]
last_name = player [6:14]
last_name_len = len(last_name)
name_short = player [:1] +'. ' + player [6:14]
chant = ' '.join([first_name +'!']* len(first_name))
good_chant = ' ' != 2

print (scorers)
print (report)
print (first_name)
print (last_name)
print (name_short)
print (last_name_len)
print (chant)
print(good_chant)