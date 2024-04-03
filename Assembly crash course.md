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
## challenge 11
```
xor rdi, 1
xor rax, rax
xor rax, 1
and rax, rdi
```
## challenge 12
```
mov rax, [0x404000]
```
## challenge 13
```
mov [0x404000], rax
```
## challenge 14
```
mov rax, [0x404000]
mov rdi, [0x404000]
add rdi, 0x1337
mov [0x404000], rdi
```
## challenge 15
```
mov al, [0x404000]
```
## challenge 16
```
mov al, [0x404000]
mov bx, [0x404000]
mov ecx, [0x404000]
mov rdx, [0x404000]
```
## challenge 17
```
mov rax, 0xdeadbeef00001337
mov rbx, 0xc0ffee0000
mov [rdi], rax
mov [rsi], rbx
```

### I have solved upto level 25 but I need more time to write the writeups...
