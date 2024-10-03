
## Lab 10 : Configuration de la sauvegarde Azure et des services de récupération

## Prérequis

- Un compte Azure actif.
- Accès au portail Azure ([https://portal.azure.com](https://portal.azure.com)).
- Droits suffisants pour créer des ressources dans Azure.

---

## Table des matières

1. Créer un coffre de services de récupération
2. Configurer la sauvegarde pour les VMs et Azure Files
3. Effectuer une opération de sauvegarde et de restauration
4. Mettre en œuvre des politiques de sauvegarde et de rétention
---


### Étapes à suivre

1. **Créer un coffre de services de récupération** :
   - Allez dans **Coffres de services de récupération**, puis cliquez sur **Créer**.
![alt text](<création du coffre recovery Services .png>)
![alt text](<création de mon compte de stockage.png>)
2. **Configurer la sauvegarde pour les VMs et Azure Files** :
   - Ajoutez les éléments que vous souhaitez sauvegarder dans le coffre.
![alt text](<configuration de la sauvegarde.png>)
![alt text](<coffre sauvegarde.png>)
![alt text](<coffre sauvegarde pt 2.png>)

3. **Effectuer une opération de sauvegarde et de restauration** :
   - Lancez une sauvegarde manuelle et vérifiez la restauration.

  ![alt text](<sauvegarde du coffre sur la vm.png>)
  ![alt text](<partage de fichier dans le compte de stockage pt 2 .png>)
  ![alt text](<partage de fichier dans le compte de stockage .png>)

4. **Mettre en œuvre des politiques de sauvegarde et de rétention** :
   - Configurez les politiques de sauvegarde selon vos besoins.

![alt text](<sauvegarde du coffre sur la vm.png>)

---