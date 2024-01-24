from ssh import ssh_mc
from template import *

mm_ip = '172.24.255.9'

ksro_cluster =[]
ksrm_cluster =[]
kspo_cluster =[]

ap_db = ssh_mc('show ap database status up | include Up | exclude Uplink', mm_ip)
ap_db = ap_db.splitlines()


for i in ap_db:
    list_apdb = i.split()
    print("Command Output:\n", list_apdb[7])
    if list_apdb[7] =='172.28.254.2' or list_apdb[7] =='172.28.254.3':
        ap_ksro = list_apdb[7]
        ksro_cluster.append(ap_ksro)
    elif list_apdb[7] =='172.29.0.2' or list_apdb[7] =='172.29.0.3':
        ap_ksrm = list_apdb[7]
        ksrm_cluster.append(ap_ksrm)
    else:
        ap_kspo = list_apdb[7]
        kspo_cluster.append(ap_kspo)
"""elif list_apdb[7] =='172.29.128.2' or list_apdb[7] =='172.29.128.2' or list_apdb[7] =='172.29.128.2':
        ap_kspo = list_apdb[7]
        kspo_cluster.append(ap_kspo)"""

ap_count_ksro = ksro_cluster.count(ap_ksro)
ap_count_ksrm = ksrm_cluster.count(ap_ksrm)
ap_count_kspo = kspo_cluster.count(ap_kspo)

print(ap_count_ksro)
print(ap_count_ksrm)
print(ap_count_kspo)