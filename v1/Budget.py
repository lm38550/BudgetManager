from sqlite3.dbapi2 import Timestamp
from tkinter import *
import tkinter.font as font
from tkinter.ttk import Combobox, Treeview
import sqlite3
from datetime import datetime
from typing import AsyncGenerator

global P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12
global R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12

"""Fonction de connexion permettant de se connecter à la base pokedex
"""
def connexion():
    try:
        #connexion à la bdd
        sqliteConnection = sqlite3.connect('./Budgetdb.db')
        return sqliteConnection
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

"""<summary>Fonction de connexion à la bdd</summary>
"""

def deconnexion(sqliteConnection):
   if (sqliteConnection):
       #fermeture de la co
            sqliteConnection.close()
            #print("The SQLite connection is closed")

def actualiser():
    Mensuel()
    affichage_comptes()
    RemplirListeDeroulanteComptes()
    AffichezHistorique()
    CalculBudget()
    calc_Rmois()
    calc_Dmois()

#création de la fenetre Tkinter
fenetre=Tk()
#permet de modifier la taille de la fenétre
dessin=Canvas(fenetre, bg='#00caff', width=1200,height=900)
fenetre.geometry("1200x900")
dessin.grid(row = 1, column = 0, columnspan = 2, padx=0, pady=0)
dessin.create_line(5,250,520,250,fill='black', width=10)
dessin.create_line(5,550,520,550,fill='black', width=10)
dessin.create_line(250,5,250,250,fill='black', width=10)
dessin.create_line(520,5,520,895,fill='black', width=10)
dessin.create_line(520,635,1195,635,fill='Black', width=10)


def affichage_comptes():
    Mensuel()
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    #ecriture de la requéte, on récupére le contenu de la listeDeroulante avec la fonction .get()
    sqlite_select_Query = "select * from comptes;"
    #execution de la requéte
    cursor.execute(sqlite_select_Query)
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()
    label_compte1.set(str(record[0][1]))
    label_compte2.set(str(record[1][1]))
    label_compte3.set(str(record[7][1]))
    label_compte4.set(str(record[3][1]))
    label_compte5.set(str(record[4][1]))
    label_compte6.set(str(record[5][1]))
    label_compte7.set(str(record[2][1]))

    value_compte1.set(str("{:.2F}".format(record[0][2])+"€"))
    value_compte2.set(str("{:.2F}".format(record[1][2])+"€"))
    value_compte3.set(str("{:.2F}".format(record[7][2])+"€"))
    value_compte4.set(str("{:.2F}".format(record[3][2])+"€"))
    value_compte5.set(str("{:.2F}".format(record[4][2])+"€"))
    value_compte6.set(str("{:.2F}".format(record[5][2])+"€"))
    value_compte7.set(str("{:.2F}".format(record[2][2])+"€"))

    total = 0
    for i in range(len(record)):
        total = total + float(record[i][2])
    value_total.set(str("{:.2F}".format(total)+"€"))
    
    cursor.close()
    deconnexion(sqliteConnection)

def RemplirListeDeroulanteComptes():
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    #ecriture de la requéte
    sqlite_select_Query = "select nom, montant from Comptes;"
    #execution de la requéte
    cursor.execute(sqlite_select_Query)
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()
    #declaration du tableau qui va contenir les données a afficher dans la liste déroulante
    tabCompte = []
    #parcours notre tableau de retour de base de données et ajoute les éléments dans le tableau data
    for row in record:
        tabCompte.append(row[0])

    #on ferme le curseur
    cursor.close()
    deconnexion(sqliteConnection)

    #retourne le tableau
    return tabCompte

def RemplirListeDeroulanteCatégorie():
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    #ecriture de la requéte
    sqlite_select_Query = "select nom from Catégories;"
    #execution de la requéte
    cursor.execute(sqlite_select_Query)
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()
    #declaration du tableau qui va contenir les données a afficher dans la liste déroulante
    tabCatégorie = []
    #parcours notre tableau de retour de base de données et ajoute les éléments dans le tableau data
    for row in record:
        tabCatégorie.append(row[0])

    #on ferme le curseur
    cursor.close()
    deconnexion(sqliteConnection)

    #retourne le tableau
    return tabCatégorie

def Virement():
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    #ecriture de la requéte, on récupére le contenu de la listeDeroulante avec la fonction .get()
    sqlite_select_Query = "select montant from Comptes where Nom ='"+listeDeroulanteComptes1.get()+"';"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    record1=record[0][0]-float(champ_montant.get())
    sqlite_select_Query = "UPDATE Comptes SET Montant = REPLACE(Montant,"+str(record[0][0])+","+str(record1)+") WHERE Comptes.Nom = '"+listeDeroulanteComptes1.get()+"'"
    cursor.execute(sqlite_select_Query)
    
    sqlite_select_Query = "select montant from Comptes where Nom ='"+listeDeroulanteComptes2.get()+"';"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    record1=record[0][0]+float(champ_montant.get())
    sqlite_select_Query = "UPDATE Comptes SET Montant = REPLACE(Montant,"+str(record[0][0])+","+str(record1)+") WHERE Comptes.Nom = '"+listeDeroulanteComptes2.get()+"'"
    cursor.execute(sqlite_select_Query)
    sqliteConnection.commit()

    cursor.close()
    deconnexion(sqliteConnection)
    actualiser()

