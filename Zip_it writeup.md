# Introduction
we have to crack a password protected zip file
# Procedure
This is a simple zip file protected by password, so we get the hash of it using the command 

`zip2john flag.zip > zip.hash`

then we can perform a bruteforce attack on it  using the command 

`john zip.hash --wordlist=/usr/share/wordlists/rockyou.txt`

found the password to be marshal

# Flag Found
`recr{found-me!}`
