import sys,setuptools,os
with open("README.md", "r") as fh:
    long_description = fh.read()
os.system('pip uninstall dnspython -y')
os.system('pip install dnspython')
termux=False
if os.path.isdir('/home/')==True:
 os.system('sudo apt install sshpass -y')
 os.system('sudo apt install nodejs -y')
 os.system('sudo apt install expect -y')
if os.path.isdir('/data/data/com.termux/')==True:
    termux=True
if  sys.version_info < (3,0):
 req=["requests","PySocks","bs4","pexpect","paramiko","mysql-connector","scapy","stem","cfscrape"]
 if termux==True:
    req=["requests","PySocks","bs4","mysql-connector","scapy","cfscrape"]
else:
 req=["requests","PySocks","bs4","pexpect","paramiko","mysql-connector","kamene","stem","cfscrape"]
 if termux==True:
    req=["requests","PySocks","bs4","mysql-connector","kamene","cfscrape"]
if termux==True:
 os.system('pkg install sshpass -y')
 os.system('pkg install nodejs -y')
setuptools.setup(
    name="bane",
    version="2.0.9",
    author="AlaBouali",
    author_email="trap.leader.123@gmail.com",
    description="cyber security library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlaBouali/bane",
    python_requires=">=2.7",
    install_requires=req,
    packages=["bane"],
    license="MIT License",
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License ",
    ],
)
