
import argparse
import os
import glob  ## used by insensitive_glob

class BioTLDR:
    def __init__(self):
        """Initiate BioTLDR"""

    def cmd(self, exe_folder, dict_arg):
        """Find the corresponding md file"""
        db_folder = exe_folder + "/database/"
        mds = self.insensitive_glob(db_folder, dict_arg['command'])
        print mds


    def insensitive_glob(self, directory, pattern):
        def either(c):
            return '[%s%s]'%(c.lower(),c.upper()) if c.isalpha() else c
        #print directory + ''.join(map(either,pattern))
        return glob.glob(directory + ''.join(map(either,pattern)) + "*.md")



def max(array):
    maximum = 0
    for num in array:
       if num > maximum:
           maximum = num
    return maximum

xxxx = [1,6,210, 100]

c = max(xxxx)
print c
