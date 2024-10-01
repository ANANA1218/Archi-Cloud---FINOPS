
## Lab 14 : Configuration d'Azure DNS et de domaines personnalisés

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

1. **Créer une zone DNS Azure** :
   - Allez dans **Zones DNS**, puis cliquez sur **Créer**.

   ![Créer zone DNS](images/creer-zone-dns.png)

2. **Gérer les enregistrements DNS pour un domaine personnalisé** :
   - Ajoutez des enregistrements pour votre domaine.

   ![Gérer enregistrements DNS](images/gerer-enregistrements-dns.png)

3. **Configurer la vérification de domaine et le mappage pour les services Azure** :
   - Suivez les étapes pour vérifier votre domaine.

   ![Configurer vérification de domaine](images/configurer-verification.png)

4. **Mettre en œuvre des alias DNS (CNAME) et des ensembles d'enregistrements** :
   - Configurez les alias pour faciliter l'accès à vos services.

   ![Mettre en œuvre des alias](images/implémenter-alias.png)

---