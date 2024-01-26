from cryptography.fernet import Fernet

from cryptography.fernet import Fernet

# Gere uma chave Fernet válida (32 bytes)
key = Fernet.generate_key()

# Crie um objeto Fernet com a chave gerada
cipher_suite = Fernet(key)

print("Chave gerada:", key)
