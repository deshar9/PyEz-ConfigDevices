from jnpr.junos import Device
from jnpr.junos.utils.config import Config

USER = "deshar"
PW = "9miraihe"
CONFIG_FILE = 'config.txt'
CONFIG_DATA = {
    'dns_server': '8.8.8.8',
    'ntp_server': '24.56.178.140',
}

def config_devices(devices='routers.txt'):
    with open(devices, 'r') as f:
        routers = f.readlines()
        routers = [x.strip() for x in routers]

        for router in routers:
            dev = Device(host=router, user=USER, password=PW).open()
            with Config(dev) as cu:
                cu.load(template_path=CONFIG_FILE, template_vars=CONFIG_DATA, format='set', merge=True)
                cu.commit(timeout=30)
                print("Committing the configuration on device: {}".format(router))
            dev.close()

if __name__ == "__main__":
    config_devices()
