import subprocess
List_package_name = ['fpdf2', ...]
def Install_Package():
    for pack in List_package_name:
        try:
            subprocess.check_call(['pip', 'install', pack])
            print("Successfully installed", pack)
        except subprocess.CalledProcessError as e:
            print("Error installing", pack, e)
    return 

def Uninstall_Package():
    for pack in List_package_name:
        try:
            subprocess.check_call(['pip', 'uninstall', pack, '-y'])
            print("Successfully uninstalled", pack)
        except subprocess.CalledProcessError as e:
            print("Error uninstalling", pack, e)
    return 
