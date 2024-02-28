import xlsxwriter
workbook = xlsxwriter.Workbook('Morning Check List.xlsx')
sheet_TotalAP = workbook.add_worksheet('AP Status')
sheet_KSRO = workbook.add_worksheet('KSRO')
sheet_KSRM = workbook.add_worksheet('KSRM')
sheet_KSPO = workbook.add_worksheet('KSPO')

# Define cell formats for header
header_format = workbook.add_format(
    {   
        'bold': True, 
        'align': 'center',
        'valign': 'vcenter',
        'border':2,
    }
)
# Define cell formats for data
data_format = workbook.add_format(
    {   
        'align': 'center',
        'valign': 'vcenter',
        'border':2,
    }
)

# Create a new Excel workbook and add a worksheet
def APStatus():
    sheet_TotalAP.merge_range('A1:F1','AP STAUS',header_format)
    sheet_TotalAP.merge_range('A2:B2','KSRO',header_format)
    sheet_TotalAP.merge_range('C2:D2','KSRM',header_format)
    sheet_TotalAP.merge_range('E2:F2','KSPO',header_format)
    # Populate the template data
    sheet_TotalAP.write('A3', 'Up', header_format)
    sheet_TotalAP.write('B3', 'Down', header_format)
    sheet_TotalAP.write('C3', 'Up', header_format)
    sheet_TotalAP.write('D3', 'Down', header_format)
    sheet_TotalAP.write('E3', 'Up', header_format)
    sheet_TotalAP.write('F3', 'Down', header_format)

def CheckSSID_KSRO():
    sheet_KSRO.merge_range('A1:K1','BSSID STATUS',header_format)

    # Populate the template data
    sheet_KSRO.write('A2','Floor',header_format)
    sheet_KSRO.write('B2', '@Enterprise', header_format)
    sheet_KSRO.write('C2', 'Narita', header_format)
    sheet_KSRO.write('D2', 'Challenger', header_format)
    sheet_KSRO.write('E2', 'Gesuto', header_format)
    sheet_KSRO.write('F2', 'Odaiba', header_format)
    sheet_KSRO.write('G2', 'Akiba', header_format)
    sheet_KSRO.write('H2', 'Atlantis', header_format)
    sheet_KSRO.write('I2', 'TABASCO', header_format)
    sheet_KSRO.write('J2', '@Telephone', header_format)
    sheet_KSRO.write('K2', 'WASABI', header_format)

def CheckSSID_KSRM():
    sheet_KSRM.merge_range('A1:K1','BSSID STATUS',header_format)
    # Populate the template data
    sheet_KSRM.write('A2','Floor',header_format)
    sheet_KSRM.write('B2', '@Enterprise', header_format)
    sheet_KSRM.write('C2', 'Narita', header_format)
    sheet_KSRM.write('D2', 'Challenger', header_format)
    sheet_KSRM.write('E2', 'Gesuto', header_format)
    sheet_KSRM.write('F2', 'Odaiba', header_format)
    sheet_KSRM.write('G2', 'Akiba', header_format)
    sheet_KSRM.write('H2', 'Atlantis', header_format)
    sheet_KSRM.write('I2', 'TABASCO', header_format)
    sheet_KSRM.write('J2', '@Telephone', header_format)
    sheet_KSRM.write('K2', 'WASABI', header_format)

def CheckSSID_KSPO():
    sheet_KSPO.merge_range('A1:K1','BSSID STATUS',header_format)
    # Populate the template data
    sheet_KSPO.write('A2','Floor',header_format)
    sheet_KSPO.write('B2', '@Enterprise', header_format)
    sheet_KSPO.write('C2', 'Narita', header_format)
    sheet_KSPO.write('D2', 'Challenger', header_format)
    sheet_KSPO.write('E2', 'Gesuto', header_format)
    sheet_KSPO.write('F2', 'Odaiba', header_format)
    sheet_KSPO.write('G2', 'Akiba', header_format)
    sheet_KSPO.write('H2', 'Atlantis', header_format)
    sheet_KSPO.write('I2', 'TABASCO', header_format)
    sheet_KSPO.write('J2', '@Telephone', header_format)
    sheet_KSPO.write('K2', 'WASABI', header_format)

def CheckAPStatus(ap_ksro, ap_ksrm, ap_kspo):
    list_ksro_up = []
    list_ksro_down = []
    count_ap_ksro_up = 0
    count_ap_ksro_down = 0

    for i in ap_ksro:
        if i == 'Up':
            list_ksro_up.append(i)
        else:
            list_ksro_down.append(i)
    count_ap_ksro_up = len(list_ksro_up)
    count_ap_ksro_down = len(list_ksro_down)
    sheet_TotalAP.write('A4', count_ap_ksro_up, header_format)
    sheet_TotalAP.write('B4', count_ap_ksro_down, header_format)

    list_ksrm_up = []
    list_ksrm_down = []
    count_ap_ksrm_up = 0
    count_ap_ksrm_down = 0

    for i in ap_ksrm:
        if i == 'Up':
            list_ksrm_up.append(i)
        else:
            list_ksrm_down.append(i)
    count_ap_ksrm_up = len(list_ksrm_up)
    count_ap_ksrm_down = len(list_ksrm_down)
    sheet_TotalAP.write('C4', count_ap_ksrm_up, header_format)
    sheet_TotalAP.write('D4', count_ap_ksrm_down, header_format)

    list_kspo_up = []
    list_kspo_down = []
    count_ap_kspo_up = 0
    count_ap_kspo_down = 0
    
    for i in ap_kspo:
        if i == 'Up':
            list_kspo_up.append(i)
        else:
            list_kspo_down.append(i)
    count_ap_kspo_up = len(list_kspo_up)
    count_ap_kspo_down = len(list_kspo_down)
    sheet_TotalAP.write('E4', count_ap_kspo_up, header_format)
    sheet_TotalAP.write('F4', count_ap_kspo_down, header_format)

APStatus()
CheckSSID_KSRO()
CheckSSID_KSRM()
CheckSSID_KSPO()
