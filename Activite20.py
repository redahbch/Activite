adresses_ip = ["192.168.0.1", "10.0.0.1", "172.16.0.1", "200.100.50.1", "169.254.0.1"]

print(adresses_ip[0])
print(adresses_ip[-1])
print(adresses_ip[2])

adresses_ip.append("172.31.0.1")
adresses_ip.remove("200.100.50.1")

print(len(adresses_ip))
print("192.168.0.1" in adresses_ip)
print("Classe A")

adresses_ip.sort()
print(adresses_ip)

def est_classe_C(ip):
    return 192 <= int(ip.split('.')[0]) <= 223

print(all(est_classe_C(ip) for ip in adresses_ip))
publiques = [ip for ip in adresses_ip if not ip.startswith(("10.", "192.168.", "172.", "169.254."))]
print(len(publiques))
