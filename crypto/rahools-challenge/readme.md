# Space Heroes CTF: Rahool's Challenge
### Description
`nc 0.cloud.chals.io 10294` \
**Author**: excaligator

<details closed>
<summary>Solution</summary>

  ### Detailed Solution:
  Let's open that `netcat` link to see what's going on:
  ```
root@kali:/home/kali/shctf# nc 0.cloud.chals.io 10294
                                   ,/(####((((/**.                                                  
                             *#%%%%%%%%%%%%%%########(#####((((/*,                                  
                          ,&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%#(##((((///*                              
                       .#&&&&&&&&&&&&&&&&&%%%%%%%%%&&%%%%###((((*,.     ...                          
                     .%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%%%%%%%,.,               .                       
                     #&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%%%%,,,, .. ..             .                    
                    *&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#,*,*,,,,..,                .                  
                   .%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&(*****,//,..., ,.  .  .,..                       
                   %&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&,****,***,*.****... .*//((((/,                    
                  (&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#,***//**,**,*,***,,*((/////(##(*                   
                 *&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&/,****,**,**,,*,*,,/##/////((/(%#/.,                 
                 %&&&&&&&&&&&&&&&&&&&&&&&&&&&&&,,*********/,,*/*,/%&########%%#(%/..                 
                (&&&&&&&&&&&&&&&&&&&&&&&&&&&&#,,,,***,**,**//*,,(&%###%%%%%#((&&%%(.                 
               .&&&&&&&&&&&&&&&&&&&&&&&&&&&&****,*/,*,**/***,,,%&####%&%%%%#/*#&&&(/,                
               #&&&&&&&&&&&&&&&&&&&&&&&&&&&,*,,,*/,**///*,**,/&&#(*.,%%%(/(%(#(&&&#(.                
              .&&&&&&&&&&&&&&&&&&&&&&&&&&(,*,**********/,**/%&&%%%(. .###(/*/(%&&&#*,                
              #&&&&&&&&&&&&&&&&&&&&&&&&@*,**,**,,/*/*,,,,/&@&#%%%##(,  ,,,,.. /&&&/,,                
              %&&&&&&&&&&&&&&&&&&&&&&&&,,,**,,,*,*****,/%@@%#####%%#,.    ..  *&&%(.                 
             ,&&&&&&&&&&&&&&&&&&&&&&&&*,*,**/,*,,***,/#@@%((((%#####(,.      .*&&#(,                 
             (&&&@&&&&&&@@&&&&&&&&&&&,,**,,*,/****,*(&@&(((##&&&&&&%##(/,. ...(&&#,                  
             ,&&&&&&&&&&&&&&&&&&&&&,**,***,*,**/#@&###(#((#####((/*,,*,.. ...,&%* .                  
             ,&&&&&&&&&&&&&&&&&&&@****/**/,,***&@&%######%%&&&&%#######%#,,..#&#, .                  
              %&&&&&&&&&&&&&&&&&&%,****/*,,,(&@&&%%%#####(############(*../,.%%(, .                  
              /&&&&&&&&&&&&&&&&&&/,***,***,/&@&%%%%%#########((/*,,,,,,,...,*&#( ,                   
              ,&&&&&&&&&&&&&&&&&&,***,,,**,%@&&&%%%%#########(/*,.       ...#%(/ .                   
              %&&&&&&&&&&&&&&@&&#**,**///*/@&&&&&&&%%%%%%%%#####(/**,,...../%#(,.                    
             (&&&&&&&&&&&&&&&&&@/,*/,/*//**&&&@@@&&&&&&&&%%%%%%%%%%#%#(*,*####(*,                    
            ,%%&&&&&&&&&&&&&&&&&*,*/***/**,%&%&@@@@@@@@@@&&&&&%%%%%%##(, ./(##(,,                    
            **,,*(#&&&&&&&&&&&&#*,/***/*/,,(&#(#(((##%&&&&&&&&&%%####/.   ,/(((*.                    
           ******,,**(%&&&&&&&%/***(******.*%#%%%###(#((((##(*.            ,/((,                     
          ,******,**,,***#%&&&%*,,,/*/,*/*..&%########((((##(/*,.            //.                     
          ,***********//*,,**/(****/*//*//, &&&%#%%%%###(((////(**..         ,///*******,.           
           ((,,****/********/*//***///(/**, %&@&&#(######((((/**, .   .       //#%&&&&&%(***/,       
       ,#&&&&&&%*,*//*****,***/(/**/////***.%@@@@&%##(/(/((((#((/,..    .    .//(#%&&&&%(********    
 @%%%%%&&@@@@@@@@@@(*****//**/*///**/((*/**.&@@@@@&&%%%##(/*,,/..... .     . *((#/*####(/***/********
 &@@@@&%##%%&&&@@@@@@@&(**/*/*///(/////(///.@@@@@@@&&&%%&%###((**/....   ,, .#((#//((#(/***//******/*
 &&%%&@@@@&%%%%%%%%%&&@@@&/*//***/(///(///*.&&@@@@@@@@@&%#%%####((,*,,.,,,  (#(##/(##(******/*****///
 %%%%%&@@&&&&&@@@&&&&%%%%&&@@/****/#(//(//,,&&@&&@@@@@@@@&&%#(#%%/#/.,... ,#((/*//**(******/*****////
 %%%%&&%&&&%%%%%%###%%&&&&&%%%&#*///((///* /&&@@@@@@@@@@@@@@@&%(/*,,.. *#%#*****///**/****/*****////*
 &&&&&&&&&&&&&&&%%%%%%#%######((//////(*(, (&#,(((##(##((##&&&%%#/****//(((%%**//*///((/(/****//(/***
 %%##########((((//(/(///////////(((((///,*////((((((((/(((((#(((((//***///((%%*///////((/(*//(/****/
 &&&&&&&&&&&&&&&&&&&&&&&&%###((((/////////(((((((#(######(((//////(///((//***//&(*///*////((((/**///*
 &&&&&&&&@&&&&&&&&&&&&&&&%####(((((//////(///////((((((///(((((((((((((/////////(&/*/////**/(((/*///*
 &&&&&&&&&&&&&&&&&&&&&&&&&%#((((((((((//////////////////////((((((((((////////////(%/**//*/*///(/////
 &&&&&&&&&&&&&&&&&&&&&%###(#####(((////////***/*/////*////////////////////////////(#&&(**////***/((#(
 &&&&&&&&%&%%%%%%%%#####%%##((((((((/((////////*/*****////////*/*//////////(((####((/##**/****//,


ESDK EDS NFIMNGDJTB XEZVZ OWV KOYRTI KT ZCT BOZ CDIY DIK Z PJ K UNMTV DIK J PJ K AKMD NSUN OWV GPXY 
TEQSGH PWDFX RXKR UNZ P RC B LJJI KOJ VDXXFX MXXRU GAIVB


We've found ourselves an encrypted engram - Can you break the (new and improved) indecipherable cipher?
Message:A + Key:B = 0 + B = O
Enter the answer with no spaces and all upper case:

  ```
  For themed CTFs, I find it really fun to figure out the cultural references in the challenge before solving them. In this case, `Rahool` is a vendor in the *Destiny 2* Tower that can decrypt engrams for you. That's what we'll be doing here.
  
  Immediately, we can tell that the ciphertext underneath the giant Rahool ASCII is substitution. This means that the plaintext is simply substituted by a value determined by the algorithm. Throwing it into this [cipher identifier](https://www.boxentriq.com/code-breaking/cipher-identifier), we find that it is a **Vigenère** cipher.
  
  Before moving on, we need to figure out what the h-e-double-hockey-sticks a Vigenère is.
  
  A Vigenère cipher is a type of encryption that uses both plaintext and a **key**. There are many ways to use this encryption method, but the most common is via **addition** and **table/tabula recta**. 
  
  To encrypt using addition, take the the position in the alphabet of the first letter in the plaintext (make sure it starts at 0, i.e. A = 0, B = 1, C = 2) and add it with the position of your key (if the key was "key", the position would be 11). Then, take the **modulo** 26 (divide by 26 to get the remainder, symbol `%`), as some numbers add up to greater than 26.
  ```
  Plaintext: hello
  Key: key
  h (07) + k (10) = r (17 % 26 = 17)
  e (04) + e (04) = i (08 % 26 = 08)
  l (11) + y (24) = j (35 % 26 = 09)
  l (11) + k (10) = v (21 % 26 = 21)
  o (14) + e (04) = s (18 % 26 = 18)
  Ciphertext: rijvs
  ```
  In a formula, where A is the plaintext's alphabetic position and B is the key's alphabetic position, in that would be:
  ```
  C = (A + B) % 26
  ```
  
  Let's decrypt this using [DCode](https://www.dcode.fr/vigenere-cipher), which can usually decrypt ciphertext without keys using 

</details>
