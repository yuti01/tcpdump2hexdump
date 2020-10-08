#!/usr/bin/env python3

def set_char_in_index(string, index, char):
	return string[:index] + char + string[index:]

def add_spaces(string):
	string_to_return = set_char_in_index(string, 6, ' ')
	
	for i in range(9, (len(string) - 4) * 2, 3):
		string_to_return = set_char_in_index(string_to_return, i, ' ')
	
	return string_to_return


tcpdump_file_path = "/home/kali/capture.txt" # CHANGE this to your input file path
hexdump_file_path = "/home/kali/capture-hexdump.txt" # CHANGE this to your output file path

print('Creating a file in hexdump style from the tcpdump output ...')

tcpdump_file = open(tcpdump_file_path, "rt")

open(hexdump_file_path, "w").close() # clear the output file
hexdump_file = open(hexdump_file_path, "a")

tcpdump_lines = tcpdump_file.readlines()

for line in tcpdump_lines:
	if line[2] != ':':
		line = line[:57]
		line = line.replace(' ','').replace('x', '').replace('\t','').replace('\n','').replace(':','')
		line_to_add = add_spaces('0' + line)		
		hexdump_file.write(line_to_add + '\n')
	else:
		hexdump_file.write('\n')

tcpdump_file.close()
hexdump_file.close()

print('Done.')

