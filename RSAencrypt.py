import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5


def rsa_encrypt(plaintext, pub_key):
    message = plaintext.encode("utf-8")
    length = len(message)
    default_length = 117
    rsakey = RSA.importKey(pub_key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    if length <= default_length:
        return default_rsa_encrypt(cipher, message)
    offset = 0
    result = []
    while length - offset > 0:
        if length - offset > default_length:
            result.append(default_rsa_encrypt(
                cipher, message[offset:offset + default_length]))
        else:
            result.append(default_rsa_encrypt(cipher, message[offset:]))
        offset += default_length
    return "\n".join(result)


def default_rsa_encrypt(cipher, message):
    ciphertext = base64.b64encode(cipher.encrypt(message))
    ciphertext_decode = ciphertext.decode("utf-8")
    return ciphertext_decode


# 调用时需要加上-----BEGIN PUBLIC KEY-----\n
#              \n-----END PUBLIC KEY-----

a = """-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAo0z/L+pelCPu6DwDFAY/3ITzesr8lnNmYjHht4XUJvLYYBwvDbHMc8xi9sPK9ohVHIKRVLVmmZ9SdmuWYN9HzCyyZ6kEHx+IDBPnulwjdeN/N0w25mVRhYDWxJ2/1C6cPIuNcISchOQdGKuAC0xR37i/kWH9sjBidAQjageYgQoj1HX81flZaPve75Esue85AHZ0VIurjwx7uEuxvQtvCIUvX1bbF13TIYuTbJbn/LrNHby1Kxp42ggNUjAkYUVSF7SC3UP+YGKruii7Vh1UnJ/rpVhjdt3It8le9px8H4Ltt9N3hzU17rBnFpp2ZnmiZVtlfMvsStY54Fl5cSJVxQIDAQAB\n-----END PUBLIC KEY-----"""
r = rsa_encrypt("Gong#0310", a)
# from urllib.parse import quote

print(r)
# Q/EfB6xHGPHd75iRS+baE33DTC/S/cgQ6RyGv9O1RGl118g4SDvEghq+XbqhMM5f0r3dY1U/Jxwi5VqNjD1NeIW/mYe6RrkXQTiZKP9cLjlcBW8Q2nLmXiJf/4kmmCsJxy674MouLEp2IT/E033Xa0rZ5gm3CrLTRHjuAh3gB/LriiY40B01SXPtzZv0MxWCyxT+zOHUgeTLHf3k9mR9/81y/y8w67oZBd2nwpJUt0n3/m/5hqimvkF2ZEVwtcj7Bj8r2CM5e0ulelc3J5cmP92DK4TaqsldkBSQH8+skDnID11shjltHrpKbhpUp6KkGwzpYkGs+ntmhGxWUSCFYQ==
