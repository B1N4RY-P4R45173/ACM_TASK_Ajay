# Level 0
The password for level 1 can be obtained by inspecting the web page and checking the body of it. The password has been commented out.

password is `g9D9cREhslqBKtcA2uocGHPfMZVzeFK6`

# Level 1
Again in this we can get the passwording by inspecting the webpage, but since the right click is disabled use the shortcut key to open up inspect menu.

password is `h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7`
# Level 2
Once again we need to inspect the web page, and there we can see an image source has been given to load it, so i checked the path of it. The path was
`/files/image.png`.After that I moved to the previous directory that `/files` and there I found users.txt, after checking that file I found the password for next 
level.

password is `G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q`

# Level 3
In this level after inspecting the webpage, we can see a commenting that not even google can find this. This mostly indicates that we need to check for robots.txt.
There I found the line `Disallow: /s3cr3t/`. And after navigating to `http://natas3.natas.labs.overthewire.org/s3cr3t/`. I found the users.txt which contained the 
password.

password is `tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm`

# Level 4
In this level we see that it only allows users from natas5. So we use burpsuite to intercept the request and change the refrer to 
"http://natas5.natas.labs.overthewire.org/". And now we have the password.

password is `Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD`

# Level 5
Similar to previous level, we just need to change the cookie:logedin to 1. And we get password to the next level.

password is `fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR`

# Level 6
In this level we are asked for secret prompt, they have given us the source code. After inspecting the first line of the code, `include "includes/secret.inc";` 
we see that it is importing the contents of that file. So I visit the webpage: `http://natas6.natas.labs.overthewire.org/includes/secret.inc`. Which clearly 
contains the secret key. The secret is `FOEIUWGHFEEUHOFUOIU`.

password is `jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr`

# Level 7
In this level, when we inspect the webpage we find that the password to natas is stored in `/etc/natas_webpass/natas8`. And also we two links, one of which links to
'home' page and the other page links us to 'about' page. If we look at the url, the url mentions `page=` which loads these pages. If we change the 
`page=/etc/natas_webpass/natas8`. We get the password

password is `a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB`

# Level 8
This level is similar to level 6, where we have to guess the password provided the source code. Consider the following lines in code:
```
$encodedSecret = "3d3d516343746d4d6d6c315669563362"
function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)))
if(encodeSecret($_POST['secret']) == $encodedSecret)
```
So if we just apply the functions in reverse order on 3d3d516343746d4d6d6c315669563362. That is first we apply hex2bin then strrev and at last base64_decode.
After this we should get answer as `oubWYf2kBq`. Entering this in the prompt gives the password to the next question.

password is `Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd`

# Level 9
In this level we can search for a word from dictonary.txt.  Looking at the source, especially at the line `passthru("grep -i $key dictionary.txt");` It is clear that
it has a command injection vulnearbility. So if we type `; cat /etc/natas_webpass/natas10 #`. We get the password to the next level.

password is `D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE`

# Level 10
In this level we can search for a word from dictonary.txt.  Looking at the source we can understand that we cannot use `/[;|&]/`
```
if($key != "") {
    if(preg_match('/[;|&]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i $key dictionary.txt");
```
So We use a wild card.Then if we type `.* /etc/natas_webpass/natas11 #`. We get the password to the next level.

password is `1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg`

