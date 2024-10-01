
## Lab 12 : Utilisation des modèles Azure Resource Manager (ARM)

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

1. **Écrire un modèle ARM pour déployer une application multi-niveaux** :
   - Créez un fichier JSON pour définir votre modèle.

   ![Écrire modèle ARM](images/ecrire-modele-arm.png)

2. **Paramétrer le modèle pour la réutilisabilité** :
   - Ajoutez des paramètres pour permettre la personnalisation lors du déploiement.

   ![Paramétrer modèle ARM](images/parametrer-modele-arm.png)

3. **Déployer des ressources en utilisant le modèle via Azure CLI** :
   - Utilisez la commande suivante pour déployer :
     ```bash
     az deployment group create --resource-group <nom_du_groupe> --template-file <chemin_du_fichier_template>
     ```

   ![Déployer via CLI](images/deployer-via-cli.png)

4. **Valider et résoudre les problèmes de déploiement** :
   - Vérifiez les erreurs de déploiement et corrigez les problèmes.

   ![Résoudre problèmes](images/resoudre-problemes.png)

---