from ssh import ssh_mc
mm_ip = '172.20.20.100'

ksrm =[]
ap_db = ssh_mc('show ap database status up | include Up | exclude Uplink', mm_ip)
ap_db = ap_db.splitlines()
print("Command Output:\n", ap_db)
count = 0
for i in ap_db:
    count =+1
    arr_apdb = i.split()
    print("Command Output:\n", arr_apdb[6])
    if arr_apdb[6] =='172.20.20.9':
        ap_ksrm = arr_apdb[6]
        ksrm.append(ap_ksrm)
count = ksrm.count('172.20.20.9')
print(count)