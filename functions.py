# -*- coding: utf-8 -*-
"""
@author: taylor.fu
"""
import re
import json
from decimal import Decimal, ROUND_HALF_UP

class CurrencyExchangeService:
    def __init__(self):
        with open('exchange_rate.json', 'r') as f:
            self.rate_reference = json.loads(f.read())

    def validate_amount(self, amount: str) -> bool:
        # validate input amount w/ or w/o separator 
        if ',' in amount:
            pattern = r"^(([1-9]\d{0,2})(,\d{3})*|0)(\.\d+)?$"
        else:
            pattern = r"^([1-9]\d*|0)(\.\d+)?$"
        return True if re.match(pattern, amount) else False
    
    def round(self, amount: Decimal, places: int) -> Decimal:
        # round half up method
        try:
            return amount.quantize(Decimal(f"0.{'0'*places}"), rounding=ROUND_HALF_UP)
        except Exception as e:
            raise ValueError('Quantizing error')
    
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
