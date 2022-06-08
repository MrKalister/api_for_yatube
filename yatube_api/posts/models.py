from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(
        max_length=50,
        unique=True)
    description = models.TextField()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts')
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True)
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True)

    class Meta:
        ordering = ['pub_date']


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments')


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик')

    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор постов')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['following', 'user'],
                name='unique_following_user'
            )
        ]

    def __str__(self):
        return f'{self.user} подписан на: {self.following}'
