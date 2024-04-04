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
## challenge 18
```
mov rax, [rdi]
mov rbx, [rdi + 8] ; here + 8 represents the offset, they said the next quat word,and in a quadword there are 64 bytes which is 8 * 8 bytes. If they said a   
                   ; doubleword the off set would have been + 4 because 32 = 8 * 4  
add rax, rbx
mov [rsi], rax
```
## challenge 19
```
pop rax
sub rax, rdi
push rax
```
## challenge 20
```
push rdi ; let rdi and rsi bea two values, so if we push rdi and then rsi into the stack, the last element in stack is rsi. now if we pop it and store in rdi, we  
         ;have sucessfully placed valure of rdi in rsi
push rsi
pop rdi
pop rsi
```
## challenge 21
```
mov rax, [rsp]
mov rbx, [rsp + 8]
mov rcx, [rsp + 16]
mov rdx, [rsp + 24]
add rax, rbx
add rcx, rdx
add rax, rcx
xor rdx, rdx  ; here we ensure rdx is zero because while performing division it concatenates rdx and rax. and with idiv rcx instruction, it divides the value in 
              ; rax with the value in rcx register. 
mov rcx, 4 
idiv rcx
push rax      ; Pushing back the value into stack
```
## challenge 22
```
mov rax, 0x403000
jmp rax
```
## challenge 23
```
jmp target
.rept 0x51 ; here though jmp target directly jumps the control flow to the target label, it is required that the instruction has to be after 0x51 bytes, so we use 
           ; nop and rept
nop
.endr
target:
mov rax, 0x1
```
## challenge 24
```
jmp target
.rept 0x51
nop
.endr
target:
pop rdi
mov rax, 0x403000
jmp rax
```
## challenge 25
```
mov ebx,[rdi+4]
mov ecx,[rdi+8]
mov edx,[rdi+12]
mov eax,[rdi]
cmp eax,0x7f454c46
jne down1
add ebx,ecx
add ebx,edx
jmp done
down1:
cmp eax,0x00005A4D
jne down2
sub ebx,ecx
sub ebx,edx
jmp done
down2:
imul ebx,ecx
imul ebx,edx
jmp done
done:
mov eax,ebx
```

