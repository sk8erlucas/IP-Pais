
#capotas-lopez@capotas-lopez.iam.gserviceaccount.com
#101456906880359472862

import gspread

def BuscarPaisenSheet(code):

    sa = gspread.service_account(filename='App/capotas-lopez-35faa4b11037.json')
    sh = sa.open('Copia de Domicilios')

    wks = sh.worksheet('Hoja 1')

    data = wks.get_all_records()

    for i in data:

        if i['Code'] == code:
            return i['Idioma/pais']

    return 'undefined'

print(BuscarPaisenSheet("AR"))