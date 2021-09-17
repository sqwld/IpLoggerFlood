class MAIN:
	__author__ = "538744533845016596"

import requests
import os
import emoji
from datetime import datetime
import ctypes
ctypes.windll.kernel32.SetConsoleTitleA("FakeLogger | Loading...")
from colorama import Fore, init
init()
r = requests.get(f"http://ip-api.com/json/").json()
os.system('cls') if os.name == 'nt' else os.system('clear')
a = Fore.LIGHTRED_EX
s = Fore.LIGHTWHITE_EX
banner = f"""
		  {a}███████{s}╗ {a}█████{s}╗ {a}██{s}╗  {a}██{s}╗{a}███████{s}╗{a}██{s}╗      {a}██████{s}╗  {a}██████{s}╗  {a}██████{s}╗ {a}███████{s}╗{a}██████{s}╗ 
		  {a}██{s}╔════╝{a}██{s}╔══{a}██{s}╗{a}██{s}║ {a}██{s}╔╝{a}██{s}╔════╝{a}██{s}║     {a}██{s}╔═══{a}██{s}╗{a}██{s}╔════╝ {a}██{s}╔════╝ {a}██{s}╔════╝{a}██{s}╔══{a}██{s}╗
		  {a}█████{s}╗  {a}███████{s}║{a}█████{s}╔╝ {a}█████{s}╗  {a}██{s}║     {a}██{s}║   {a}██{s}║{a}{a}██{s}║  {a}███{s}╗{a}██{s}║  {a}███{s}╗{a}█████{s}╗  {a}██████{s}╔╝
		  {a}██{s}╔══╝  {a}██{s}╔══{a}██{s}║{a}██{s}╔═{a}██{s}╗ {a}██{s}╔══╝  {a}██{s}║     {a}██{s}║   {a}██{s}║{a}██{s}║   {a}██{s}║{a}██{s}║   {a}██{s}║{a}██{s}╔══╝  {a}██{s}{s}╔══{a}██{s}{s}╗
		  {a}██{s}║     {a}██{s}║  {a}██{s}║{a}██{s}║  {a}██{s}╗{a}███████{s}╗{a}███████{s}╗╚{a}██████{s}╔╝╚{a}██████{s}╔╝╚{a}██████{s}╔╝{a}███████{s}╗{a}██{s}║  {a}██{s}{s}║
		  {s}╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝{s}╚═╝  {s}╚═╝
{Fore.RESET}

		  {Fore.LIGHTRED_EX}[{Fore.LIGHTWHITE_EX}!{Fore.LIGHTRED_EX}] Discord: https://discord.gg/5dwVQ5jTPs
		  {Fore.LIGHTRED_EX}[{Fore.LIGHTWHITE_EX}!{Fore.LIGHTRED_EX}] DevId: 538744533845016596
		  {Fore.LIGHTRED_EX}[{Fore.LIGHTWHITE_EX}!{Fore.LIGHTRED_EX}] Github: https://github.com/sqwld/
		  {Fore.LIGHTRED_EX}[{Fore.LIGHTWHITE_EX}!{Fore.LIGHTRED_EX}] IP: {r['query']}

"""
print(banner)
ctypes.windll.kernel32.SetConsoleTitleA("FakeLogger | Main")

print(f'{Fore.LIGHTRED_EX}┌─[{Fore.LIGHTWHITE_EX}fakelogger{Fore.LIGHTYELLOW_EX}@{Fore.LIGHTWHITE_EX}root{Fore.LIGHTRED_EX}]-[{Fore.LIGHTGREEN_EX}~{Fore.LIGHTRED_EX}] Url:')
x = input(f"└──╼ >{Fore.LIGHTBLACK_EX}>{Fore.LIGHTWHITE_EX}> ")


class FloodLogs(type):
	def __init__(cls, self, headers, proxies):
		self.headers = cls.headers = dict(headers)
		self.proxxies = cls.proxies = dict(proxies)


	def __new__(self, cls, proxies,headers):
		self.count = 0
		ctypes.windll.kernel32.SetConsoleTitleA("FakeLogger | Requesting...")
		while 100:
			self.responce = requests.get(
				url = x, 
				headers = {'user-agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15"},
				proxies = proxies
			)
			self.count += 1
			print(f"{Fore.LIGHTRED_EX}┌─[ {Fore.LIGHTWHITE_EX}fakelogger{Fore.LIGHTRED_EX} | {Fore.LIGHTWHITE_EX}Requests: {self.count}{Fore.LIGHTRED_EX} ]")
			if self.responce.status_code == 200 or 204:
				print(f"{Fore.LIGHTRED_EX}└──╼{Fore.LIGHTWHITE_EX} {datetime.utcnow().strftime('%H:%M:%S')}  Succes  {Fore.LIGHTRED_EX}{Fore.LIGHTGREEN_EX}{self.responce.status_code}")
			else:
				print(f"{Fore.LIGHTRED_EX}└──╼{Fore.LIGHTWHITE_EX} {datetime.utcnow().strftime('%H:%M:%S')}  Error  {Fore.LIGHTRED_EX}{self.responce.status_code}")		

class cfg(metaclass = FloodLogs):
	headers = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
	proxies = {'https':"176.31.111.139:80"}

if __name__ == "__main__":
	cfg(FloodLogs())
	input()