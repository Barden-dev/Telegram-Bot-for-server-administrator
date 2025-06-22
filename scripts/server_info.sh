#!/bin/bash
while true; do
  GLANCES=$(glances --stdout cpu.total,mem.used.percent,mem.used,mem.free | tr '\n' ',' | sed 's/,$//')
  TEMP=$(sensors | grep 'Core 0' | awk '{print $3}' | tr -d '+°C')
  echo "${GLANCES},cpu_temp: ${TEMP}"
# >> /root/TGBot/server_info.txt
  sleep 1
done
