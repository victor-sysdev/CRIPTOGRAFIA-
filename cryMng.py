print(r"""
███╗   ███╗ █████╗ ███████╗███████╗
████╗ ████║██╔══██╗██╔════╝██╔════╝
██╔████╔██║███████║███████╗█████╗  
██║╚██╔╝██║██╔══██║╚════██║██╔══╝  
██║ ╚═╝ ██║██║  ██║███████║███████╗
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝

        CRIPTOGRAFIA
""")


from cryptography.fernet import Fernet 
import gpg 

print(r"  === Chave Simétrica ===   ")

cipher_input = input("Qual e a mensagem que vc deseja criptografar?") 
key = Fernet.generate_key()
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(cipher_input.encode())
plain_text = cipher_suite.decrypt(cipher_text)

print("Text criptografado: " , cipher_text)
print("Text descriptografado: " , plain_text)


print(r"  === Chave Assimétrica ===   ")


