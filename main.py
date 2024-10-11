# pip install oauth2client
# pip install gspread
# pip install macaddress

import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import macaddress

scope = ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive']

#개인에 따라 수정 필요 - 다운로드 받았던 키 값 경로 
json_key_path = "D:/choijo/Downloads/drive-python-sync-438223-75723873f612.json"

credential = ServiceAccountCredentials.from_json_keyfile_name(json_key_path, scope)
gc = gspread.authorize(credential)


#개인에 따라 수정 필요 - 스프레드시트 url 가져오기
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1hsXB4UNvLLggaH6OtWmfAKqHS9Q6KdgqlwYoy8tM-Fg/edit?usp=sharing"
# spreadsheet_url = "https://docs.google.com/spreadsheets/d/1hsXB4UNvLLggaH6OtWmfAKqHS9Q6KdgqlwYoy8tM-Fg/edit?gid=0#gid=0"

doc = gc.open_by_url(spreadsheet_url)
print(doc)
#개인에 따라 수정 필요 - 시트 선택하기 (시트명을 그대로 입력해주면 된다.)
sheet = doc.worksheet("KEY")
# sheet.update([['API 테스트']], 'A1')

print(sheet.get_all_values())
#데이터 프레임 생성하기
df = pd.DataFrame(sheet.get_all_values())

print(df)
#불러온 데이터 프레임 정리
df.rename(columns=df.iloc[0], inplace = True)
df.drop(df.index[0], inplace=True)

df.head()

''' mac address 불러오기 '''
import uuid
def getMacAddress():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])

macc = getMacAddress()
# ipp = showpublicIp()
print(macc)

''' mac address 불러오기 '''