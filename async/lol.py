#!/usr/bin/python3.6
# MY FILES
from covertURL import covertURL
from covertCoins import converter_forex_python, GetRate
from numpy import double
import datetime
import time
import Proxygrabber
# imort other models
import json
from requests_html import HTMLSession
import random
import re
import requests
from fake_useragent import UserAgent
from lxml.html import fromstring
import password


render = 3
allcoins = r'(AED)|(AFN)|(ALL)|(AMD)|(ANG)|(AOA)|(ARS)|(AUD)|(AWG)|(AZN)|(BAM)|(BBD)|(BDT)|(BGN)|(BHD)|(BIF)|(BMD)|(BND)|(BOB)|(BRL)|(BSD)|(BTC)|(BTN)|(BWP)|(BYN)|(BYR)|(BZD)|(CAD)|(CDF)|(CHF)|(CLF)|(CLP)|(CNY)|(COP)|(CRC)|(CUC)|(CUP)|(CVE)|(CZK)|(DJF)|(DKK)|(DOP)|(DZD)|(EGP)|(ERN)|(ETB)|(EUR)|(FJD)|(FKP)|(GBP)|(GEL)|(GGP)|(GHS)|(GIP)|(GMD)|(GNF)|(GTQ)|(GYD)|(HKD)|(HNL)|(HRK)|(HTG)|(HUF)|(IDR)|(ILS)|(IMP)|(INR)|(IQD)|(IRR)|(ISK)|(JEP)|(JMD)|(JOD)|(JPY)|(KES)|(KGS)|(KHR)|(KMF)|(KPW)|(KRW)|(KWD)|(KYD)|(KZT)|(LAK)|(LBP)|(LKR)|(LRD)|(LSL)|(LTL)|(LVL)|(LYD)|(MAD)|(MDL)|(MGA)|(MKD)|(MMK)|(MNT)|(MOP)|(MRO)|(MUR)|(MVR)|(MWK)|(MXN)|(MYR)|(MZN)|(NAD)|(NGN)|(NIO)|(NOK)|(NPR)|(NZD)|(OMR)|(PAB)|(PEN)|(PGK)|(PHP)|(PKR)|(PLN)|(PYG)|(QAR)|(RON)|(RSD)|(RUB)|(RWF)|(SAR)|(SBD)|(SCR)|(SDG)|(SEK)|(SGD)|(SHP)|(SLL)|(SOS)|(SRD)|(STD)|(SVC)|(SYP)|(SZL)|(THB)|(TJS)|(TMT)|(TND)|(TOP)|(TRY)|(TTD)|(TWD)|(TZS)|(UAH)|(UGX)|(USD)|(UYU)|(UZS)|(VEF)|(VND)|(VUV)|(WST)|(XAF)|(XAG)|(XAU)|(XCD)|(XDR)|(XOF)|(XPF)|(YER)|(ZAR)|(ZMK)|(ZMW)|(ZWL)|(aed)|(afn)|(all)|(amd)|(ang)|(aoa)|(ars)|(aud)|(awg)|(azn)|(bam)|(bbd)|(bdt)|(bgn)|(bhd)|(bif)|(bmd)|(bnd)|(bob)|(brl)|(bsd)|(btc)|(btn)|(bwp)|(byn)|(byr)|(bzd)|(cad)|(cdf)|(chf)|(clf)|(clp)|(cny)|(cop)|(crc)|(cuc)|(cup)|(cve)|(czk)|(djf)|(dkk)|(dop)|(dzd)|(egp)|(ern)|(etb)|(eur)|(fjd)|(fkp)|(gbp)|(gel)|(ggp)|(ghs)|(gip)|(gmd)|(gnf)|(gtq)|(gyd)|(hkd)|(hnl)|(hrk)|(htg)|(huf)|(idr)|(ils)|(imp)|(inr)|(iqd)|(irr)|(isk)|(jep)|(jmd)|(jod)|(jpy)|(kes)|(kgs)|(khr)|(kmf)|(kpw)|(krw)|(kwd)|(kyd)|(kzt)|(lak)|(lbp)|(lkr)|(lrd)|(lsl)|(ltl)|(lvl)|(lyd)|(mad)|(mdl)|(mga)|(mkd)|(mmk)|(mnt)|(mop)|(mro)|(mur)|(mvr)|(mwk)|(mxn)|(myr)|(mzn)|(nad)|(ngn)|(nio)|(nok)|(npr)|(nzd)|(omr)|(pab)|(pen)|(pgk)|(php)|(pkr)|(pln)|(pyg)|(qar)|(ron)|(rsd)|(rub)|(rwf)|(sar)|(sbd)|(scr)|(sdg)|(sek)|(sgd)|(shp)|(sll)|(sos)|(srd)|(std)|(svc)|(syp)|(szl)|(thb)|(tjs)|(tmt)|(tnd)|(top)|(try)|(ttd)|(twd)|(tzs)|(uah)|(ugx)|(usd)|(uyu)|(uzs)|(vef)|(vnd)|(vuv)|(wst)|(xaf)|(xag)|(xau)|(xcd)|(xdr)|(xof)|(xpf)|(yer)|(zar)|(zmk)|(zmw)|(zwl)|(د.إ;)|(Afs)|(L)|(AMD)|(NAƒ)|(Kz)|(\$)|(ƒ)|(AZN)|(KM)|(Bds\$)|(৳)|(BGN)|(.د.ب)|(FBu)|(BD\$)|(B\$)|(Bs.)|(R\$)|(Nu.)|(P)|(Br)|(BZ\$)|(F)|(Fr.)|(¥)|(Col\$)|(₡)|(Esc)|(Kč)|(Fdj)|(Kr)|(RD\$)|(د.ج)|(£)|(Nfa)|(€)|(FJ\$)|(GEL)|(GH₵)|(D)|(FG)|(Q)|(GY\$)|(HK\$)|(kn)|(G)|(Ft)|(Rp)|(₪)|(₹)|(د.ع)|(IRR)|(kr)|(J\$)|(JOD)|(KSh)|(сом)|(៛)|(KMF)|(W)|(KWD)|(KY\$)|(T)|(KN)|(Rs)|(L\$)|(M)|(Lt)|(Ls)|(LD)|(MAD)|(MDL)|(FMG)|(MKD)|(K)|(₮)|(UM)|(Rf)|(MK)|(RM)|(N\$)|(₦)|(C\$)|(NRs)|(NZ\$)|(OMR)|(B./)|(S/.)|(₱)|(Rs.)|(zł)|(₲)|(QR)|(din.)|(R)|(SR)|(SI\$)|(SDG)|(S\$)|(Le)|(Sh.)|(LS)|(E)|(฿)|(TJS)|(m)|(DT)|(TRY)|(TT\$)|(NT\$)|(TZS)|(UAH)|(USh)|(US\$)|(\$U)|(UZS)|(₫)|(VT)|(WS\$)|(CFA)|(EC\$)|(SDR)|(YER)|(ZK)'


