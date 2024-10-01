## Lab 6 : Configuration d'Azure Active Directory (Azure AD)

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

1. **Créer et gérer des utilisateurs et groupes dans Azure AD** :
   - Allez dans **Azure Active Directory**, puis **Utilisateurs** ou **Groupes** pour ajouter de nouveaux utilisateurs ou groupes.

   ![Gérer utilisateurs](images/gerer-utilisateurs.png)

2. **Configurer l'authentification multifacteur (MFA) pour les utilisateurs** :
   - Dans les paramètres de sécurité, activez la MFA.

   ![Configurer MFA](images/configurer-mfa.png)

3. **Configurer les enregistrements d'applications et les principaux de service** :
   - Allez dans **Enregistrements d'applications**, puis créez un nouvel enregistrement.

   ![Enregistrer une application](images/enregistrer-application.png)

4. **Mettre en œuvre des politiques d'accès conditionnel** :
   - Configurez les règles d'accès conditionnel pour renforcer la sécurité.

   ![Configurer accès conditionnel](images/acces-conditionnel.png)

---