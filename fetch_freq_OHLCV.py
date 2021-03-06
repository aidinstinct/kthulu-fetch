import sys, os, asyncio, logging, re

logging.basicConfig(filename='build_kraken_data.log', level=logging.DEBUG)


async def build_kraken_data():
    thisdir = os.getcwd()
    get_coins = ['XBT', 'ETH', 'USDT']
    #get_coins = ['XBT']
    print(thisdir+'/kraken_csv/all')
    for r, d, f in os.walk(thisdir+'/kraken_csv/all'):
        for coin in get_coins:
            for file in f:
                if re.match(coin,file):
                    print(file)
                    #get trading pair data
                    print("Current job:" + str(file))
                    cp = os.path.join(r,file)
                    do_fetch_format = {
                        'cp'              : f'cp {cp} {thisdir}/kraken_csv/avengers',
                        'fetch_freq_json' : f'cd {thisdir}/kraken_csv/avengers; sed -i "s/e/E/g" {file}; cut -d"," -f -6 {file} > {thisdir}/tmp/output_{file}',
                        'export'          : f'sudo python3 export_to_freq.py {file} output_{file} {coin} {thisdir}'
                        }
                    
                    for k in do_fetch_format:
                        init_sys_fetch = await asyncio.create_subprocess_shell(str(do_fetch_format[k]), stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE, shell=True)
                        stdout, stderr = await init_sys_fetch.communicate()
                        if stdout:
                            logging.info(f'[stdout]\n{stdout.decode()}')
                            print(f'[stdout]\n{stdout.decode()}')
                        if stderr:
                            logging.info(f'[stderr]\n{stderr.decode()}')
                            print(f'[stderr]\n{stderr.decode()}')
                            sys.exit(1)
                    #Export to freqtrade read-in &&mongodb
                    """
                    do_export_to_freq = {'export': f'sudo python3 export_to_freq.py {file} output_{file} {coin} {thisdir}'}
                    for ex in do_export_to_freq:
                        print('made it to export')
                        init_sys_export = await asyncio.create_subprocess_shell(str(do_export_to_freq[ex]), stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE, shell=True)
                        stdout, stderr = await init_sys_export.communicate()

                        if stdout:
                            logging.info(f'[stdout]\n{stdout.decode()}')
                            print(f'[stdout]\n{stdout.decode()}')

                        if stderr:
                            logging.info(f'[stderr]\n{stderr.decode()}')
                            print(f'[stderr]\n{stderr.decode()}')
                            sys.exit(1)
                    """
asyncio.run(build_kraken_data())

