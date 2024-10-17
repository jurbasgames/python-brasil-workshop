from django.db import models


class Post(models.Model):

    title = models.CharField(blank=True, null=True, max_length=200)
    content = models.TextField(
        blank=True, default="Esse texto é padrão", help_text="Escreva um conteúdo para o Post", )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
