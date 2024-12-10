import requests, time, os, pyfiglet
from colorama import Fore, Style, init
GREEN=f'{Fore.GREEN}{Style.BRIGHT}'
RED=f'{Fore.RED}{Style.BRIGHT}'
WHITE=f'{Fore.WHITE}{Style.BRIGHT}'

init(autoreset=True)

print(f"{RED}" + pyfiglet.figlet_format(" Pyfuzzer"))

print(f' INTRODUZCA LA URL SIN EL (/) AL FINAL\n DE ESTA FORMA: https://www.google.com\n')
url = input(' INTRODUZCA LA URL => ')
n=1 ; found=[]

foundx = 'links_encontrados.txt'

if os.path.exists(foundx):
	os.remove(foundx)
wordlist = input(' INTRODUZCA LA RUTA DEL DICCIONARIO => ')
print("")
with open(wordlist, 'r') as f:
	v = f.readlines()
	for r in v:
		rr = r.replace('\n', '')
		end = rr[-1]
		if end == '/':
			rr = rr[:-1]
		link = f"{url}/{rr}"
		try:
			r = requests.head(link, allow_redirects=True)
			st = str(r.status_code)[0:2]
			if int(st) == 20:
				print(f" {WHITE}[{n}]{Style.RESET_ALL} FOUND = {GREEN}{link}")
				found.append(f'{link}')
			else:
				print(f" {RED}NOT FOUND = {WHITE}[{n}]{Style.RESET_ALL} ")
			n=n+1
		except:
			if n == 1:
				print(" COMPRUEBA LA CONEXION")
				break
			else:
				n=1
				print("\n LINKS ENCONTRADOS => \n")
				for i in found:
					w=f"[{n}] {i}\n"
					print(f" {WHITE}[{n}] {GREEN}{i}")
					with open('links_encontrados.txt', 'a') as f:
						f.write(w)
						f.close()
					n=n+1
				print("\n HAZ PRESIONADO [CTRL + C]")
				input(" PRESIONA ENTER PARA SALIR...")