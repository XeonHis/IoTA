import subprocess
import time
from open import open_door
import requests


def check(nfc_list):
    with open('/home/pi/ZYDEMO/iota/nfc_list.txt', 'r') as nfc_fp:
        data = nfc_fp.readlines()
        # print(nfc_list)
        if nfc_list in data[0]:
            # print(nfc_list[0])
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print('nfc open at ', current_time)
            open_door(current_time)
            with open('/home/pi/ZYDEMO/iota/open_detail.txt', 'a') as log_fp:
                log_fp.write(
                    'nfc ' + nfc_list + ' open at ' + str(current_time) + '\n')
                log_fp.flush()

            nfc_payload = "{{\"card_no\": {}}}".format(str(nfc_list))
            requests.post(url='https://demo.thingsboard.io/api/v1/iK0zWkznWEoYqBnmAtQf/telemetry', data=nfc_payload)

            time.sleep(2)
            # return True
        # count = len(data)
        # for i in range(count):
        #     temp_data = data[i].split(',')
        #     r_nfcid = temp_data[0]
        #     r_sakid = temp_data[1]
        #     r_atsid = temp_data[2]
        #     if nfc_list[2] is 0:
        #         if nfc_list[0] == r_nfcid and nfc_list[1] == r_sakid:
        #             return True
        #     else:
        #         if nfc_list[1] == r_sakid and nfc_list[2] == r_atsid:
        #             return True
        #     if i == count:
        #         return False


def nfc():
    while True:
        time.sleep(0.2)
        output = str(subprocess.Popen(['nfc-list'], stdout=subprocess.PIPE, shell=True).communicate()[0])
        # print(output)
        nfc_start = 'NFCID'
        # sak_start = 'SEL_RES'
        # ats_start = 'ATS'
        nfc_index = output.find(nfc_start)
        # sak_index = output.find(sak_start)
        nfcid = output[nfc_index + 8:nfc_index + 24].replace(' ', '')

        # if ats_start in output:
        #     ats_index = output.find(ats_start)
        #     atsid = output[ats_index + 4:ats_index + 14]
        #     sakid = output[sak_index + 9:ats_index]
        # else:
        #     sakid = output[sak_index + 9:sak_index + 17]
        #     atsid = 0
        # if nfcid !='istuseslibnfc':
        #     print(nfcid)
        #     check(nfcid)
        # print(sakid)
        # print(atsid)
        # return [nfcid, sakid, atsid]
        # return nfcid
        check(nfcid)

# temp = check(nfc())
# print(temp)
