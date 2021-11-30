# Generated by Django 3.2.9 on 2021-11-26 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211125_0432'),
    ]

    operations = [
        migrations.CreateModel(
            name='Csv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(blank=True, null=True)),
                ('Name', models.TextField(blank=True, null=True)),
                ('Lvl1', models.TextField(blank=True, null=True)),
                ('Lvl2', models.TextField(blank=True, null=True)),
                ('Lvl3', models.TextField(blank=True, null=True)),
                ('Cost', models.TextField(blank=True, null=True)),
                ('CostSP', models.TextField(blank=True, null=True)),
                ('Count', models.TextField(blank=True, null=True)),
                ('FieldProp', models.TextField(blank=True, null=True)),
                ('Purch', models.TextField(blank=True, null=True)),
                ('Unit', models.TextField(blank=True, null=True)),
                ('Img', models.TextField(blank=True, null=True)),
                ('Display', models.TextField(blank=True, null=True)),
                ('Desc', models.TextField(blank=True, null=True)),
            ],
        ),
    ]