def AffichezHistorique():

    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    #ecriture de la requéte
    sqlite_select_Query = "SELECT * FROM Historique INNER JOIN Comptes ON Historique.Compte=Comptes.idCompte INNER JOIN Catégories ON Historique.Catégorie= Catégories.idCatégorie ORDER BY Année DESC,Mois DESC,Jour DESC "
    #execution de la requéte
    cursor.execute(sqlite_select_Query)
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()
    #vidange du tableau
    tree.delete(*tree.get_children())
    #on parcours le tableau record pour afficher et on insert une nouvelle ligne à chaque row.
    for row in record:
        tree.insert('', 'end',text=str(row[2])+'/'+str(row[1])+'/'+str(row[0]),
                            values=(str(row[3])+'€',
                                    str(row[7]),
                                    str(row[10])))


    #on ferme le curseur
    cursor.close()
    #deconnexion de la bdd
    deconnexion(sqliteConnection)

def Revenu():
    global activite
    if activite!=True:
        bouton_revenu.configure(bg='green')
        bouton_depense.configure(bg='white')
        activite=True
    else:
        pass

def Depense():
    global activite
    if activite!=False:
        bouton_revenu.configure(bg='white')
        bouton_depense.configure(bg='green')
        activite=False
    else:
        pass

def Activite():
    global activite

    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    compte = listeDeroulanteComptes.get()
    catégorie = listeDeroulanteCatégorie.get()
    année=str(datetime.now().year)
    mois=str(datetime.now().month)
    jour=str(datetime.now().day)
    montant = entre_activite.get()
    #ecriture de la requéte, on récupére le contenu de la listeDeroulante avec la fonction .get()
    sqlite_select_Query = "select idCatégorie from Catégories where Nom ='"+catégorie+"';"
    cursor.execute(sqlite_select_Query)
    record1 = cursor.fetchall()
    sqlite_select_Query = "select idCompte from Comptes where Nom ='"+compte+"';"
    cursor.execute(sqlite_select_Query)
    record2 = cursor.fetchall()
    sqlite_select_Query = "select Montant from Comptes where Nom ='"+compte+"';"
    cursor.execute(sqlite_select_Query)
    record3 = cursor.fetchall()
    sqlite_select_Query = "select Utilisé from Budget where Catégorie ='"+str(record1[0][0])+"' and mois = '"+str(mois) + "' and année = '" + str(année) + "';"
    cursor.execute(sqlite_select_Query)
    record4 = cursor.fetchall()

    if activite==True:
        pm='+'
        nouveau_montant=record3[0][0]+float(montant)
    elif activite==False:
        pm='-'
        nouveau_montant=record3[0][0]-float(montant)
        if record1[0][0] in [1,2,3,4,7,8,13,14]:
            sqlite_select_Query = "UPDATE Budget SET Utilisé = '"+str(record4[0][0]+float(montant))+"' where Catégorie = '" + str(record1[0][0]) + "' and mois = '"+str(mois) + "' and année = '" + str(année) + "'"
            cursor.execute(sqlite_select_Query)
            CalculBudget()

    sqlite_select_Query = "INSERT INTO Historique VALUES ("+année+","+mois+","+jour+","+pm+montant+","+str(record1[0][0])+","+str(record2[0][0])+")"
    cursor.execute(sqlite_select_Query)
    sqliteConnection.commit()

    sqlite_select_Query = "UPDATE Comptes SET Montant = REPLACE(Montant,"+str(record3[0][0])+","+str(nouveau_montant)+") WHERE Comptes.Nom = '"+str(compte)+"'"
    cursor.execute(sqlite_select_Query)
    sqliteConnection.commit()

    actualiser()
    actu_texte()
    cursor.close()
    deconnexion(sqliteConnection)

