# Generated by Django 4.2.1 on 2023-08-04 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_addprojects_github_code_addprojects_live_demo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nuquestion',
            name='question_image',
            field=models.FileField(upload_to='question_image'),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
