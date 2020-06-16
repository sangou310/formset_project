# Generated by Django 3.0.7 on 2020-06-16 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='quantity',
        ),
        migrations.AddField(
            model_name='stock',
            name='stock_quantity',
            field=models.IntegerField(default=1, verbose_name='在庫数'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stock',
            name='code',
            field=models.CharField(max_length=20, verbose_name='コード'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_quantity', models.IntegerField(verbose_name='注文数')),
                ('remarks', models.CharField(max_length=200, verbose_name='備考')),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Stock')),
            ],
        ),
    ]