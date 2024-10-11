import gspread
from oauth2client.service_account import ServiceAccountCredentials


def Account_Info(Input_Key) :
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
    #개인에 따라 수정 필요 - 시트 선택하기 (시트명을 그대로 입력해주면 된다.)
    sheet = doc.worksheet("KEY")

    # B열 검색
    # Input_Key = "K5AR-RI4Y-5ZSL-05FZ-L96L"
    cell_list = sheet.findall(Input_Key, in_column=2)  # B열은 2번 인덱스

    # 검색된 열의 값들 불러오기
    # values = []
    for cell in cell_list:
        Key_values = sheet.row_values(cell.row)

    Get_No = Key_values[0]
    Get_Key = Key_values[1]
    Get_Pro = Key_values[2]
    Get_Usr = Key_values[3]
    Get_MAC = Key_values[4]
    Get_Date = Key_values[5]

    print(Get_No, Get_Key, Get_Pro, Get_Usr, Get_MAC, Get_Date)


Input_Key = "K5AR-RI4Y-5ZSL-05FZ-L96L"
Account_Info(Input_Key)