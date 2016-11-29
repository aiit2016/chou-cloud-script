# coding: utf-8
import sys
import subprocess
import os

args = sys.argv

cmd = "virsh undefine " + args[1]
subprocess.call( cmd.strip().split(" ")  )

os.remove("/var/kvm/disk/kvm_centos7/" + args[1] + "disk.qcow2")
