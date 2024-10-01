
## Lab 13 : Mise en œuvre d'Azure Key Vault

## Prérequis

- Un compte Azure actif.
- Accès au portail Azure ([https://portal.azure.com](https://portal.azure.com)).
- Droits suffisants pour créer des ressources dans Azure.

---

## Table des matières

1. [Créer un réseau virtuel (VNet) avec plusieurs sous-réseaux](#etape-1-créer-un-réseau-virtuel-vnet-avec-plusieurs-sous-réseaux)
2. [Configurer les Groupes de Sécurité Réseau (NSG)](#etape-2-configurer-les-groupes-de-sécurité-réseau-nsg)
3. [Déployer des machines virtuelles dans les sous-réseaux](#etape-3-déployer-des-machines-virtuelles-dans-les-sous-réseaux)
4. [Configurer le peering entre deux VNets](#etape-4-configurer-le-peering-entre-deux-vnets)

---


### Étapes à suivre

1. **Créer un Azure Key Vault** :
   - Allez dans **Key Vaults**, puis cliquez sur **Créer**.

   ![Créer Key Vault](images/creer-key-vault.png)

2. **Stocker et récupérer des secrets, clés et certificats** :
   - Ajoutez des secrets et configurez les accès.

   ![Stocker secrets](images/stocker-secrets.png)

3. **Intégrer Key Vault avec une application pour la gestion des secrets** :
   - Configurez votre application pour utiliser le Key Vault.

   ![Intégrer Key Vault](images/integrer-key-vault.png)

4. **Configurer des politiques d'accès et de surveillance** :
   - Définissez des politiques d'accès pour contrôler qui peut accéder à vos secrets.

   ![Configurer politiques accès](images/configurer-politiques-acces.png)

5. **Utiliser une de vos clés dans une application** :
   - Développez votre application pour récupérer les clés du Key Vault.

   ![Utiliser clé dans application](images/utiliser-cle.png)

---