# -*- coding: utf-8 -*-
"""
@author: taylor.fu
"""
from fastapi import FastAPI
import re

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

    def validate_amount(self, amount):
        # validate input amount w/ or w/o separator 
        if ',' in amount:
            pattern = r"^([1-9]\d{0,2}|0)(,\d{3})*(\.\d+)?$"
        else:
            pattern = r"^([1-9]\d*|0)(\.\d+)?$"
        return True if re.match(pattern, amount) else False
    
    def convert(self, source, target, amount):
        pass

currency_service = CurrencyExchangeService()

@app.get('/convert_currency')
def convert_currency(source: str, target: str, amount: str) -> dict:
    try:
        amount = currency_service.convert(source, target, amount)
        return {"msg":"successful", "amount":amount}
    except ValueError as e:
        return {"msg":f"failed: {e}", "amount":None}