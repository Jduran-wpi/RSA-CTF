from hashlib import sha512

#Global variables
n = 169 #Public Key
e = 7 #Constant exponent

def sign():
    msg = input("Enter the message you wish to sign: ").encode('utf8')
    hash = int.from_bytes(msg, byteorder='big') % n
    
    

    #input check for int
    flag = True

    while flag:
        priv_key = input("Enter the private key you wish to use to sign: ")
        
        if priv_key.strip().isdigit():
            d = int(priv_key)
            signature = pow(hash, d,n)
            print("Hash: ", hash)
            print("Signature Int: ", signature)
            print("Signature:", hex(signature))
            flag = False
        else:
            print("User input is not an integer!")
        
    
def main():
    sign()

if __name__ == "__main__":
    main()
