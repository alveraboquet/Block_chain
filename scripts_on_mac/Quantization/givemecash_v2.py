import v5api
import math
import time
from v5api import Banzhuangongren,Gongren
from multiprocessing import Process,Queue
import multiprocessing
import threading
import os,signal
import random

#secretKey = 'E151509E0F8AA6F30BABA39C03A9E32E'
secretKey = '8A3EAF3B40791AD60A3C06CA34E99EE6'

#apiKey = '31b9093b-a2fb-446d-8008-3c6ef81c1f1d'
apiKey = '17eaacb2-d33d-4eb7-b2dd-6a068964d942'
#现在正在交易的ins
global ins_list
#因为买卖差价过大不交易的比重，每两小时更新一次，最重要
global ins_list_2
#queue3过30分钟后传出来
global ins_list_3
#大仓位交易
global ins_list_4
#不交易Ins
global ins_list_5
#要改成一个大仓位，一个普通仓位
global transfer_amount_normal
global position_amount_normal
global transfer_amount_huge
global position_amount_huge
global dic_instruments
global spot_instruments
#最多有多少个普通仓位的ins在交易
global amount_normal
global short_win_ratio
global short_lose_ratio
global swap_tickers
global long_signal
global short_signal
global long_win_ratio

amount_normal = 400
short_win_ratio = 0.15
short_lose_ratio = 0.03
ins_list = []
ins_list_2 = []
ins_list_3 = []
#大仓位Ins列表
ins_list_4 = []
#不交易ins
ins_list_5 = []
#交易仓位
position_amount_normal = 400

position_amount_huge = 400
spot_instruments = []
dic_instruments = {}
swap_tickers = {}
long_signal = 1
short_signal = 1
long_win_ratio = 0.5
long_lose_ratio = 0.03

def thread_inp(q4,q6,q7):
    global ins_list
    global ins_list_2
    global ins_list_3
    global ins_list_4
    global ins_list_5
    global thread_input
    global transfer_amount_normal
    global position_amount_normal
    global transfer_amount_huge
    global position_amount_huge
    global dic_instruments
    global spot_instruments
    global amount_normal
    global short_win_ratio
    global short_lose_ratio
    global long_signal
    global short_signal
    global long_win_ratio
    thread_input = None

    while thread_input == None:
        try:
            thread_input = input()
            if thread_input == '1':
                print('chang positon')
                transfer_amount_normal = int(input('transfer_amount_normal(100 for example:'))
                position_amount_normal = int(input('transfer_amount_normal(950 for example:'))
                transfer_amount_huge = int(input('transfer_amount_normal(200 for example:'))
                position_amount_huge = int(input('transfer_amount_normal(1950 for example:'))
                print(transfer_amount_normal,position_amount_normal,transfer_amount_huge,position_amount_huge)
                thread_input = None
            elif thread_input == '2':
                aa = input('not trade ins:')
                if aa == '1':
                    ins_list_5 = input('create/reset new not trade list:')
                    print(ins_list_5)
                    thread_input = None
                elif aa == '2':
                    iii = input('add not trade ins:')
                    ins_list_5 = ins_list_5 + iii
                    print(ins_list_5)
                    thread_input = None
            elif thread_input == '3':
                ins_list_4 = input('create huge position ins:')
                ins_list_4 = ins_list_4.split(',')
                print(ins_list_4)
                thread_input = None
            elif thread_input == '4':
                print(dic_instruments)
                print(spot_instruments)
                spot_instrument = input('please type add ins:')
                amount = float(input('please type amount per future:'))
                spot_instruments.append(spot_instrument)
                dic_instruments[spot_instrument] = amount
                print(spot_instrument)
                print(amount)
                thread_input = None
            elif thread_input == '5':
                print('ins1',ins_list,len(ins_list),'ins2', ins_list_2,len(ins_list_2),'ins3', ins_list_3,len(ins_list_3),'ins4', ins_list_4,len(ins_list_4),'ins5',ins_list_5,len(ins_list_5))
                thread_input = None
            elif thread_input == '6':
                remove_ins = input('please type remove ins:')
                ins_list.remove(remove_ins)
                ins_list_3.remove(remove_ins)
                thread_input = None
            elif thread_input == '7':
                print('kill parent process')
                pid = os.getpid()
                os._exit()
            elif thread_input == '8':
                try:
                    print('kill specific process:')
                    pid = int(input())
                    os.kill(pid,signal.SIGKILL)
                except:
                    print('kill error')
                thread_input = None
            elif thread_input == '9':
                print('situation')
                q4.put(1)
                print(len(ins_list))
                print(ins_list)
                print(ins_list_4)
                time.sleep(7)
                q4.get()
                thread_input = None
            elif thread_input == '10':
                amount_normal = int(input('please type amount_normal:'))
                thread_input = None
            elif thread_input == '11':
                collect_usdt()
                thread_input = None
            elif thread_input == '12':
                print('close short')
                q6.put(1)
                time.sleep(10)
                q6.get()
                thread_input = None
            elif thread_input == '13':
                print('close long')
                q7.put(1)
                time.sleep(10)
                q7.get()
                thread_input = None
            elif thread_input == '14':
                short_win_ratio = float(input('please type short_win_ratio:'))
                print(short_win_ratio)
                short_lose_ratio = float(input('please type short_lose_ratio:'))
                print(short_lose_ratio)
                thread_input = None
            elif thread_input == '15':
                long_signal = 10
                print('long_signal = ',long_signal,'no long trade')
                thread_input = None
            elif thread_input == '16':
                long_signal = 1
                print('long_signal = ',long_signal,'have long trade')
                thread_input = None
            elif thread_input == '17':
                long_signal = 0.1
                print('short_signal = ',short_signal,'no short trade')
                thread_input = None
            elif thread_input == '18':
                short_signal = 1
                print('short_signal = ',short_signal,'have short trade')
                thread_input = None
            elif thread_input == '19':
                long_win_ratio = float(input('please type long_win_ratio:'))
                print(long_win_ratio)
                thread_input = None
            elif thread_input == '20':
                st = float(input('please type remove ins_list_2:'))
                ins_list_2.remove(st)
                print(ins_list_2)
                thread_input = None
            elif thread_input == '21':
                st = float(input('please type remove ins_list_3:'))
                ins_list_3.remove(st)
                print(ins_list_3)
                thread_input = None
            elif thread_input == '22':
                st = float(input('please type remove ins_list_4:'))
                ins_list_4.remove(st)
                print(ins_list_4)
                thread_input = None
            elif thread_input is not None:
                print('error')
                thread_input = None
        except:
            thread_input = None
            print('123')

