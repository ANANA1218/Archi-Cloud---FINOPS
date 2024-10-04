# Guide : Installation de logiciels et prise d'instantanés sur une machine virtuelle Azure

Ce guide décrit les étapes pour :
1. Créer une connexion SSH ou RDP à une VM Azure.
2. Installer des logiciels sur une VM (Linux ou Windows).
3. Prendre des instantanés (snapshots) des disques de la VM via le portail Azure.

## Prérequis
- Un compte Azure actif.
- Une machine virtuelle Azure (Linux ou Windows) en cours d'exécution.
- Une clé privée (.pem) pour les connexions SSH si vous utilisez une VM Linux.
- Les informations de connexion (adresse IP publique, nom d'utilisateur et mot de passe) pour la VM.
![alt text](<creation de la vm.png>)
![alt text](<creation de la vm pt2.png>)
---

## Table des matières

1. **Connexion à la VM**
2. **Prendre un instantané (snapshot) via le Portail Azure**
3. **Mettre en œuvre des groupes d'action pour les notifications d'alerte**


## Étape 1 : Connexion à la VM

### Connexion à une VM Linux (via SSH)

1. Ouvrez un terminal sur votre machine locale.
2. Exécutez la commande suivante pour vous connecter à la VM en utilisant votre clé privée :
   ```bash
   ssh -i /chemin/vers/votre_cle_privee.pem utilisateur@adresse-ip-publique
   ```
   Par exemple :
   ```bash
   ssh -i air.pem azure@40.0.100.0
   ```

   > Remarque : Assurez-vous que les permissions sur votre clé privée sont correctes. Utilisez la commande `chmod 600 air.pem` si nécessaire.
![alt text](<Connexion à la machine vituelle.png>)
---

## Étape 2 : Prendre un instantané (snapshot) via le Portail Azure

1. Accédez au **Portail Azure** : [https://portal.azure.com](https://portal.azure.com)
2. **Accédez à votre machine virtuelle** :
   - Dans le menu de gauche, cliquez sur **"Machines virtuelles"**.
   - Sélectionnez la VM concernée.

3. **Arrêter la VM** avant de prendre un instantané :
   - Cliquez sur **"Arrêter"** pour éviter des problèmes avec l'instantané d'une machine active.

4. **Créer un instantané** :
   - Dans le menu de la VM, sélectionnez **"Disques"**.
   - Cliquez sur le disque principal.
   - Sélectionnez **"Instantanés"** (Snapshots) et cliquez sur **"Créer un instantané"**.
   - Donnez un nom à l'instantané, choisissez le stockage, puis cliquez sur **"Créer"**.
![alt text](<creation du snapshot.png>)
![alt text](<creation du snapshot pt 2.png>)
---

## Étape 3 : Redémarrer la VM

Après avoir pris l'instantané, vous pouvez redémarrer la VM :

1. Retournez dans la section **"Vue d'ensemble"** de la VM dans le portail Azure.
2. Cliquez sur **"Démarrer"**.

---



