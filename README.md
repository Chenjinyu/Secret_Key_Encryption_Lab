# Secret_Key_Encryption_Lab
this is a very simple script for the Secret-Key Encryption Lab for some students who do not have experience with coding.


## Secret-key encryption
openssl has a lot of models to encrypt file to cihper file, decrypt cihper files to plain one.

example:
```
openssl enc --help 
```
there lists Valid ciphername values:
```
-aes-128-cbc              -aes-128-cfb              -aes-128-cfb1            
 -aes-128-cfb8             -aes-128-ctr              -aes-128-ecb             
 -aes-128-gcm              -aes-128-ofb              -aes-128-xts             
 -aes-192-cbc              -aes-192-cfb              -aes-192-cfb1            
 -aes-192-cfb8             -aes-192-ctr              -aes-192-ecb             
 -aes-192-gcm              -aes-192-ofb              -aes-256-cbc             
 -aes-256-cfb              -aes-256-cfb1             -aes-256-cfb8            
 -aes-256-ctr              -aes-256-ecb              -aes-256-gcm             
 -aes-256-ofb              -aes-256-xts              -aes128                  
 -aes192                   -aes256                   -bf                      
 -bf-cbc                   -bf-cfb                   -bf-ecb                  
 -bf-ofb                   -blowfish                 -camellia-128-cbc        
 -camellia-128-cfb         -camellia-128-cfb1        -camellia-128-cfb8       
 -camellia-128-ecb         -camellia-128-ofb         -camellia-192-cbc        
 -camellia-192-cfb         -camellia-192-cfb1        -camellia-192-cfb8       
 -camellia-192-ecb         -camellia-192-ofb         -camellia-256-cbc        
 -camellia-256-cfb         -camellia-256-cfb1        -camellia-256-cfb8       
 -camellia-256-ecb         -camellia-256-ofb         -camellia128             
 -camellia192              -camellia256              -cast                    
 -cast-cbc                 -cast5-cbc                -cast5-cfb               
 -cast5-ecb                -cast5-ofb                -chacha                  
 -des                      -des-cbc                  -des-cfb                 
 -des-cfb1                 -des-cfb8                 -des-ecb                 
 -des-ede                  -des-ede-cbc              -des-ede-cfb             
 -des-ede-ofb              -des-ede3                 -des-ede3-cbc            
 -des-ede3-cfb             -des-ede3-cfb1            -des-ede3-cfb8           
 -des-ede3-ofb             -des-ofb                  -des3                    
 -desx                     -desx-cbc                 -gost89                  
 -gost89-cnt               -gost89-ecb               -id-aes128-GCM           
 -id-aes192-GCM            -id-aes256-GCM            -rc2                     
 -rc2-40-cbc               -rc2-64-cbc               -rc2-cbc                 
 -rc2-cfb                  -rc2-ecb                  -rc2-ofb                 
 -rc4                      -rc4-40                   -rc4-hmac-md5  
```

```
openssl enc -esc-128-cbc -e -in plain.txt -out cipher.bin  -K 00112233445566778889aabbccddeeff -iv 0102030405060708
```

## Substitution cipher and frequency analysis
I provided a python script in the repo, you can get some ideas from the example.
change the char_count in the main function before running the below command
```
python freq_analysis.py
```

## Encryption modes and paddings

## Programming using the crypto library

I will provide the report documenation here in the near future.
