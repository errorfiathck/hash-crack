#!/usr/bind/env python
#_*_ coding: utf8 _*_

import os


#COLORS
RED = '\033[1;31m'
BLUE = '\033[1;34m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
MAGENTA = '\033[1;35m'
WHITE = '\033[1;37m'
CYAN = '\033[1;36m'
END = '\033[0m'
RED_NORMAL = '\033[0;31m'
GREEN_NORMAL = '\033[0;32m'


def banner():
	print(f"""
{WHITE}    __  __           __             {RED_NORMAL}██████╗██████╗  █████╗  ██████╗██╗  ██╗
{WHITE}   / / / /___ ______/ /_           {RED_NORMAL}██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝ 
{WHITE}  / /_/ / __ `/ ___/ __ \   ______ {RED_NORMAL}██║     ██████╔╝███████║██║     █████╔╝  
{WHITE} / __  / /_/ (__  ) / / /  /_____/ {RED_NORMAL}██║     ██╔══██╗██╔══██║██║     ██╔═██╗  
{WHITE}/_/ /_/\__,_/____/_/ /_/           {RED_NORMAL}╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗    
                                    {RED_NORMAL}╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝

\t\t\t\033[1;31m----<\033[0;m \033[1;37mGithub: \033[1;41;37mERROR._.FIAT\033[0;m \033[1;31m>----\033[0;m
""")					

banner()
