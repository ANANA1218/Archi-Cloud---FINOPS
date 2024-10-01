## Lab 7 : Mise en œuvre des fonctions Azure

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

1. **Créer une application de fonction Azure** :
   - Allez dans **Fonctions Azure**, puis cliquez sur **Créer**.

   ![Créer une fonction](images/creer-fonction.png)

2. **Développer une fonction sans serveur déclenchée par une requête HTTP** :
   - Créez une nouvelle fonction et sélectionnez le déclencheur HTTP.

   ![Développer une fonction HTTP](images/developper-fonction-http.png)

3. **Intégrer la fonction avec Azure Storage ou Azure Queue** :
   - Configurez les liaisons pour connecter votre fonction à d'autres services Azure.

   ![Intégrer avec Azure Storage](images/integrer-azure-storage.png)

4. **Surveiller les performances et les journaux de la fonction** :
   - Utilisez **Azure Monitor** pour visualiser les performances et les journaux.

  

 ![Surveiller la fonction](images/surveiller-fonction.png)

---