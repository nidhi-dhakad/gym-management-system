# Generated by Django 3.2.3 on 2021-06-03 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('contect', models.CharField(max_length=10)),
                ('emailid', models.CharField(max_length=60)),
                ('age', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=10)),
                ('unit', models.CharField(max_length=10)),
                ('date', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contect', models.CharField(max_length=10)),
                ('emailid', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=40)),
                ('plan', models.CharField(max_length=40)),
                ('joindate', models.CharField(max_length=40)),
                ('expiredate', models.CharField(max_length=10)),
                ('initialamount', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('amount', models.CharField(max_length=10)),
                ('duration', models.CharField(max_length=10)),
            ],
        ),
    ]
