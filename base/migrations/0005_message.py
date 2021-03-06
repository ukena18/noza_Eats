# Generated by Django 4.0.2 on 2022-03-04 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_cart_transaction_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.TextField(blank=True, null=True)),
                ('msg_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.person')),
                ('msg_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.cook')),
            ],
        ),
    ]
