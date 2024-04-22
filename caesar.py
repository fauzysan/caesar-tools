

def encrypt(key, msg):

    enc = ""
    for char in msg:
        if char.isalpha():
            if char.isupper():
                enc_char = chr((ord(char) - ord('A' ) + key) % 26 + ord('A'))
            else:
                enc_char = chr((ord(char) - ord('a' ) + key) % 26 + ord('a'))
        else:
            enc_char = char
        enc += enc_char
    return enc

def decrypt(key, c):

    dec = ""
    for char in c:
        if char.isalpha():
            if char.isupper():
                dec_char = chr((ord(char) - ord('A' ) - key) % 26 + ord('A'))
            else:
                dec_char = chr((ord(char) - ord('a' ) - key) % 26 + ord('a'))
        else:
            dec_char = char
        dec += dec_char
    return dec
def brute_force(n, c):
    for i in range(n):
        brute_enc = decrypt(i, c)
        
        print(f"[{i+1}]{brute_enc}")
    


if __name__ == "__main__":

    while True:
        print("""\n
        <!-----TOOLS UNTUK ENCRYPTION AND DECRYPTION CAESAR CIPHER------!>
            [1]Encrypt
            [2]Decrypt
            [0]exit\n
""")
        option = int(input("Masukan pilihan: "))

        if option == 1:
            plaintext = input("Masukan Pesan: ")
            key = int(input("Masukan Kunci: "))
            Enc = encrypt(key, plaintext)
            print(f"Plaintext: {plaintext}\nKunci:{key}\nPesan Enckripsi:{Enc}")
        
        elif option == 2:
            cipher = input("Masukan Pesan Cipher: ")
            option_brute = input("Apakah mau bruteforce Key?y/n: ")
            if option_brute.upper() == "Y":
                n = int(input("Masukan panjang key: "))
                brute = brute_force(n, cipher)
                print(brute)
            else:
                key = int(input("Masukan Kunci: "))
                Dec = decrypt(key, cipher)
                print(f"Pesan Cipher:{cipher}\nKunci:{key}\nPesan Deckripsi:{Dec}")
        elif option == 0:
            break
        else:
            print("Masukan Angka Yang Ada Di Pilihan")
