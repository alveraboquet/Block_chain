import hmac
import base64
import requests
import json
import time
import math

CONTENT_TYPE = 'Content-Type'
OK_ACCESS_KEY = 'OK-ACCESS-KEY'
OK_ACCESS_SIGN = 'OK-ACCESS-SIGN'
OK_ACCESS_TIMESTAMP = 'OK-ACCESS-TIMESTAMP'
OK_ACCESS_PASSPHRASE = 'OK-ACCESS-PASSPHRASE'
APPLICATION_JSON = 'application/json'
MARKET_URL = 'https://api.huobi.pro'

apiKey = '17eaacb2-d33d-4eb7-b2dd-6a068964d942'
secretKey='8A3EAF3B40791AD60A3C06CA34E99EE6'

global dic_instruments
#dic_instruments = {'GRT': '10', 'OMG': '1', 'NEAR': '10', 'EGLD': '0.1', 'WAVES': '1', 'BNT': '10', 'BAT': '10', '1INCH': '1', 'SOL': '1', 'LON': '1', 'BADGER': '0.1', 'MIR': '1', 'TORN': '0.01', 'NEO': '1', 'MASK': '1', 'LINK': '1', 'CFX': '10', 'DASH': '0.1', 'CHZ': '10', 'ADA': '100', 'MANA': '10', 'ZEC': '0.1', 'ALPHA': '1', 'XTZ': '1', 'LUNA': '0.1', 'ONT': '10', 'FTM': '10', 'ATOM': '1', 'QTUM': '1', 'XLM': '100', 'XMR': '0.1', 'IOTA': '10', 'ALGO': '10', 'IOST': '1000', 'THETA': '10', 'KNC': '1', 'COMP': '0.1', 'DOGE': '1000', 'CONV': '10', 'DORA': '0.1', 'FIL': '0.1', 'ENJ': '1', 'SRM': '1', 'SAND': '10', 'SNX': '1', 'PERP': '1', 'ANT': '1', 'ANC': '1', 'ZRX': '10', 'SC': '100', 'MKR': '0.01', 'CRO': '10', 'DOT': '1', 'XEM': '10', 'RVN': '10', 'LPT': '0.1', 'MATIC': '10', 'XCH': '0.01', 'SHIB': '1000000', 'ICP': '0.01', 'CSPR': '1', 'LAT': '10', 'MINA': '1', 'JST': '100', 'REN': '10', 'KSM': '0.1', 'TRB': '0.1', 'RSR': '100', 'BAL': '0.1', 'STORJ': '10', 'BTM': '100', 'LRC': '10', 'BTC': '0.01', 'LTC': '1', 'ETH': '0.1', 'TRX': '1000', 'BCH': '0.1', 'BSV': '1', 'EOS': '10', 'XRP': '100', 'ETC': '10', 'YFI': '0.0001', 'YFII': '0.001', 'SUSHI': '1', 'CRV': '1', 'UMA': '0.1', 'BAND': '1', 'WNXM': '0.1', 'ZIL': '100', 'BTT': '10000', 'SWRV': '1', 'SUN': '0.1', 'UNI': '1', 'AVAX': '1', 'FLM': '10', 'ZEN': '1', 'AAVE': '0.1', 'CVC': '100'}
dic_instruments = {'BTC': '0.01', 'ETH': '0.1', 'LTC': '1', 'DOT': '1', 'DOGE': '1000', 'FIL': '0.1', 'YFII': '0.001', 'ETC': '10', 'OP': '1', '1INCH': '1', 'AAVE': '0.1', 'ADA': '100', 'AGLD': '1', 'ALGO': '10', 'ALPHA': '1', 'ANT': '1', 'APE': '0.1', 'API3': '1', 'ASTR': '10', 'ATOM': '1', 'AVAX': '1', 'AXS': '0.1', 'BABYDOGE': '1000000000', 'BADGER': '0.1', 'BAL': '0.1', 'BAND': '1', 'BAT': '10', 'BCH': '0.1', 'BICO': '1', 'BNT': '10', 'BSV': '1', 'BTM': '100', 'BTT': '1000000', 'BZZ': '0.1', 'CELO': '1', 'CEL': '10', 'CFX': '10', 'CHZ': '10', 'COMP': '0.1', 'CONV': '10', 'CQT': '1', 'CRO': '10', 'CRV': '1', 'CSPR': '1', 'CVC': '100', 'DASH': '0.1', 'DOME': '100', 'DORA': '0.1', 'DYDX': '1', 'EFI': '1', 'EGLD': '0.1', 'ELON': '1000000', 'ENJ': '1', 'ENS': '0.1', 'EOS': '10', 'FITFI': '10', 'FLM': '10', 'FTM': '10', 'GALA': '10', 'GMT': '1', 'GODS': '1', 'GRT': '10', 'ICP': '0.01', 'IMX': '1', 'IOST': '1000', 'IOTA': '10', 'JST': '100', 'KISHU': '1000000000', 'KNC': '1', 'KSM': '0.1', 'LAT': '10', 'LINK': '1', 'LON': '1', 'LOOKS': '1', 'LPT': '0.1', 'LRC': '10', 'LUNA': '1', 'MANA': '10', 'MASK': '1', 'MATIC': '10', 'MINA': '1', 'MKR': '0.01', 'NEAR': '10', 'NEO': '1', 'NFT': '1000000', 'NYM': '1', 'OMG': '1', 'ONT': '10', 'PEOPLE': '100', 'PERP': '1', 'QTUM': '1', 'REN': '10', 'RSR': '100', 'RSS3': '10', 'RVN': '10', 'SAND': '10', 'SC': '100', 'SHIB': '1000000', 'SLP': '10', 'SNX': '1', 'SOL': '1', 'SOS': '1000000', 'SRM': '1', 'STARL': '100000', 'STORJ': '10', 'SUSHI': '1', 'SWRV': '1', 'THETA': '10', 'TORN': '0.01', 'TRB': '0.1', 'TRX': '1000', 'UMA': '0.1', 'UMEE': '10', 'UNI': '1', 'WAVES': '1', 'WNCG': '1', 'WNXM': '0.1', 'XCH': '0.01', 'XEM': '10', 'XLM': '100', 'XMR': '0.1', 'XRP': '100', 'XTZ': '1', 'YFI': '0.0001', 'YGG': '1', 'ZEC': '0.1', 'ZEN': '1', 'ZIL': '100', 'ZRX': '10'}