avengers = """
ADAGBP_5.csv
ADAEUR_60.csv
ADAAUD_720.csv
ADAGBP_1440.csv
ADAXBT_60.csv
ADAAUD_60.csv
ADAETH_5.csv
ADAETH_720.csv
ADAAUD_1.csv
ADAETH_15.csv
ADAEUR_720.csv
ADAGBP_60.csv
ADAXBT_720.csv
ADAAUD_1440.csv
ADAEUR_5.csv
ADAGBP_15.csv
ADAUSDT_15.csv
ADAUSDT_1440.csv
ADAXBT_5.csv
ADAETH_60.csv
ADAXBT_1440.csv
ADAUSDT_60.csv
ADAUSD_15.csv
ADAUSDT_720.csv
ADAEUR_15.csv
ADAEUR_1440.csv
ADAXBT_15.csv
ADAUSDT_5.csv
ADAGBP_1.csv
ADAUSD_60.csv
ADAXBT_1.csv
ADAGBP_720.csv
ADAAUD_15.csv
ADAUSD_720.csv
ADAUSD_1.csv
ADAUSDT_1.csv
ADAEUR_1.csv
ADAUSD_5.csv
ADAETH_1.csv
ADAETH_1440.csv
ADAUSD_1440.csv
ADAAUD_5.csv
MLNEUR_5.csv
MLNETH_1440.csv
MLNUSD_1.csv
MLNUSD_1440.csv
MLNEUR_15.csv
MLNXBT_1.csv
MLNETH_720.csv
MLNETH_60.csv
MLNEUR_1.csv
MLNXBT_1440.csv
MLNUSD_5.csv
MLNEUR_720.csv
MLNXBT_5.csv
MLNXBT_60.csv
MLNXBT_720.csv
MLNUSD_60.csv
MLNETH_5.csv
MLNUSD_15.csv
MLNUSD_720.csv
MLNETH_1.csv
MLNXBT_15.csv
MLNEUR_1440.csv
MLNETH_15.csv
MLNEUR_60.csv
EWTXBT_15.csv
EWTUSD_1440.csv
EWTXBT_1440.csv
EWTUSD_720.csv
EWTUSD_15.csv
EWTUSD_60.csv
EWTGBP_60.csv
EWTUSD_1.csv
EWTEUR_5.csv
EWTGBP_15.csv
EWTGBP_1440.csv
EWTEUR_720.csv
EWTGBP_720.csv
EWTXBT_60.csv
EWTXBT_1.csv
EWTXBT_720.csv
EWTEUR_1440.csv
EWTXBT_5.csv
EWTEUR_15.csv
EWTUSD_5.csv
EWTEUR_60.csv
EWTGBP_1.csv
EWTGBP_5.csv
EWTEUR_1.csv
AAVEETH_1.csv
AAVEUSD_720.csv
AAVEETH_60.csv
AAVEEUR_1.csv
AAVEETH_720.csv
AAVEXBT_1440.csv
AAVEGBP_5.csv
AAVEUSD_5.csv
AAVEAUD_15.csv
AAVEGBP_60.csv
AAVEEUR_15.csv
AAVEAUD_1440.csv
AAVEETH_1440.csv
AAVEGBP_15.csv
AAVEXBT_60.csv
AAVEXBT_15.csv
AAVEGBP_720.csv
AAVEGBP_1.csv
AAVEAUD_720.csv
AAVEUSD_15.csv
AAVEAUD_1.csv
AAVEEUR_1440.csv
AAVEAUD_60.csv
AAVEEUR_720.csv
AAVEXBT_720.csv
AAVEETH_5.csv
AAVEUSD_1.csv
AAVEGBP_1440.csv
AAVEEUR_60.csv
AAVEEUR_5.csv
AAVEETH_15.csv
AAVEXBT_1.csv
AAVEAUD_5.csv
AAVEUSD_1440.csv
AAVEXBT_5.csv
AAVEUSD_60.csv
ALGOUSD_720.csv
ALGOGBP_15.csv
ALGOGBP_5.csv
ALGOXBT_1.csv
ALGOUSD_1.csv
ALGOETH_60.csv
ALGOXBT_60.csv
ALGOGBP_1440.csv
ALGOEUR_60.csv
ALGOGBP_1.csv
ALGOEUR_1440.csv
ALGOUSD_5.csv
ALGOGBP_60.csv
ALGOETH_1.csv
ALGOETH_720.csv
ALGOETH_1440.csv
ALGOUSD_15.csv
ALGOXBT_720.csv
ALGOUSD_1440.csv
ALGOEUR_720.csv
ALGOETH_5.csv
ALGOXBT_5.csv
ALGOEUR_15.csv
ALGOGBP_720.csv
ALGOUSD_60.csv
ALGOXBT_15.csv
ALGOEUR_1.csv
ALGOEUR_5.csv
ALGOETH_15.csv
ALGOXBT_1440.csv
ATOMAUD_1.csv
ATOMGBP_1.csv
ATOMAUD_15.csv
ATOMAUD_720.csv
ATOMXBT_1.csv
ATOMXBT_60.csv
ATOMEUR_15.csv
ATOMAUD_60.csv
ATOMAUD_1440.csv
ATOMETH_720.csv
ATOMGBP_720.csv
ATOMGBP_15.csv
ATOMEUR_1440.csv
ATOMUSD_1440.csv
ATOMUSD_60.csv
ATOMXBT_1440.csv
ATOMEUR_1.csv
ATOMGBP_5.csv
ATOMUSD_720.csv
ATOMXBT_5.csv
ATOMETH_5.csv
ATOMUSD_1.csv
ATOMEUR_5.csv
ATOMGBP_1440.csv
ATOMETH_60.csv
ATOMUSD_15.csv
ATOMETH_1.csv
ATOMEUR_720.csv
ATOMGBP_60.csv
ATOMAUD_5.csv
ATOMXBT_720.csv
ATOMXBT_15.csv
ATOMETH_1440.csv
ATOMUSD_5.csv
ATOMETH_15.csv
ATOMEUR_60.csv
BCHGBP_1440.csv
BCHUSDT_60.csv
BCHGBP_60.csv
BCHETH_5.csv
BCHGBP_5.csv
BCHGBP_15.csv
BCHXBT_720.csv
BCHXBT_1.csv
BCHUSDT_15.csv
BCHUSDT_5.csv
BCHETH_1.csv
BCHETH_60.csv
BCHGBP_1.csv
BCHEUR_15.csv
BCHAUD_1440.csv
BCHXBT_1440.csv
BCHJPY_1.csv
BCHUSDT_1440.csv
BCHETH_1440.csv
BCHUSD_1440.csv
BCHAUD_60.csv
BCHUSD_1.csv
BCHETH_15.csv
BCHUSD_15.csv
BCHAUD_720.csv
BCHJPY_5.csv
BCHUSD_720.csv
BCHJPY_15.csv
BCHXBT_5.csv
BCHEUR_1440.csv
BCHEUR_5.csv
BCHJPY_60.csv
BCHXBT_60.csv
BCHUSD_60.csv
BCHETH_720.csv
BCHUSDT_1.csv
BCHEUR_720.csv
BCHEUR_1.csv
BCHEUR_60.csv
BCHAUD_15.csv
BCHUSD_5.csv
BCHJPY_720.csv
BCHAUD_5.csv
BCHJPY_1440.csv
BCHUSDT_720.csv
BCHAUD_1.csv
BCHGBP_720.csv
BCHXBT_15.csv
EOSETH_1440.csv
EOSXBT_720.csv
EOSEUR_1440.csv
EOSXBT_1.csv
EOSUSD_1440.csv
EOSEUR_5.csv
EOSEUR_15.csv
EOSUSDT_1.csv
EOSXBT_15.csv
EOSXBT_5.csv
EOSETH_720.csv
EOSETH_60.csv
EOSETH_5.csv
EOSEUR_720.csv
EOSUSDT_15.csv
EOSUSD_5.csv
EOSUSD_60.csv
EOSUSD_720.csv
EOSUSDT_1440.csv
EOSUSD_1.csv
EOSUSDT_60.csv
EOSUSD_15.csv
EOSUSDT_720.csv
EOSXBT_1440.csv
EOSEUR_60.csv
EOSETH_1.csv
EOSUSDT_5.csv
EOSXBT_60.csv
EOSETH_15.csv
EOSEUR_1.csv
ETCUSD_15.csv
ETCEUR_5.csv
ETCEUR_15.csv
ETCXBT_1.csv
ETCXBT_60.csv
ETCETH_60.csv
ETCETH_15.csv
ETCUSD_5.csv
ETCXBT_1440.csv
ETCEUR_720.csv
ETCUSD_60.csv
ETCEUR_1.csv
ETCXBT_720.csv
ETCUSD_720.csv
ETCUSD_1440.csv
ETCUSD_1.csv
ETCETH_1.csv
ETCEUR_60.csv
ETCXBT_5.csv
ETCXBT_15.csv
ETCETH_5.csv
ETCEUR_1440.csv
ETCETH_1440.csv
ETCETH_720.csv
KAVAUSD_15.csv
KAVAUSD_60.csv
KAVAUSD_720.csv
KAVAETH_720.csv
KAVAEUR_5.csv
KAVAUSD_1.csv
KAVAETH_1.csv
KAVAETH_60.csv
KAVAXBT_5.csv
KAVAETH_15.csv
KAVAXBT_1.csv
KAVAETH_1440.csv
KAVAEUR_15.csv
KAVAXBT_15.csv
KAVAETH_5.csv
KAVAEUR_1440.csv
KAVAXBT_1440.csv
KAVAXBT_60.csv
KAVAEUR_720.csv
KAVAUSD_1440.csv
KAVAUSD_5.csv
KAVAEUR_1.csv
KAVAEUR_60.csv
KAVAXBT_720.csv
KSMETH_60.csv
KSMETH_5.csv
KSMUSD_60.csv
KSMAUD_1.csv
KSMDOT_60.csv
KSMAUD_720.csv
KSMETH_15.csv
KSMXBT_720.csv
KSMDOT_1440.csv
KSMAUD_15.csv
KSMXBT_15.csv
KSMDOT_1.csv
KSMUSD_5.csv
KSMEUR_15.csv
KSMXBT_60.csv
KSMGBP_720.csv
KSMGBP_1440.csv
KSMGBP_60.csv
KSMEUR_1440.csv
KSMEUR_720.csv
KSMDOT_5.csv
KSMAUD_60.csv
KSMXBT_5.csv
KSMEUR_5.csv
KSMXBT_1.csv
KSMGBP_5.csv
KSMETH_720.csv
KSMDOT_15.csv
KSMDOT_720.csv
KSMUSD_1440.csv
KSMETH_1440.csv
KSMUSD_720.csv
KSMGBP_1.csv
KSMGBP_15.csv
KSMEUR_60.csv
KSMXBT_1440.csv
KSMETH_1.csv
KSMAUD_1440.csv
KSMUSD_15.csv
KSMEUR_1.csv
KSMAUD_5.csv
KSMUSD_1.csv
LINKGBP_1.csv
LINKETH_1440.csv
LINKGBP_720.csv
LINKEUR_5.csv
LINKGBP_15.csv
LINKXBT_5.csv
LINKXBT_15.csv
LINKAUD_720.csv
LINKUSD_1.csv
LINKAUD_1.csv
LINKETH_60.csv
LINKEUR_1440.csv
LINKXBT_60.csv
LINKAUD_1440.csv
LINKUSD_5.csv
LINKGBP_60.csv
LINKETH_1.csv
LINKETH_15.csv
LINKUSDT_1440.csv
LINKEUR_1.csv
LINKAUD_60.csv
LINKETH_5.csv
LINKUSD_1440.csv
LINKXBT_1.csv
LINKUSD_60.csv
LINKXBT_720.csv
LINKAUD_15.csv
LINKUSDT_15.csv
LINKXBT_1440.csv
LINKEUR_60.csv
LINKEUR_720.csv
LINKGBP_1440.csv
LINKUSD_15.csv
LINKAUD_5.csv
LINKUSDT_1.csv
LINKGBP_5.csv
LINKUSDT_60.csv
LINKUSDT_5.csv
LINKUSD_720.csv
LINKETH_720.csv
LINKUSDT_720.csv
LINKEUR_15.csv
LTCETH_5.csv
LTCJPY_15.csv
LTCUSDT_15.csv
LTCAUD_1.csv
LTCUSD_720.csv
LTCEUR_1440.csv
LTCAUD_60.csv
LTCXBT_1440.csv
LTCUSDT_60.csv
LTCUSD_60.csv
LTCUSDT_1.csv
LTCETH_60.csv
LTCEUR_1.csv
LTCXBT_720.csv
LTCUSD_15.csv
LTCAUD_720.csv
LTCAUD_15.csv
LTCUSD_1.csv
LTCETH_1440.csv
LTCEUR_15.csv
LTCUSD_1440.csv
LTCAUD_5.csv
LTCUSD_5.csv
LTCJPY_5.csv
LTCJPY_1440.csv
LTCUSDT_5.csv
LTCXBT_15.csv
LTCJPY_720.csv
LTCXBT_5.csv
LTCEUR_60.csv
LTCGBP_1.csv
LTCUSDT_1440.csv
LTCXBT_1.csv
LTCGBP_1440.csv
LTCXBT_60.csv
LTCUSDT_720.csv
LTCETH_1.csv
LTCETH_15.csv
LTCGBP_720.csv
LTCAUD_1440.csv
LTCJPY_1.csv
LTCEUR_720.csv
LTCGBP_15.csv
LTCGBP_60.csv
LTCETH_720.csv
LTCEUR_5.csv
LTCGBP_5.csv
LTCJPY_60.csv
MANAEUR_1440.csv
MANAEUR_15.csv
MANAETH_1440.csv
MANAUSD_15.csv
MANAEUR_5.csv
MANAUSD_5.csv
MANAXBT_1440.csv
MANAETH_720.csv
MANAUSD_1440.csv
MANAEUR_720.csv
MANAETH_5.csv
MANAEUR_1.csv
MANAUSD_720.csv
MANAXBT_720.csv
MANAETH_15.csv
MANAETH_60.csv
MANAXBT_5.csv
MANAXBT_15.csv
MANAUSD_1.csv
MANAEUR_60.csv
MANAETH_1.csv
MANAXBT_60.csv
MANAUSD_60.csv
MANAXBT_1.csv
MLNEUR_5.csv
MLNETH_1440.csv
MLNUSD_1.csv
MLNUSD_1440.csv
MLNEUR_15.csv
MLNXBT_1.csv
MLNETH_720.csv
MLNETH_60.csv
MLNEUR_1.csv
MLNXBT_1440.csv
MLNUSD_5.csv
MLNEUR_720.csv
MLNXBT_5.csv
MLNXBT_60.csv
MLNXBT_720.csv
MLNUSD_60.csv
MLNETH_5.csv
MLNUSD_15.csv
MLNUSD_720.csv
MLNETH_1.csv
MLNXBT_15.csv
MLNEUR_1440.csv
MLNETH_15.csv
MLNEUR_60.csv
QTUMUSD_5.csv
QTUMUSD_720.csv
QTUMEUR_5.csv
QTUMETH_1.csv
QTUMUSD_1440.csv
QTUMXBT_1440.csv
QTUMETH_60.csv
QTUMETH_5.csv
QTUMUSD_1.csv
QTUMXBT_60.csv
QTUMUSD_60.csv
QTUMEUR_60.csv
QTUMEUR_1440.csv
QTUMETH_15.csv
QTUMUSD_15.csv
QTUMEUR_720.csv
QTUMXBT_1.csv
QTUMXBT_5.csv
QTUMEUR_15.csv
QTUMXBT_15.csv
QTUMXBT_720.csv
QTUMETH_1440.csv
QTUMETH_720.csv
QTUMEUR_1.csv
STORJXBT_15.csv
STORJETH_5.csv
STORJEUR_1440.csv
STORJETH_15.csv
STORJUSD_5.csv
STORJXBT_5.csv
STORJETH_1.csv
STORJEUR_5.csv
STORJXBT_60.csv
STORJXBT_1.csv
STORJEUR_720.csv
STORJUSD_60.csv
STORJEUR_60.csv
STORJETH_1440.csv
STORJUSD_1440.csv
STORJEUR_15.csv
STORJEUR_1.csv
STORJUSD_1.csv
STORJETH_60.csv
STORJXBT_720.csv
STORJUSD_15.csv
STORJETH_720.csv
STORJXBT_1440.csv
STORJUSD_720.csv
WAVESXBT_15.csv
WAVESXBT_60.csv
WAVESETH_60.csv
WAVESXBT_720.csv
WAVESEUR_1.csv
WAVESETH_5.csv
WAVESUSD_5.csv
WAVESEUR_15.csv
WAVESUSD_15.csv
WAVESXBT_5.csv
WAVESEUR_5.csv
WAVESEUR_1440.csv
WAVESETH_1440.csv
WAVESUSD_1.csv
WAVESEUR_60.csv
WAVESUSD_1440.csv
WAVESEUR_720.csv
WAVESETH_15.csv
WAVESUSD_60.csv
WAVESETH_1.csv
WAVESUSD_720.csv
WAVESXBT_1440.csv
WAVESETH_720.csv
WAVESXBT_1.csv
XTZXBT_60.csv
XTZGBP_1440.csv
XTZXBT_15.csv
XTZUSD_15.csv
XTZETH_1.csv
XTZGBP_5.csv
XTZGBP_60.csv
XTZEUR_5.csv
XTZAUD_1.csv
XTZGBP_15.csv
XTZETH_1440.csv
XTZGBP_720.csv
XTZUSD_1440.csv
XTZETH_60.csv
XTZAUD_5.csv
XTZEUR_60.csv
XTZETH_720.csv
XTZXBT_1440.csv
XTZETH_5.csv
XTZUSD_720.csv
XTZAUD_720.csv
XTZEUR_720.csv
XTZAUD_15.csv
XTZXBT_1.csv
XTZEUR_1.csv
XTZUSD_1.csv
XTZUSD_5.csv
XTZEUR_15.csv
XTZEUR_1440.csv
XTZXBT_5.csv
XTZAUD_1440.csv
XTZUSD_60.csv
XTZETH_15.csv
XTZAUD_60.csv
XTZXBT_720.csv
XTZGBP_1.csv
"""
