from requests import get, utils
import re
from decimal import Decimal
import datetime


def currency_rates(valute):
    valute = valute.upper()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings).replace('/', '')
    content_list = re.split('<CharCode>|<Value>', content.replace(',', '.'))
    index_date = content.index('Date')
    date = datetime.datetime.strptime(content[index_date + 6:index_date + 16], '%d.%m.%Y').date()
    for i, v in enumerate(content_list):
        if valute == v:
            return Decimal(content_list[i + 2]).quantize(Decimal('1.11')), date
    return None, None