def actu_texte():
    global P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12
    global R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12
    labelP1.configure(text=(str("{:.2F}".format(P1))+'%'))
    labelP1.place(width=T1)
    labelR1.configure(text='Reste:'+str("{:.2F}".format(R1))+'€')
    labelA1.configure(text='Total:'+str("{:.2F}".format(A1))+'€')
    labelP2.configure(text=(str("{:.2F}".format(P2))+'%'))
    labelP2.place(width=T2)
    labelR2.configure(text='Reste:'+str("{:.2F}".format(R2))+'€')
    labelA2.configure(text='Total:'+str("{:.2F}".format(A2))+'€')
    labelP3.configure(text=(str("{:.2F}".format(P3))+'%'))
    labelP3.place(width=T3)
    labelR3.configure(text='Reste:'+str("{:.2F}".format(R3))+'€')
    labelA3.configure(text='Total:'+str("{:.2F}".format(A3))+'€')
    labelP4.configure(text=(str("{:.2F}".format(P4))+'%'))
    labelP4.place(width=T4)
    labelR4.configure(text='Reste:'+str("{:.2F}".format(R4))+'€')
    labelA4.configure(text='Total:'+str("{:.2F}".format(A4))+'€')
    labelP5.configure(text=(str("{:.2F}".format(P5))+'%'))
    labelP5.place(width=T5)
    labelR5.configure(text='Reste:'+str("{:.2F}".format(R5))+'€')
    labelA5.configure(text='Total:'+str("{:.2F}".format(A5))+'€')
    labelP6.configure(text=(str("{:.2F}".format(P6))+'%'))
    labelP6.place(width=T6)
    labelR6.configure(text='Reste:'+str("{:.2F}".format(R6))+'€')
    labelA6.configure(text='Total:'+str("{:.2F}".format(A6))+'€')
    labelP7.configure(text=(str("{:.2F}".format(P7))+'%'))
    labelP7.place(width=T7)
    labelR7.configure(text='Reste:'+str("{:.2F}".format(R7))+'€')
    labelA7.configure(text='Total:'+str("{:.2F}".format(A7))+'€')
    labelP8.configure(text=(str("{:.2F}".format(P8))+'%'))
    labelP8.place(width=T8)
    labelR8.configure(text='Reste:'+str("{:.2F}".format(R8))+'€')
    labelA8.configure(text='Total:'+str("{:.2F}".format(A8))+'€')
    labelR10.configure(text='TOTAL : '+str("{:.2F}".format(R10))+'€')
    labelR11.configure(text='TOTAL : '+str("{:.2F}".format(R11))+'€')
    labelP12.configure(text=(str("{:.2F}".format(P12))+'%'))
    labelP12.place(width=T12)
    labelR12.configure(text='Reste:'+str("{:.2F}".format(R12))+'€')
    labelA12.configure(text='Total:'+str("{:.2F}".format(A12))+'€')

def CalculBudget():
    global P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12
    global R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    #ecriture de la requéte
    sqlite_select_Query = "select montant, utilisé from Budget WHERE mois in ("+str(datetime.now().month)+",100000) and année in ("+str(datetime.now().year)+",100000) ORDER BY année, mois"
    #execution de la requéte
    cursor.execute(sqlite_select_Query)
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()
    P1=(record[0][1]*100/record[0][0])
    T1=round(P1*4)
    A1=record[0][0]
    R1=record[0][0]-record[0][1]
    P2=(record[1][1]*100/record[1][0])
    T2=round(P2*4)
    A2=record[1][0]
    R2=record[1][0]-record[1][1]
    P3=(record[2][1]*100/record[2][0])
    T3=round(P3*4)
    A3=record[2][0]
    R3=record[2][0]-record[2][1]
    P4=(record[3][1]*100/record[3][0])
    T4=round(P4*4)
    A4=record[3][0]
    R4=record[3][0]-record[3][1]
    P5=(record[4][1]*100/record[4][0])
    T5=round(P5*4)
    A5=record[4][0]
    R5=record[4][0]-record[4][1]
    P6=(record[5][1]*100/record[5][0])
    T6=round(P6*4)
    A6=record[5][0]
    R6=record[5][0]-record[5][1]
    P7=(record[6][1]*100/record[6][0])
    T7=round(P7*4)
    A7=record[6][0]
    R7=record[6][0]-record[6][1]
    P8=(record[7][1]*100/record[7][0])
    T8=round(P8*4)
    A8=record[7][0]
    R8=record[7][0]-record[7][1]
    R10=record[10][0]
    R11=record[8][1]
    P12=(record[9][1]*100/record[9][0])
    T12=round(P12*4)
    A12=record[9][0]
    R12=record[9][0]-record[9][1]
    if T1 > 400: T1=405
    if T2 > 400: T2=405
    if T3 > 400: T3=405
    if T4 > 400: T4=405
    if T5 > 400: T5=405
    if T6 > 400: T6=405
    if T7 > 400: T7=405
    if T8 > 400: T8=405
    if T12 > 400: T12=405

    #on ferme le curseur
    cursor.close()
    deconnexion(sqliteConnection)

def BP1():
    global budget
    budget='BP1'
    ChangerBudget()
def BP2():
    global budget
    budget='BP2'
    ChangerBudget()
def BP3():
    global budget
    budget='BP3'
    ChangerBudget()
def BP4():
    global budget
    budget='BP4'
    ChangerBudget()
def BP5():
    global budget
    budget='BP5'
    ChangerBudget()
def BP6():
    global budget
    budget='BP6'
    ChangerBudget()
def BP7():
    global budget
    budget='BP7'
    ChangerBudget()
def BP8():
    global budget
    budget='BP8'
    ChangerBudget()
def BP11():
    global budget
    budget='BP11'
    ChangerBudget2()
def BP12():
    global budget
    budget='BP12'
    ChangerBudget2()

