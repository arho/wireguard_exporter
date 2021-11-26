# Prometheus Wireguard Exporter
## Summary
Provides Information on currently active peers (active within the last 3 minutes) as well as TX and RX information of each peer per instance.
## Requirements
- python 3.9.x (Earlier versions might work)
- prometheus-client library
- wireguard-tools (as this exporter uses `wg` to gather metrics)
## Installation
### Using the install script:
- Clone the repository into a desired location, and run `install.sh` which handles the rest.
- Start the Service
- Profit.
### Manual Install:
- Clone the repository into a desired location.
- Copy the files in the `src` directory to your install path.
- Create a symlink from `exporter` to the location included in your `$PATH`.
- Copy the sample systemd unit file from `unit-file` directory to the required location and update it based on your configuration.
- Start the Service
- Profit.

## Metrics
| Metric       | Name                   | Labels                   |
|--------------|------------------------|--------------------------|
| Active Peers | `wg_active_peer_total` | `wginterface`            |
| Peers RX     | `wg_peer_rx_bytes`     | `wginterface` and `peer` |
| Peers TX     | `wg_peer_tx_bytes`     | `wginterface` and `peer` |