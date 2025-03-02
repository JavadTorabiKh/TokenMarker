from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    pblicKey = models.CharField(max_length=100)


class Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    token_type = models.CharField(
        max_length=100, choices=[("ERC20", "ERC20"), ("ERC721", "ERC721")])
    count = models.BigIntegerField()
