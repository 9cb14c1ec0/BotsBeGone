import os
import stat
import subprocess

if os.getuid() != 0:
    print('You must be root to install.  Exiting...')
    exit()

if 'not enough args' not in subprocess.getoutput('/sbin/ufw'):
    print('ufw is not installed.  Exiting...')
    exit()

if 'usage: git' not in subprocess.getoutput('/bin/git'):
    print('git is not installed.  Exiting...')
    exit()


data_path = '/var/lib/BotsBeGone'
bin_path = os.path.join(data_path, 'BotsBeGone')

os.mkdir(data_path)
os.system(f'/bin/git -C {data_path} clone https://github.com/9cb14c1ec0/BotsBeGone')

os.system(f'cp {os.path.join(bin_path, "botsbegone.timer")} /etc/systemd/system/botsbegone.timer')
os.system(f'cp {os.path.join(bin_path, "botsbegone.service")} /etc/systemd/system/botsbegone.service')
os.system('systemctl daemon-reload')
os.system('systemctl enable --now botsbegone.timer')

# do initial run
os.system('/bin/python3 /var/lib/BotsBeGone/BotsBeGone/botsbegone.py')
