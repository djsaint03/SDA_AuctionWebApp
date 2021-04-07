# Generated by Django 3.1.7 on 2021-04-02 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0002_auto_20210324_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_to_pay', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('user_name', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=128)),
                ('account_creation_date', models.DateTimeField(auto_now=True)),
                ('account_status', models.CharField(default='ACTIVE', max_length=20)),
                ('logotype', models.ImageField(upload_to='media/users/')),
                ('type', models.CharField(default='NORMAL', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='location',
            field=models.CharField(default='London', max_length=60),
        ),
        migrations.AddField(
            model_name='item',
            name='no_of_visits',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auction.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auction.user')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_rating', models.IntegerField()),
                ('sellers_comment', models.TextField(max_length=250)),
                ('buyer_rating', models.IntegerField()),
                ('buyers_comment', models.TextField(max_length=250)),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auction.purchase')),
            ],
        ),
        migrations.AddField(
            model_name='purchase',
            name='auction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auction.item'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auction.user'),
        ),
        migrations.CreateModel(
            name='Bidding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_to_pay', models.DecimalField(decimal_places=2, max_digits=10)),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auction.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auction.user')),
            ],
        ),
    ]