def SameCurrencyCheck(getList1, getList2):
    getList1 = re.findall(allcoins, ",".join(getList1).replace(" ", ""))
    getList2 = re.findall(allcoins, ",".join(getList2).replace(" ", ""))
    getList1 = list(
        map(lambda x: list(filter(lambda y: y != '', x))[0], getList1))
    getList2 = list(
        map(lambda x: list(filter(lambda y: y != '', x))[0], getList2))
    if(len(set(getList1)) == 1 and len(set(getList2)) == 1):
        return (getList1[0], getList2[0])
    elif len(set(getList1)) != 1 and len(set(getList2)) != 1:
        raise ValueError(2)
    elif len(set(getList1)) != 1:
        raise ValueError(0)
    else:
        raise ValueError(1)


def Mymin(getList):
    getList = re.findall(
        r'((\d+)(,\d{3})*(\.\d{1,2})?)', " , ".join(getList).replace(" ", ""))
    getList = list(map(lambda x: x[0], getList))
    return min(getList)


def get_proxies():
    grabber = Proxygrabber.ProxyGrabber()
    grabber.grab_proxies()
    return set(grabber.get_proxy_list())


def getPrice(URL, Xpath, proxy=None, browser=None):
    if(proxy and browser):
        response = requests.get(URL, timeout=30, proxies={"http": proxy, "https": proxy}, headers={"User-Agent": browser, "Content-type": "application/x-www-form-urlencoded", "charset": "utf-8"})
        print(proxy + " : " + browser + " Connnection ")
    else:
        response = requests.get(URL, timeout=30, headers={"Content-type": "application/x-www-form-urlencoded", "charset": "utf-8"})
    parser = fromstring(response.text)
    price_list = parser.xpath(Xpath)
    if not price_list:       
        if (proxy and browser):
            response = requests.get(URL, timeout=30, proxies={
                                        "http": proxy, "https": proxy}, headers={"User-Agent": browser})
        else:
            response = requests.get(URL, timeout=30)
        parser = fromstring(response.text)
        price_list = parser.xpath(Xpath)

    if not price_list:
        try:
            time.sleep(0.5)
            session = HTMLSession()
            if(proxy and browser):
                response = session.get(URL, timeout=10, proxies={"http": proxy, "https": proxy}, headers={
                    "User-Agent": browser, "Content-type": "application/x-www-form-urlencoded", "charset": "utf-8"})
            else:
                response = session.get(URL)
            maxcount = 0
            while(maxcount < render and not price_list):
                try:
                    time.sleep(0.5)
                    response.html.render(timeout=40)
                    parser = fromstring(response.html.html)
                    price_list = parser.xpath(Xpath)
                    maxcount = maxcount+1
                except:
                    maxcount = maxcount+1
        except:
            pass
        if not price_list:  # new need check
            try:
                session = HTMLSession()

                if(proxy and browser):
                    response = session.get(URL, timeout=10, proxies={"http": proxy, "https": proxy}, headers={
                        "User-Agent": browser})
                else:
                    response = session.get(URL)
                maxcount = 0
                while(maxcount < render and not price_list):
                    time.sleep(0.5)
                    response = response.html.render(timeout=40)
                    parser = fromstring(response.html.html)
                    price_list = parser.xpath(Xpath)
                    maxcount = maxcount+1
            except:
                pass
        if not price_list:
            try:
                session = HTMLSession()

                if(proxy and browser):
                    response = session.get(URL, timeout=10, proxies={"http": proxy, "https": proxy}, headers={
                        "User-Agent": browser, "Content-type": "application/x-www-form-urlencoded", "charset": "utf-8", 'Set-Cookie': None})
                else:
                    response = session.get(URL)
                time.sleep(0.5)
                response.html.arender()
                parser = fromstring(response.html.html)
                price_list = parser.xpath(Xpath)
            except:
                print("arender no work this time ")
    return price_list


