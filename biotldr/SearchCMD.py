#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function  # To suppress the space character as well, you can either use
import argparse
import os
import glob  ## used by insensitive_glob
import re
from colorama import Fore, Back, Style, init
init(autoreset=True) #If you find yourself repeatedly sending reset sequences to turn off color changes at the end of every print, then init(autoreset=True) will automate this. 

class SearchCMD:
    def __init__(self):
        """Initiate BioTLDR"""

    def cmd(self, exe_folder, dict_arg):
        """Find the corresponding md file"""
        db_folder = exe_folder + "/database/cmd/"
        mds = self.insensitive_glob(db_folder, dict_arg['command'])
        if len(mds) ==0:
            self.cmd_not_found(dict_arg)
            self.cmd_not_found_dim(dict_arg) 
        elif len(mds) == 1: 
            self.cmd_found1(mds[0])
        elif len(mds) > 1:
            index = self.get_cmd_index(mds)
            self.cmd_found1(mds[index])

    def get_cmd_index(self, mds):
        """
        Return: the index of markdown files. [0 - based]
        """
        print(Back.BLACK + Fore.MAGENTA + "We found more than one tools from our database:")
        flag = 1
        while(flag): ## This is to 
            for i in range(len(mds)):
                basename = os.path.basename(mds[i])
                base_prefix = re.sub(r'.md$', "", basename)
                print(Back.BLACK + Fore.CYAN + "    " + str(i+1) + ": " + base_prefix)
            message = Back.BLACK + Fore.MAGENTA + 'Choose the tool by typing an integer number [1-' + str(len(mds)) + ']: '
            try: 
                nb = int(raw_input(message))
            except ValueError:
                print(Back.YELLOW + Fore.RED + "Not an integer! Try again!")
            else:
                if nb -1 >=0 and nb -1 < len(mds):
                    flag = flag - 1 ## This is used to determine whether I need to jump out of the loop.  
        return int(nb) - 1

    def cmd_found1(self, md):
        """
        Input: <markdown file>
        """
        pattern = re.compile("`")
        print(Fore.CYAN + Back.BLACK + "\n")
        last_line = ""
        with open(md, 'r') as f:
            for line in f:
                if pattern.search(line):
                    print(Back.BLACK + Fore.CYAN +  line, end="")
                else:
                    print(Back.BLACK + Fore.GREEN +  line, end="")
                last_line = line
        if not last_line.isspace(): ## This method returns true if there are only whitespace characters (newline included) in the string and there is at least one character, false otherwise.
            print(Fore.CYAN + Back.BLACK + "\n")

    def cmd_not_found(self, dict_arg):
        """
        """
        print(Fore.BLUE + "Please check the command line name: ", end = "")
        print(Fore.RED +  dict_arg['command'])

        print(Fore.BLUE + "Or maybe the command ", end = "")
        print(Fore.RED +  dict_arg['command'], end=" ")
        print(Fore.BLUE + "does NOT existed in  ourdatabse. Please let us know if you use this very ofen. " + Style.RESET_ALL)           
 
    def cmd_not_found_dim(self, dict_arg):
        """
        """
        print(Style.BRIGHT + "Please check the command line name: ", end = "")
        print(Style.BRIGHT +  dict_arg['command'])

        print(Style.BRIGHT + "Or maybe the command ", end = "")
        print(Style.BRIGHT +  dict_arg['command'], end=" ")
        print(Style.BRIGHT + "does NOT existed in  ourdatabse. Please let us know if you use this very ofen. ")    
 
    def insensitive_glob(self, directory, pattern):
        """
        Find the corresponding mardown files 
        Input: <Folder of the main code> <pattern>
        Output: [md file names] 
        """
        def either(c): # return a regexp that is insensitive to cases. 
            return '[%s%s]'%(c.lower(),c.upper()) if c.isalpha() else c

        #print directory + ''.join(map(either,pattern))
        return glob.glob(directory + ''.join(map(either,pattern)) + "*.md")
