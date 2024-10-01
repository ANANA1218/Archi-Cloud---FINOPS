
## Lab 9 : Mise en œuvre de l'équilibreur de charge Azure et du Traffic Manager

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

1. **Déployer un équilibreur de charge Azure pour distribuer le trafic entre les VMs** :
   - Allez dans **Équilibreurs de charge**, puis cliquez sur **Créer**.

   ![Créer un équilibreur de charge](images/creer-equilibreur-charge.png)

2. **Configurer les sondes de santé et les règles de répartition de charge** :
   - Définissez des sondes de santé pour surveiller l'état des VMs.

   ![Configurer sondes de santé](images/configurer-sondes.png)

3. **Configurer Azure Traffic Manager pour le routage du trafic basé sur DNS** :
   - Créez une ressource **Traffic Manager** et configurez les profils.

   ![Créer Traffic Manager](images/creer-traffic-manager.png)

4. **Tester les scénarios de basculement** :
   - Simulez des échecs pour vérifier le comportement de l'équilibreur de charge.

   ![Tester basculement](images/tester-basculement.png)

---