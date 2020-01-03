from forex_python.converter import CurrencyRates, CurrencyCodes
import requests
import json


def converter_forex_python(coin, amount, Cdict, dict_rate2):
    if amount <= 0:
        return 0
    coin = coin.upper()
    try:
        if coin in Cdict.keys():
            return amount / Cdict.get(coin)
        else:
            symbolDict = dict()
            symbol = CurrencyCodes()
            for key in Cdict.keys():
                symbolDict[symbol.get_symbol(key)] = key
            return amount / Cdict.get(symbolDict.get(coin))
    except:
        return converter_fixerio(coin, amount,dict_rate2)


def converter_fixerio(coin, amount, dict_rate2):
    if amount <= 0:
        return 0
    coin = coin.upper()
    try:
        if coin in dict_rate2.keys():
            return amount / dict_rate2.get(coin)
        else:
            symbolDict = {'د.إ;': 'AED', 'Afs': 'AFN', 'L': 'RON', 'AMD': 'AMD', 'NAƒ': 'ANG', 'Kz': 'AOA', '$': 'SRD', 'ƒ': 'AWG', 'AZN': 'AZN', 'KM': 'BAM', 'Bds$': 'BBD', '৳': 'BDT', 'BGN': 'BGN', '.د.ب': 'BHD', 'FBu': 'BIF', 'BD$': 'BMD', 'B$': 'BSD', 'Bs.': 'BOB', 'R$': 'BRL', None: 'ZWL', 'Nu.': 'BTN', 'P': 'MOP', 'Br': 'ETB', 'BZ$': 'BZD', 'F': 'XPF', 'Fr.': 'CHF', '¥': 'JPY', 'Col$': 'COP', '₡': 'CRC', 'Esc': 'CVE', 'Kč': 'CZK', 'Fdj': 'DJF', 'Kr': 'DKK', 'RD$': 'DOP', 'د.ج': 'DZD', '£': 'SHP', 'Nfa': 'ERN', '€': 'EUR', 'FJ$': 'FJD', 'GEL': 'GEL', 'GH₵': 'GHS', 'D': 'GMD', 'FG': 'GNF', 'Q': 'GTQ', 'GY$': 'GYD', 'HK$': 'HKD', 'kn': 'HRK', 'G': 'HTG', 'Ft': 'HUF', 'Rp': 'IDR', '₪': 'ILS', '₹': 'INR', 'د.ع': 'IQD', 'IRR': 'IRR', 'kr': 'SEK', 'J$': 'JMD', 'JOD': 'JOD', 'KSh': 'KES', 'сом': 'KGS', '៛': 'KHR', 'KMF': 'KMF', 'W': 'KRW', 'KWD': 'KWD',
                          'KY$': 'KYD', 'T': 'KZT', 'KN': 'LAK', 'Rs': 'MUR', 'L$': 'LRD', 'M': 'LSL', 'Lt': 'LTL', 'Ls': 'LVL', 'LD': 'LYD', 'MAD': 'MAD', 'MDL': 'MDL', 'FMG': 'MGA', 'MKD': 'MKD', 'K': 'PGK', '₮': 'MNT', 'UM': 'MRO', 'Rf': 'MVR', 'MK': 'MWK', 'RM': 'MYR', 'N$': 'NAD', '₦': 'NGN', 'C$': 'NIO', 'NRs': 'NPR', 'NZ$': 'NZD', 'OMR': 'OMR', 'B./': 'PAB', 'S/.': 'PEN', '₱': 'PHP', 'Rs.': 'PKR', 'zł': 'PLN', '₲': 'PYG', 'QR': 'QAR', 'din.': 'RSD', 'R': 'ZAR', 'SR': 'SCR', 'SI$': 'SBD', 'SDG': 'SDG', 'S$': 'SGD', 'Le': 'SLL', 'Sh.': 'SOS', 'LS': 'SYP', 'E': 'SZL', '฿': 'THB', 'TJS': 'TJS', 'm': 'TMT', 'DT': 'TND', 'TRY': 'TRY', 'TT$': 'TTD', 'NT$': 'TWD', 'TZS': 'TZS', 'UAH': 'UAH', 'USh': 'UGX', 'US$': 'USD', '$U': 'UYU', 'UZS': 'UZS', '₫': 'VND', 'VT': 'VUV', 'WS$': 'WST', 'CFA': 'XOF', 'EC$': 'XCD', 'SDR': 'XDR', 'YER': 'YER', 'ZK': 'ZMK'}
            return amount / dict_rate2.get(symbolDict.get(coin))
    except:
        return -1



def GetRate():
    c = CurrencyRates()
    return c.get_rates('EUR')
