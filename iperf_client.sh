iperf -V -c fe80::9683:c4ff:fe10:23b7%wlan0  -i 1 -u -b 100M -t 10 -l 20000 -m | tee iperf.txt
