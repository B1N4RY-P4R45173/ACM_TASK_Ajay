# Introduction
Here the values of n, ct and e are given. Which likely states that it is an rsa encrytion.

# Problem And Solution
Here we are not given the value of private key exponent(d). So it is not possible for us to decrypt it directly with a key. 

But if you notice there is something odd with the value of e. The value of e is very small.After some research I found that

this is one of the simplest attacks on RSA which arises when m^e is less than n(Note:Here m is the message,e the exponent and n the modulus).

When this is the case, the modulo n loses it's significance and the encryption reduces to m^e (Note: normal encryption is (m^e)%n).

Thus ciphertext becomes m^e which implies m is the eth root of ciphertext(eg:2^4=16 implies 2 is the fourth root of 16).

# Code to solve it
[Click Here](https://github.com/koppakaajay/ACM_TASK_Ajay/blob/main/small_e_attack.py) for the code.

# Flag Found

`b'recr{flaggie}'`