def BastPrice(htmls, dict_rate, dict_rate2):
    while (len(htmls.keys()) > 1):
        for key1 in htmls.keys():
            for key2 in htmls.keys():
                if key1 != key2:
                    try:
                        min1 = Mymin(htmls.get(key1))
                    except:
                        del htmls[key1]
                        break
                    try:
                        min2 = Mymin(htmls.get(key2))
                    except:
                        del htmls[key2]
                        break
                    try:
                        Tuple = SameCurrencyCheck(
                            htmls.get(key1), htmls.get(key2))
                        if(Tuple[0] != Tuple[1]):
                            min1 = converter_forex_python(
                                Tuple[0], double(min1), dict_rate, dict_rate2)
                            min2 = converter_forex_python(
                                Tuple[1], double(min2), dict_rate, dict_rate2)
                            htmls[key1] = ['EUR'+str(min1)]
                            htmls[key2] = ['EUR'+str(min2)]
                        if min1 < min2 or (abs(min1-min2) < 5 and key2 != "regular"):
                            del htmls[key2]
                        else:
                            del htmls[key1]
                    except ValueError as err:
                        if str(err) == "0":
                            del htmls[key1]
                        elif str(err) == "1":
                            del htmls[key2]
                        else:
                            del htmls[key1]
                            del htmls[key2]
                    break
            break
    return htmls


