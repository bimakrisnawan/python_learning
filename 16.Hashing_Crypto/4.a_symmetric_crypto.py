from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# Generate private and public keys
print('Generating private and public keys…')
key = RSA.generate(2048)

# Save private key to a file
private_key = key.export_key()
with open('my_rsa_private_key.pem', 'wb') as f:
    f.write(private_key)

# Save public key to a file
public_key = key.publickey().export_key()
with open('my_rsa_public_key.pem', 'wb') as f:
    f.write(public_key)

print('Keys generated and saved.')

message = 'hello world from python'
print('Plaintext:', message)

# Encrypt data using the recipient's public key
with open('my_rsa_public_key.pem', 'rb') as f:
    recipient_key = RSA.import_key(f.read())
cipher_rsa = PKCS1_OAEP.new(recipient_key)
encrypted_msg = cipher_rsa.encrypt(message.encode())
print('Encrypted:', binascii.hexlify(encrypted_msg))

# Decrypt data using the private key
with open('my_rsa_private_key.pem', 'rb') as f:
    private_key = RSA.import_key(f.read())
cipher_rsa = PKCS1_OAEP.new(private_key)
decrypted_msg = cipher_rsa.decrypt(encrypted_msg)
print('Decrypted:', decrypted_msg.decode("utf-8"))
