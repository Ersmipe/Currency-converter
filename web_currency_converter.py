#!/usr/bin/env python3
# coding=UTF-8

import requests
import flask


class CurrencyConverter:
	rates = {}
	currency_codes = []
	amount = None
	input_currency = None
	output_currency = None

	def __init__(self, url):
		data = requests.get(url).json()
		self.rates = data['rates']
		self.rates["EUR"] = 1.0
		currency_symbols = {"€": "EUR", "£": "GBP", "$": "USD", "¥": "JPY"}
		for c_symbol, c_code in currency_symbols.items():
			self.rates[c_symbol] = self.rates[c_code]
		for c_code in self.rates:
			self.currency_codes.append(c_code)

	def set_input_currency(self, code):
		if code in self.currency_codes:
			self.input_currency = code
			return True
		return False

	def set_output_currency(self, code):
		if code in self.currency_codes:
			self.output_currency = code
			return True
		return False

	def convert(self):
		output = {"input": {"amount": self.amount, "currency": self.input_currency}, "output": {}}

		self.amount = self.amount / self.rates[self.input_currency]
		if self.output_currency is None:
			for c_code in self.currency_codes:
				if len(c_code) > 1:
					output["output"][c_code] = self.amount * self.rates[c_code]
		else:
			output["output"] = {self.output_currency: self.amount * self.rates[self.output_currency]}
		return output


converter = CurrencyConverter("https://api.exchangeratesapi.io/latest")

app = flask.Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
host_ip = ''


@app.route('/', methods=['GET'])
def home():
	return "<h1>Currency converter</h1>"


@app.route('/currency_converter', methods=['GET'])
def api_convert():
	global host_ip
	host_ip = flask.request.remote_addr

	try:
		converter.amount = float(flask.request.args.get('amount'))
	except (ValueError, TypeError):
		return 'Please fill in amount.'

	if not converter.set_input_currency(flask.request.args.get('input_currency')):
		return 'Please choose input currency. Possible options: {}'.format(converter.currency_codes)

	if 'output_currency' in flask.request.args:
		if not converter.set_output_currency(flask.request.args.get('output_currency')):
			return 'Please input valid output currency code or skip "output_currency" argument. Valid options: {}'.format(
				converter.currency_codes)
	else:
		converter.output_currency = None

	return flask.jsonify(converter.convert())


app.run(host=host_ip, threaded=True)
