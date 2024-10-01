
## Lab 10 : Configuration de la sauvegarde Azure et des services de récupération

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

1. **Créer un coffre de services de récupération** :
   - Allez dans **Coffres de services de récupération**, puis cliquez sur **Créer**.

   ![Créer coffre de récupération](images/creer-coffre-recuperation.png)

2. **Configurer la sauvegarde pour les VMs et Azure Files** :
   - Ajoutez les éléments que vous souhaitez sauvegarder dans le coffre.

   ![Configurer sauvegarde](images/configurer-sauvegarde.png)

3. **Effectuer une opération de sauvegarde et de restauration** :
   - Lancez une sauvegarde manuelle et vérifiez la restauration.

   ![Sauvegarde et restauration](images/sauvegarde-restauration.png)

4. **Mettre en œuvre des politiques de sauvegarde et de rétention** :
   - Configurez les politiques de sauvegarde selon vos besoins.

   ![Configurer politiques](images/configurer-politiques-sauvegarde.png)

---