def ChangerBudget():
    global budget
    if budget=='BP1': cate=1
    if budget=='BP2': cate=2
    if budget=='BP3': cate=3
    if budget=='BP4': cate=4
    if budget=='BP5': cate=7
    if budget=='BP6': cate=8
    if budget=='BP7': cate=13
    if budget=='BP8': cate=14

    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    sqlite_select_Query = "select montant from Budget where Catégorie ='"+str(cate)+"' and mois = '"+str(datetime.now().month)+"' and Année ='"+str(datetime.now().year)+"';"
    cursor.execute(sqlite_select_Query)
    record1 = cursor.fetchall()
    sqlite_select_Query = "select montant from Budget where Catégorie ='9' and mois = '100000' and Année ='100000';"
    cursor.execute(sqlite_select_Query)
    record2 = cursor.fetchall()
    sqlite_select_Query = "UPDATE Budget SET Montant = '"+str(record2[0][0]+10)+"'  where Catégorie = '9'"
    cursor.execute(sqlite_select_Query)
    sqliteConnection.commit()
    sqlite_select_Query = "UPDATE Budget SET Montant = '"+str(record1[0][0]-10)+"'  where Catégorie = '"+str(cate)+"'"
    cursor.execute(sqlite_select_Query)
    sqliteConnection.commit()

    #on ferme le curseur
    cursor.close()
    deconnexion(sqliteConnection)
    actualiser()
    actu_texte()

def ChangerBudget2():
    global budget
    if budget=='BP12': cate=10
    if budget=='BP11': cate=11


    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    sqlite_select_Query = "select utilisé from Budget where Catégorie ='"+str(cate)+"'"
    cursor.execute(sqlite_select_Query)
    record1 = cursor.fetchall()
    sqlite_select_Query = "select montant from Budget where Catégorie ='9' and mois = '0' and Année ='0';"
    cursor.execute(sqlite_select_Query)
    record2 = cursor.fetchall()
    sqlite_select_Query = "UPDATE Budget SET Montant = '"+str(record2[0][0]-10)+"'  where Catégorie = '9'"
    cursor.execute(sqlite_select_Query)
    sqliteConnection.commit()
    sqlite_select_Query = "UPDATE Budget SET Utilisé = '"+str(record1[0][0]+10)+"'  where Catégorie = '"+str(cate)+"'"
    cursor.execute(sqlite_select_Query)
    sqliteConnection.commit()

    #on ferme le curseur
    cursor.close()
    deconnexion(sqliteConnection)
    actualiser()
    actu_texte()

def Mensuel():
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    sqlite_select_Query = "select * from Budget where mois ='"+str(datetime.now().month)+"' and Année ='"+str(datetime.now().year)+"';"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    
    if record==[]:
        AllCate=[1,2,3,4,7,8,13,14]
        AllMont=[120,20,150,625,30,0,10,10]
        if str(datetime.now().month) == '1':
            mois='12'
            année=str((datetime.now().year)-1)
        else:
            mois=str((datetime.now().month)-1)
            année=str(datetime.now().year)
        sqlite_select_Query = "Select Montant, Utilisé from Budget where Catégorie in ('1','2','3','4','7','8','13','14') and mois ='"+mois+"' and Année ='"+année+"';"
        cursor.execute(sqlite_select_Query)
        record1 = cursor.fetchall()
        Reste=[]
        for i in range(8):
            Reste.append(record1[i][0]-record1[i][1])
        for i in range(8):
            sqlite_select_Query = "INSERT INTO Budget VALUES ('"+str(datetime.now().year)+"','"+str(datetime.now().month)+"','"+str(AllCate[i])+"','"+str(AllMont[i]+Reste[i])+"','0')"
            cursor.execute(sqlite_select_Query)
            sqliteConnection.commit()

    cursor.close()
    deconnexion(sqliteConnection)

def calc_Dmois():
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    sqlite_select_Query = "select montant FROM Historique where mois ='"+str(datetime.now().month)+"' and Année ='"+str(datetime.now().year)+"';"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()

    depM=0

    for i in range(len(record)):
        if float(record[i][0])<0:
            depM=depM+float(record[i][0])
    
    depenseM.set(str("{:.2F}".format(-depM)))

    cursor.close()
    deconnexion(sqliteConnection)


def calc_Rmois():
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    sqlite_select_Query = "select montant FROM Historique where mois ='"+str(datetime.now().month)+"' and Année ='"+str(datetime.now().year)+"';"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()

    revM=0

    for i in range(len(record)):
        if float(record[i][0])>0:
            revM=revM+float(record[i][0])

    revenuM.set(str("{:.2F}".format(revM)))
    
    cursor.close()
    deconnexion(sqliteConnection)



########################################-------- RELEVE COMPTE --------########################################

label_compte = Label(fenetre,background='#00caff',text='MES COMPTES',anchor="center",font='Arial 18 bold underline')
label_compte.place(x=10,y=9,width=200, height=31)

label_compte1 = StringVar()
value_compte1 = StringVar()
champ_label_compte1 = Label(fenetre,background='#00caff',textvariable=label_compte1,anchor="e",font='Arial 12')
champ_value_compte1 = Label(fenetre,background='#00caff',textvariable=value_compte1,anchor="w",font='Arial 12')
champ_label_compte1.place(x=10,y=45,width=115, height=20)
champ_value_compte1.place(x=130,y=45,width=80, height=20)

label_compte2 = StringVar()
value_compte2 = StringVar()
champ_label_compte2 = Label(fenetre,background='#00caff',textvariable=label_compte2,anchor="e",font='Arial 12')
champ_value_compte2 = Label(fenetre,background='#00caff',textvariable=value_compte2,anchor="w",font='Arial 12')
champ_label_compte2.place(x=10,y=70,width=115, height=20)
champ_value_compte2.place(x=130,y=70,width=80, height=20)

