# Generated by Django 3.0.2 on 2020-03-10 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DEMOAPP1', '0007_auto_20200310_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Domain', models.CharField(max_length=120, verbose_name='Domain')),
                ('Query', models.CharField(max_length=264)),
                ('LastRefreshedOn', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Table',
        ),
        migrations.AlterField(
            model_name='item',
            name='family',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DEMOAPP1.FAMILY'),
        ),
    ]