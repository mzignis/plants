import network


def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('FIBERMAX_R104P072411', '')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())


if __name__ == '__main__':
    pass
