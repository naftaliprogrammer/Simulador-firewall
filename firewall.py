import random
def generate_random_ip():
    return f"192.168.1.{random.randint(0,20)}"


def check_firewall_rules(ip, rules):
    for rules_ip, acao in rules.items():
        if ip == rules_ip:
            return acao
    return "permitido"




def main():
    firewall_rules = {"192.168.1.1": "bloqueado",
                      "192.168.1.4": "bloqueado",
                      "192.168.1.13": "bloqueado"


    }
    for _ in range(12):
        ip_adress = generate_random_ip()
        acao = check_firewall_rules(ip_adress, firewall_rules)
        numero_aleatorio = random.randint(0, 999)
        print(f"IP {ip_adress}, Ação:{acao}, Aleatorio: {numero_aleatorio}")

main()