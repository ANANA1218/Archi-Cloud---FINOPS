## Lab 16 : Gestion du contrôle d'accès basé sur les rôles (RBAC)

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

1. **Attribuer des rôles intégrés aux utilisateurs et groupes** :
   - Dans Azure AD, attribuez des rôles aux utilisateurs.

   ![Attribuer des rôles](images/attribuer-roles.png)

2. **Créer des rôles personnalisés avec des autorisations spécifiques** :
   - Définissez des rôles personnalisés pour un accès spécifique.

   ![Créer rôles personnalisés](images/creer-roles-personnalises.png)

3. **Tester les niveaux d'accès pour différents rôles** :
   - Vérifiez les autorisations pour chaque rôle.

   ![Tester accès](images/tester-acces.png)

4.

 **Auditer l'accès à l'aide des journaux d'activité** :
   - Consultez les journaux d'activité pour suivre les accès.

   ![Auditer accès](images/auditer-acces.png)

---