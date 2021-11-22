# Functions for Gathering Users Using wg
import subprocess

def interface_names():
    return (((subprocess.check_output(['wg','show','interfaces'])).decode('utf-8')).split())

def gather_information(get_interfaces=interface_names()):
    # Get Interface Names
    get_interfaces = ((subprocess.check_output(['wg','show','interfaces'])).decode('utf-8')).split()
    # Get All Interface Metrics
    get_metrics = ((subprocess.check_output(['wg','show','all','dump'])).decode('utf-8')).split('\n')
    get_metrics.pop()
    interfaces = {interface:[] for interface in get_interfaces}
    for i in get_metrics:
        item = i.split('\t')
        if item[0] in list(interfaces.keys()):
            interfaces[item[0]].append(item)

    for j in interfaces:
        interfaces[j] = interfaces[j][1:]

    return interfaces
