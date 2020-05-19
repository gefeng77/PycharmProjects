import time
import datetime
import random
import hashlib
import os
import json


defaultParams = {'timestamp': None, 'nonce': None, 'alg': 'MD5'}
key = 'secret-haha'


def createSign(mySign):
    myHash = hashlib.md5()
    myHash.update(mySign.encode(encoding='UTF-8'))
    createSign = myHash.hexdigest().lower()
    return createSign


def signFunc_Post(**myJson):
    mySign  =   ''
    defaultParams['nonce']  =   random.randint(1,99)
    myJson.update(defaultParams)
    dictKey = myJson.keys()
    sorted_dictKey  =   sorted(dictKey)
    myJson['timestamp'] =   int(time.time())
    for i in sorted_dictKey:
        if myJson[i] != '' and myJson[i] is not None:
            if myJson[i] == True and str(myJson[i]) == 'True':
                myJson = '%s%s=%s&' % (mySign, i, 'false')
            elif myJson[i] == False and str(myJson[i]) == 'False':
                mySign = '%s%s=%s&' % (mySign, i, 'false')
            else:
                mySign = '%s%s=%s&' %   (mySign, i, myJson[i])
    mySign = "%skey=%s" %   (mySign, key)
    mySign = mySign.replace(' None', 'null')
    mySign = mySign.replace(' True', 'true')
    mySign = mySign.replace(' False', 'false')
    mySign = mySign.replace('\"', '\\\"')
    mySign = mySign.replace(': ', ':')
    mySign = mySign.replace(', ', ',')
    mySign = mySign.replace('\'', '"')
    return myJson


def signFunc_Get(**myJson):
    mySign = ''
    blanks = ''
    defaultParams['nonce'] = random.randint(1,99)
    myJson.update(defaultParams)
    dictKey = myJson.keys()
    sorted_dictKey = sorted(dictKey)
    myJson['timestamp'] = int(time.time())
    for i in sorted_dictKey:
        if myJson[i] !='' and myJson[i]!= None:
            if myJson[i] == True and str(myJson[i] == 'True'):
                mySign = '%s%s=%s&' % (mySign, i, 'true')
            elif myJson[i] == False and str(myJson[i]) == 'False':
                mySign = '%s%s=%s&' % (mySign, i, 'false')
            elif myJson[i] == None:
                pass
            else:
                mySign = '%s%s=%s&' % (mySign, i, myJson[i])
        else:
            blanks = '%s%s=&' % (blanks, i)
    mySign2 = mySign + blanks + 'sign='
    mySign = "%skey=%s" % (mySign, key)
    mySign = mySign.replace(' None', 'null')
    mySign = mySign.replace(' True', 'true')
    mySign = mySign.replace(' False', 'false')
    mySign = mySign.replace('\"', '\\\"')
    mySign = mySign.replace(': ', ':')
    mySign = mySign.replace(', ', ',')
    mySign = mySign.replace('\'', '"')
    myJson['sign'] = createSign(mySign)
    mySign2 += createSign(mySign)
    return mySign2


def myTimestamp():
    time.sleep(0.5)
    return int(time.time())


def myLTimestamp():
    return int(round(time.time()*1000))


def myPresentTime():
    return time.strftime("%Y.%m.%d %H:%M:%S", time.localtime())


def myPresentime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def myPresentTime_M():
    return time.strftime("%Y.%m.%d %H:%M", time.localtime())


def myTimeInterval():
    startTime = time.strftime("%Y.%m.%d", time.localtime())
    endTIme = (datetime.datetime.now() + datetime.timedelta(days=7))
    endTime = endTIme.strftime("%Y.%m.%d")
    return '%s,%s'   % (startTime, endTime)


def myExeStartTime():
    myExeEndTime = (datetime.datetime.now() + datetime.timedelta(days=7))
    return myExeEndTime.strftime("%Y-%m-%d")


def myExeEndTime():
    myExeEndTime = (datetime.datetime.now() + datetime.timedelta(days=7))
    return myExeEndTime("%Y-%m-%d")


def file_binary(path):
    with open(path, 'rb') as f:
        result = f.read()
    return result


def get_img_path(path, num):
    imgspath = '.'+path
    imgs = random.sample(os.listdir(imsgpath), num)
    for x in range(len(imgs)):
        imgs[x] = imgspath + imgs[x]
    return imgs


def random_path():
    return get_img_path('/imgs/', 1)


def file_name(path):
    return (path.split('/')[-1])


def file_mime(path):
    file_mime = path.split('.')[-1]
    if file_mime == 'jpg':
        return 'image/jpeg'
    else:
        return 'image/' + file_mime


def file_ext(path):
    return path.split('.')[-1]


def get_img_detail(path):
    img_details = []
    for x in path:
        fileSize = os.path.getsize(x)
        fileName = file_name(x)
        name = fileName.split(',')[0]
        img_details.append({'name': name, 'suffix': file_ext(x), 'fileName': fileName,'contentType': file_mime(x), 'fileSize': fileSize,'filePath':x})
    return img_details


def file_md5(fileBinary):
    myHash = hashlib.md5()
    myHash.update(fileBinary)
    md5 = myHash.hexdigest().lower()
    return md5


def savedraft_itemList(itemList, createTime, createBy):
    itemList[0]['createTime'] = createTime
    itemList[0]['createBy'] = createBy
    itemList[0]['exist'] = True
    return itemList


def editdraft_itemList(itemList):
    if itemList[0]['itemTypeId'] == 150:
        itemList[0]['itemDetailList'] = [{'title': '工时', 'value': '6', 'statistic': 1}, {'title': '工作内容', 'value': '自动化数据', 'statistic': 0}]
    elif itemList[0]['itemTypeId'] == 151:
        itemList[0]['itemDetailList'] = [{'title': '单价（元/吨）', 'value': '66.6', 'staticstic': 0},{'title': '重量（吨）','value': '10', 'statistic':0},{'title': '总价（元)','value': '666.000','statistic': '1'}]
    return itemList


def editdraft_attachmentList(attachmentVOList, imgUrl):
    attachmentVOList[0]['imgUrl'] = imgUrl
    attachmentVOList[0]['status'] = 'success'
    attachmentVOList[0]['progress'] = 100
    return attachmentVOList


def myNone():
    return None


def myTrue():
    return True


def myFalse():
    return False


def edit_checkListAttributeFormList(templateAttribute,tplId,checklistName,zxr):
    templateAttribute[0]['value'] = tplId
    templateAttribute[1]['value'] = checklistName
    templateAttribute[2]['value'] = zxr
    templateAttribute[3]['value'] = myTimeInterval()
    templateAttribute[4]['value'] = 4
    templateAttribute[5]['value'] = '自动化数据'
    templateAttribute[6]['value'] = '2'
    templateAttribute[7]['value'] = '目标位置'
    templateAttribute[8]['value'] = zxr
    templateAttribute[9]['value'] = '-1'
    templateAttribute[10]['value'] = '-1'
    templateAttribute[11]['value'] = '单文本输入'
    templateAttribute[12]['value'] = ' -1.001'
    templateAttribute[13]['value'] = '多行文本输入'
    templateAttribute[14]['value'] = 3
    templateAttribute[15]['value'] = '1,2,3,4,5'
    templateAttribute[16]['value'] = myPresentime()
    templateAttribute[17]['value'] = myTimeInterval()
    return templateAttribute


