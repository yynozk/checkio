def checkio(data):
    def tob(ip):
        return "{:08b}{:08b}{:08b}{:08b}".format(*map(int, ip.split(".")))
    bins = list(map(tob, data))

    subnet = len(bins[0])-1
    for b in bins:
        for i in range(subnet+1, 0, -1):
            if bins[0].startswith(b[0:i]):
                break
            subnet = i-1

    ansbin = bins[0][0:subnet].ljust(32, "0")
    ip = [int(ansbin[i*8:i*8+8], 2) for i in range(4)]
    return ".".join(map(str, ip)) + "/" + str(subnet)
