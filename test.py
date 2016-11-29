# coding: utf-8
# タグの中身のテキストにアクセス
 
from xml.dom import minidom
 
# sample.xmlファイルを読み込む
xdoc = minidom.parse("/etc/libvirt/qemu/chou.xml")
 
# recipe タグの0番目の要素を取得
recipe_element = xdoc.getElementsByTagName("devices")[0]
datadev = recipe_element.getElementsByTagName("disk")[0]
datadev = datadev.getElementsByTagName("source")[0]
# データを表示
print(datadev.getAttribute("file"))
