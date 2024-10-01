## Lab 11 : Mise en œuvre de la surveillance et des alertes Azure

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

1. **Configurer Azure Monitor pour collecter les métriques et les journaux** :
   - Allez dans **Azure Monitor** et activez la collecte des métriques.

   ![Configurer Azure Monitor](images/configurer-azure-monitor.png)

2. **Créer des alertes basées sur les métriques des ressources** :
   - Créez des alertes pour être notifié lorsque certaines conditions sont remplies.

   ![Créer alertes](images/creer-alertes.png)

3. **Visualiser les données à l'aide des tableaux de bord Azure** :
   - Créez des tableaux de bord personnalisés pour visualiser les métriques importantes.

   ![Visualiser données](images/visualiser-donnees.png)

4. **Mettre en œuvre des groupes d'action pour les notifications d'alerte** :
   - Configurez les notifications pour les alertes afin d'informer les utilisateurs.

   ![Configurer groupes d'action](images/configurer-groupes-action.png)

---