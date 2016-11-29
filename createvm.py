# coding: utf-8
# タグの属性にアクセス
 
from xml.dom import minidom
import sys
import shutil
import random
import uuid
import subprocess
import os
import getpass
import time

def randomMAC():
        mac = [ 0x00, 0x16, 0x3e,
                random.randint(0x00, 0x7f),
                random.randint(0x00, 0xff),
                random.randint(0x00, 0xff) ]
        return ':'.join(map(lambda x: "%02x" % x, mac))

args = sys.argv
print args[1]
files =os.listdir('/var/kvm/disk/kvm_centos7/')
for file in files:
	print file
print getpass.getuser()
shutil.copyfile("/var/kvm/disk/kvm_centos7/disk.qcow2", "/var/kvm/disk/kvm_centos7/" + args[1] + "disk.qcow2")
print "2"
# xmlファイルを読み込む
xdoc = minidom.parse("/etc/libvirt/qemu/kvm_centos7.xml")
print "3"
# nameタグ取得
recipe_element = xdoc.getElementsByTagName("name")[0]
print "4"
# データを変更
recipe_element.childNodes[0].data = args[1]
print "5"
# memoryタグ取得
recipe_element = xdoc.getElementsByTagName("memory")[0]
print "6"
# データを変更
recipe_element.childNodes[0].data = args[3]
print "7"
# currentmemoryタグ取得
recipe_element = xdoc.getElementsByTagName("currentMemory")[0]

# データを変更
recipe_element.childNodes[0].data = args[3]

# vcpu取得
recipe_element = xdoc.getElementsByTagName("vcpu")[0]

# データを変更
recipe_element.childNodes[0].data = args[2]

# sourceタグ取得
recipe_element = xdoc.getElementsByTagName("devices")[0]
datadev = recipe_element.getElementsByTagName("disk")[0]
datadev = datadev.getElementsByTagName("source")[0]
# データを変更
datadev.setAttribute("file","/var/kvm/disk/kvm_centos7/" + args[1] + "disk.qcow2")

# sourceタグ取得
recipe_element = xdoc.getElementsByTagName("devices")[0]
datadev = recipe_element.getElementsByTagName("channel")[0]
datadev = datadev.getElementsByTagName("source")[0]
# データを変更
datadev.setAttribute("path","/var/lib/libvirt/qemu/channel/target/domain-" + args[1] + "/org.qemu.guest_agent.0")

# uuid取得と変更
recipe_element = xdoc.getElementsByTagName("uuid")[0]
recipe_element.childNodes[0].data = uuid.uuid4()

# MACアドレス取得と変更
recipe_element = xdoc.getElementsByTagName("devices")[0]
datadev = recipe_element.getElementsByTagName("interface")[0]
datadev = datadev.getElementsByTagName("mac")[0]
# データを変更
datadev.setAttribute("address",randomMAC())

#xml保存
f1 = open('/etc/libvirt/qemu/'+ args[1] + '.xml', 'w')
f1.write(xdoc.toprettyxml('  ', '\n', 'utf-8'))
f1.close()
print "10"
cmd = "virsh define /etc/libvirt/qemu/" + args[1] + ".xml"
subprocess.call( cmd.strip().split(" ")  ) 


time.sleep(5.0) #sleep(秒指定)
cmd = "virsh start " + args[1]
subprocess.call( cmd.strip().split(" ")  )
