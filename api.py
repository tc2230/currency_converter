# -*- coding: utf-8 -*-
"""
@author: taylor.fu
"""
from fastapi import FastAPI
import re
from decimal import Decimal, ROUND_HALF_UP

app = FastAPI()

class CurrencyExchangeService:
    def __init__(self):
        self.rate_reference = {
            "currencies": {
                "TWD": {
                    "TWD": 1,
                    "JPY": 3.669,
                    "USD": 0.03281
                },
                "JPY": {
                    "TWD": 0.26956,
                    "JPY": 1,
                    "USD": 0.00885
                },
                "USD": {
                    "TWD": 30.444,
                    "JPY": 111.801,
                    "USD": 1
                }
            }
        }

    def validate_amount(self, amount: str) -> bool:
        # validate input amount w/ or w/o separator 
        if ',' in amount:
            pattern = r"^([1-9]\d{0,2}|0)(,\d{3})*(\.\d+)?$"
        else:
            pattern = r"^([1-9]\d*|0)(\.\d+)?$"
        return True if re.match(pattern, amount) else False
    
    def round(self, amount: Decimal, places: int) -> Decimal:
        # round half up method
        return amount.quantize(Decimal(f"0.{'0'*places}"), rounding=ROUND_HALF_UP)
    
    def convert(self, source: str, target: str, amount: str) -> str:
        # validate source/target
        if (source not in self.rate_reference['currencies']) or (target not in self.rate_reference['currencies'][source]):
            print(source, target, amount)
            raise ValueError('Unrecognized curreny option')
        
        # validate input amount
        if not self.validate_amount(amount):
            raise ValueError('Invalid input amount')
        
        # round input number
        amount = Decimal(amount.replace(',', ''))
        amount = self.round(amount, 2)

        # convert
        rate = Decimal(str(self.rate_reference['currencies'][source][target]))
        converted_amount = rate * amount

        # round converted amount
        converted_amount = self.round(converted_amount, 2)
        
        return format(converted_amount, ',')

currency_service = CurrencyExchangeService()

@app.get('/convert_currency')
def convert_currency(source: str, target: str, amount: str) -> dict:
    try:
        amount = currency_service.convert(source, target, amount)
        return {"msg":"successful", "amount":amount}
    except ValueError as e:
        return {"msg":f"failed: {e}", "amount":None}