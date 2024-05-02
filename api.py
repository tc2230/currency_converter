# -*- coding: utf-8 -*-
"""
@author: taylor.fu
"""
from fastapi import FastAPI

app = FastAPI()

class CurrencyExchangeService:
    def __init__(self):
        pass

    def round(self, amount, places):
        pass

    def validate_amount(self, amount):
        pass
    
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