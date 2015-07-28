user_string = raw_input("whats the word")
user_num = input("what number?")

try:
    our_num = int(user_num)
except:
    our_num = float(user_num)

if not '.' in user_num:
    print(user_string[our_num])
else:
    ratio = round(len(user_string)*our_num)
    print(user_string[ratio])