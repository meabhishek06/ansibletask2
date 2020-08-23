import os
os.system("ansible-playbook galaxylaunch.yml")
os.system("ansible-playbook --private-key=linuxlw.pem -u ec2-user galaxy2.yml --ask-become-pass --become")
