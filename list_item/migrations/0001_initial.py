# Generated by Django 3.0.5 on 2020-04-25 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListItemModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130, verbose_name='Название дела')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_done', models.BooleanField(default=False)),
                ('expare_date', models.DateTimeField(auto_now=True)),
                ('id_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ListModel')),
            ],
            options={
                'verbose_name': 'Список задач',
            },
        ),
    ]
