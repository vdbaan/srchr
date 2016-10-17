#SrchR v0.2
by @vdbaan (S. van der Baan)

### About
SrchR is a rewrite of Findsploit v1.4 (by 1N3 - https://github.com/1N3/findsploit) but then in Python. It uses a configuration file to remember where the various locations are that will be searched. This version is without copysploit or compilesploit as you should be able to do that yourselves.

### Credits
1N3 (https://github.com/1N3) - for an awesome idea

### History
0.2 - Added options to be able to target results.
0.1 - Initial version

### Help
```
root@kali:/# findsploit 

  ______   _______      ______  ____  ____  _______     
.' ____ \ |_   __ \   .' ___  ||_   ||   _||_   __ \    
| (___ \_|  | |__) | / .'   \_|  | |__| |    | |__) |   
 _.____`.   |  __ /  | |         |  __  |    |  __ /    
| \____) | _| |  \ \_\ `.___.'\ _| |  | |_  _| |  \ \_  
 \______.'|____| |___|`.____ .'|____||____||____| |___|              

  - v0.2 by S. van der Baan 
Based on Findsploit by 1N3 (https://github.com/1N3/findsploit)

Usage: srchr [-n] [-m] [-e] [-b] ARG ...

optional arguments:
  -h    --help          Show this help message and exit
  -n    --nmap          Search the NMap scripts
  -e    --exploitdb     Searches the exploit db
  -m    --metasploit    Search the Metasploit project
  -s    --setoolkit     Search the SEToolKit project
  -b    --browser       Launch searches in your browser

The default uses: --nmap, --exploitdb, --metasploit and --setoolkit


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

  - v0.2 by S. van der Baan 
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
