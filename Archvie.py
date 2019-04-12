#!/user/bin/python
import commands
import json
import re
import sys
import os
import shutil


#=======================
#Update App Info Class
#=======================
class UpdateAppInfo(object):

    # ------- App Logo Config ---
    @staticmethod
    def updateAppLogo(scheme):
        if len(scheme) == 0:
            return
        target_file_path = 'dfc_v2/Images.xcassets/AppIcon.appiconset/'
        source_file_path = 'ArchvieResource/'+scheme+'/AppLogo/'
        fileNamesArray = []
        for root, dirs, files in os.walk(source_file_path):
            fileNamesArray = files
        if len(fileNamesArray) == 0:
            print("The Logo Count is 0!!!")
            return
        if len(fileNamesArray) < 9:
            print("The Logo Count is wrong!!!")
        for f_png in fileNamesArray:
            imageFile = source_file_path + f_png
            shutil.copy(imageFile, target_file_path)

        print("Update AppLogo Successfully")


    # ----- App LaunchImage Config ---
    @staticmethod
    def updateLaunchImage(scheme):
        if len(scheme) == 0:
            return
        target_file_path = 'dfc_v2/Images.xcassets/LaunchImage.launchimage/'
        source_file_path = 'ArchvieResource/'+scheme+'/AppLaunchImage/'
        fileNamesArray = []
        for root, dirs, files in os.walk(source_file_path):
            fileNamesArray = files
        if len(fileNamesArray) == 0:
            print("The Logo Count is 0!!!")
            return
        if len(fileNamesArray) < 5:
            print("The Logo Count is wrong!!!")
        for f_png in fileNamesArray:
            imageFile = source_file_path + f_png
            shutil.copy(imageFile, target_file_path)

        print("Update App LaunchImage Successfully")

    @staticmethod
    def updateGitLog(scheme):
        cmd = 'git log --pretty=format:"%H" -1'
        resposeStr = commands.getoutput(cmd)
        print(resposeStr)

    @staticmethod
    def saveAppName(appConfigration):
        # read old json file
        file_path = 'ArchvieResource/main.json'
        file_object = open(file_path)
        try:
            file_context = file_object.read()
            if len(file_context) > 10:
                oldDict = json.loads(file_context)
        finally:
            file_object.close()
            oldDict['AppName'] = appConfigration
        newStr = json.dumps(oldDict)
        print(newStr)
        file_write = open(file_path, 'w')
        file_write.write(newStr)

#---------------------------
#--------- Host Conifg -----
#---------------------------

class UpdateHost(object):
    @staticmethod
    def updatePreHubHost(scheme):
        # old:new
        hostKeyMap = {
            'authorize': 'audit',
            'azeroth': 'certificateCenter',
            'basic': 'seapig',
            'cashier': 'cashier',
            'crm': 'cupid',
            'generalOrderBaseURI': 'heimdall',
            'upgrade': 'piebridge',
            'order': 'oemOrder',
            'sso': 'ssoServer',
            'H5assets': 'f2e',
            'H5Page': 'f2e',
            'H5Server': 'f2e',
            'msgCenter': 'msgcenter'
        }
        cmd = "curl -H 'version: 1.1.1' -H 'Souche-Std-Response: 1' -H 'User-Agent: iOS' -H 'appname: dfc' -H 'Host: config.souche-inc.com' --data 'app=single-unit&token=NN8oMicEa7&type=" + scheme + "' --compressed 'http://config.souche-inc.com/app/config/keys.json' 2>/dev/null"

        print(cmd)

        resposeStr = commands.getoutput(cmd)
        newHostDict = json.loads(resposeStr)
        newHostArray = newHostDict['data']
        print newHostArray

        # filter file
        file_path = ''
        if scheme == 'PREPUB':
            file_path = 'dfc_v2/testHosts-pre.json'
        elif scheme == 'PRO':
            file_path = 'dfc_v2/productHosts.json'
        elif scheme == 'DEV-A':
            file_path = 'dfc_v2/testHosts.json'

        # read old json file
        file_object = open(file_path)
        try:
            file_context = file_object.read()
            if len(file_context) > 10:
                oldHostDict = json.loads(file_context)
            else:
                oldHostDict = hostKeyMap
        finally:
            file_object.close()

        # update new data in old json file
        for item in newHostArray:
            oldHostDict[item['key']] = item['value']
            for mapKey in hostKeyMap:
                if item['key'] == hostKeyMap[mapKey]:
                    oldHostDict[mapKey] = item['value']

        # write in host file
        newHostStr = json.dumps(oldHostDict)
        newHostStr = newHostStr.replace('{', '{\n')
        newHostStr = newHostStr.replace('}', '\n}')
        newHostStr = newHostStr.replace('",', '",\n')
        file_write = open(file_path, 'w')
        file_write.write(newHostStr)
        print("Update finish")


#-------main---------
if __name__ == '__main__':
    # update app infp
    print("Update ---------------- ")
    AppConfigration = ''
    for i in range(1, len(sys.argv)):
        AppConfigration = sys.argv[i]

    # filter scheme
    if AppConfigration == 'Debug' or AppConfigration == 'PreRelease' or AppConfigration == 'InHouse':
        AppConfigration = 'Default'
    else:
        tempArr = AppConfigration.split('_')
        AppConfigration = tempArr[0]
    # update
#    print(AppConfigration)
#    updateAppInfo = UpdateAppInfo()
#    updateAppInfo.updateAppLogo(AppConfigration)
#    updateAppInfo.updateLaunchImage(AppConfigration)
#    updateAppInfo.updateGitLog('DEV-A')
#    updateAppInfo.saveAppName(AppConfigration)
    # update host
    updateHost = UpdateHost()
    updateHost.updatePreHubHost('DEV-A')
#    updateHost.updatePreHubHost('PREPUB')
#    updateHost.updatePreHubHost('PRO')
