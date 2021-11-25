#!/bin/bash
# Install the Exporter
mkdir /opt/wireguard_exporter
cp $(pwd)/src/* /opt/wireguard_exporter
cd src/
ln -s $(pwd)/exporter /usr/local/bin/wireguard_exporter

# Install the unit file
cd ..
cp $(pwd)/unit-file/wireguard-exporter.service /usr/lib/systemd/system/
systemctl daemon-reload # Adding a new file doesn't need the daemon to be reloaded. Just for good luck ;)
