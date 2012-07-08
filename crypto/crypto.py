"""
Text decryption and encryption.
We are using AES-128 with ECB mode.

This code depends on the PyCrypto toolkit - before trying it out, you need to pip install pycrypto.
"""
import unittest2
from Crypto.Cipher import AES



def try_to_decrypt_text(text, enabled, secret_key):
    """
    Tries to decrypt text string.
    If not possible, returns None.
    """
    # If encryption is disabled, do nothing
    if not enabled:
        return text

    # Create cipher
    cipher = AES.new(secret_key, AES.MODE_ECB)

    try:
        # Decode hex encoded message
        decoded_msg = text.decode('hex')

        # Decrypt message
        decrypted_msg = cipher.decrypt(decoded_msg)

        # Strip padding
        n = ord(decrypted_msg[-1])
        unpadded_msg = decrypted_msg[:-n]

        # Decode utf8
        unpadded_msg = unpadded_msg.decode('utf8')

    except Exception:
        return None

    return unpadded_msg



def encrypt_text(text, enabled, secret_key):
    """
    Encrypts text string.
    """
    # If encryption is disabled, do nothing
    if not enabled:
        return text

    # Encode utf8
    text = text.encode('utf8')

    # Create cipher
    cipher = AES.new(secret_key, AES.MODE_ECB)

    # Append PKCS padding to input message
    n = AES.block_size - (len(text) % AES.block_size)
    padded_msg = text + (chr(n) * n)

    # Encrypt message
    encrypted_msg = cipher.encrypt(padded_msg)

    # Encode message with hex encoding
    encoded_msg = encrypted_msg.encode('hex')

    return encoded_msg



class TestEncryption(unittest2.TestCase):
    def test_encryption_and_decryption(self):
        secret_key = '0123456789012345'
        original_text = 'this is some text to test encryption and decription'
        encrypted_text = encrypt_text(text=original_text, enabled=True, secret_key=secret_key)
        decrypted_text = try_to_decrypt_text(text=encrypted_text, enabled=True, secret_key=secret_key)

        self.assertEqual(original_text, decrypted_text)




if __name__ == '__main__':
    unittest2.main()
