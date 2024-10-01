## Lab 5 : Mise en œuvre des bases de données Azure SQL

---

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

1. **Déployer une instance de base de données Azure SQL** :
   - Allez dans **Bases de données SQL**, cliquez sur **Créer**.
   - Remplissez les informations requises.

   ![Créer une base de données SQL](images/creer-base-de-donnees-sql.png)

2. **Configurer les paramètres de pare-feu pour permettre l'accès aux clients** :
   - Dans les paramètres de la base de données, ajoutez les adresses IP autorisées.

   ![Configurer pare-feu](images/configurer-pare-feu.png)

3. **Importer des données dans la base de données** :
   - Utilisez l'outil **Azure Data Studio** ou **SQL Server Management Studio** pour importer vos données.

   ![Importer des données](images/importer-donnees.png)

4. **Mettre en œuvre la géo-réplication pour la haute disponibilité** :
   - Dans les paramètres de la base de données, activez la géo-réplication.

   ![Géo-réplication](images/geo-replication.png)

---
