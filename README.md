#SrchR v0.1
by @vdbaan (S. van der Baan)

### About
SrchR is a rewrite of Findsploit v1.4 (by 1N3 - https://github.com/1N3/findsploit) but then in Python. It uses a configuration file to remember where the various locations are that will be searched. This version is without copysploit or compilesploit as you should be able to do that yourselves.

### Help
```
root@kali:/# findsploit 

  ______   _______      ______  ____  ____  _______     
.' ____ \ |_   __ \   .' ___  ||_   ||   _||_   __ \    
| (___ \_|  | |__) | / .'   \_|  | |__| |    | |__) |   
 _.____`.   |  __ /  | |         |  __  |    |  __ /    
| \____) | _| |  \ \_\ `.___.'\ _| |  | |_  _| |  \ \_  
 \______.'|____| |___|`.____ .'|____||____||____| |___|              

  - v0.1 by S. van der Baan 
Based on Findsploit by 1N3 (https://github.com/1N3/findsploit)

Usage: ./srchr.py [-b] <ARG ...>

        -b       Also search in browser
        ARG ...  One or more arguments to search for

```
### Example
```
root@kali:/# findsploit MS08 67

  ______   _______      ______  ____  ____  _______     
.' ____ \ |_   __ \   .' ___  ||_   ||   _||_   __ \    
| (___ \_|  | |__) | / .'   \_|  | |__| |    | |__) |   
 _.____`.   |  __ /  | |         |  __  |    |  __ /    
| \____) | _| |  \ \_\ `.___.'\ _| |  | |_  _| |  \ \_  
 \______.'|____| |___|`.____ .'|____||____||____| |___|              

  - v0.1 by S. van der Baan 
Based on Findsploit by 1N3 (https://github.com/1N3/findsploit)

[*] Searching for: MS08 67

[-] Searching in NMap scripts ...
------------------------------------------------------------------------------------------------
/usr/local/share/nmap/scripts/smb-vuln-ms08-067.nse
------------------------------------------------------------------------------------------------

[-] Searching in Exploit-DB ...
------------------------------------------------- ----------------------------------------------
 Exploit Title                                   |  Path
                                                 | (/pentest/exploitation/exploit-db/platforms)
------------------------------------------------- ----------------------------------------------
Microsoft Windows GDI+ - PoC (MS08-052) (2)      | ./windows/dos/6716.pl
------------------------------------------------- ----------------------------------------------

[-] Searching in MetaSploit ...
------------------------------------------------------------------------------------------------
/opt/metasploit-framework/embedded/framework/modules/exploits/windows/smb/ms08_067_netapi.rb
------------------------------------------------------------------------------------------------

[-] Searching in SEToolKit ...
------------------------------------------------------------------------------------------------
/pentest/exploitation/setoolkit/src/fasttrack/exploits/ms08067.py
------------------------------------------------------------------------------------------------

[*] Done.

```