def banzhuangongren(instrument_id, q4,q6,q7,position_amount):
    # 做空
    global ins_list_4
    global ins_list_2
    global ins_list_3
    global short_win_ratio
    global short_lose_ratio
    global swap_tickers
    # 获得当前时间时间戳
    now = int(time.time())
    #转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
    timeArray = time.localtime(now)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(otherStyleTime)
    print(time.time(),'short swap'+ instrument_id)
    gongren = Banzhuangongren(instrument_id, position_amount)
    gongren.get_ticker()
    gongren.make_order()
    gongren.now_price = gongren.last
    win_price = gongren.last * (1 - short_win_ratio)
    time.sleep(1)
    print(gongren.last)
    print(instrument_id)

    close_price = gongren.last * (1 + short_lose_ratio)

    while 1:
        time.sleep(0.5)
        #数据获取
        #swap_tickers = q5.get(block=True, timeout=None)
        #q5.put(swap_tickers, block=True, timeout=None)
        tickers = swap_tickers
        for ticker in tickers:
            if ticker['instId'] == instrument_id:
                gongren.last = float(ticker["last"])

        if gongren.last > close_price:
            gongren.close_position()
            print(instrument_id,'swap finish short')
            #q2.put(instrument_id.split('-')[0])
            #q3.put(instrument_id.split('-')[0])
            ins_list_2.remove(instrument_id.split('-')[0])
            ins_list_3.remove(instrument_id.split('-')[0])
            break
        if gongren.last < win_price:
            #win_price = win_price * (1 - 0.1)
            #close_price = win_price / (1 - 0.1) * (1 + 0.03)
            time.sleep(240)
            gongren.close_position_win()
            print(instrument_id,'swap win finish short')
            #q2.put(instrument_id.split('-')[0])
            ins_list_2.remove(instrument_id.split('-')[0])
            time.sleep(3600*12)
            #q3.put(instrument_id.split('-')[0])
            ins_list_3.remove(instrument_id.split('-')[0])
            break

        if q4.empty() == False:
            print('ins short',instrument_id,'buy price',gongren.now_price,'last price',gongren.last,'position_amount',position_amount,'pid',os.getpid())
            time.sleep(10)

        if q6.empty() == False:
            time.sleep(random.randint(1,10))
            print(instrument_id,'swap close finish short')
            gongren.close_position_win()
            #q2.put(instrument_id.split('-')[0])
            ins_list_2.remove(instrument_id.split('-')[0])
            #q3.put(instrument_id.split('-')[0])
            ins_list_3.remove(instrument_id.split('-')[0])
            time.sleep(10)
            break
     

