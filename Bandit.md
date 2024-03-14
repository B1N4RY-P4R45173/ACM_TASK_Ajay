# Bandit
# Challenge Description:
we need to complete till 20 levels of Bandit OverTheWire.
# Approach:
##  Level 0:
Using `ssh bandit0@bandit.lab.overthewire.org -p 2220` we connect to the host.

Using ls command we find a readme file.

using `cat readme` we get the password to level 1.
Password: NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL
##  Level 1:
Using `cat ./-` we get the password.

Password: rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi
##  Level 2:
Using `cat 'spaces in this filename'` we read the file and get the password.

Password: aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG
##  Level 3:
We can access the inhere dir using cd inhere and use `ls -al`

Password: 2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe

##  Level 4:
We use `file ./*` to check the file types of all files in the dir.

We find file07 has human readable text.

We use `cat ./-file07`

Password: lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR

##  Level 5:
We need to check for a specific executable file of size 1033 bytes.

Using `find -type f -size 1033c` we find which dir the file we need is in. I just found the file without using execution command and the attribut "c" at the last of 1033 is to make sure it reads in bytes.

We use cat to read the password.

Password: P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU

##  Level 6:
We use `find / -user bandit7 -group bandit6 -size 33c` to find the file containing the file.

Using `cat /var/lib/dpkg/info/bandit7.password` we read the password.

Password: z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S

##  Level 7:
We use `cat data.txt | grep millionth` to find the password in data.txt.

Password: TESKZC0XvTetK0S9xNwm25STk5iWrBvP
##  Level 8:
We use `sort data.txt | uniq -u` to find the password.

Password: EN632PlfYiZbn3PhVK3XOGSlNInNE00t
##  Level 9:
We use `strings data.txt | grep ===` to find the strings in the file which are followed by several '=' characters. I just entered 3 = symbol because it said it ahdd many, so i thought i could narraow it down with this

Password: G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s
##  Level 10:
The password in data.txt is base64 encoded.

We use `cat data.txt | base64 --decode` to pipe the contents of data.txt to the base64 decoding command.

This gives us the string "The password is 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM"

Password: 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM
##  Level 11:
Reading data.txt with cat, I got a rot13 encrypted string.

I Used an online tool we decrypt the string and get the password.

Password: JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv
##  Level 12:
We create a dir using mkdir to handle the files. `mkdir /tmp/hex`

We use `cp data.txt /tmp/hex` command to copy data.txt to the dir we created.

Using `xxd -r data.txt > data` we reverse the hexdump to the original file.

I used `file data` to know the file type (gzip)

We rename data to data.gz and extract it using `gzip -d data.gz`

Now I used file command and found it's type is bzip2.

I used mv to rename the file to data.bz2.

We extract from it by using `bzip2 -d data.bz2`

Now the file type is tar.

I used `tar xf data.tar` after `mv data5bin data.tar`

Now the file is bz2.

We repeat this until we get the file type as ASCII text.

`cat data` gives us the password as wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw
##  Level 13:
For this level we are given an RSA key sshkey.private

We use `ssh -i sshkey.private bandit14@localhost` to use the key as a password.

Password: fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq
##  Level 14:
We use `cat /etc/bandit_pass/bandit14` to get the password.

I then did  `echo fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq | nc localhost 30000` to submit the password.

We get the password for level 15.

Password: jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt
##  Level 15:
We read `cat /etc/bandit_pass/bandit15` to read the password.

We use `openssl s_client -connect localhost:30001` to connect to the port and enter the password.

Password: JQttfApK4SeyHwDlI9SXGR50qclOAil1
##  Level 16:
We use `nmap -A localhost -p 31000-32000` to find out with port speaks ssl.

The required port is 31790

We use `openssl s_client -connect localhost:31790` to connect to port 31790

Entering the password gives us an 'RSA Private Key'.

Then just copy the key and create a text file, paste the RSA key in it and save it.

Use `ssh -i "file name" bandit17@bandit.labs.overthewire.org -p 2220` to connect to the next level.
##  Level 17:
We use the above RSA key to connect using to this level.

This level contains 2 files passwords.old and passwords.new.

We can find the changed line using `diff passwords.old passwords.new`

Alternatively we can use `grep -vf passwords.old passwords.new`

Password: hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg
##  Level 18:
This level uses .bashrc to kick you out after entering the password.

We can bypsass this using `ssh -t bandit18@bandit.labs.overthewire.org -p 2220 /bin/sh`

-t allows a pseudo-terminal to run which allows the terminal to open another shell.

Password: awhqfNnAbc1naukrpqDYcF95h7HoMTrC
##  Level 19:
We can use `ls -la` to list file perms and owners.

We see that bandit19 can execute the bandit20-do file.

Executing bandit20-do tells us that it runs a command as another user.

I used `./bandit20-do cat /etc/bandit_pass/bandit20` to get the password.

Password: VxCazJaVykI6W36BkBU0mJTCM8rR95XT

##  level 20:
We find a file called 'suconnect' which connects to a given port and returns the next password if it receives the correct password.

`echo 'VxCazJaVykI6W36BkBU0mJTCM8rR95XT' | nc -lp 1234 &`

We use echo to pipe the password to netcat which we use to listen on the port 1234.
Here we can enter any random port instead of 1234.

The '&' allows the command to run in the background.

Next, we use `./suconnect 1234` to get the next password.

Password: NvEJF7oVjkddltPSrdKEFOllh9V1IBcq
