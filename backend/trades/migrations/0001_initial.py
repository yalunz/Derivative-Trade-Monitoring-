# Generated by Django 3.0.2 on 2020-02-13 15:22

from django.db import migrations, models
import django.db.models.deletion
import trades.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('company_trade_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CurrencyValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('currency', models.CharField(max_length=200)),
                ('value_in_usd', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='DerivativeTrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_trade', models.DateField()),
                ('trade_id', models.CharField(max_length=200)),
                ('product', models.CharField(max_length=200)),
                ('buying_party', models.CharField(max_length=200)),
                ('selling_party', models.CharField(max_length=200)),
                ('notational_amount', models.FloatField()),
                ('quantity', models.FloatField()),
                ('notational_currency', models.CharField(max_length=200)),
                ('maturity_date', models.DateField()),
                ('underlying_price', models.FloatField()),
                ('underlying_currency', models.CharField(max_length=200)),
                ('strike_price', models.FloatField()),
            ],
            options={
                'ordering': ['-date_of_trade'],
            },
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('product', models.CharField(max_length=200)),
                ('market_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductSeller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=200)),
                ('company_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('report', models.FileField(upload_to=trades.models.Report.get_upload_path)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='StockPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company_id', models.CharField(max_length=200)),
                ('stock_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='DerivativeTradeHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history_type', models.CharField(choices=[('E', 'Edit'), ('D', 'Delete')], max_length=1)),
                ('date_modified', models.DateTimeField(auto_now_add=True)),
                ('added_to_report', models.BooleanField(default=False)),
                ('date_of_trade', models.DateField()),
                ('trade_id', models.CharField(max_length=200)),
                ('product', models.CharField(max_length=200)),
                ('buying_party', models.CharField(max_length=200)),
                ('selling_party', models.CharField(max_length=200)),
                ('notational_amount', models.FloatField()),
                ('quantity', models.FloatField()),
                ('notational_currency', models.CharField(max_length=200)),
                ('maturity_date', models.DateField()),
                ('underlying_price', models.FloatField()),
                ('underlying_currency', models.CharField(max_length=200)),
                ('strike_price', models.FloatField()),
                ('up_to_date_trade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='history', to='trades.DerivativeTrade')),
            ],
            options={
                'ordering': ['-date_modified', '-id'],
            },
        ),
    ]
