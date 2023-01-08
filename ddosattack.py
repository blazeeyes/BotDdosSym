import platform
import threading
import time
import logging, sys
import pathlib as pathlib
from distlib.compat import raw_input
import os
def a():
	os.system("wireshark")
def b():
	os.system("xterm -e \"sudo python slowloris.py\"")
def c():
	os.system("xterm -e \"sudo python synFlooding.py\"")
def d():
	os.system("xterm -e \"sudo wget https://inmon.com/products/sFlow-RT/sflow-rt.tar.gz\"")
	os.system("xterm -e \"sudo tar -xvzf sflow-rt.tar.gz\"")
	os.system("xterm -e \"sudo "+path+"/sflow-rt/get-app.sh sflow-rt browse-metrics\"")
	os.system("xterm -e \"sudo "+path+"/sflow-rt/get-app.sh sflow-rt browse-flows\"")
	os.system("xterm -e \"sudo "+path+"/sflow-rt/get-app.sh sflow-rt ddos-protect\"")
	file = pathlib.Path("sflow-rt.tar.gz")
	if file.exists():
		os.remove(file)
def e():
	os.system("xterm -e \"sudo "+path+"/sflow-rt/start.sh\"")
	os.system("xterm -e \"sudo systemctl restart sflow-rt\"")
def f():
	os.system("google-chrome --no-sandbox http://localhost:8008")
def clear():
	linux = 'clear'
	windows = 'cls'
	os.system([linux, windows][os.name == 'nt'])

logging.disable(sys.maxsize)
number = 1
data = ""
os.environ['TERM'] = 'xterm'
path = os. getcwd()