label_compte3 = StringVar()
value_compte3 = StringVar()
champ_label_compte3 = Label(fenetre,background='#00caff',textvariable=label_compte3,anchor="e",font='Arial 12')
champ_value_compte3 = Label(fenetre,background='#00caff',textvariable=value_compte3,anchor="w",font='Arial 12')
champ_label_compte3.place(x=10,y=95,width=115, height=20)
champ_value_compte3.place(x=130,y=95,width=80, height=20)

label_compte4 = StringVar()
value_compte4 = StringVar()
champ_label_compte4 = Label(fenetre,background='#00caff',textvariable=label_compte4,anchor="e",font='Arial 12')
champ_value_compte4 = Label(fenetre,background='#00caff',textvariable=value_compte4,anchor="w",font='Arial 12')
champ_label_compte4.place(x=10,y=120,width=115, height=20)
champ_value_compte4.place(x=130,y=120,width=80, height=20)

label_compte5 = StringVar()
value_compte5 = StringVar()
champ_label_compte5 = Label(fenetre,background='#00caff',textvariable=label_compte5,anchor="e",font='Arial 12')
champ_value_compte5 = Label(fenetre,background='#00caff',textvariable=value_compte5,anchor="w",font='Arial 12')
champ_label_compte5.place(x=10,y=145,width=115, height=20)
champ_value_compte5.place(x=130,y=145,width=80, height=20)

label_compte6 = StringVar()
value_compte6 = StringVar()
champ_label_compte6 = Label(fenetre,background='#00caff',textvariable=label_compte6,anchor="e",font='Arial 12')
champ_value_compte6 = Label(fenetre,background='#00caff',textvariable=value_compte6,anchor="w",font='Arial 12')
champ_label_compte6.place(x=10,y=170,width=115, height=20)
champ_value_compte6.place(x=130,y=170,width=80, height=20)

label_compte7 = StringVar()
value_compte7 = StringVar()
champ_label_compte7 = Label(fenetre,background='#00caff',textvariable=label_compte7,anchor="e",font='Arial 12')
champ_value_compte7 = Label(fenetre,background='#00caff',textvariable=value_compte7,anchor="w",font='Arial 12')
champ_label_compte7.place(x=10,y=195,width=115, height=20)
champ_value_compte7.place(x=130,y=195,width=80, height=20)

value_total = StringVar()
champ_label_total = Label(fenetre,background='#00caff',text='TOTAL',font='Arial 12')
champ_value_total = Label(fenetre,background='#00caff',textvariable=value_total,font='Arial 12')
champ_label_total.place(x=10,y=225,width=95, height=20)
champ_value_total.place(x=110,y=225,width=100, height=20)


########################################-------- VIREMENTS --------########################################

label_transfert = Label(fenetre,background='#00caff',text='VIREMENT',anchor="center",font='Arial 18 bold underline')
label_transfert.place(x=300,y=9,width=200, height=31)

tabCompte1=RemplirListeDeroulanteComptes()
listeDeroulanteComptes1 = Combobox(fenetre, values=tabCompte1)
listeDeroulanteComptes1.current()
listeDeroulanteComptes1.place(x=300,y=55,width=200, height=24)

montant_transfert = StringVar()
champ_transfert = Label(fenetre,background='#00caff',text='MONTANT',anchor="center",font='Arial 14')
champ_transfert.place(x=300,y=100,width=100, height=30)
champ_montant = Entry(fenetre, textvariable=montant_transfert, width=20)
champ_montant.place(x=300,y=140,width=100, height=24)

bouton_transfert=Button(fenetre, text="VIREMENT", command=Virement)
bouton_transfert.place(x=420,y=110,width=80, height=44)

tabCompte2=RemplirListeDeroulanteComptes()
listeDeroulanteComptes2 = Combobox(fenetre, values=tabCompte2)
listeDeroulanteComptes2.current()
listeDeroulanteComptes2.place(x=300,y=201,width=200, height=24)


########################################-------- ACTIVITE --------########################################

label_transfert = Label(fenetre,background='#00caff',text='DEPENSE/REVENU',anchor="center",font='Arial 21 bold underline')
label_transfert.place(x=10,y=280,width=490, height=35)

champ_label_activite = Label(fenetre,background='#00caff',text='Compte',anchor="w",font='Arial 12')
champ_label_activite.place(x=20,y=330,width=80, height=20)

tabCompte=RemplirListeDeroulanteComptes()
listeDeroulanteComptes = Combobox(fenetre, values=tabCompte)
listeDeroulanteComptes.current()
listeDeroulanteComptes.place(x=10,y=355,width=250, height=24)

champ_label_activite2 = Label(fenetre,background='#00caff',text='Catégorie',anchor="w",font='Arial 12')
champ_label_activite2.place(x=20,y=400,width=80, height=20)

tabCompte=RemplirListeDeroulanteCatégorie()
listeDeroulanteCatégorie = Combobox(fenetre, values=tabCompte)
listeDeroulanteCatégorie.current()
listeDeroulanteCatégorie.place(x=10,y=425,width=250, height=24)

