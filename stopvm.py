# coding: utf-8
import sys
import subprocess
import os

args = sys.argv

cmd = "virsh destroy " + args[1]
subprocess.call( cmd.strip().split(" ")  )

