# Generated by Django 3.2.8 on 2022-12-23 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalDiary', '0003_diary_mood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='mood',
            field=models.CharField(choices=[('n', 'Normal'), ('h', 'Happy'), ('s', 'Sad')], default='n', max_length=50, verbose_name='mood'),
        ),
    ]