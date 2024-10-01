
## Lab 19 : Mise en œuvre d'Azure Cosmos DB

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

1. **Créer un compte Cosmos DB avec une API choisie (SQL, MongoDB, etc.)** :
   - Allez dans **Cosmos DB** et créez un compte.

   ![Créer compte Cosmos DB](images/creer-compte-cosmos-db.png)

2. **Insérer et interroger des données à l'aide de l'Explorateur de données** :
   - Utilisez l'Explorateur pour ajouter et interroger vos données.

   ![Insérer données](images/insérer-données.png)

3. **Configurer le débit et le partitionnement** :
   - Définissez les paramètres de débit pour vos besoins.

   ![Configurer débit](images/configurer-debit.png)

4. **Mettre en œuvre la distribution mondiale** :
   - Activez la distribution dans plusieurs régions.

   ![Distribution mondiale](images/distribution-mondiale.png)

---