montant_activite = StringVar()
champ_activite = Label(fenetre,background='#00caff',text='MONTANT',anchor="w",font='Arial 12')
champ_activite.place(x=20,y=470,width=250, height=20)
entre_activite = Entry(fenetre, textvariable=montant_activite, width=20)
entre_activite.place(x=10,y=495,width=250, height=24)

global activite
activite=bool

bouton_revenu=Button(fenetre, bg='white', text="REVENU",command=Revenu)
bouton_revenu.place(x=300,y=330,width=90, height=100)

bouton_depense=Button(fenetre, bg='white', text="DEPENSE",command=Depense)
bouton_depense.place(x=410,y=330,width=90, height=100)

bouton_valider=Button(fenetre, text="VALIDER", command=Activite)
bouton_valider.place(x=300,y=450,width=200, height=70)

########################################-------- HISTORIQUE --------########################################

label_transfert = Label(fenetre,background='#00caff',text='HISTORIQUE',anchor="center",font='Arial 21 bold underline')
label_transfert.place(x=10,y=600,width=490, height=35)

tree = Treeview(fenetre, columns=('Date','Montant', 'Compte', 'Catégorie'))

AffichezHistorique()

# Set the heading (Attribute Names)
tree.heading('#0', text='Date')
tree.heading('#1', text='Montant')
tree.heading('#2', text='Compte')
tree.heading('#3', text='Catégorie')
# Specify attributes of the columns (We want to stretch it!)
tree.column('#0',width=100, stretch=YES)
tree.column('#1',width=100, stretch=YES)
tree.column('#2',width=110, stretch=YES)
tree.column('#3',width=180, stretch=YES)

tree.place(x=10,y=640,width=490, height=250)



label_DM = Label(fenetre,background='#00caff',text='Dépenses du mois : ',anchor="w",font='Arial 11')
label_DM.place(x=990,y=550,width=170, height=25)

label_RM = Label(fenetre,background='#00caff',text='Revenus du mois : ',anchor="w",font='Arial 11')
label_RM.place(x=990,y=580,width=170, height=25)

depenseM = StringVar()
revenuM = StringVar()
champ_depenseM = Label(fenetre,background='#00caff',textvariable=depenseM,anchor="e",font='Arial 11')
champ_revenuM  = Label(fenetre,background='#00caff',textvariable=revenuM,anchor="e",font='Arial 11')
champ_depenseM.place(x=1130,y=550,width=60, height=25)
champ_revenuM.place(x=1130,y=580,width=60, height=25)


########################################-------- BUDGETS --------########################################

label_transfert = Label(fenetre,background='#00caff',text='BUDGET',anchor="center",font='Arial 25 bold underline')
label_transfert.place(x=530,y=5,width=670, height=35)

actualiser()

labelB1 = Label(fenetre,background='#00caff',text='Courses alimentaires',anchor="sw",font='Arial 12')
labelB1.place(x=560,y=70,width=150, height=20)
labelP1 = Label(fenetre,background='#ff0000',text=(str("{:.2F}".format(P1))+'%'),anchor="e",font='Arial 10')
labelP1.place(x=550,y=91,width=T1, height=18)
dessin.create_line(550,100,950,100,fill='White', width=20)
dessin.create_line(650,100,650,110,fill='Black', width=1)
dessin.create_line(750,90,750,110,fill='Black', width=1)
dessin.create_line(850,100,850,110,fill='Black', width=1)
labelR1 = Label(fenetre,background='#00caff',text='Reste:'+str("{:.2F}".format(R1))+'€',anchor="w",font='Arial 10')
labelR1.place(x=750,y=70,width=100, height=18)
labelA1 = Label(fenetre,background='#00caff',text='Total:'+str("{:.2F}".format(A1))+'€',anchor="e",font='Arial 10')
labelA1.place(x=875,y=70,width=100, height=18)
bouton_M1=Button(fenetre, text="-",command=BP1)
bouton_M1.place(x=955,y=90,width=20, height=20)

labelB2 = Label(fenetre,background='#00caff',text='Transport',anchor="sw",font='Arial 12')
labelB2.place(x=560,y=120,width=150, height=20)
labelP2 = Label(fenetre,background='#00ff00',text=(str("{:.2F}".format(P2))+'%'),anchor="e",font='Arial 10')
labelP2.place(x=550,y=141,width=T2, height=18)
dessin.create_line(550,150,950,150,fill='White', width=20)
dessin.create_line(650,150,650,160,fill='Black', width=1)
dessin.create_line(750,140,750,160,fill='Black', width=1)
dessin.create_line(850,150,850,160,fill='Black', width=1)
labelR2 = Label(fenetre,background='#00caff',text='Reste:'+str("{:.2F}".format(R2))+'€',anchor="w",font='Arial 10')
labelR2.place(x=750,y=120,width=100, height=18)
labelA2 = Label(fenetre,background='#00caff',text='Total:'+str("{:.2F}".format(A2))+'€',anchor="e",font='Arial 10')
labelA2.place(x=875,y=120,width=100, height=18)
bouton_M2=Button(fenetre, text="-",command=BP2)
bouton_M2.place(x=955,y=140,width=20, height=20)

