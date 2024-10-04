
## Lab 12 : Utilisation des modèles Azure Resource Manager (ARM)

## Prérequis

- Un compte Azure actif.
- Accès au portail Azure ([https://portal.azure.com](https://portal.azure.com)).
- Droits suffisants pour créer des ressources dans Azure.

---

## Table des matières

1. **Écrire un modèle ARM pour déployer une application multi-niveaux**
2. **Paramétrer le modèle pour la réutilisabilité** 
3. **Déployer des ressources en utilisant le modèle via Azure CLI**
4. **Valider et résoudre les problèmes de déploiement**

---


### Étapes à suivre

1. **Écrire un modèle ARM pour déployer une application multi-niveaux** :
   - Créez un fichier JSON pour définir votre modèle.

2. **Paramétrer le modèle pour la réutilisabilité** :
   - Ajoutez des paramètres pour permettre la personnalisation lors du déploiement.

3. **Déployer des ressources en utilisant le modèle via Azure CLI** :
   - Utilisez la commande suivante pour déployer :
     ```bash
     az deployment group create --resource-group <nom_du_groupe> --template-file <chemin_du_fichier_template>
     ```

 ![alt text](<deploy de mon arm.json.png>)

4. **Valider et résoudre les problèmes de déploiement** :
   - Vérifiez les erreurs de déploiement et corrigez les problèmes.


---