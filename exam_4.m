n = input("Enter un nombre d'etudiants N:")
resultat = fopen('resultat.txt','w');

% ecrir dans le fichier
for i = 1:n
    nom = input("Enter le nom d'etudiant")
    prenom = input("Enter le prenom d'etudiant")
    mod1 = input("Enter la note du module 1")
    mod2 = input("Enter la note du module 2")
    mod3 = input("Enter la note du module 3")
    moyenne = (mod1+mod2+mod3) ./ 3
    res = "Ajourne"
    if (moyenne>=10)
        res = "Ajourne"
    end
    formatSpec = 'Nom: %s , prenom: %s , moyenne: %s , resultat: %s \n';
    sprintf(formatSpec,nom,prenom,moyenne,res)
end
fclose(resultat);

%  lire a partir du fichier:

resultat = fopen('resultat.txt','r');
formatSpec = '%s';
lecture = fscanf(fileID,formatSpec)
fclose(resultat);




