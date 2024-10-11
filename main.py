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

'''
print(sheet.get_all_values())
#데이터 프레임 생성하기
df = pd.DataFrame(sheet.get_all_values())

print(df)
#불러온 데이터 프레임 정리
df.rename(columns=df.iloc[0], inplace = True)
df.drop(df.index[0], inplace=True)

df.head()
'''
# B열 검색
search_term = "K5AR-RI4Y-5ZSL-05FZ-L96L"
cell_list = sheet.findall(search_term, in_column=2)  # B열은 2번 인덱스

# 검색된 열의 값들 불러오기
values = []
for cell in cell_list:
    row_values = sheet.row_values(cell.row)
    values.append(row_values)

print(values)

''' mac address 불러오기 '''
import uuid
def getMacAddress():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])

macc = getMacAddress()
# ipp = showpublicIp()
print(macc)

''' mac address 불러오기 '''

# import random
# import string
#
# def generate_unique_codes(n):
#     codes = set()
#     while len(codes) < n:
#         code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
#         formatted_code = '-'.join([code[i:i+4] for i in range(0, len(code), 4)])
#         codes.add(formatted_code)
#     return list(codes)
#
# codes = generate_unique_codes(3000)
# # sheet.update([['API 테스트']], 'A1')
#
# i = 2
# for K in codes:
#
#     t_no = i-1
#     t_a = 'A'+str(i)
#     t_b = 'B'+str(i)
#     # sheet.update([[t_no, K]], t_a, t_b)
#     print(t_no, K)
#     i = i+1
#
# print(codes)