import xlsxwriter
workbook = xlsxwriter.Workbook('Morning Check List.xlsx')
sheet_TotalAP = workbook.add_worksheet('AP Status')


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
def AP_Status():
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

    # Save the workbook
    workbook.close()

AP_Status()