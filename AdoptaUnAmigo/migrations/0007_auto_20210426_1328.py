# Generated by Django 3.1.7 on 2021-04-26 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdoptaUnAmigo', '0006_anuncios_fav_anuncio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anuncios_fav',
            name='anuncio',
        ),
        migrations.AddField(
            model_name='anuncios_fav',
            name='anuncio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AdoptaUnAmigo.anuncio'),
        ),
    ]
