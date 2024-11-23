import os
print('''\033[1;36;40m Welcome to CyberRowX ~ Tony Stark
Your Device Must Be Rooted
If Any Question,
Contact Me On Telegram
Tg_User:@CyberRowX \n''')
os.system("pkg install -y root-repo")
os.system("pkg install -y git tsu python wpa-supplicant pixiewps iw")
os.system("cd ..;git clone https://github.com/CyberRowX/WF")

os.system("cd ..;chmod +x WF/nahid.py")

print("\033[1;34;40mThanks.\nInstallation Done.\nNow Go To Home Directory[~] And Enter This Command :\nsudo python WF/nahid.py -i wlan0 -K")