# signature
def signature(timestamp, method, request_path, secret_key, body):
    if str(body) == '{}' or str(body) == 'None':
        body = ''
    message = str(timestamp) + str.upper(method) + request_path + str(body)
    mac = hmac.new(bytes(secret_key, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
    d = mac.digest()
    return base64.b64encode(d)

# set request header
def get_header(api_key, sign, timestamp, passphrase):
    header = dict()
    header[CONTENT_TYPE] = APPLICATION_JSON
    header[OK_ACCESS_KEY] = api_key
    header[OK_ACCESS_SIGN] = sign
    header[OK_ACCESS_TIMESTAMP] = str(timestamp)
    header[OK_ACCESS_PASSPHRASE] = 'Aa123456!'
    return header

def parse_params_to_str(params):
    url = '?'
    for key, value in params.items():
        if value == None:
            pass
        else:
            url = url + str(key) + '=' + str(value) + '&'
    if len(url) == 1:
        return None
    return url[0:-1]
#Account
#Get Currencies
#????????????????????????????????????
def Get_Currencies(secretKey,apiKey): 
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/account/balance'
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489?A')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#Get Balance
#????????????????????????????????????
def Get_Balance(secretKey,apiKey,ccy = None): 
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/account/balance'
    params = {'ccy': ccy}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489?A')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#Get Positions
#????????????????????????????????????????????????????????????????????????????????????????????????net????????????????????????????????????????????????????????????long???????????????short???????????????
def Get_Positions(secretKey,apiKey,instType=None,instId=None,posId=None): 
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/account/positions'
    params = {'instType' : instType,'instId' : instId,'posId' : posId}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#Get account and position risk
#???????????????????????????
def Get_account_and_position_risk(secretKey,apiKey,instType=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/account/account-position-risk'
    params = {'instType' : instType}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#????????????????????????????????????????????????????????????????????????????????????????????????7?????????????????????
def Get_Bills_Details_last_7_days(secretKey,apiKey,instType=None,ccy=None,mgnMode=None,ctType=None,type=None,subType=None,after=None,before=None,limit=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/account/bills'
    params = {'instType':instType,'ccy':ccy,'mgnMode':mgnMode,'ctType':ctType,'type':type,'subType':subType,'after':after,'before':before,'limit':limit}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#????????????????????????????????????????????????????????????????????????????????????????????????3????????????????????????
def Get_Bills_Details_last_3_months(secretKey,apiKey,instType=None,ccy=None,mgnMode=None,ctType=None,type=None,subType=None,after=None,before=None,limit=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/account/bills-archive'
    params = {'instType':instType,'ccy':ccy,'mgnMode':mgnMode,'ctType':ctType,'type':type,'subType':subType,'after':after,'before':before,'limit':limit}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#?????????????????????????????????
def Get_Account_Configuration(secretKey,apiKey):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/account/config'
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????2?????????????????????
def Set_Position_mode(secretKey,apiKey,posMode=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/account/set-position-mode'
    params = {'posMode' : posMode}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    url = base_url + request_path
    timestamp = round(time.time(), 3)
    # request header and body
    body = json.dumps(params)
    header = get_header(apiKey, signature(timestamp, 'POST', request_path, secretKey, body), timestamp, 'cht32489')
    # do request
    response = requests.post(url, data=body, headers=header, timeout=10)
    return response.json()

#??????????????????
def Set_Leverage(secretKey,apiKey,instId=None,ccy=None,lever=None,mgnMode=None,posSide=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/account/set-leverage'
    params = {'instId':instId,'ccy':ccy,'lever':lever,'mgnMode':mgnMode,'posSide':posSide}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    url = base_url + request_path
    timestamp = round(time.time(), 3)
    # request header and body
    body = json.dumps(params)
    header = get_header(apiKey, signature(timestamp, 'POST', request_path, secretKey, body), timestamp, 'cht32489')
    # do request
    response = requests.post(url, data=body, headers=header, timeout=10)
    return response.json()

#?????????????????????/????????????
def Get_maximum_buy_sell_amount_or_open_amount(secretKey,apiKey,instId=None,tdMode=None,ccy=None,px=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/account/max-size'
    params = {'instId':instId,'tdMode':tdMode,'ccy':ccy,'px':px}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#????????????????????????
def Get_Maximum_Available_Tradable_Amount(secretKey,apiKey,ccy=None,tdMode=None,reduceOnly=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/account/max-avail-size'
    params = {'ccy':ccy,'tdMode':tdMode,'reduceOnly':reduceOnly}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#????????????????????????????????????
def Increase_Decrease_margin(secretKey,apiKey,instId=None,posSide=None,type=None,amt=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/account/position/margin-balance'
    params = {'instId':instId,'posSide':posSide,'type':type,'amt':amt}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    url = base_url + request_path
    timestamp = round(time.time(), 3)
    # request header and body
    body = json.dumps(params)
    header = get_header(apiKey, signature(timestamp, 'POST', request_path, secretKey, body), timestamp, 'cht32489')
    # do request
    response = requests.post(url, data=body, headers=header, timeout=10)
    return response.json()

#??????????????????
def Get_Leverage(secretKey,apiKey,instId=None,mgnMode=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/account/leverage-info'
    params = {'instId':instId,'mgnMode':mgnMode}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#??????????????????????????????
def Get_the_maximum_loan_of_instrument(secretKey,apiKey,instId=None,mgnMode=None,mgnCcy=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/account/max-loan'
    params = {'instId':instId,'mgnMode':mgnMode,'mgnCcy':mgnCcy}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#???????????????????????????????????????
def Get_Fee_Rates(secretKey,apiKey,instType=None,instId=None,uly=None,category=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/account/trade-fee'
    params = {'instType':instType,'instId':instId,'uly':uly,'category':category}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#??????????????????
def Get_interest_accrued(secretKey,apiKey,instId=None,ccy=None,mgnMode=None,after=None,before=None,limit=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/account/interest-accrued'
    params = {'instId':instId,'ccy':ccy,'mgnMode':mgnMode,'after':after,'before':before,'limit':limit}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#????????????????????????????????????
def Get_interest_rate(secretKey,apiKey,ccy=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/account/interest-rate'
    params = {'ccy':ccy}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#??????????????????????????????
def Get_Maximum_Withdrawals(secretKey,apiKey,ccy=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/account/max-withdrawal'
    params = {'ccy':ccy}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#??????????????????PA/BS??????
def Set_Greeks_PA_BS(secretKey,apiKey,greeksType=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/account/set-greeks'
    params = {'greeksType':greeksType}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    url = base_url + request_path
    timestamp = round(time.time(), 3)
    # request header and body
    body = json.dumps(params)
    header = get_header(apiKey, signature(timestamp, 'POST', request_path, secretKey, body), timestamp, 'cht32489')
    # do request
    response = requests.post(url, data=body, headers=header, timeout=10)
    return response.json()

#Trade

#??????
def Place_Order(secretKey,apiKey,instId=None,tdMode=None,ccy=None,clOrdId=None,tag=None,side=None,posSide=None,ordType=None,sz=None,px=None,reduceOnly=None,tgtCcy=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/trade/order'
    params = {'instId':instId,'tdMode':tdMode,'ccy':ccy,'clOrdId':clOrdId,'tag':tag,'side':side,'posSide':posSide,'ordType':ordType,'sz':sz,'px':px,'reduceOnly':reduceOnly,'tgtCcy':tgtCcy}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    url = base_url + request_path
    timestamp = round(time.time(), 3)
    # request header and body
    body = json.dumps(params)
    header = get_header(apiKey, signature(timestamp, 'POST', request_path, secretKey, body), timestamp, 'cht32489')
    # do request
    response = requests.post(url, data=body, headers=header, timeout=10)
    return response.json()

#????????????
def Place_Multiple_Orders(secretKey,apiKey,instId=None,tdMode=None,ccy=None,clOrdId=None,tag=None,side=None,posSide=None,ordType=None,sz=None,px=None,reduceOnly=None,tgtCcy=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/account/set-greeks'
    params = {'instId':instId,'tdMode':tdMode,'ccy':ccy,'clOrdId':clOrdId,'tag':tag,'side':side,'posSide':posSide,'ordType':ordType,'sz':sz,'px':px,'reduceOnly':reduceOnly,'tgtCcy':tgtCcy}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    url = base_url + request_path
    timestamp = round(time.time(), 3)
    # request header and body
    body = json.dumps(params)
    header = get_header(apiKey, signature(timestamp, 'POST', request_path, secretKey, body), timestamp, 'cht32489')
    # do request
    response = requests.post(url, data=body, headers=header, timeout=10)
    return response.json()

#??????
def Cancel_Order(secretKey,apiKey,instId=None,ordId=None,clOrdId=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/trade/cancel-order'
    params = {'instId':instId,'ordId':ordId,'clOrdId':clOrdId}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    url = base_url + request_path
    timestamp = round(time.time(), 3)
    # request header and body
    body = json.dumps(params)
    header = get_header(apiKey, signature(timestamp, 'POST', request_path, secretKey, body), timestamp, 'cht32489')
    # do request
    response = requests.post(url, data=body, headers=header, timeout=10)
    return response.json()

#????????????
def Cancel_Multiple_Orders(secretKey,apiKey,instId=None,ordId=None,clOrdId=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/trade/cancel-batch-orders'
    params = {'instId':instId,'ordId':ordId,'clOrdId':clOrdId}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    url = base_url + request_path
    timestamp = round(time.time(), 3)
    # request header and body
    body = json.dumps(params)
    header = get_header(apiKey, signature(timestamp, 'POST', request_path, secretKey, body), timestamp, 'cht32489')
    # do request
    response = requests.post(url, data=body, headers=header, timeout=10)
    return response.json()

#????????????,??????????????????????????????
def Amend_Order(secretKey,apiKey,instId=None,cxlOnFail=None,ordId=None,clOrdId=None,reqId=None,newSz=None,newPx=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/trade/amend-order'
    params = {'instId':instId,'cxlOnFail':cxlOnFail,'ordId':ordId,'clOrdId':clOrdId,'reqId':reqId,'newSz':newSz,'newPx':newPx}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    url = base_url + request_path
    timestamp = round(time.time(), 3)
    # request header and body
    body = json.dumps(params)
    header = get_header(apiKey, signature(timestamp, 'POST', request_path, secretKey, body), timestamp, 'cht32489')
    # do request
    response = requests.post(url, data=body, headers=header, timeout=10)
    return response.json()

#??????????????????,??????????????????????????????????????????????????????20??????????????????????????????????????????????????????
def Amend_Multiple_Orders(secretKey,apiKey,instId=None,cxlOnFail=None,ordId=None,clOrdId=None,reqId=None,newSz=None,newPx=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/trade/amend-order'
    params = {'instId':instId,'cxlOnFail':cxlOnFail,'ordId':ordId,'clOrdId':clOrdId,'reqId':reqId,'newSz':newSz,'newPx':newPx}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    url = base_url + request_path
    timestamp = round(time.time(), 3)
    # request header and body
    body = json.dumps(params)
    header = get_header(apiKey, signature(timestamp, 'POST', request_path, secretKey, body), timestamp, 'cht32489')
    # do request
    response = requests.post(url, data=body, headers=header, timeout=10)
    return response.json()

#??????????????????,??????????????????????????????????????????
def Close_Positions(secretKey,apiKey,posSide=None,mgnMode=None,ccy=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/trade/close-position'
    params = {'posSide':posSide,'mgnMode':mgnMode,'ccy':ccy}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    url = base_url + request_path
    timestamp = round(time.time(), 3)
    # request header and body
    body = json.dumps(params)
    header = get_header(apiKey, signature(timestamp, 'POST', request_path, secretKey, body), timestamp, 'cht32489')
    # do request
    response = requests.post(url, data=body, headers=header, timeout=10)
    return response.json()

#??????????????????
def Get_Order_Details(secretKey,apiKey,instId=None,ordId=None,clOrdId=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/trade/order'
    params = {'instId':instId,'ordId':ordId,'clOrdId':clOrdId}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#????????????????????????????????????????????????
def Get_Order_List(secretKey,apiKey,instType=None,uly=None,instId=None,ordType=None,state=None,after=None,before=None,limit=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/trade/orders-pending'
    params = {'instType':instType,'uly':uly,'instId':instId,'ordType':ordType,'state':state,'after':after,'before':before,'limit':limit}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#????????????7????????????????????????????????????????????????????????????????????? ?????????2??????
def Get_Order_History_last_7_days(secretKey,apiKey,instType=None,uly=None,instId=None,ordType=None,state=None,category=None,after=None,before=None,limit=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/trade/orders-history'
    params = {'instType':instType,'uly':uly,'instId':instId,'ordType':ordType,'state':state,'category':category,'after':after,'before':before,'limit':limit}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#????????????3???????????????????????????????????????????????????????????????????????? ?????????2??????
def Get_Order_History_last_3_months(secretKey,apiKey,instType=None,uly=None,instId=None,ordType=None,state=None,category=None,after=None,before=None,limit=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/trade/orders-history-archive'
    params = {'instType':instType,'uly':uly,'instId':instId,'ordType':ordType,'state':state,'category':category,'after':after,'before':before,'limit':limit}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#?????????3??????????????????????????????
def Get_Transaction_Details_last_3_days(secretKey,apiKey,instType=None,uly=None,instId=None,ordId=None,after=None,before=None,limit=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/trade/fills'
    params = {'instType':instType,'uly':uly,'instId':instId,'ordId':ordId,'after':after,'before':before,'limit':limit}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#?????????3?????????????????????????????????
def Get_Transaction_Details_last_3_months(secretKey,apiKey,instType=None,uly=None,instId=None,ordId=None,after=None,before=None,limit=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/trade/fills-history'
    params = {'instType':instType,'uly':uly,'instId':instId,'ordId':ordId,'after':after,'before':before,'limit':limit}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#??????????????????,?????????????????????????????? ??????????????????????????????????????????
def Place_Algo_Order(secretKey,apiKey,instId=None,tdMode=None,ccy=None,clOrdId=None,tag=None,side=None,posSide=None,ordType=None,sz=None,px=None,reduceOnly=None,tgtCcy=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/trade/order-algo'
    params = {'instId':instId,'tdMode':tdMode,'ccy':ccy,'clOrdId':clOrdId,'tag':tag,'side':side,'posSide':posSide,'ordType':ordType,'sz':sz,'px':px,'reduceOnly':reduceOnly,'tgtCcy':tgtCcy}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    url = base_url + request_path
    timestamp = round(time.time(), 3)
    # request header and body
    body = json.dumps(params)
    header = get_header(apiKey, signature(timestamp, 'POST', request_path, secretKey, body), timestamp, 'cht32489')
    # do request
    response = requests.post(url, data=body, headers=header, timeout=10)
    return response.json()

#???????????????????????????????????????????????????10??????????????????
def Cancel_Algo_Order(secretKey,apiKey,algoId=None,instId=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/trade/cancel-algos'
    params = {'algoId':algoId,'instId':instId}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    url = base_url + request_path
    timestamp = round(time.time(), 3)
    # request header and body
    body = json.dumps(params)
    header = get_header(apiKey, signature(timestamp, 'POST', request_path, secretKey, body), timestamp, 'cht32489')
    # do request
    response = requests.post(url, data=body, headers=header, timeout=10)
    return response.json()

#??????????????????????????????????????????????????????
def Get_Algo_Order_List(secretKey,apiKey,algoId=None,instType=None,instId=None,ordType=None,after=None,before=None,limit=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/trade/orders-algo-pending'
    params = {'algoId':algoId,'instType':instType,'instId':instId,'ordType':ordType,'after':after,'before':before,'limit':limit}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#????????????3????????????????????????????????????????????????
def Get_Algo_Order_History(secretKey,apiKey,state=None,algoId=None,instType=None,instId=None,ordType=None,after=None,before=None,limit=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/trade/orders-algo-history'
    params = {'state':state,'algoId':algoId,'instType':instType,'instId':instId,'ordType':ordType,'after':after,'before':before,'limit':limit}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#MARKET DATA

#??????????????????????????????
def Get_Tickers(secretKey,apiKey,instType=None,uly=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/market/tickers'
    params = {'instType':instType,'uly':uly}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#??????????????????????????????
def Get_Ticker(secretKey,apiKey,instId=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/market/ticker'
    params = {'instId':instId}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#????????????????????????
def Get_Index_Tickers(secretKey,apiKey,quoteCcy=None,instId=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/market/index-tickers'
    params = {'quoteCcy':quoteCcy,'instId':instId}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#????????????????????????
def Get_Order_Book(secretKey,apiKey,instId=None,sz=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/market/books'
    params = {'instId':instId,'sz':sz}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#??????K????????????K??????????????????????????????????????????K??????????????????????????????????????????1440??????
def Get_Candlesticks(secretKey,apiKey,instId=None,after=None,before=None,bar=None,limit=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/market/candles'
    params = {'instId':instId,'after':after,'before':before,'bar':bar,'limit':limit}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#????????????????????????K??????????????????????????????????????????????????????k?????????
def Get_Candlesticks_History_top_currencies_only(secretKey,apiKey,instId=None,after=None,before=None,bar=None,limit=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/market/history-candles'
    params = {'instId':instId,'after':after,'before':before,'bar':bar,'limit':limit}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#??????K??????????????????????????????????????????1440??????
def Get_Index_Candlesticks(secretKey,apiKey,instId=None,after=None,before=None,bar=None,limit=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/market/index-candles'
    params = {'instId':instId,'after':after,'before':before,'bar':bar,'limit':limit}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#????????????K??????????????????????????????????????????1440??????
def Get_Mark_Price_Candlesticks(secretKey,apiKey,instId=None,after=None,before=None,bar=None,limit=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/market/mark-price-candles'
    params = {'instId':instId,'after':after,'before':before,'bar':bar,'limit':limit}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#????????????????????????????????????,????????????????????????????????????
def Get_Trades(secretKey,apiKey,instId=None,limit=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/market/trades'
    params = {'instId':instId,'limit':limit}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#????????????24??????????????????,24?????????????????????????????????USD??????????????????
def Get_24H_Total_Volume(secretKey,apiKey):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/market/platform-24-volume'
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#Oracle ?????????????????? ?????????Open Oracle???????????????????????????????????????????????????
def Get_Oracle(secretKey,apiKey):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/market/open-oracle'
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#FUNDING

#???????????????????????????????????????????????????????????????????????????
def Get_Currencies(secretKey,apiKey):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/asset/currencies'
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489?A')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#?????????????????????????????????????????????????????????????????????????????????????????????
def Get_Balance(secretKey,apiKey,ccy=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/asset/balances'
    params = {'ccy':ccy}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489?A')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#????????????,?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
def Funds_Transfer(secretKey,apiKey,ccy=None,amt=None,type=None,_from=None,to=None,subAcct=None,instId=None,toInstId=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/asset/transfer'
    params = {'ccy':ccy,'amt':amt,'type':type,'from':_from,'to':to,'subAcct':subAcct,'instId':instId,'toInstId':toInstId}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    url = base_url + request_path
    timestamp = round(time.time(), 3)
    # request header and body
    body = json.dumps(params)
    header = get_header(apiKey, signature(timestamp, 'POST', request_path, secretKey, body), timestamp, 'cht32489?A')
    # do request
    response = requests.post(url, data=body, headers=header, timeout=10)
    return response.json()

#?????????????????????????????????????????????????????????????????????
def Asset_Bills_Details(secretKey,apiKey,ccy=None,type=None,after=None,before=None,limit=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/asset/bills'
    params = {'ccy':ccy,'type':type,'after':after,'before':before,'limit':limit}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489?A')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()

#PUBLIC DATA

#?????????????????????????????????????????????
def Get_Instruments(secretKey,apiKey,instType=None,uly=None,instId=None):
    base_url = 'https://www.okex.com'
    request_path = '/api/v5/public/instruments'
    params = {'instType':instType,'uly':uly,'instId':instId}
    if parse_params_to_str(params) == None:
        request_path = request_path
    else:
        request_path = request_path + parse_params_to_str(params)
    timestamp = round(time.time(), 3)
    header = get_header(apiKey, signature(timestamp, 'GET', request_path, secretKey, body=''), timestamp, 'cht32489?A')
    response = requests.get(base_url + request_path, headers=header, timeout=10)
    return response.json()
#?????????

class Banzhuangongren():
    #??????
    global secretKey
    global apiKey
    def __init__(self,instrument_id,position_amount):
        self.instrument_id = instrument_id
        self.position_amount = position_amount
        self.lowest = 10000000000000

    def get_ticker(self):
        '''
        ???????????????20???/2s
        '''
        
        try:
            ticker_dict = Get_Ticker(secretKey,apiKey,self.instrument_id)['data'][0]
            if 'last' in ticker_dict:
                self.last = float(ticker_dict['last'])
                self.best_bid = float(ticker_dict['bidPx'])
                self.best_ask = float(ticker_dict['askPx'])
                if self.last < self.lowest:
                    self.lowest = self.last
                return ticker_dict

            else:
                print('future tick')
                print(time.ctime())
                time.sleep(10)
        except:
            time.sleep(10)
            print('ticker error')
    def get_position(self):
        '''
        ????????????????????????
        '''
        self.order_position = math.floor(self.position_amount/(float(dic_instruments[self.instrument_id.split('-')[0]])*self.last))

    def get_sell_position(self):
        try:
            position_data  = Get_Positions(secretKey,apiKey,instId=self.instrument_id)['data'][:]
        except:
            pass
        try:
            for i in position_data:
                if i['posSide'] == 'short' and int(i['availPos'])>0 and i['mgnMode'] == 'isolated':
                    self.order_position = int(i['availPos'])
        except:
            pass
     
    def cancel_order(self):
        Cancel_Order(secretKey, apiKey,instId=self.instrument_id,ordId=self.order_id)
    
    def make_order(self):
        '''
        '''
        #Place_Order(secretKey,apiKey,instId='XCH-USDT-SWAP',tdMode='isolated',side='buy',ordType='limit',sz='1',px='3'))
        self.get_position()
        resp = Place_Order(secretKey, apiKey, px="{:.18f}".format(self.best_bid * 0.999), tdMode='isolated',sz=self.order_position, instId=self.instrument_id,side='sell',ordType='limit',posSide='short')
        self.order_id = resp['data'][0]['ordId']
        print(resp)
        return resp

    def close_position(self):
        '''
        ??????
        '''
        self.cancel_order()
        self.get_ticker()
        self.get_sell_position()
        resp = Place_Order(secretKey, apiKey, tdMode='isolated',px="{:.18f}".format(self.best_ask*1.001), sz=self.order_position, instId=self.instrument_id,side='buy',ordType='limit',posSide='short')
        return resp

    def close_position_win(self):
        '''
        ????????????
        '''
        self.cancel_order()
        self.get_ticker()
        self.get_sell_position()
        resp = Place_Order(secretKey, apiKey, tdMode='isolated',px="{:.18f}".format(self.best_bid), sz=self.order_position, instId=self.instrument_id,side='buy',ordType='limit',posSide='short')
        return resp

class Gongren():
    #??????
    global secretKey
    global apiKey
    def __init__(self,instrument_id,position_amount):
        self.instrument_id = instrument_id
        self.position_amount = position_amount
        self.highest = 0

    def get_ticker(self):
        '''
        ???????????????20???/2s
        '''
        
        try:
            ticker_dict = Get_Ticker(secretKey,apiKey,self.instrument_id)['data'][0]
            if 'last' in ticker_dict:
                self.last = float(ticker_dict['last'])
                self.best_bid = float(ticker_dict['bidPx'])
                self.best_ask = float(ticker_dict['askPx'])
                if self.last > self.highest:
                    self.highest = self.last
                return ticker_dict

            else:
                print('future tick')
                print(time.ctime())
                time.sleep(10)
        except:
            time.sleep(10)
            print('ticker error')
    def get_position(self):
        '''
        ????????????????????????
        '''
        self.order_position = math.floor(self.position_amount/(float(dic_instruments[self.instrument_id.split('-')[0]])*self.last))

    def get_sell_position(self):
        try:
            position_data  = Get_Positions(secretKey,apiKey,instId=self.instrument_id)['data'][:]
        except:
            pass
        try:
            for i in position_data:
                if i['posSide'] == 'long' and int(i['availPos'])>0 and i['mgnMode'] == 'isolated':
                    self.order_position = int(i['availPos'])
        except:
            pass
    def cancel_order(self):
        Cancel_Order(secretKey, apiKey,instId=self.instrument_id,ordId=self.order_id)
    
    def make_order(self):
        '''
        '''
        #Place_Order(secretKey,apiKey,instId='XCH-USDT-SWAP',tdMode='isolated',side='buy',ordType='limit',sz='1',px='3'))
        self.get_position()
        resp = Place_Order(secretKey, apiKey, tdMode='isolated',px="{:.18f}".format(self.best_ask*1.001), sz=self.order_position, instId=self.instrument_id,side='buy',ordType='limit',posSide='long')
        self.order_id = resp['data'][0]['ordId']
        print(resp)
        return resp

    def close_position(self):
        '''
        ??????
        '''
        self.cancel_order()
        self.get_ticker()
        self.get_sell_position()
        resp = Place_Order(secretKey, apiKey, tdMode='isolated',px="{:.18f}".format(self.best_bid*0.999), sz=self.order_position, instId=self.instrument_id,side='sell',ordType='limit',posSide='long')
        return resp

    def close_position_win(self):
        '''
        ????????????
        '''
        self.cancel_order()
        self.get_ticker()
        self.get_sell_position()
        resp = Place_Order(secretKey, apiKey, tdMode='isolated',px="{:.18f}".format(self.best_ask), sz=self.order_position, instId=self.instrument_id,side='sell',ordType='limit',posSide='long')
        return resp

#print(Get_Candlesticks(secretKey,apiKey,'TORN-USDT',bar='30m'))
#Place_Order(secretKey,apiKey,instId=None,tdMode=None,ccy=None,clOrdId=None,tag=None,side=None,posSide=None,ordType=None,sz=None,px=None,reduceOnly=None,tgtCcy=None):
#def Get_Instruments(secretKey,apiKey,instType=None,uly=None,instId=None):

#print(Get_Instruments(secretKey,apiKey,instType='SWAP'))
#print(Place_Order(secretKey,apiKey,instId='XCH-USDT-SWAP',tdMode='isolated',side='sell',ordType='limit',sz='1',px='240',posSide='short'))
#print(Get_Ticker(secretKey,apiKey,instId='XCH-USDT-SWAP'))
#print(Set_Position_mode(secretKey,apiKey,posMode='long_short_mode'))
#print(Get_Account_Configuration(secretKey,apiKey))
#print(Get_Positions(secretKey,apiKey,instId='XCH-USDT-SWAP')['data'][0])
#print(Get_Tickers(secretKey,apiKey,instType='SWAP'))
#print(Get_Candlesticks(secretKey,apiKey,instId='XCH-USDT-SWAP',limit = '300'))
#print(Get_Tickers(secretKey,apiKey,instType='SWAP'))
#a = Get_Positions(secretKey,apiKey,instId='LPT-USDT-SWAP')['data'][:]
#Set_Position_mode(secretKey,apiKey,posMode='long_short_mode')
#a = Get_Instruments(secretKey,apiKey,instType='SWAP',uly=None,instId=None)
'''
spot_instruments = ['DOT', 'DOGE', 'FIL', 'YFII', 'ETC', 'OP', '1INCH', 'AAVE', 'ADA', 'AGLD', 'ALGO', 'ALPHA', 'ANT', 'APE', 'API3', 'ASTR', 'ATOM', 'AVAX', 'AXS', 'BABYDOGE', 'BADGER', 'BAL', 'BAND', 'BAT', 'BCH', 'BICO', 'BNT', 'BSV', 'BTM', 'BTT', 'BZZ', 'CELO', 'CEL', 'CFX', 'CHZ', 'COMP', 'CONV', 'CQT', 'CRO', 'CRV', 'CSPR', 'CVC', 'DASH', 'DOME', 'DORA', 'DYDX', 'EFI', 'EGLD', 'ELON', 'ENJ', 'ENS', 'EOS', 'FITFI', 'FLM', 'FTM', 'GALA', 'GMT', 'GODS', 'GRT', 'ICP', 'IMX', 'IOST', 'IOTA', 'JST', 'KISHU', 'KNC', 'KSM', 'LAT', 'LINK', 'LON', 'LOOKS', 'LPT', 'LRC', 'LUNA', 'MANA', 'MASK', 'MATIC', 'MINA', 'MKR', 'NEAR', 'NEO', 'NFT', 'NYM', 'OMG', 'ONT', 'PEOPLE', 'PERP', 'QTUM', 'REN', 'RSR', 'RSS3', 'RVN', 'SAND', 'SC', 'SHIB', 'SLP', 'SNX', 'SOL', 'SOS', 'SRM', 'STARL', 'STORJ', 'SUSHI', 'SWRV', 'THETA', 'TORN', 'TRB', 'TRX', 'UMA', 'UMEE', 'UNI', 'WAVES', 'WNCG', 'WNXM', 'XCH', 'XEM', 'XLM', 'XMR', 'XRP', 'XTZ', 'YFI', 'YGG', 'ZEC', 'ZEN', 'ZIL', 'ZRX']

for i in spot_instruments:
    time.sleep(0.2)
    print(Set_Leverage(secretKey,apiKey,instId=i+'-USDT-SWAP',ccy=None,lever='15',mgnMode='isolated',posSide='long'))
    time.sleep(0.2)
    print(Set_Leverage(secretKey,apiKey,instId=i+'-USDT-SWAP',ccy=None,lever='15',mgnMode='isolated',posSide='short'))
    '''