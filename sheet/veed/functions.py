import os
import requests
import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


def get_service_sacc():
    creds_json = os.path.dirname(__file__) + "\my-project-92209-8d39b380aac8.json"
    scopes = ['https://www.googleapis.com/auth/spreadsheets']

    creds_service = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
    return build('sheets', 'v4', http=creds_service)


def get_vol():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    h = requests.get(url).json()
    return str(h['Valute']['USD']['Value'])[:-5]


def get_data(i, n):
    t = int(i[2]) * n
    return i[0], i[1], t, i[3]


def main():
    resp = get_service_sacc().spreadsheets().values().get(spreadsheetId='132TLhei0WD3pE8D6P-DEp-1GTKzIhU2tkvSw2hMS9cA', range="Лист1!A1:F100").execute()
    result = []
    f = 0
    n = int(get_vol())
    for i in resp['values']:
        f += 1
        if f > 1:
            data = get_data(i, n)
            result.append(data)

    return result


if __name__ == '__main__':
    main()

