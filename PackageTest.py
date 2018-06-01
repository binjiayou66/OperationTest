
import os
import plistlib
import sys

def infoPlistUpdateVersion(app_info_plist):
    mainPath = os.getcwd()
    app_info_plist_path = ("%s/%s" % (mainPath, app_info_plist))
    info_plist = plistlib.readPlist(app_info_plist_path)
    app_version = info_plist['CFBundleShortVersionString']
    app_version_list = list(app_version)
    lastNum = app_version_list[len(app_version_list)-1]
    app_version_list.pop()
    lastNum = int(lastNum) + 1
    app_version_list.append(str(lastNum))
    
    app_version_pdate = "".join(app_version_list)
    print(app_version_pdate)
    app_bundle_version_update = app_version_pdate + '.19120623'

    info_plist["CFBundleShortVersionString"] = app_version_pdate
    info_plist["CFBundleVersion"] = app_bundle_version_update
    plistlib.writePlist(info_plist, app_info_plist_path)

git_branch_name = os.popen('git branch')
print(git_branch_name)
for name in git_branch_name:
  print(name)