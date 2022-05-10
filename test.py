""" function checking and testing 
enviroment for new or complex 
libraries and algorithms """
import os

def fn_map(ip, subnet, filename):
    os.system(f"sudo nmap -O -A -T4 -Pn {ip}/{subnet} >> angel_targets/{filename}.txt")



    