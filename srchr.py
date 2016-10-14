#!/usr/bin/env python
import os,sys
import ConfigParser

try:
    input = raw_input
except NameError:
    pass


banner = '''
  ______   _______      ______  ____  ____  _______     
.' ____ \ |_   __ \   .' ___  ||_   ||   _||_   __ \    
| (___ \_|  | |__) | / .'   \_|  | |__| |    | |__) |   
 _.____`.   |  __ /  | |         |  __  |    |  __ /    
| \____) | _| |  \ \_\ `.___.'\ _| |  | |_  _| |  \ \_  
 \______.'|____| |___|`.____ .'|____||____||____| |___|              
'''

attr = '''Based on Findsploit by 1N3 (https://github.com/1N3/findsploit)'''

version = '0.1'
class bcolors:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERL = '\033[4m'
    ENDC = '\033[0m'
    backBlack = '\033[40m'
    backRed = '\033[41m'
    backGreen = '\033[42m'
    backYellow = '\033[43m'
    backBlue = '\033[44m'
    backMagenta = '\033[45m'
    backCyan = '\033[46m'
    backWhite = '\033[47m'



# main status calls for print functions
def print_special(indicator,message,spaces=''):
    print bcolors.BLUE + bcolors.BOLD + spaces + "["+indicator+"] " + bcolors.ENDC + str(message)

def print_special_warning(indicator,message,spaces=''):
    print bcolors.YELLOW + bcolors.BOLD + spaces + "["+indicator+"] " + bcolors.ENDC + str(message)

def print_special_status(indicator,message,spaces=''):
    print bcolors.GREEN + bcolors.BOLD + spaces + "["+indicator+"] " + bcolors.ENDC + str(message)

def print_special_error(indicator,message,spaces=''):
    print bcolors.RED + bcolors.BOLD + spaces + "["+indicator+"] " + bcolors.ENDC + str(message)

def print_status(message):
    print_special_status('*',message)

def print_info(message):
    print_special('-',message)

def print_info_spaces(message):
     print_special('-',message,spaces='  ')

def print_warning(message):
    print_special_warning('!',message)

def print_error(message):
    print_special_error('!',message)



def getTerminalSize():
    import os
    env = os.environ
    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct, os
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,
        '1234'))
        except:
            return
        return cr
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        cr = (env.get('LINES', 25), env.get('COLUMNS', 80))
    return int(cr[1]), int(cr[0])

def check_config():
    SCRIPT_ROOT = os.path.dirname(os.path.realpath(__file__))
    myconfigfile = '%s/srchr.cfg'%SCRIPT_ROOT
    config = ConfigParser.RawConfigParser()  
    config.read(myconfigfile)
    if len(config.sections()) == 0:
        config.add_section('srchr')
        # check nmap location for scripts '/usr/local/share/nmap/scripts'
        config.set('srchr','nmap-location',input('Enter location of the nmap scripts [/usr/local/share/nmap/scripts]') or '/usr/local/share/nmap/scripts')
        # check exploit-db location '/pentest/exploitation/exploit-db'
        config.set('srchr','exploitdb',input('Enter location of exploit-db [/pentest/exploitation/exploit-db]') or '/pentest/exploitation/exploit-db')
        # check metasploit location '/opt/metasploit-framework'
        config.set('srchr','metasploit',input('Enter location of metasploit [/opt/metasploit-framework]') or '/opt/metasploit-framework')
        # check setoolkit location '/pentest/exploitation/setoolkit'
        config.set('srchr','setoolkit',input('Enter location of metasploit [/pentest/exploitation/setoolkit]') or '/pentest/exploitation/setoolkit')
        with open(myconfigfile, 'wb') as configfile:
            config.write(configfile)
    return config

def help():
    print("Usage: %s [-b] <ARG ...>"%__file__)
    print("")
    print("        -b       Also search in browser")
    print("        ARG ...  One or more arguments to search for")
    exit()

def build_nmap(nmap,sargv):
    result = ""
    result += "fgrep -ri %s %s"%(sargv[0],nmap)
    for arg in sargv[1:]:
        result += "|fgrep -i %s"%arg
    result += '|cut -d \':\' -f1|sort|uniq|grep --color=always -ie "%s"'%('\\|'.join(sargv))
    return result

if __name__ == "__main__":
    os.system('clear')
    print (bcolors.YELLOW + bcolors.BOLD +banner+ bcolors.ENDC)
    print (bcolors.RED + bcolors.BOLD +'  - v%s by S. van der Baan '%version+ bcolors.ENDC)
    print (bcolors.BLUE + bcolors.BOLD +attr+ bcolors.ENDC)
    
    print('')
    config = check_config()     
    args = sys.argv
    use_browser = False
    if '-b' in args:
        use_browser = True
        args.remove('-b')
    if (len(args) == 1):
        help()
    (width, height) = getTerminalSize()
    del args[0]
    print_status('Searching for: '+' '.join(args))
    print('')
    print_info("Searching in NMap scripts ...")
    print ("-" * width)
    os.system(build_nmap(config.get('srchr','nmap-location'),args))
    print ("-" * width)
    print('')
    print_info("Searching in Exploit-DB ...")
    os.system('%s/searchsploit %s'%(config.get('srchr','exploitdb')," ".join(args)))
    print('')
    print_info("Searching in MetaSploit ...")
    print ("-" * width)
    os.system(build_nmap('%s/embedded/framework/modules'%config.get('srchr','metasploit'),args))
    print ("-" * width)
    print('')
    print_info("Searching in SEToolKit ...")
    print ("-" * width)
    os.system(build_nmap('%s/src'%config.get('srchr','setoolkit'),args))
    print ("-" * width)

    if use_browser:
        print('')
        print_info("Making your browser search too ...")
        os.system('xdg-open http://www.google.com/search?q=%s+exploit 1>/dev/null'%('\'%20\''.join(args)))
        os.system('xdg-open http://www.google.com/search?q=%s+exploit+site:www.securityfocus.com 1>/dev/null'%('\'%20\''.join(args)))
        os.system('xdg-open http://www.google.com/search?q=%s+site:0day.today 1>/dev/null'%('\'%20\''.join(args)))
        os.system('xdg-open http://www.google.com/search?q=%s+site:www.security-database.com 1>/dev/null'%('\'%20\''.join(args)))
        os.system('xdg-open http://www.google.com/search?q=%s+site:packetstormsecurity.com 1>/dev/null'%('%20'.join(args)))
        os.system('xdg-open https://exploits.shodan.io?q=%s 1>/dev/null'%('\'%20\''.join(args)))
    print('')
    print_status('Done.')
    print('')
    