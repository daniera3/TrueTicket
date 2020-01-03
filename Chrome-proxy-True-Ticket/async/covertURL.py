
import requests
def covertURL(HostName): 
    url = 'https://asqwzx1.pythonanywhere.com/GetFullURL'
    data={'HostName':HostName}
    response = requests.post(url,json = data, auth=('DN', 'DN123123'))
    result=eval(response.text)
    print(result)
    if  result['data']=="":
        URL=HostName
    elif result['data'] =='ERROR':
        URL=HostName
    else:
        URL=result['data']
    return URL


