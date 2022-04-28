ip=$1
ping $ip | while read pong; do echo "$(date): $pong"; done > ping_log.csv

