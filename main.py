import urllib.request as req
import json
import os


def Company():
    print()
    company = input('請輸入巴士公司（NWFB / CTB） : ')
    print()
    url = 'https://rt.data.gov.hk/v1/transport/citybus-nwfb/company/' + company
    with req.urlopen(url) as res:
        data = json.load(res)
    data = data['data']
    print('公司編號: '+data['co'])
    print('公司名稱: '+data['name_tc'])
    print('公司網站: '+data['url'])


def Route():
    print()
    company = input('請輸入巴士公司（NWFB / CTB） : ')
    route = input('請輸入路線號碼 : ')
    print()
    url = 'https://rt.data.gov.hk/v1/transport/citybus-nwfb/route/' + company + '/' + route
    with req.urlopen(url) as res:
        data = json.load(res)
    data = data['data']
    print('公司編號 : ' + data['co'])
    print('路線號碼 : ' + data['route'])
    print('起點站: ' + data['orig_tc'])
    print('終點站: ' + data['dest_tc'])


def Stop():
    print()
    stopid = input('請輸入巴士站編號 : ')
    print()
    url = 'https://rt.data.gov.hk/v1/transport/citybus-nwfb/stop/' + stopid
    with req.urlopen(url) as res:
        data = json.load(res)
    data = data['data']
    print('巴士站編號 : ' + data['stop'])
    print('停站名稱 : ' + data['name_tc'])


def RouteStop():
    print()
    company = input('請輸入巴士公司（NWFB / CTB） : ')
    route = input('請輸入路線號碼 : ')
    dire = input('請輸入方向（inbound / outbound） : ')
    print()
    url = 'https://rt.data.gov.hk/v1/transport/citybus-nwfb/route-stop/' + \
        company+'/'+route+'/'+dire
    with req.urlopen(url) as res:
        data = json.load(res)
    data = data['data']
    print('巴士站編號 地點')
    for stops in data:
        stop = stops['stop']
        url = 'https://rt.data.gov.hk/v1/transport/citybus-nwfb/stop/' + stop
        with req.urlopen(url) as res:
            data = json.load(res)
        data = data['data']
        print(
            '  {0:8} {1}'.format(stops['stop'], data['name_tc']))


def ETA():
    print()
    company = input('請輸入巴士公司（NWFB / CTB） : ')
    route = input('請輸入路線號碼 : ')
    stop = input('請輸入巴士站編號 : ')
    print()
    url = 'https://rt.data.gov.hk/v1/transport/citybus-nwfb/eta/' + \
        company + '/' + stop + '/' + route
    with req.urlopen(url) as res:
        data = json.load(res)
    print("資料更新時間: " + data["generated_timestamp "][11:19])
    data = data['data']
    for eta in data:
        print('第 {0} 班 往 {1} 預計到達時間 : {2}'.format(
            eta['eta_seq'], eta['dest_tc'], eta['eta'][11:19]))


def ETAStop():
    print()
    company = input('請輸入巴士公司（NWFB / CTB） : ')
    route = input('請輸入路線號碼 : ')
    dire = input('請輸入方向（inbound / outbound） : ')
    print()
    url = 'https://rt.data.gov.hk/v1/transport/citybus-nwfb/route-stop/' + \
        company+'/'+route+'/'+dire
    with req.urlopen(url) as res:
        data = json.load(res)
    data = data['data']
    for stops in data:
        stop = stops['stop']
        stopurl = 'https://rt.data.gov.hk/v1/transport/citybus-nwfb/stop/' + stop
        with req.urlopen(stopurl) as res:
            data = json.load(res)
        stopdata = data['data']
        etaurl = 'https://rt.data.gov.hk/v1/transport/citybus-nwfb/eta/' + \
            company + '/' + stop + '/' + route
        with req.urlopen(etaurl) as res:
            data = json.load(res)
        etadata = data['data']

        print(stops["stop"]+" "+stopdata["name_tc"])
        for etabus in etadata:
            print('第 {0} 班 往 {1} 預計到達時間 : {2} 備注 : {3}'.format(
                etabus['eta_seq'], etabus['dest_tc'], etabus['eta'][11:19], etabus['rmk_tc']))
        print()


def Restart():
    print()
    print('=====查詢完成（按“空白鍵”回到選擇界面）=====')
    input()
    os.system('cls')


while True:
    print('''
1.公司數據
2.巴士路線數據
3.巴士站數據
4.個別路線的巴士站數據
5.預計到達時間數據
6.個別路線的巴士站及預計到達時間數據
7.離開
''')
    case = input('請輸入查詢的選項 : ')
    if case == '1':
        Company()
        Restart()
    elif case == '2':
        Route()
        Restart()
    elif case == '3':
        Stop()
        Restart()
    elif case == '4':
        RouteStop()
        Restart()
    elif case == '5':
        ETA()
        Restart()
    elif case == '6':
        ETAStop()
        Restart()
    elif case == '7':
        exit()
    else:
        print('[！] 輸入錯誤，請重新輸入 [！]')
        Restart()
