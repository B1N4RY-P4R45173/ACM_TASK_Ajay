# Level 1
## Introduction
In this we are are directly given the flag.
## Flag Found
`crypto{y0ur_f1rst_fl4g}`

# Level 2
## Introduction
In this level we are given a python code, which iterates through a list and xors each value with 0x32 (decimal value 50).
## Process
In this we just need to run the python code to get the flag :)

```
ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]
print("Here is your flag:")
print("".join(chr(o ^ 0x32) for o in ords))
```
## Flag Found 
`crypto{z3n_0f_pyth0n}`

# Level 3
## Introduction
In this level we are given an array of integer values which are to be converted to their respective ascii values.
## Process
I made some minute changes to the previous code to get flag for this level.
```
ords = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125] # Copied ascii values to this list
print("Here is your flag:")
print("".join(chr(o) for o in ords)) # Used a list comprehension and chr() function to convert integers to their respective letters.
```
## Flag Found
`crypto{ASCII_pr1nt4bl3}`

# Level 4
## Introduction
In this level we need to get the bytes from a hex value
## Process
Wrote a simple python code to do this
```
hex = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d" # Copied the Hex
print (bytes.fromhex(hex)) # Converted it into bytes
```
## Flag Found
`crypto{You_will_be_working_with_hex_strings_a_lot}`

# Level 5
## Introduction
In this level we need to convert the hex into bytes and encode them with base 64 to get the flag.
## Process
Wrote a simple python code to do this
```
import base64 # imports the base 64
hex = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf" # Copied the hex
bas64 = bytes.fromhex(hex)                                    #converts into bytes
print (base64.b64encode(bas64))                               #encodes into base 64
```
## Flag found
`crypto/Base+64+Encoding+is+Web+Safe/`

# Level 6
## Introduction
In this level we need to convert an integer back into a message.
## Process
Wrote a simple python code to do this
```
from Crypto.Util.number import * # to import everything from PyCryptodome
a = 11515195063862318899931685488813747395775516287289682636499965282714637259206269 # Copied the number to a variable
print(long_to_bytes(a)) # Converted it into bytes
```
## Flag Found
`crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}`

# Level 7
## Introduction
This is similar to level where we xor each letter in the string "label" with 13
## Process
Wrote a simple python code to do this
`print("Here is your flag:\ncrypto{"+"".join(chr(ord(o) ^ 13) for o in "label")+ "}") # prints the flag by converting letters into their ascii values and joining the characters after getting the asii numbers again`
## Flag Found
`crypto{aloha}`

# Level 8
## Introduction
In this level we need to find the flag by using xor's properties. Here we are given multiple hex codes and we need to xor key1,key2,key3 with flag,key1,key2,key3 to geth the flag.
## Process
Wrote a simple python code to do this
```
from pwn import xor # imports xor module from pwn
KEY1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313") # Converts it into bytes
KEY2_KEY3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1") # Converts it into bytes
FLAG_KEY1_KEY3_KEY2 = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf") # Converts it into bytes
print(xor(KEY1,KEY2_KEY3,FLAG_KEY1_KEY3_KEY2)) # xors the three values
```
## Flag Found
`crypto{x0r_i5_ass0c1at1v3}`

# Level 9
## Introduction
In this level we have a cipher text with a single byte xor encryption, Since the maximum value of one byte is 256, so I tried to bruteforce it.
## Process
Wrote a simple python code to do this
```
from pwn import xor
hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
bytes = bytes.fromhex(hex)
for i in range (256):
    xored = str(xor(bytes,i))
    if xored.startswith("b'crypto{"):
        print(xored)
```
## Flag Found
`crypto{0x10_15_my_f4v0ur173_by7e}`

# Level 10
## Introduction
In this level we need to perform crib drag attack, since we know the starting part of the flag, we can xor the hex value with the string "crypto{"
## Process
Wrote two simple python codes to do this

The first code is to find the key.
```
from pwn import xor
hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
bytes = bytes.fromhex(hex)
flag = "crypto{"
print (xor(bytes,flag))
```
With this i got the starting part of the key to be `myXORke` and it is clear that the complete key is `myXORkey`.

So I replaced the word `crypto{` with `myXORkey` in the code. Now the code should look like
```
from pwn import xor
hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
bytes = bytes.fromhex(hex)
flag = "myXORkey"
print (xor(bytes,flag))
```
## Flag Found
`crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}`





