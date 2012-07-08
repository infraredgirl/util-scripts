# coding=utf-8

import unittest2
from crypto import encrypt_text, try_to_decrypt_text



class TestEncryption(unittest2.TestCase):
    def test_encryption_and_decryption_enabled(self):
        secret_key = '0123456789012345'
        original_text = u'This is a test of encryption and decription. Here are some unicode chars: šđčćžŠĐČĆŽ.'

        encrypted_text = encrypt_text(text=original_text, enabled=True, secret_key=secret_key)
        decrypted_text = try_to_decrypt_text(text=encrypted_text, enabled=True, secret_key=secret_key)

        self.assertEqual(original_text, decrypted_text)


    def test_encryption_and_decryption_disabled(self):
        secret_key = '0123456789012345'
        original_text = u'This is a test of encryption and decription. Here are some unicode chars: šđčćžŠĐČĆŽ.'

        encrypted_text = encrypt_text(text=original_text, enabled=False, secret_key=secret_key)
        decrypted_text = try_to_decrypt_text(text=encrypted_text, enabled=False, secret_key=secret_key)

        self.assertEqual(original_text, encrypted_text)
        self.assertEqual(original_text, decrypted_text)



if __name__ == '__main__':
    unittest2.main()

