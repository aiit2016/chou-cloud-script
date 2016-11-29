# coding: utf-8
import sys
import subprocess

args = sys.argv

cmd = "virsh start " + args[1]
subprocess.call( cmd.strip().split(" ")  )
