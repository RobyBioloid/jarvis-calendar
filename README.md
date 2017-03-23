## Dependance
Ce plugin à besoin de la librairie Google client
Executez la commande suivante pour installer la librairie
sudo pip install --upgrade google-api-python-client

## Description
Ce plugin permet de gérer son agenda "Google Calendar"

Vous pouvez :
- consulter les prochains événements,
- consulter les événements du jour,
- consulter les événements du lendemain,
- demander quand aura lieu un événement précis,
- creer un événement.

Lors de la création de l'événement, plusieurs questions seront demandées à l'utilisateur.

Concernant la date, il est possible de donner une date sous la forme :
- jour mois année ex : 10 aout 2017,
- Aujourd'hui,
- Demain.

## Usage
```
You: Quel sont les événements à venir ?
Jarvis: Je regarde.
Jarvis: Vos 3 prochains événements sont :
Jarvis: Aujoud'hui à 19 heure, Repas chez la belle-mère.
Jarvis: Demain à 9 heure, Rendez vous chez le dentiste.
Jarvis: Le 23 septembre à 16 heure, Fête d'anniverssaire d'Emilie

You: Ajoute-moi un événement
Jarvis: Oui bien sûr, quel est le titre de l'événement à ajouter?
You: Aller chercher des fleurs pour la st-Valentin
Jarvis: Où doit se dérouler l'événement?
You: A la boutique de fleurs
Jarvis: Donnez moi une description petite description de l'événement
You: Petite pensée pour ma femme pour la St-Valentin
Jarvis: Quel jour aura lieu l'événement?
You: 14 février 2017
Jarvis: A quelle heure ?
You: 10 heure
Jarvis: Quel jour prendra fin l'événement
You: 14 février 2017
Jarvis: Quelle heure?
You: 10 heure 30
Jarvis: L'événement vient d'être ajouté au calendrier.
```

## Activation de l'API Google Calendar
a) Rendez-vous sur cet adresse https://console.developers.google.com/flows/enableapi?apiid=calendar afin de créer ou sélectionner un projet dans la console Google Developers et activer automatiquement l'API.
- Cliquez sur "Continuer",
- Cliquez sur "Passer à l'étape "Identifiants".

b) Dans la page "Ajouter des identifiants au projet"

  1) Déterminer les identifiats dont vous avez besoin
- Quelle API utilisez-vous : Laisser "Google Calendar API".
- Quelle plate-forme utilisez-vous pour appeler l'API : Choisissez "Autre plate-forme avec interface utilisateur
- A quelles données allez-vous accéder ? : Cochez "Données utilisateur

Cliquez sur "De quels identifiants ai-je besoin?"

  2) Créer un ID client OAuth 2.0
- Choisissez un nom de client puis cliquez sur "Creer un ID client

  3) Configurer l'écran d'autorisation d'OAuth 2.0
- Adresse e-mail : enregistrer votre adresse gmail.com
- Nom de produit affiché pour les utilisateurs : Donnez un nom de produit
- Cliquez sur "Continuer"

  4) Cliquer sur Télécharger, renomer le fichier "client_secret.json" et placer le dans
le repertoire jarvis/plugins/jarvis-calendar/python
- Cliquez sur "OK"

## Author
[RobyBioloid](https://github.com/RobyBioloid/jarvis-calendar)
