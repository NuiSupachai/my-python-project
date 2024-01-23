import xlsxwriter

# Create a new Excel workbook and add a worksheet
workbook = xlsxwriter.Workbook('template.xlsx')
worksheet = workbook.add_worksheet('KSRM')

# Define cell formats for header and data
header_format = workbook.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter', 'bg_color': '#C6EFCE'})
data_format = workbook.add_format({'align': 'center', 'valign': 'vcenter'})

# Populate the template data
worksheet.write('A1', 'Name', header_format)
worksheet.write('B1', 'Age', header_format)
worksheet.write('A2', 'John', data_format)
worksheet.write('B2', 25, data_format)
worksheet.write('A3', 'Alice', data_format)
worksheet.write('B3', 30, data_format)

# Save the workbook
workbook.close()