while number != '0':

	data += ' ----------------------------\n'
	if os.name == "nt":
		print(' [!] Please run the script on Linux Machine !')
		quit()
	elif os.name != "nt":
		data = (' ----------------------------\n')
		data += ' Hi ' + platform.uname()[1] + ' !\n'

	data += ' ----------------------------\n'
	data += ' Select option:\n'
	data += ' [1] Start Apache2\n'
	data += ' [2] Stop Apache2\n'
	data += ' [3] ReStart Apache2\n'
	data += ' [4] Open Localhost\n'
	data += ' [5] Ettercap Scanner IP Lan\n'
	data += ' [6] Scanner port target\n'
	data += ' [7] Scanner IP Lan\n'
	data += ' [8] Attack Slow Loris\n'
	data += ' [9] ICMP flooding\n'
	data += ' [A] Attack Ettercap with analyzing Wireshark\n'
	data += ' [B] Installation Grafana, Prometheus, Apache Exporter\n'
	data += ' [C] Launch service Remotely Triggered Black Hole\n'
	data += ' [D] Stop DDOS Attack by Remotely Triggered Black Hole (RTBH) Routing\n'
	data += ' [0] Exit\n'
	print(data)
	number = input(" Number~# ")
	if number == '1':
		print("\n [***] Please wait ...")
		os.system("sudo service apache2 start")
		print(" [I] Apache2 Service has been Started !\n")
		time.sleep(5)
		clear()
		data = ""
	elif number == '2':
		print('\n [***] Please wait ...')
		os.system("sudo service apache2 stop")
		print(" [O] Apache2 Service has been Stoped !\n")
		time.sleep(5)
		clear()
		data = ""
	elif number == '3':
		print('\n [***] Please wait ...')
		os.system("sudo service apach2 restart")
		print(" [R] Apache2 Service has been ReStarted !\n")
		time.sleep(5)
		clear()
		data = ""
	elif number == '4':
		print("\n [***] Please wait ...\n")
		print(" [O] Opening http://127.0.0.1 ...\n")
		os.system("firefox http://127.0.0.1")
		print(" Successfully !\n")
		time.sleep(5)
		clear()
		data = ""
	elif number == '5':
		print("\n Ettercap Scanner IP Lan ...\n")
		os.system("ifconfig")
		iface = raw_input("What interface to use (ie eth0) Press 'q' to stop precess ?  \n")
		print("ettercap -T -i " + iface)
		os.system("sudo ettercap -T -i " + iface)
		clear()
		data = ""
	elif number == '6':
		print("\n Scanner port target...\n")
		ipAdress = raw_input("What Ip address to use ?  => ")
		portRange = raw_input("What Range of port to scan ? =>")
		print("nmap " + ipAdress + " --top-ports " + portRange)
		os.system("nmap " + ipAdress + " --top-ports " + portRange)
		data = ""
	elif number == '7':
		print("\n Scanner IP Lan...\n")
		os.system("sudo python ifconfig.py")
		data = ""
	elif number == '8':
		print("\n [SlowLoris Attack ...\n")
		threading.Thread(target=a).start()
		threading.Thread(target=b).start()
		threading.Thread(target=d).start()
		print("\n [SlowLoris Attack ...\n")
		print("\033[H\033[J", end="")
		data = ""
	elif number == '9':
		print("\n [ICMP flooding ...\n")
		threading.Thread(target=a).start()
		threading.Thread(target=c).start()
		threading.Thread(target=d).start()
		print("\033[H\033[J", end="")
		data = ""
	elif number == 'A':
		print("\n [Attarck Ettercap with analyzing Wireshark  ...\n")
		os.system("python ettercapAttack.py")
		time.sleep(5)
		clear()
		data = ""
	elif number == 'B':
		print("\n [Installation monitoring ...\n")
		# update system package
		os.system("xterm -e \"sudo apt update && sudo apt install wget curl\"")
		# install nodejs & npm
		os.system("xterm -e \"sudo apt-get install -y nodejs\"")
		os.system("xterm -e \"sudo apt-get install -y npm\"")
		# install wireshark
		os.system("xterm -e \"sudo apt-get install -y wireshark\"")
		# install prometheus
		os.system("xterm -e \"tar -xvf prometheus-files.tar.gz\"")
		os.system("xterm -e \"sudo cp apache_exporter-*.linux-amd64/apache_exporter /usr/local/bin\"")
		os.system("sudo chmod +x /usr/local/bin/apache_exporter")
		os.system("sudo groupadd --system prometheus")
		os.system("sudo useradd -s /sbin/nologin --system -g prometheus prometheus")
		os.system("xterm -e \"sudo apt-get -y install daemonize\"")
		os.system("sudo systemctl daemon-reload")
		os.system("sudo systemctl start apache_exporter.service")
		os.system("sudo systemctl enable apache_exporter.service")
		os.system("sudo systemctl restart prometheus")
		os.system("xterm -e \"sudo apt-get install -y apt-transport-https software-properties-common\"")
		os.system("xterm -e \"wget -O - https://packages.grafana.com/gpg.key | sudo apt-key add -\"")
		os.system("xterm -e \"sudo add-apt-repository deb https://packages.grafana.com/enterprise/deb stable main\"")
		os.system("xterm -e \"sudo apt-get update\"")
		# install grafana-enterprise
		os.system("xterm -e \"sudo apt-get install -y grafana-enterprise\"")
		os.system("xterm -e \"sudo /bin/systemctl start grafana-server\"")
		os.system("sudo useradd --no-create-home --shell /bin/false prometheus")
		folder = pathlib.Path("/etc/prometheus")
		if not os.path.exists(folder):
			os.system("sudo mkdir /etc/prometheus")
		# install dashboards
		folder = pathlib.Path("/var/lib/grafana/dashboards")
		if not os.path.exists(folder):
			os.system("sudo mkdir /var/lib/grafana/dashboards")
		dashboards = "sudo cp "+path+"/dashboards/apache_rev1.json /var/lib/grafana/dashboards"
		os.system(dashboards)
		# install prometheus
		folder = pathlib.Path("/var/lib/prometheus")
		if not os.path.exists(folder):
			os.system("sudo mkdir /var/lib/prometheus")
		os.system("sudo chown prometheus:prometheus /etc/prometheus")
		os.system("sudo chown prometheus:prometheus /var/lib/prometheus")
		prometheusfiles = "sudo cp "+path+"/prometheus-files/prometheus /usr/local/bin/"
		os.system(prometheusfiles)
		promtool = "sudo cp "+path+"/prometheus-files/promtool /usr/local/bin/"
		os.system(promtool)
		os.system("sudo chown prometheus:prometheus /usr/local/bin/prometheus")
		os.system("sudo chown prometheus:prometheus /usr/local/bin/promtool")
		consoles = "sudo cp -r "+path+"/prometheus-files/consoles /etc/prometheus"
		os.system(consoles)
		consolelibraries = "sudo cp -r "+path+"/prometheus-files/console_libraries /etc/prometheus"
		os.system(consolelibraries)
		os.system("sudo chown -R prometheus:prometheus /etc/prometheus/consoles")
		os.system("sudo chown -R prometheus:prometheus /etc/prometheus/console_libraries")
		os.system("sudo chown prometheus:prometheus /etc/prometheus/prometheus.yml")
		os.system("sudo systemctl daemon-reload")
		prometheus_yml = "sudo cp -r "+path+"/monitoring/prometheus.yml /etc/prometheus/"
		os.system(prometheus_yml)
		prometheus_service = "sudo cp -r "+path+"/monitoring/prometheus.service /etc/systemd/system/"
		os.system(prometheus_service)
		# create apache_exporter
		apache_exporter = "sudo cp -r "+path+"/monitoring/apache_exporter /etc/sysconfig/"
		os.system(apache_exporter)
		apache_exporter_service = "sudo cp -r "+path+"/monitoring/apache_exporter.service /etc/systemd/system/"
		os.system(apache_exporter_service)
		# install chrome browser
		os.system("xterm -e \"wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb\"")
		os.system("xterm -e \"apt install ./google-chrome-stable_current_amd64.deb\"")
		print("[O] Opening http://localhost:3000 ...\n")
		os.system("google-chrome --no-sandbox http://localhost:3000/d/6_KsLxBmk/apache2?orgId=1&refresh=5s")
		file = pathlib.Path("google-chrome-stable_current_amd64.deb")
		if file.exists():
			os.remove(file)
		clear()
		data = ""
	elif number == 'C':
		print("\n Launch service Remotely Triggered Black Hole  ...\n")
		threading.Thread(target=e).start()
		clear()
		data = ""
	elif number == 'D':
		print("\n Stop DDOS Attack by Remotely Triggered Black Hole (RTBH) Routing  ...\n")
		threading.Thread(target=f).start()
		clear()
		data = ""
	elif number == '0':
		print('\n [+] Good Bye ' + platform.uname()[1] + ' !\n')
		quit()
	else:
		print("\n [X] Error !\n [!] Select this number: 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B or 0\n")
