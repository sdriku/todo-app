user_prompt = input('Enter a new member: ')
user_prompt = user_prompt.strip()

file = open('files/members.txt', 'r')
members = file.readlines()
file.close()

members.append(user_prompt + '\n')

file = open('files/members.txt', 'w')
file.writelines(members)
file.close()