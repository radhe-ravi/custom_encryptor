import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

class CustomEncryptor:
    def __init__(self, secret: str, salt: str, iterations: int = 100_000):
        """
        secret     -> master secret (string)
        salt       -> application-specific salt
        iterations -> must match for encrypt/decrypt
        """
        if not secret or not salt:
            raise ValueError("Secret and salt are required")

        self.iterations = iterations
        self.key = self._derive_key(secret, salt)
        self.cipher = Fernet(self.key)

    def _derive_key(self, secret: str, salt: str) -> bytes:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt.encode(),
            iterations=self.iterations,
        )
        return base64.urlsafe_b64encode(kdf.derive(secret.encode()))

    def encrypt(self, data: str) -> str:
        return self.cipher.encrypt(data.encode()).decode()

    def decrypt(self, token: str) -> str:
        return self.cipher.decrypt(token.encode()).decode()