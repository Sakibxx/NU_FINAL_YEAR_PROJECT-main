# Generated by Django 4.2.1 on 2023-08-05 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_multiimagesquestion_remove_nuquestion_question_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nuquestion',
            name='question_image',
        ),
        migrations.DeleteModel(
            name='MultiimagesQuestion',
        ),
        migrations.AddField(
            model_name='nuquestion',
            name='question_image',
            field=models.ImageField(blank=True, upload_to='question_image'),
        ),
    ]