def RequestsAndcheck(URL, Xpath, proxies, dict_rate2):
    dict_rate = GetRate()
    URL = covertURL(URL)
    htmls = {}
    for j in range(10):  # try get price with regular counect
        try:
            regular_result = getPrice(URL, Xpath)
            time.sleep(2.6)
            if regular_result:
                print(regular_result)
                break
        except:
            pass
    # proxy
    UserAgents = ['Mozilla/5.0 (Linux; Android 5.0; Nexus 6 Build/LRX21D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; KFAUWI Build/LVY48F) AppleWebKit/537.36 (KHTML, like Gecko) Silk/68.2.6 like Chrome/68.0.3440.85 Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0; Nexus 6P Build/MDB08L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.69 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; SM-T715 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel Build/OPR3.170623.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G935F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; Pixel 2 XL Build/PPR1.180610.009) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36', 'Mozilla/5.0 (Android 9; Tablet; rv:61.0) Gecko/61.0 Firefox/61.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13C75 Safari/601.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12D508 Safari/600.1.4', 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/546.10 (KHTML, like Gecko) Version/6.0 Mobile/7E18WD Safari/8536.25', 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B329 Safari/8536.25', 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
                  'Mozilla/5.0 (iPad; CPU OS 9_0 like Mac OS X) AppleWebKit/601.1.17 (KHTML, like Gecko) Version/8.0 Mobile/13A175 Safari/600.1.4', 'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4', 'Mozilla/5.0 (iPad; CPU OS 7_0_2 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11A501', 'Mozilla/5.0 (iPad; CPU OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B329 Safari/8536.25', 'Mozilla/5.0 (iPad; CPU OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134', 'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; MDDCJS)', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0;  Trident/5.0)', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36 OPR/52.0.2871.64', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:58.0) Gecko/20100101 Firefox/58.0']
    for i in range(0, len(proxies)):
        # Get a proxy from the pool
        proxy = proxies[i]
        print("Request #%d" % i)
        try:
            if(len(UserAgents) > 0):
                browser = UserAgents[random.randint(0, len(UserAgents)-1)]
            else:
                try:
                    ua = UserAgent(cache=False, use_cache_server=False)
                    ua.update()
                    UserAgents = ([str(ua.safari), str(ua.ff), str(ua.firefox), str(ua.google), str(ua.chrome), str(
                        ua.opera), str(ua["Internet Explorer"]), str(ua["google chrome"]), str(ua.msie), str(ua.ie), str(ua.chrome)])
                    browser = ua.random
                except:
                    UserAgents = ['Mozilla/5.0 (Linux; Android 5.0; Nexus 6 Build/LRX21D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; KFAUWI Build/LVY48F) AppleWebKit/537.36 (KHTML, like Gecko) Silk/68.2.6 like Chrome/68.0.3440.85 Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0; Nexus 6P Build/MDB08L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.69 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; SM-T715 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel Build/OPR3.170623.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G935F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; Pixel 2 XL Build/PPR1.180610.009) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36', 'Mozilla/5.0 (Android 9; Tablet; rv:61.0) Gecko/61.0 Firefox/61.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13C75 Safari/601.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12D508 Safari/600.1.4', 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/546.10 (KHTML, like Gecko) Version/6.0 Mobile/7E18WD Safari/8536.25', 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B329 Safari/8536.25', 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
                                  'Mozilla/5.0 (iPad; CPU OS 9_0 like Mac OS X) AppleWebKit/601.1.17 (KHTML, like Gecko) Version/8.0 Mobile/13A175 Safari/600.1.4', 'Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4', 'Mozilla/5.0 (iPad; CPU OS 7_0_2 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11A501', 'Mozilla/5.0 (iPad; CPU OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B329 Safari/8536.25', 'Mozilla/5.0 (iPad; CPU OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134', 'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; MDDCJS)', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0;  Trident/5.0)', 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)', 'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36 OPR/52.0.2871.64', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:58.0) Gecko/20100101 Firefox/58.0']
                    browser = UserAgents[random.randint(0, len(UserAgents)-1)]
            price_list = getPrice(URL, Xpath, proxy, browser)
            if not price_list:
                pass
            else:
                print(price_list)
                htmls[(proxy, browser)] = price_list
                UserAgents.remove(browser)
        except:
            print(proxy + " : " + browser + " Skipping. Connnection error")
    htmls = BastPrice(htmls, dict_rate, dict_rate2)
    if not regular_result and not htmls:
        return ('unsupported', False)
    if not regular_result:
        for Proxy_UA in htmls.keys():
            return (Proxy_UA, False)
    if not htmls:
        return ('only regular find', False)
    htmls["regular"] = regular_result
    htmls = BastPrice(htmls, dict_rate, dict_rate2)
    if not htmls:
        return ('Erorr', False)
    else:
        for Proxy_UA in htmls.keys():
            if Proxy_UA == "regular":
                return (Proxy_UA, True)
            return (Proxy_UA, False)


def RequestsAndcheckAll():

    try:
        proxies = list(get_proxies())
        print(len(proxies))
    except:
        print("dont hes enternent")
        exit(1)
    try:
        try:
            params = {'base': 'EUR',
                      'access_key': password.api_key2}
            response = requests.get(
                "http://data.fixer.io/api/latest", params=params)
            dict_rate = json.loads(response.text)["rates"]
        except:
            params = {'base': 'EUR',
                      'access_key': password.api_key1}
            response = requests.get(
                "http://data.fixer.io/api/latest", params=params)
            dict_rate = json.loads(response.text)["rates"]
    except:
        dict_rate = ""
    data=json.dumps({'key':password.key})
    header = {"Content-Type": "application/json"}
    response = requests.post(
        'https://asqwzx1.pythonanywhere.com/GetCheckList', headers=header, data=data, auth=(password.user, password.password))
    print(response.text)
    for URLxpath in json.loads(response.text)['data']:
        try:
            result = RequestsAndcheck(URLxpath['HostName'], URLxpath['xpath'], proxies, dict_rate)
            print(result)
            if type(result[0]) is tuple:
                data = {'HostName': URLxpath['HostName'], 'Result': result[1],
                        'ip': result[0][0], 'userAgent': result[0][1],'key':password.key}
            else:
                data = {'HostName': URLxpath['HostName'], 'Result': result[1],'key':password.key}
            print(data)
            url = 'https://asqwzx1.pythonanywhere.com/SaveResult'
            data = json.dumps(data)
            header = {"Content-Type": "application/json"}
            response = requests.post(
                url, data=data, headers=header, auth=(password.user, password.password))
            print(response.text)
        except:
            print("erorr in ", URLxpath['HostName'])


RequestsAndcheckAll()
