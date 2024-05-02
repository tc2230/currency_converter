# -*- coding: utf-8 -*-
"""
@author: taylor.fu
"""
from fastapi import FastAPI
from functions import CurrencyExchangeService

app = FastAPI()
currency_service = CurrencyExchangeService()

@app.get('/convert_currency')
def convert_currency(source: str, target: str, amount: str) -> dict:
    try:
        amount = currency_service.convert(source, target, amount)
        return {"msg":"successful", "amount":amount}
    except ValueError as e:
        return {"msg":f"failed: {e}", "amount":None}