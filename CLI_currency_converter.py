#!/usr/bin/env python3
# coding=UTF-8

import json
import argparse
import requests


class CurrencyConverter:
	rates = {}
	currency_codes = []

	def __init__(self, url):
		data = requests.get(url).json()
		self.rates = data['rates']
		self.rates["EUR"] = 1.0
		currency_symbols = {"€": "EUR", "£": "GBP", "$": "USD", "¥": "JPY"}
		for c_symbol, c_code in currency_symbols.items():
			self.rates[c_symbol] = self.rates[c_code]
		for c_code in self.rates:
			self.currency_codes.append(c_code)

	def convert(self):
		output = {"input": {}, "output": {}}
		amount = user_input.amount
		input_currency = user_input.input_currency
		output_currency = user_input.output_currency
		output["input"] = {"amount": amount, "currency": input_currency}

		if input_currency is None:
			return "Please, fill in input currency code."
		elif amount is None:
			return "Please fill in amount."

		amount = amount / self.rates[input_currency]
		if output_currency is None:
			for c_code in self.currency_codes:
				if len(c_code) > 1:
					output["output"][c_code] = amount * self.rates[c_code]
		else:
			output["output"] = {output_currency: amount * self.rates[output_currency]}
		return json.dumps(output, indent=4, ensure_ascii=False)


converter = CurrencyConverter("https://api.exchangeratesapi.io/latest")

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--amount", type=float, help="Currency value you wish to convert. This argument is mandatory")
parser.add_argument("-i", "--input_currency", type=str, choices=converter.currency_codes,
					help="Code of input currency. This argument is mandatory")
parser.add_argument("-o", "--output_currency", type=str, choices=converter.currency_codes,
					help="Code of currency which should be \"amount\" converted to. If it is blank input is converted"
						 " to all known currencies")

user_input = parser.parse_args()
print(converter.convert())
