"""
Vaším úkolem je doplnit funkci own_print tak, aby využila funkci print a
výpis byl stejný jako kdybychom zadané parametry funkce zadali v té samé posloupnosti do funkce print.
"""
import os


def own_print(*args, **kwargs):
	...


own_print('G', 'R', 'E', 'A', 'T', sep='\t', end='!!!\n', file=open('test.txt', 'w'))
own_print(['ahoj', 'cau',], file=open('test.txt', 'a'))
own_print((1, 2, 3), file=open('test.txt', 'a'), end='(1, 2, 3)\n')
own_print(*[1, 2, 3], file=open('test.txt', 'a'), end='some end\n', sep='  ')
own_print({'ahoj', 'ahoj', 'ahoj', 'test'}, file=open('test.txt', 'a'), end=' set_is_useful\n')
own_print({'dict': 'is', 'useful': 'too'}, **{'file': open('test.txt', 'a'), 'end': '!\n'})
own_print(*{'only': 'values', 'keys': 'are', 'are': 'here', 'printed': 'useless'}, **{'file': open('test.txt', 'a'), 'end': '!\n'})
own_print(*('stars', 'in', 'python', 'have', 'been', 'understood'), end='( ͡° ͜ʖ ͡°)\n', file=open('test.txt', 'a'))

with open('test.txt', 'r') as test_file:
	assert test_file.readline() == "G\tR\tE\tA\tT!!!\n"
	assert test_file.readline() == "['ahoj', 'cau']\n"
	assert test_file.readline() == "(1, 2, 3)(1, 2, 3)\n"
	assert test_file.readline() == "1  2  3some end\n"
	line = test_file.readline()
	assert line == "{'ahoj', 'test'} set_is_useful\n" or line == "{'test', 'ahoj'} set_is_useful\n"
	assert test_file.readline() == "{'dict': 'is', 'useful': 'too'}!\n"
	assert test_file.readline() == "only keys are printed!\n"
	assert test_file.readline() == "stars in python have been understood( ͡° ͜ʖ ͡°)\n"

os.remove('test.txt') # Cleanup
