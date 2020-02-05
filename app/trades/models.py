from django.db import models


class CompanyCode(models.Model):
    """
    Model to store a Company Code.
    """
    company_name = models.CharField(max_length=200)
    company_trade_id = models.CharField(max_length=200)

class ProductSeller(models.Model):
    """
    Model to store a Product Sellers.
    """
    product = models.CharField(max_length=200)
    company_id = models.CharField(max_length=100)

class StockPrice(models.Model):
    """
    Model to store a Stock Price.
    """
    date = models.DateField()
    company_id = models.CharField(max_length=200)
    stock_price = models.FloatField()

class ProductPrice(models.Model):
    """
    Model to store a Product Price.
    """ 
    date = models.DateField()
    product = models.CharField(max_length=200)
    market_price = models.FloatField()

class CurrencyValue(models.Model):
    """
    Model to store a Currency Value.
    """
    date = models.DateField()
    currency = models.CharField(max_length=200)
    value_in_usd = models.FloatField()

class DerivataveTrade(models.Model):
    """
    Model to store a Derivative Trade.
    """
    date_of_trade = models.DateField()
    trade_id = models.CharField(max_length=200)
    product = models.CharField(max_length=200)
    buying_party = models.CharField(max_length=200) 
    selling_party = models.CharField(max_length=200)
    notational_amount = models.FloatField()
    quantity = models.FloatField()
    notational_currency = models.CharField(max_length=200)
    maturity_date = models.DateField()
    underlying_price = models.FloatField()
    underlying_currency = models.CharField(max_length=200)
    strike_price = models.FloatField()
