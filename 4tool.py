#!/user/bin/python3

import os

import time

input ("do you went to start this tool ?: ")
name = input ( "what is your name ?: ")
if name == "Hacker" or name =="hacker":
              print("get out")
              exit()
else:
             print("""
             #### ######   ######
#     #     ##    #        #    #    #      #
 #   # #   # #### #        #    #   # #    # #
  # #   # #  #    #        #    #  #   #  #   #
   #     #   #### #######  ###### #     #      #
             """)
print("select option")

name = input ("""
1.metasploit frame work
2.PassGen
3.keylogger
4.T-Header
""")
if name == "1":
                            print("##installing metasploit##")
                            os.system("pkg install wget")
                            os.system("git clone https://github.com/gushmazuko/metasploit_in_termux/raw/master/metasploit.sh
")
                            exit()
if name == "2":
                            print("installing PassGen")
                            os.system("https://github.com/Broham/PassGen.git")
                            exit()
if name == "3":
                            print("installing keylogger")
                            os.system("https://github.com/GiacomoLaw/Keylogger.git")
                            exit()
if name == "4":
                            print("installing T-Header")
                            os.system("git clone https://github.com/remo7777/T-Header.git")                         