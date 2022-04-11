test_file = open('read_file.txt', 'a')

test_file.write('\nNow you have written in the file\n')
test_file.close()

test_file = open('read_file.txt', 'r')
print(test_file.read())