def gongren(instrument_id, q4,q6,q7,position_amount):
    # 永续合约做多
    global ins_list_4
    global ins_list
    global swap_tickers
    global long_win_ratio
    # 获得当前时间时间戳
    now = int(time.time())
    #转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
    timeArray = time.localtime(now)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(otherStyleTime)
    print(time.time(),'long swap'+ instrument_id)
    gongren = Gongren(instrument_id,position_amount)
    gongren.get_ticker()
    gongren.make_order()
    gongren.now_price = gongren.last
    win_price = gongren.last * (1 + long_win_ratio)
    time.sleep(1)
    print(gongren.last)
    print(instrument_id)

    close_price = gongren.last * (1 - long_lose_ratio)

    while 1:
        time.sleep(0.5)
        tickers = swap_tickers
        for ticker in tickers:
            if ticker['instId'] == instrument_id:
                gongren.last = float(ticker["last"])

        if gongren.last < close_price:
            gongren.close_position()
            print(instrument_id,'swap long lose finish')
            #q1.put(instrument_id.split('-')[0])
            ins_list_4.remove(instrument_id.split('-')[0])
            
            break
        if gongren.last > win_price:
            #win_price = win_price * (1 - 0.1)
            #close_price = win_price / (1 - 0.1) * (1 + 0.03)
            time.sleep(60)
            gongren.close_position_win()
            print(instrument_id,'swap long win finish')
            #q1.put(instrument_id.split('-')[0])
            time.sleep(3600*12)
            ins_list_4.remove(instrument_id.split('-')[0])

            break

        if q4.empty() == False:
            print('ins long',instrument_id,'buy price',gongren.now_price,'last price',gongren.last,'position_amount',position_amount,'pid',os.getpid())
            time.sleep(10)
       

        if q7.empty() == False:
            time.sleep(random.randint(1,10))
            print(instrument_id,'swap long finish')
            gongren.close_position_win()
            #q1.put(instrument_id.split('-')[0])
            ins_list_4.remove(instrument_id.split('-')[0])
            time.sleep(10)
            break


