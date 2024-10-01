
## Lab 18 : Configuration d'Azure Virtual Desktop

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

1. **Configurer l'environnement Azure Virtual Desktop** :
   - Accédez à Azure Virtual Desktop et créez un environnement.

   ![Configurer Virtual Desktop](images/configurer-virtual-desktop.png)

2. **Configurer des pools d'hôtes, des hôtes de session et des espaces de travail** :
   - Créez les composants nécessaires pour votre environnement.

   ![Configurer pools d'hôtes](images/configurer-pools.png)

3. **Publier des applications de bureau à distance** :
   - Définissez les applications accessibles aux utilisateurs.

   ![Publier applications](images/publier-applications.png)

4. **Se connecter aux bureaux virtuels en tant qu'utilisateur** :
   - Utilisez un client pour vous connecter à votre bureau virtuel.

   ![Se connecter](images/se-connecter.png)

---