from django.db import models
from cryptography.fernet import Fernet

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"



# Generate a key and save it securely in an environment variable
key = Fernet.generate_key()
cipher = Fernet(key)

class PasswordEntry(models.Model):
    website = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    encrypted_password = models.BinaryField()
    created_at = models.DateTimeField(auto_now_add=True)

    def set_password(self, raw_password):
        self.encrypted_password = cipher.encrypt(raw_password.encode())

    def get_password(self):
        return cipher.decrypt(self.encrypted_password).decode()
