def encrypt(message, shift):
    if str(shift).isdigit():
        scrambled=''
        for char in message:
            if char.isalpha():
                char=ord(char)
                char+=shift
                if char>122:
                    char-=26
                char=chr(char)
                scrambled+=char
            else:
                scrambled+=char
        return scrambled
    else:
        scrambled=''
        n=0
        shiftlist=[]
        for let in shift:
            let=ord(let)-97
            shiftlist.append(let)
        for char in message:
            if char.isalpha():
                 char=ord(char)
                 char+=shiftlist[n]
                 if char>122:
                     char-=26
                 char=chr(char)
                 n+=1
                 scrambled+=char
                 if n>=len(shiftlist):
                     n=0
            else:
                scrambled+=char
                
        return scrambled
def decrypt(scrambled, shift):
   message=''
   if str(shift).isdigit():
       for char in scrambled:
           if char.isalpha():
               char=ord(char)
               char-=shift
               if char<97:
                   char+=26
               char=chr(char)
               message+=char
           else:
               message+=char
   else:
       n=0
       shiftlist=[]
       for let in shift:
           let=ord(let)-97
           shiftlist.append(let)
       for char in scrambled:
           if char.isalpha():
               char=ord(char)
               char-=shiftlist[n]
               if char<97:
                   char+=26
               char=chr(char)
               n+=1
               message+=char
               if n>=len(shiftlist):
                   n=0
   return message
def main():
    message=input("Enter message to encrypt: ")
    shift=input("Enter encryptor: ")
    if shift.isdigit():
        shift=int(shift)
    scrambled=encrypt(message, shift)
    nmessage=decrypt(scrambled, shift)
    print("Encrypted message is "+scrambled)
    print("Decrypted message is "+message)
    if 'y' in input('Would you like to encrypt another message?\n').lower():
        main()
    else:
        quit()
main()
