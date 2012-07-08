crypto
============

Text decryption and encryption.
We are using AES-128 with ECB mode.

Before trying out this code, make sure you install required packages by running:
```
pip install -r requirements.txt
```

To try out encryption and decryption:
```python
from crypto import encrypt_text, try_to_decrypt_text

original_text = 'this is some text'
print 'Original text:', original_text

encrypted_text = encrypt_text(text=original_text, enabled=True, secret_key='key1key1key1key1')
print 'Encrypted text:', encrypted_text

decrypted_text = try_to_decrypt_text(text=encrypted_text, enabled=True, secret_key='key1key1key1key1')
print 'Decrypted text:', decrypted_text

```
