
## Lab 20 : Déploiement d'Azure Kubernetes Service (AKS)

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

1. **Configurer un cluster AKS** :
   - Allez dans **Kubernetes services**, puis cliquez sur **Créer**.

   ![Configurer cluster AKS](images/configurer-cluster-aks.png)

2. **Déployer une application conteneurisée à l'aide de manifests Kubernetes** :
   - Créez vos manifests et déployez-les.

   ![Déployer application](images/deployer-application.png)

3. **Échelonner les applications et gérer les pods** :
   - Utilisez les commandes Kubernetes pour gérer les ressources.

   ![Gérer pods](images/gerer-pods.png)

4. **Mettre en œuvre des politiques réseau pour la communication des pods** :
   - Configurez les politiques réseau pour sécuriser les communications.

   ![Configurer politiques réseau](images/configurer-politiques-reseau.png)