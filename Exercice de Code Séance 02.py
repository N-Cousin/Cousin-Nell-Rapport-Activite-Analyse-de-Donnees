#coding:utf8

import pandas as pd
import matplotlib.pyplot as plt

# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/
with open("./data/resultats-elections-presidentielles-2022-1er-tour.csv","r") as fichier:
    contenu = pd.read_csv(fichier)
    
# Question 5
df=pd.DataFrame(data=contenu)
print(df)

# Question 6
lignes=len(df)
colonnes=len(df.columns)
print("Le tableau contient",lignes,"lignes et",colonnes,"colonnes.")

# # Question 7
Int=df.select_dtypes(include='int')
Float=df.select_dtypes(include='float')
Str=df.select_dtypes(include='object')
Bool=df.select_dtypes(include='bool')
types = [Int,Float,Str,Bool]
print(Int)

# # Question 8
head=df.head(0)
print(head)

# Question 9

# Question 10
table = []
for k in df:
    if k in Int:
        table.append(k) #ajoute le nom de la colonne
        k = df[k].sum()
        table.append(k) #ajoute la somme des valeurs de la colonne
    elif k in Float:
        table.append(k) 
        k = df[k].sum()
        table.append(k)
    else:
        continue
print("Les effectifs sont :",table)


# Question 11
# nb = 0
# for g in df['Libellé du département']:
    # Ins=df.iloc[[nb], 2]
    # Vot=df.iloc[[nb], 4]
    # if g=='Français établis hors de France':
        # fig, ax = plt.subplots()
        # ax.bar(g, Ins, label='Inscrits')
        # ax.bar(g, Vot, label='Votants')
        # ax.legend()
        # plt.title("Nombre d'Inscrits et de Votants selon le département")
        # plt.savefig("Graphiques en Barre/Diagramme-{}.png".format(nb))
    # else:
        # fig, ax = plt.subplots()
        # ax.bar(g, Ins, label='Inscrits')
        # ax.bar(g, Vot, label='Votants')
        # ax.legend()
        # plt.title("Nombre d'Inscrits et de Votants selon le département")
        # plt.savefig("Graphiques en Barre/Diagramme-{}.png".format(nb))
    # nb = nb + 1

# Question 12
# nb=0
# for g in df['Libellé du département']:
    # Abs=df.iloc[[nb], 3]
    # Bla=df.iloc[[nb], 5]
    # Nul=df.iloc[[nb], 6]
    # Exp=df.iloc[[nb], 7]
    # courses=[Abs,Bla,Nul,Exp]
    # labels=['Abstention','Blancs','Nuls','Exprimés']
    # dictionary = {'courses':courses, 'labels':labels}
    # python_pie_chart_df = pd.DataFrame(dictionary)
    # colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
    # if nb==106:
        # plt.pie(python_pie_chart_df.courses,colors=colors)
        # plt.legend(labels = python_pie_chart_df.labels, loc = [0.95,0.35])
        # plt.title(["Proportion des votes selon les inscrits",g])
        # plt.savefig("Graphiques Circulaires/Graphique-{}.png".format(nb))
        # break
    # else:
        # plt.pie(python_pie_chart_df.courses,colors=colors)
        # plt.legend(labels = python_pie_chart_df.labels, loc = [0.95,0.35])
        # plt.title(["Proportion des votes selon les inscrits",g])
        # plt.savefig("Graphiques Circulaires/Graphique-{}.png".format(nb))
    # nb = nb + 1

# Question 13
plt.title("Distribution des inscrits")
plt.xlabel("Nombre d'inscrits (en millions)")
plt.ylabel("Quantité")
plt.hist(df['Inscrits'], bins=20)
plt.savefig("Histogramme de la distribution des inscrits.png")