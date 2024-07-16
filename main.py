from dotenv import load_dotenv
import time
import os
import jwt

from load_excel import load_excel
from put_boond import put_contact

load_dotenv()
# MY_ENV_VAR = os.getenv('MY_ENV_VAR')


def main():

    ###### Payload BM #####
    user_payload = {
        "userToken": os.getenv('userToken'),
        "clientToken": os.getenv('clientToken'),
        "time": int(time.time()),
        "mode": "god"
    }
    encoded_user_payload = jwt.encode(user_payload, os.getenv('clientKey'), algorithm="HS256")

    excel_path = "C:\\Users\\EmileCaubet\\OneDrive - ORLADE\\Bureau\\"
    excel_name = "Liste de contacts liés aux RO Op2_20240605.xlsx"
    excel_sheetname = "contacts (12)"

    wb, ws = load_excel(excel_path, excel_name, excel_sheetname)
    last_line = ws.max_row

    for row in range(2, last_line + 1):
        ccon = ws.cell(row, 1).value[4:]
        put_contact(ccon, encoded_user_payload)
        print(f"Modification {row} sur {last_line}")

    wb.close()


if __name__ == "__main__":
    main()
