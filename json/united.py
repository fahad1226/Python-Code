
import json

text = """
    {
    'title':'Fahad Bin Munir',
    'composer':'Sakib Al Hasan',
    'realese_year':2010,
    'buudgets':1800000020,
    'actors':null,
    'won_oscer':false

    }"""

tron = json.loads(text)
print(tron)
