# Generated by Django 2.0.1 on 2018-06-11 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_question_correct_num'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='correct_num',
            new_name='correct_count',
        ),
        migrations.AddField(
            model_name='question',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]