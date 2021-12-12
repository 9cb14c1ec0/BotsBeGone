#BotsBeGone
Threat intel on current botnets seeking to ensnare your linux servers.  Daily
updates to firewall rules keep you protected.

##Prerequites
BotsBeGone depends on the `ufw` and `git` utilities to manage firewall.  Installation 
will fail if `ufw` or `git` are not present.  This software has only been tested on Debian
based distros and may fail to run on anything else.

##Installation
To install, run these commands as root.
```commandline
git clone https://github.com/9cb14c1ec0/BotsBeGone
cd BotsBeGone
python3 install.py
```

##Disclaimer
BotsBeGone will not block all botnets out there.  You should not depend on this
software as your only line of defense.  THIS IS NOT A SUBSITUTE FOR BASIC SECURITY
PRECAUTIONS LIKE STRONG PASSWORDS.

##License

The MIT License (MIT) Copyright © 2021 Edwin Zimmerman, https://github.com/9cb14c1ec0 


Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to
deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: 
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. 
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE