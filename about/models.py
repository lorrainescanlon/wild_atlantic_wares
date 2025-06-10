from django.db import models


class Contact(models.Model):
    """
    A model to create and manage contact messages
    """

    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Contact form {self.name}"
