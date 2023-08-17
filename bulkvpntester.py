import pandas as pd
import sys
from termcolor import colored
import requests
import subprocess
import time

def vpnJKTon():
    vpnJKT = r'"C:\Program Files\OpenVPN Connect\OpenVPNConnect" --connect-shortcut=1690112655655 --hide-tray'#bisa disesuaikan kalau mau copas perintah saya, pastikan cek sendiri dengan benar, biar commandnya tidak arror
    jkt = subprocess.run(vpnJKT, shell=True, text=True)
    print("VPN Jakarta ON")
    time.sleep(2)

def vpnSBYoff():
    vpnmetu = r'"C:\Program Files\OpenVPN Connect\OpenVPNConnect" --quit'
    metu = subprocess.run(vpnmetu, shell=True, text=True)
    print("Keluar dari VPN Surabaya")
    time.sleep(2)

def vpnSBYon():
    vpnSBY = r'"C:\Program Files\OpenVPN Connect\OpenVPNConnect" --connect-shortcut=1690110411169 --hide-tray'
    sby = subprocess.run(vpnSBY, shell=True, text=True)
    print("VPN Surabaya ON")
    time.sleep(2)

def vpnJKToff():
    vpnmetu = r'"C:\Program Files\OpenVPN Connect\OpenVPNConnect" --quit'
    metu = subprocess.run(vpnmetu, shell=True, text=True)
    print("Keluar dari VPN Jakarta")
    time.sleep(2)

if len(sys.argv) == 2:
    if str(sys.argv[1]) == "run":
        try:
            i=0
            ipSupermicro = pd.read_csv('ipSupermicro.csv')
            ipS = ipSupermicro.shape[0]
            for tektek in range(ipS):
                i += 1
                if i <= 68:
                    print(colored("-"*50,"magenta"))
                    print(colored("-"*19,"yellow").ljust(15), end='')
                    print(colored(f"Tes VPN ke {i}","yellow").ljust(15), end='')
                    print(colored("-"*19,"yellow"))
                    alamat = ipSupermicro.iloc[i]['target']
                    if pd.notnull(alamat):
                        tektek = alamat.split(',')
                        for url in tektek:
                            url = url.strip()
                            url2 = "http://" + url
                            nakniknuk = url
                            try:
                                vpnJKTon()
                                time.sleep(3)
                                sc = requests.get(url2)
                                if sc.status_code == 200 :
                                    enum = url2
                                    print(colored(f"\n{nakniknuk} menggunakan vpn Jakarta","green"))
                                    vpnJKToff()
                                else:
                                    vpnJKTon()
                                    time.sleep(3)
                                    cek2 = url2
                                    sc = requests.get(cek2)
                                    if sc.status_code == 200 :
                                        enum = url2
                                        print(colored(f"\n{nakniknuk} menggunakan vpn Jakarta","green"))
                                        vpnJKToff()
                            except requests.exceptions.ConnectionError:
                                vpnJKToff()
                                print(f"\n{nakniknuk}")
                                print(colored("\nIP tidak bisa di kunjungi bosqiuu :V\n","red"))
                            try:
                                vpnSBYon()
                                time.sleep(3)
                                sc = requests.get(url2)
                                if sc.status_code == 200 :
                                    enum = url2
                                    print(colored(f"\n{nakniknuk} menggunakan vpn Surabaya","green"))
                                    vpnSBYoff()
                                else:
                                    vpnSBYon()
                                    time.sleep(3)
                                    cek2 = url2
                                    sc = requests.get(cek2)
                                    if sc.status_code == 200 :
                                        enum = url2
                                        print(colored(f"\n{nakniknuk} menggunakan vpn Surabaya","green"))
                                        vpnSBYoff()
                            except requests.exceptions.ConnectionError:
                                vpnSBYoff()
                                print(f"\n{nakniknuk}")
                                print(colored("\nIP tidak bisa di kunjungi bosqiuu :V\n","red"))
                        continue
                else:
                    sys.exit()
        except KeyboardInterrupt:
            print(colored("\nTerimakasih salam Tektektek :)\n","magenta"))
            sys.exit()
    else:
        print("\nInputan gak jelas boskuh waduh baleni maneh\n")
else:
        print("\nUntuk menjalankan: python3 bulkvpntester.py run\n")