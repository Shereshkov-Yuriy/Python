from requests import get, utils
from decimal import Decimal
import re


def currency_rates(valute):
    valute = valute.upper()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings).replace('/', '')
    content_list = re.split('<CharCode>|<Value>', content.replace(',', '.'))
    for i, v in enumerate(content_list):
        if valute in v:
            return Decimal(content_list[i + 2]).quantize(Decimal('1.11'))
    return None


print(currency_rates('uSd'))
print(currency_rates('euR'))
print(currency_rates('uadsfgasg'))
