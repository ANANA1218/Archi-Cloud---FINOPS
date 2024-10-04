## Lab 15 : Mise en œuvre d'Azure DevOps pour les pipelines CI/CD

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

1. **Configurer une organisation et un projet Azure DevOps** :
   - Accédez à Azure DevOps et créez une nouvelle organisation et un projet.

   ![Configurer Azure DevOps](images/configurer-azure-devops.png)

2. **Créer un dépôt Git et valider du code** :
   - Créez un nouveau dépôt dans votre projet et téléversez votre code.

   ![Créer un dépôt Git](images/creer-depot-git.png)

3. **Configurer un pipeline CI pour construire l'application** :
   - Créez un pipeline dans Azure DevOps pour automatiser la construction.

   ![Configurer pipeline CI](images/configurer-pipeline-ci.png)

4. **Configurer un pipeline CD pour déployer un modèle d'application dans Azure App Service** :
   - Créez un pipeline de déploiement pour publier votre application.

   ![Configurer pipeline CD](images/configurer-pipeline-cd.png)

---