import os
import pathlib
import platform
import time

from distlib.compat import raw_input


def clear():
	linux = 'clear'
	windows = 'cls'
	os.system([linux, windows][os.name == 'nt'])


number = 1
data = ""
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
	data += ' [0] Exit\n'
	print(data)
	number = input(" Number~# ")
	if number == '1':
		print("\n [***] Please wait ...")
		os.system("service apache2 start")
		print(" [I] Apache2 Service has been Started !\n")
		time.sleep(5)
		clear()
		data = ""
	elif number == '2':
		print('\n [***] Please wait ...')
		os.system("service apache2 stop")
		print(" [O] Apache2 Service has been Stoped !\n")
		time.sleep(5)
		clear()
		data = ""
	elif number == '3':
		print('\n [***] Please wait ...')
		os.system("service apach2 restart")
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
		os.system("ettercap -T -i " + iface)
		clear()
		data = ""
	elif number == '6':
		print("\n Scanner port target...\n")
		ipAdress = raw_input("What Ip address to use ?  \n")
		portRange = raw_input("What Range of port to scan ? \n")
		print("nmap " + ipAdress + " --top-ports " + portRange)
		os.system("nmap " + ipAdress + " --top-ports " + portRange)
		data = ""
	elif number == '7':
		print("\n Scanner IP Lan...\n")
		os.system("python ifconfig.py")
		data = ""
	elif number == '8':
		print("\n [SlowLoris Attack ...\n")
		os.system("python slowloris.py")
		time.sleep(5)
		clear()
		data = ""
	elif number == '9':
		print("\n [ICMP flooding ...\n")
		os.system("python synFlooding.py")
		time.sleep(5)
		clear()
		data = ""
	elif number == 'A':
		print("\n [Attarck Ettercap with analyzing Wireshark  ...\n")
		os.system("python ettercapAttack.py")
		time.sleep(5)
		clear()
		data = ""
	elif number == 'B':
		print("\n [Installation monitoring ...\n")
		path = os. getcwd()

		os.system("sudo apt update && sudo apt install wget curl")
		os.system("sudo apt-get install wireshark")
		os.system("tar -xvf prometheus-files.tar.gz")
		os.system("sudo cp apache_exporter-*.linux-amd64/apache_exporter /usr/local/bin")
		os.system("sudo chmod +x /usr/local/bin/apache_exporter")
		os.system("sudo groupadd --system prometheus")
		os.system("sudo useradd -s /sbin/nologin --system -g prometheus prometheus")
		os.system("sudo apt-get -y install daemonize")
		os.system("sudo systemctl daemon-reload")
		os.system("sudo systemctl start apache_exporter.service")
		os.system("sudo systemctl enable apache_exporter.service")
		os.system("sudo /etc/init.d/apache_exporter start")
		os.system("sudo systemctl restart prometheus")
		os.system("sudo apt-get install apt-transport-https software-properties-common")
		os.system("wget -O - https://packages.grafana.com/gpg.key | sudo apt-key add -")
		os.system("sudo add-apt-repository deb https://packages.grafana.com/enterprise/deb stable main")
		os.system("sudo apt-get update")
		os.system("sudo apt-get install grafana-enterprise")
		os.system("sudo /bin/systemctl start grafana-server")
		os.system("sudo apt-get update -y")
		os.system("mv prometheus-2.41.0.linux-amd64 prometheus-files")
		os.system("sudo useradd --no-create-home --shell /bin/false prometheus")
		os.system("sudo mkdir /etc/prometheus")
		os.system("sudo mkdir /var/lib/grafana/dashboards")
		dashboards = "sudo cp "+path+"/dashboards/apache_rev1.json /var/lib/grafana/dashboards"
		os.system(dashboards)
		dashboards = "sudo cp "+path+"/dashboards/apache_rev7.json /var/lib/grafana/dashboards"
		os.system(dashboards)
		os.system("sudo mkdir /var/lib/prometheus")
		os.system("sudo chown prometheus:prometheus /etc/prometheus")
		os.system("sudo chown prometheus:prometheus /var/lib/prometheus")
		prometheusfiles = "sudo cp "+path+"/prometheus-files/prometheus /usr/local/bin/"
		os.system(prometheusfiles)
		promtool = "sudo cp "+path+"/prometheus-files/promtool /usr/local/bin/"
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
		apache_exporter = "sudo cp -r "+path+"/monitoring/apache_exporter /etc/sysconfig/"
		os.system(apache_exporter)
		apache_exporter_service = "sudo cp -r "+path+"/monitoring/apache_exporter.service /etc/systemd/system/"
		os.system(apache_exporter_service)
		os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
		os.system("apt install ./google-chrome-stable_current_amd64.deb")
		os.system("sudo systemctl restart grafana-server")
		print("[O] Opening http://localhost:3000 ...\n")
		os.system("google-chrome --no-sandbox http://localhost:3000")
		file = pathlib.Path("google-chrome-stable_current_amd64.deb")
		if file.exists():
			os.remove(file)
		clear()
		data = ""
	elif number == 0:
		print('\n [+] Good Bye ' + platform.uname()[1] + ' !\n')
		quit()
	else:
		print("\n [X] Error !\n [!] Select this number: 1, 2, 3, 4, 5, 6 or 0\n")
