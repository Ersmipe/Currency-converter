# Web and CLI currency converter

## Usage

Web app
- You have to have installed flask and requests to run this app!

CLI script
- You have to have installed argparse and requests to run this app!

Responses with arguments "amount", "input_currency" and "output_currency" will have form:

```json
{
    "input": {
        "amount": 55,
        "currency": "$"
    },
    "output": {
        "AUD": 71.62911459250131
    }
}
```
Responses with arguments "amount" and "input_currency" will have form:
```json
{
  "input": {
    "amount": 50.0, 
    "currency": "$"
  }, 
  "output": {
    "AUD": 71.62911459250131, 
    "BGN": 86.06759373349762, 
    "BRL": 191.97324414715717, 
    "CAD": 65.77627178313676, 
    "CHF": 48.904242210878365, 
    "CNY": 343.8611160007041, 
    "CZK": 1121.5455025523675, 
    "DKK": 328.5117056856187, 
    "EUR": 44.0063369125154, 
    "GBP": 39.43099806372118, 
    "HKD": 390.4418236226017, 
    "HRK": 325.4532652701989, 
    "HUF": 14236.049991198732, 
    "IDR": 708399.929589861, 
    "ILS": 179.6558704453441, 
    "INR": 3457.5998943847912, 
    "ISK": 6226.896673120929, 
    "JPY": 5386.375638091886, 
    "KRW": 57774.15947896497, 
    "MXN": 959.2149269494807, 
    "MYR": 207.37546206653755, 
    "NOK": 425.6864988558352, 
    "NZD": 74.82837528604118, 
    "PHP": 2572.4344305580003, 
    "PLN": 187.58581235697937, 
    "RON": 207.79792290089773, 
    "RUB": 3152.609575778912, 
    "SEK": 463.98081323710613, 
    "SGD": 67.71255060728744, 
    "THB": 1538.2415067769757, 
    "TRY": 288.2415067769759, 
    "USD": 50.0, 
    "ZAR": 716.4319662031332
  }
}
```
