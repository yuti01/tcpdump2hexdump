# tcpdump2hexdump
Python3 script to convert tcpdump output to hexdump. 

You can then import the output file into wireshark and then save it as pcap or pcapng file.

It is useful when you can't use the -w option of tcpdump.

To get the hex output from tcpdump, use -XX option to print the hex content of the packets (including ethernet and ip headers). 

Ex: tcpdump -i eth0 -XX -c 250 

!! Before you execute the script modify the paths to the input and output files !!
