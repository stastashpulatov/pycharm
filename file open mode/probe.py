from pprint import pprint

file_name = 'byron.txt'
file = open(file_name, mode='rb')   # mode - режим - чтение бинарное
file_content = file.read()
file.close()
pprint(file_content)
