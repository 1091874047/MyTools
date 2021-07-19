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
a = """-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCVWOMgz8bTlahOmH3Tb+WwLwowHWwk4mP1JsF8VhMfShB0QG5Mjh69iRtJvHGUm2IUPypogTMR2yeIKbj8Mwsslpl4uMws+XK4/aw55V9hokEU1jJMPHo9DMJhzmY8w8RO9oIxuSCYOz36xvxz5AEj38L/9z1z9A/LWgV/vVPvQQIDAQAB\n-----END PUBLIC KEY-----"""
r = rsa_encrypt("DAIBKP", a)
print(a)