def main():
    global transfer_amount_normal
    global position_amount_normal
    global transfer_amount_huge
    global position_amount_huge
    global ins_list
    global ins_list_2
    global ins_list_3
    global ins_list_4
    global ins_list_5
    global amount_normal
    global dic_instruments
    global spot_instruments
    global swap_tickers
    global long_signal
    global short_signal
    dic_instruments = {'DOT': '1', 'DOGE': '1000', 'FIL': '0.1', 'YFII': '0.001', 'ETC': '10', 'OP': '1', '1INCH': '1', 'AAVE': '0.1', 'ADA': '100', 'AGLD': '1', 'ALGO': '10', 'ALPHA': '1', 'ANT': '1', 'APE': '0.1', 'API3': '1', 'ASTR': '10', 'ATOM': '1', 'AVAX': '1', 'AXS': '0.1', 'BABYDOGE': '1000000000', 'BADGER': '0.1', 'BAL': '0.1', 'BAND': '1', 'BAT': '10', 'BCH': '0.1', 'BICO': '1', 'BNT': '10', 'BSV': '1', 'BTM': '100', 'BTT': '1000000', 'BZZ': '0.1', 'CELO': '1', 'CEL': '10', 'CFX': '10', 'CHZ': '10', 'COMP': '0.1', 'CONV': '10', 'CQT': '1', 'CRO': '10', 'CRV': '1', 'CSPR': '1', 'CVC': '100', 'DASH': '0.1', 'DOME': '100', 'DORA': '0.1', 'DYDX': '1', 'EFI': '1', 'EGLD': '0.1', 'ELON': '1000000', 'ENJ': '1', 'ENS': '0.1', 'EOS': '10', 'FITFI': '10', 'FLM': '10', 'FTM': '10', 'GALA': '10', 'GMT': '1', 'GODS': '1', 'GRT': '10', 'ICP': '0.01', 'IMX': '1', 'IOST': '1000', 'IOTA': '10', 'JST': '100', 'KISHU': '1000000000', 'KNC': '1', 'KSM': '0.1', 'LAT': '10', 'LINK': '1', 'LON': '1', 'LOOKS': '1', 'LPT': '0.1', 'LRC': '10', 'LUNA': '1', 'MANA': '10', 'MASK': '1', 'MATIC': '10', 'MINA': '1', 'MKR': '0.01', 'NEAR': '10', 'NEO': '1', 'NFT': '1000000', 'NYM': '1', 'OMG': '1', 'ONT': '10', 'PEOPLE': '100', 'PERP': '1', 'QTUM': '1', 'REN': '10', 'RSR': '100', 'RSS3': '10', 'RVN': '10', 'SAND': '10', 'SC': '100', 'SHIB': '1000000', 'SLP': '10', 'SNX': '1', 'SOL': '1', 'SOS': '1000000', 'SRM': '1', 'STARL': '100000', 'STORJ': '10', 'SUSHI': '1', 'SWRV': '1', 'THETA': '10', 'TORN': '0.01', 'TRB': '0.1', 'TRX': '1000', 'UMA': '0.1', 'UMEE': '10', 'UNI': '1', 'WAVES': '1', 'WNCG': '1', 'WNXM': '0.1', 'XCH': '0.01', 'XEM': '10', 'XLM': '100', 'XMR': '0.1', 'XRP': '100', 'XTZ': '1', 'YFI': '0.0001', 'YGG': '1', 'ZEC': '0.1', 'ZEN': '1', 'ZIL': '100', 'ZRX': '10'}
    spot_instruments = ['DOT', 'DOGE', 'FIL', 'YFII', 'ETC', 'OP', '1INCH', 'AAVE', 'ADA', 'AGLD', 'ALGO', 'ALPHA', 'ANT', 'APE', 'API3', 'ASTR', 'ATOM', 'AVAX', 'AXS', 'BABYDOGE', 'BADGER', 'BAL', 'BAND', 'BAT', 'BCH', 'BICO', 'BNT', 'BSV', 'BTM', 'BTT', 'BZZ', 'CELO', 'CEL', 'CFX', 'CHZ', 'COMP', 'CONV', 'CQT', 'CRO', 'CRV', 'CSPR', 'CVC', 'DASH', 'DOME', 'DORA', 'DYDX', 'EFI', 'EGLD', 'ELON', 'ENJ', 'ENS', 'EOS', 'FITFI', 'FLM', 'FTM', 'GALA', 'GMT', 'GODS', 'GRT', 'ICP', 'IMX', 'IOST', 'IOTA', 'JST', 'KISHU', 'KNC', 'KSM', 'LAT', 'LINK', 'LON', 'LOOKS', 'LPT', 'LRC', 'LUNA', 'MANA', 'MASK', 'MATIC', 'MINA', 'MKR', 'NEAR', 'NEO', 'NFT', 'NYM', 'OMG', 'ONT', 'PEOPLE', 'PERP', 'QTUM', 'REN', 'RSR', 'RSS3', 'RVN', 'SAND', 'SC', 'SHIB', 'SLP', 'SNX', 'SOL', 'SOS', 'SRM', 'STARL', 'STORJ', 'SUSHI', 'SWRV', 'THETA', 'TORN', 'TRB', 'TRX', 'UMA', 'UMEE', 'UNI', 'WAVES', 'WNCG', 'WNXM', 'XCH', 'XEM', 'XLM', 'XMR', 'XRP', 'XTZ', 'YFI', 'YGG', 'ZEC', 'ZEN', 'ZIL', 'ZRX']
    ins_list_2 = []
    ins_list_4 = []
    q1 = Queue(10)
    #main函数处理交易完的Ins,从ins_list中剔除
    q2 = Queue(10)

    q3 = Queue(30)
    #子进程上传状态信号
    q4 = Queue(1)

    #传所有的合约信息
    q5 = Queue(1)

    q6 = Queue(1)

    q7 = Queue(1)
    #swap_tickers = v3api.swapTickers(secretKey,apiKey)
    temp_swap_tickers = v5api.Get_Tickers(secretKey,apiKey,instType='SWAP')['data']
    print(3)
    while len(temp_swap_tickers) < 30:
        print('1 swap_tickers')
        time.sleep(10)
        temp_swap_tickers = v5api.Get_Tickers(secretKey,apiKey,instType='SWAP')['data']
    swap_tickers = temp_swap_tickers
    #t1 = threading.Thread(target = thread_inp,args=[q4,q6,q7])
    #t1.start()
    count=time.time()
    print(4)
    while True:
        try:
            dic_high = {}
            dic_low = {}
            print(5)
            for spot_ins in spot_instruments:
                time.sleep(1)
                k_lines = v5api.Get_Candlesticks(secretKey,apiKey,instId=spot_ins + '-USDT',bar='1H',limit='300')['data']
                #最低价
                k_lines_1 = k_lines[:300]
                #最高价
                k_lines = v5api.Get_Candlesticks(secretKey,apiKey,instId=spot_ins + '-USDT',bar='1H',limit='300')['data']
                k_lines_2 = k_lines[:300]
                
                high = -100000000000000000000
                for k_line in k_lines_2:
                    average_high = (max(float(k_line[1]),float(k_line[4])) + float(k_line[2]))/2
                    if average_high > high:
                        high = average_high

                if spot_ins in spot_instruments:
                    dic_high[spot_ins] = high
                low = 100000000000000000000
                for k_line in k_lines_1:
                    average_low = (min(float(k_line[1]),float(k_line[4]))+float(k_line[3]))/2
                    if average_low < low:
                        low = average_low
                if spot_ins in spot_instruments:
                    dic_low[spot_ins] = low

        except Exception as ex:
            time.sleep(20) 
            print('main Process error 1')
            print(ex)  
       
        

        #获取全部币种实时价格
        try:
            print('k线更新完毕 进入价格监测')
            while True:
                swap_tickers = v5api.Get_Tickers(secretKey,apiKey,instType='SWAP')['data']
                a  = v5api.Get_Tickers(secretKey,apiKey,instType='SPOT')['data']
                for ticker in a:
                    if ticker['instId'].split('-')[0] in spot_instruments and 'USDT' in ticker['instId']:
                        time.sleep(1)
                        if float(ticker['last']) < short_signal * float(dic_low[ticker['instId'].split('-')[0]]) and ticker['instId'].split('-')[0] in dic_instruments:
                            
                            dic_low[ticker['instId'].split('-')[0]] = ticker['last']
                            if ticker['instId'].split('-')[0] in ins_list:
                                pass
                            elif ticker['instId'].split('-')[0] in ins_list_5:
                                pass
                            elif ticker['instId'].split('-')[0] in ins_list_3:
                                pass
                            elif ticker['instId'].split('-')[0] in ins_list_2:
                                pass

                            else:
                                position_amount = position_amount_normal
                                
                                short = threading.Thread(target=banzhuangongren,args=(ticker['instId']+'-SWAP',q4,q6,q7,position_amount))
                                
                                short.start()
                                
                                print(ticker['instId'].split('-')[0],'开空')
                                ins_list_2.append(ticker['instId'].split('-')[0])
                                ins_list_3.append(ticker['instId'].split('-')[0])
                        if float(ticker['last']) > long_signal * float(dic_high[ticker['instId'].split('-')[0]]) and ticker['instId'].split('-')[0] in dic_instruments:
                                
                                #做多
                            dic_high[ticker['instId'].split('-')[0]] = ticker['last']
                                
                            if ticker['instId'].split('-')[0] in ins_list_5:
                                pass
                            elif ticker['instId'].split('-')[0] in ins_list_4:
                                pass

                            else:
                                position_amount = position_amount_normal
                                long = threading.Thread(target=gongren,args=(ticker['instId']+'-SWAP',q4,q6,q7,position_amount))
                                long.start()
                                print(ticker['instId'].split('-')[0],'开多')
                                ins_list_4.append(ticker['instId'].split('-')[0])
                    
                if time.time() - count > 3600*4:
                    count = time.time()
                    print(ins_list_2)
                    print(ins_list_3)
                    print(ins_list_4)
                    break
                
            
        except Exception as ex:
 
    
            time.sleep(20)
            print('main Process error 2')
            print(ex)  
  
#有一个裁判去具体判断是否买入，由工人去做具体买入操作


if __name__=='__main__':
    # 获得当前时间时间戳
    now = int(time.time())
    #转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
    timeArray = time.localtime(now)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(otherStyleTime)
    main()
    
