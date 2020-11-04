import subprocess
import time


def check(nfc_list):
    with open('/home/pi/ZYDEMO/iota/nfc_list.txt', 'r') as fp:
        data = fp.readlines()
        if nfc_list in data[0]:
            # print(nfc_list[0])
            return True
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
    if nfcid !='istuseslibnfc':
        print(nfcid, time.time())
    # print(sakid)
    # print(atsid)
    # return [nfcid, sakid, atsid]
    return nfcid

# temp = check(nfc())
# print(temp)