labelB3 = Label(fenetre,background='#00caff',text='Loisirs',anchor="sw",font='Arial 12')
labelB3.place(x=560,y=170,width=150, height=20)
labelP3 = Label(fenetre,background='yellow',text=(str("{:.2F}".format(P3))+'%'),anchor="e",font='Arial 10')
labelP3.place(x=550,y=191,width=T3, height=18)
dessin.create_line(550,200,950,200,fill='White', width=20)
dessin.create_line(650,200,650,210,fill='Black', width=1)
dessin.create_line(750,190,750,210,fill='Black', width=1)
dessin.create_line(850,200,850,210,fill='Black', width=1)
labelR3 = Label(fenetre,background='#00caff',text='Reste:'+str("{:.2F}".format(R3))+'€',anchor="w",font='Arial 10')
labelR3.place(x=750,y=170,width=100, height=18)
labelA3 = Label(fenetre,background='#00caff',text='Total:'+str("{:.2F}".format(A3))+'€',anchor="e",font='Arial 10')
labelA3.place(x=875,y=170,width=100, height=18)
bouton_M3=Button(fenetre, text="-",command=BP3)
bouton_M3.place(x=955,y=190,width=20, height=20)

labelB4 = Label(fenetre,background='#00caff',text='Maison',anchor="sw",font='Arial 12')
labelB4.place(x=560,y=220,width=150, height=20)
labelP4 = Label(fenetre,background='#ff00ff',text=(str("{:.2F}".format(P4))+'%'),anchor="e",font='Arial 10')
labelP4.place(x=550,y=241,width=T4, height=18)
dessin.create_line(550,250,950,250,fill='White', width=20)
dessin.create_line(650,250,650,260,fill='Black', width=1)
dessin.create_line(750,240,750,260,fill='Black', width=1)
dessin.create_line(850,250,850,260,fill='Black', width=1)
labelR4 = Label(fenetre,background='#00caff',text='Reste:'+str("{:.2F}".format(R4))+'€',anchor="w",font='Arial 10')
labelR4.place(x=750,y=220,width=100, height=18)
labelA4 = Label(fenetre,background='#00caff',text='Total:'+str("{:.2F}".format(A4))+'€',anchor="e",font='Arial 10')
labelA4.place(x=875,y=220,width=100, height=18)
bouton_M4=Button(fenetre, text="-",command=BP4)
bouton_M4.place(x=955,y=240,width=20, height=20)

labelB5 = Label(fenetre,background='#00caff',text='Vetements',anchor="sw",font='Arial 12')
labelB5.place(x=560,y=270,width=150, height=20)
labelP5 = Label(fenetre,background='orange',text=(str("{:.2F}".format(P5))+'%'),anchor="e",font='Arial 10')
labelP5.place(x=550,y=291,width=T5, height=18)
dessin.create_line(550,300,950,300,fill='White', width=20)
dessin.create_line(650,300,650,310,fill='Black', width=1)
dessin.create_line(750,290,750,310,fill='Black', width=1)
dessin.create_line(850,300,850,310,fill='Black', width=1)
labelR5 = Label(fenetre,background='#00caff',text='Reste:'+str("{:.2F}".format(R5))+'€',anchor="w",font='Arial 10')
labelR5.place(x=750,y=270,width=100, height=18)
labelA5 = Label(fenetre,background='#00caff',text='Total:'+str("{:.2F}".format(A5))+'€',anchor="e",font='Arial 10')
labelA5.place(x=875,y=270,width=100, height=18)
bouton_M5=Button(fenetre, text="-",command=BP5)
bouton_M5.place(x=955,y=290,width=20, height=20)

labelB6 = Label(fenetre,background='#00caff',text='Essence',anchor="sw",font='Arial 12')
labelB6.place(x=560,y=320,width=150, height=20)
labelP6 = Label(fenetre,background='#0000ff',text=(str("{:.2F}".format(P6))+'%'),anchor="e",font='Arial 10')
labelP6.place(x=550,y=341,width=T6, height=18)
dessin.create_line(550,350,950,350,fill='White', width=20)
dessin.create_line(650,350,650,360,fill='Black', width=1)
dessin.create_line(750,340,750,360,fill='Black', width=1)
dessin.create_line(850,350,850,360,fill='Black', width=1)
labelR6 = Label(fenetre,background='#00caff',text='Reste:'+str("{:.2F}".format(R6))+'€',anchor="w",font='Arial 10')
labelR6.place(x=750,y=320,width=100, height=18)
labelA6 = Label(fenetre,background='#00caff',text='Total:'+str("{:.2F}".format(A6))+'€',anchor="e",font='Arial 10')
labelA6.place(x=875,y=320,width=100, height=18)
bouton_M6=Button(fenetre, text="-",command=BP6)
bouton_M6.place(x=955,y=340,width=20, height=20)

