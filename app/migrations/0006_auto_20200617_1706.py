# Generated by Django 3.0.7 on 2020-06-17 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_order_remarks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15, verbose_name='コード')),
                ('name', models.CharField(max_length=50, verbose_name='部品名')),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Material'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Material'),
        ),
    ]
