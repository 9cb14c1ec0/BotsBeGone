import os
import stat
import pathlib

data_path = '/var/lib/BotsBeGone'
bin_path = os.path.join(data_path, 'BotsBeGone')

os.mkdir(data_path)
os.system(f'/bin/git -C {data_path} clone https://github.com/9cb14c1ec0/BotsBeGone')

os.chmod(os.path.join(bin_path, 'botsbegone.py'), stat.S_IXOTH | stat.S_IXUSR | stat.S_IXGRP)

os.system(f'cp {os.path.join(bin_path, "botsbegone.timer")} /etc/systemd/system/botsbegone.timer')
os.system(f'cp {os.path.join(bin_path, "botsbegone.service")} /etc/systemd/system/botsbegone.service')
os.system('systemctl daemon-reload')
os.system('systemctl enable --now botsbegone.timer')