labelB7 = Label(fenetre,background='#00caff',text='Etudes',anchor="sw",font='Arial 12')
labelB7.place(x=560,y=370,width=150, height=20)
labelP7 = Label(fenetre,background='purple',text=(str("{:.2F}".format(P7))+'%'),anchor="e",font='Arial 10')
labelP7.place(x=550,y=391,width=T7, height=18)
dessin.create_line(550,400,950,400,fill='White', width=20)
dessin.create_line(650,400,650,410,fill='Black', width=1)
dessin.create_line(750,390,750,410,fill='Black', width=1)
dessin.create_line(850,400,850,410,fill='Black', width=1)
labelR7 = Label(fenetre,background='#00caff',text='Reste:'+str("{:.2F}".format(R7))+'€',anchor="w",font='Arial 10')
labelR7.place(x=750,y=370,width=100, height=18)
labelA7 = Label(fenetre,background='#00caff',text='Total:'+str("{:.2F}".format(A7))+'€',anchor="e",font='Arial 10')
labelA7.place(x=875,y=370,width=100, height=18)
bouton_M7=Button(fenetre, text="-",command=BP7)
bouton_M7.place(x=955,y=390,width=20, height=20)

labelB8 = Label(fenetre,background='#00caff',text='Santé',anchor="sw",font='Arial 12')
labelB8.place(x=560,y=420,width=150, height=20)
labelP8 = Label(fenetre,background='maroon',text=(str("{:.2F}".format(P8))+'%'),anchor="e",font='Arial 10')
labelP8.place(x=550,y=441,width=T8, height=18)
dessin.create_line(550,450,950,450,fill='White', width=20)
dessin.create_line(650,450,650,460,fill='Black', width=1)
dessin.create_line(750,440,750,460,fill='Black', width=1)
dessin.create_line(850,450,850,460,fill='Black', width=1)
labelR8 = Label(fenetre,background='#00caff',text='Reste:'+str("{:.2F}".format(R8))+'€',anchor="w",font='Arial 10')
labelR8.place(x=750,y=420,width=100, height=18)
labelA8 = Label(fenetre,background='#00caff',text='Total:'+str("{:.2F}".format(A8))+'€',anchor="e",font='Arial 10')
labelA8.place(x=875,y=420,width=100, height=18)
bouton_M8=Button(fenetre, text="-",command=BP8)
bouton_M8.place(x=955,y=440,width=20, height=20)

labelB10 = Label(fenetre,background='#00caff',text='EPARGNE',anchor="center",font='Arial 25')
labelB10.place(x=985,y=150,width=210, height=30)
labelR10 = Label(fenetre,background='#00caff',text='TOTAL : '+str("{:.2F}".format(R10))+'€',anchor="center",font='Arial 20')
labelR10.place(x=985,y=200,width=210, height=25)

labelB11 = Label(fenetre,background='#00caff',text='Reserve prévention',anchor="center",font='Arial 18')
labelB11.place(x=985,y=300,width=210, height=25)
labelR11 = Label(fenetre,background='#00caff',text='TOTAL : '+str("{:.2F}".format(R11))+'€',anchor="w",font='Arial 16')
labelR11.place(x=990,y=340,width=190, height=20)
bouton_M11=Button(fenetre, text="+",command=BP11)
bouton_M11.place(x=1150,y=338,width=40, height=22)

labelB12 = Label(fenetre,background='#00caff',text='Projet Espagne',anchor="sw",font='Arial 12')
labelB12.place(x=560,y=570,width=150, height=20)
labelP12 = Label(fenetre,background='pink',text=(str("{:.2F}".format(P12))+'%'),anchor="e",font='Arial 10')
labelP12.place(x=550,y=191,width=T12, height=18)
dessin.create_line(550,600,950,600,fill='White', width=20)
dessin.create_line(650,600,650,610,fill='Black', width=1)
dessin.create_line(750,590,750,610,fill='Black', width=1)
dessin.create_line(850,600,850,610,fill='Black', width=1)
labelR12 = Label(fenetre,background='#00caff',text='Reste:'+str("{:.2F}".format(R12))+'€',anchor="w",font='Arial 10')
labelR12.place(x=750,y=570,width=100, height=18)
labelA12 = Label(fenetre,background='#00caff',text='Total:'+str("{:.2F}".format(A12))+'€',anchor="e",font='Arial 10')
labelA12.place(x=875,y=570,width=100, height=18)
bouton_M12=Button(fenetre, text="+",command=BP12)
bouton_M12.place(x=955,y=590,width=20, height=20)

########################################-------- NOTES --------########################################

labelNote = Label(fenetre,background='#00caff',text='1 PAYER         Loyer         615€\n1 REVENU      Crous        458.7€\n4 REVENU      Parents     450€\n9 PAYER         TCL           0€\n15 PAYER       Banque     3€      ',anchor="nw",font='Arial 12',justify='left')
labelNote.place(x=535,y=650,width=250, height=240)
labelRapp = Label(fenetre,background='#00caff',text='CA  - 120\nT     - 20 \nL     - 150\nM    - 625\nV     - 30 \nEs  - 0 \nEt   - 10 \nS    - 10 ',anchor="nw",font='Arial 12',justify='left')
labelRapp.place(x=810,y=650,width=250, height=240)



actualiser()
fenetre.mainloop()