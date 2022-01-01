import os
import argparse

def main(args=None):
  parser = argparse.ArgumentParser(description='Simple menu script for nmcli.')

  parser.add_argument("-r", "--rescan", help="scans for nearby networks", action="store_true")
  parser.add_argument("-l", "--list", help="prints a list of networks", action="store_true")
  parser.add_argument("-n", "--nopass", help="use to connect without password", action="store_true")
  parser.add_argument("-d", "--device", help="Manually select device", action="store")


  args = parser.parse_args()

  if args.rescan:
      os.system("nmcli dev wifi rescan")

  if args.list:
      os.system("clear ; nmcli dev wifi list ; echo")

  ssid = input("SSID: ")

  passwd = ""
  if not args.nopass:
      in_passwd = input("Password: ")
      if in_passwd != "":
          passwd = " password " + in_passwd

  if args.device == None:
      device = os.popen("""iw dev | awk '$1=="Interface"{print $2}'""").read()
   
  else:
      device = args.device
     
  os.system("""nmcli d wifi connect "{}"{} ifname {}""".format(ssid, passwd, device))
