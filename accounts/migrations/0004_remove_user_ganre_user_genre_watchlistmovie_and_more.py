# Generated by Django 4.2 on 2023-12-22 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movieinfo', '0001_initial'),
        ('accounts', '0003_remove_user_genre_user_ganre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='ganre',
        ),
        migrations.AddField(
            model_name='user',
            name='genre',
            field=models.ManyToManyField(blank=True, to='movieinfo.genre'),
        ),
        migrations.CreateModel(
            name='WatchlistMovie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchlists', to='movieinfo.movieinfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchlists', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WatchedMovie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watcheds', to='movieinfo.movieinfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watcheds', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LikeMovie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='movieinfo.movieinfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
