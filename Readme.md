# README : Labs Azure

Ce document présente les labs effectués sur Azure, incluant la configuration de services et l'utilisation d'API. Chaque section détaille les étapes nécessaires pour mettre en œuvre divers services Azure.

## Table des matières

1. [Lab 1 : Connexion et configuration des machines virtuelles (VM)](#lab-1)
2. [Lab 2 : Mise en œuvre des réseaux virtuels Azure](#lab-2)
3. [Lab 3 : Déploiement d'applications Web Azure App Service](#lab-3)
4. [Lab 4 : Gestion des comptes de stockage Azure et des blobs](#lab-4)
5. [Lab 5 : Mise en œuvre des bases de données Azure SQL](#lab-5)
6. [Lab 6 : Configuration d'Azure Active Directory (Azure AD)](#lab-6)
7. [Lab 7 : Mise en œuvre des fonctions Azure](#lab-7)
8. [Lab 8 : Utilisation des services cognitifs Azure](#lab-8)
9. [Lab 8 : Mise en œuvre de l'équilibreur de charge Azure et du Traffic Manager](#lab-9)
10. [Lab 10 : Configuration de la sauvegarde Azure et des services de récupération](#lab-10)
11. [Lab 11 : Mise en œuvre de la surveillance et des alertes Azure](#lab-11)
12. [Lab 12 : Utilisation des modèles Azure Resource Manager (ARM)](#lab-12)
13. [Lab 13 : Mise en œuvre d'Azure Key Vault](#lab-13)

---

## Lab 1 : Connexion et configuration des machines virtuelles (VM)

### Étapes

1. **Connexion aux VM via RDP et SSH** :
   - Utiliser des clés privées pour se connecter.
   - Vérifier les permissions des fichiers de clés.


## Lab 2 : Mise en œuvre des réseaux virtuels Azure

### Étapes

1. **Créer un Réseau Virtuel (VNet) avec plusieurs sous-réseaux**.
2. **Configurer les Groupes de Sécurité Réseau (NSG)** pour contrôler le trafic entrant et sortant.
3. **Déployer des VMs dans des sous-réseaux spécifiques**.
4. **Configurer le peering VNet entre deux VNets**.

---

## Lab 3 : Déploiement d'applications Web Azure App Service

### Étapes

1. **Créer un plan Azure App Service**.
2. **Déployer une application web**.
3. **Configurer des domaines personnalisés et des certificats SSL**.
4. **Mettre en œuvre des slots de déploiement pour la mise en scène et la production**.

---

## Lab 4 : Gestion des comptes de stockage Azure et des blobs

### Étapes

1. **Créer un Compte de Stockage avec différentes options de réplication**.
2. **Télécharger et gérer des blobs via le Portail Azure et Azure CLI**.
3. **Configurer des Signatures d'Accès Partagé (SAS)** pour un accès sécurisé.
4. **Mettre en œuvre des politiques de gestion du cycle de vie**.

---

## Lab 5 : Mise en œuvre des bases de données Azure SQL

### Étapes

1. **Déployer une instance de base de données Azure SQL**.
2. **Configurer les paramètres de pare-feu pour permettre l'accès client**.
3. **Importer des données dans la base de données**.
4. **Mettre en œuvre la géo-réplication pour la haute disponibilité**.

---

## Lab 6 : Configuration d'Azure Active Directory (Azure AD)

### Étapes

1. **Créer et gérer des utilisateurs et groupes dans Azure AD**.
2. **Configurer l'authentification multifacteur (MFA)** pour les utilisateurs.
3. **Configurer les enregistrements d'applications et les principes de service**.
4. **Mettre en œuvre des politiques d'accès conditionnel**.

---

## Lab 7 : Mise en œuvre des fonctions Azure

### Étapes

1. **Créer une application de fonction Azure**.
2. **Développer une fonction sans serveur déclenchée par une requête HTTP**.
3. **Intégrer la fonction avec Azure Storage ou Azure Queue**.
4. **Surveiller les performances et les journaux de la fonction**.

---

## Lab 8 : Utilisation des services cognitifs Azure

### Étapes

1. **Créer une ressource de services cognitifs pour la traduction**.
2. **Développer une application qui utilise l'API de Traduction de texte**.
3. **Tester l'application pour traduire du texte**.
4. **Surveiller l'utilisation de l'API et gérer les clés d'accès**.


---
## Lab 9 : Mise en œuvre de l'équilibreur de charge Azure et du Traffic Manager

### Étapes

1. **Déployer un équilibreur de charge Azure pour distribuer le trafic entre les VMs**.
2. **Configurer les sondes de santé et les règles de répartition de charge**.
3. **Configurer Azure Traffic Manager pour le routage du trafic basé sur DNS**.
4. **Tester les scénarios de basculement**.

---
## Lab 10 : Configuration de la sauvegarde Azure et des services de récupération

### Étapes

1. **Créer un coffre de services de récupération**
2. **Configurer la sauvegarde pour les VMs et Azure Files**
3. **Effectuer une opération de sauvegarde et de restauration**
4. **Mettre en œuvre des politiques de sauvegarde et de rétention**

---
## Lab 11 : Mise en œuvre de la surveillance et des alertes Azure

### Étapes

1. **Configurer Azure Monitor pour collecter les métriques et les journaux**
2. **Créer des alertes basées sur les métriques des ressources**
3. **Visualiser les données à l'aide des tableaux de bord Azure**
4. **Mettre en œuvre des groupes d'action pour les notifications d'alerte** 

---

## Lab 12 : Utilisation des modèles Azure Resource Manager (ARM)

### Étapes

1. **Écrire un modèle ARM pour déployer une application multi-niveaux**
2. **Paramétrer le modèle pour la réutilisabilité** 
3. **Déployer des ressources en utilisant le modèle via Azure CLI**
4. **Valider et résoudre les problèmes de déploiement**

---

## Lab 12 : Mise en œuvre d'Azure Key Vault

### Étapes

1. **Créer un Azure Key Vault**
2. **Stocker et récupérer des secrets, clés et certificats** 
3. **Intégrer Key Vault avec une application pour la gestion des secrets**
4. **Configurer des politiques d'accès et de surveillance**
5. **Utiliser une de vos clés dans une application** 

---