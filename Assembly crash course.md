# General Code

```
.global_start
_start:
.intel_syntax noprefix
```
## Challenge 1
```
mov rdi, 0x1337
```
## Challenge 2
```
mov rax, 0x1337
mov r12, 0xCAFED00D1337BEEF
mov rsp, 0x31337
 ```
## chalenge 3
```
add rdi, 0x331337
mov rax, rdi
```
## challenge 4
```
imul rdi, rsi
add rdi, rdx
mov rax, rdi
```
## challenge 5
```
mov rax, rdi
div rsi
```
## challenge 6
```
mov rax, rdi
div rsi
mov rax, rdx
```
## challenge 7
```
mov ah, 0x42
```
## challenge 8
```
mov al, dil
mov bx, si
```
## challenge 9
```
mov rax, rdi
shl rax, 24
shr rax, 56
```
## challenge 10
```
xor rax, rax

and rdi, rsi
add rax, rdi
```

### I have solved upto level 25 but I need more time to write the writeups...
