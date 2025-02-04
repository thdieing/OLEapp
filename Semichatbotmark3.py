import streamlit as st
import glob
import pandas as pd
from datetime import date
from Levenshtein import distance
#import spacy
import time
import openpyxl
# add Text field extra question
today = date.today()
todaychar = today.strftime("%Y-%m-%d")

# Define the pattern to search for CSV files
pattern = "Nouns*.csv"
csv_files = glob.glob(pattern)
latest_file = max(csv_files, key=lambda x: x.split(".")[0].split("_")[-1])
data = pd.read_csv(latest_file)

#data=data[data["type"]=="grundständig"]
#data=data[data["code"]==8]
datafilter=data

osadata=pd.read_excel('OSA.xlsx', nrows=136)
# Load the German language model
#nlp = spacy.load("de_core_news_sm")
def extract_nouns(text):
    # Tokenize the text into words
    words = text.split()
    
    # Filter out words that start with a capital letter (likely nouns)
    nouns = [word for word in words if word[0].isupper()]
    
    return nouns

def questionInterest(nouns, df):
    matching_sentences = []
    sentences1 = df["Nouns"]
    for sentence1 in sentences1: 
        c=0
        sentence1=sentence1[1:-1].split(", ")
        for i in sentence1:
            if any(distance(noun, i) <= 2 for noun in nouns):
                c+=1
        if c>0:
            matching_sentences.append(1)
        else:
            matching_sentences.append(0)
    return matching_sentences

# Function answer1
def reaction1(answer1,skip):
    if skip:
        return 1
    elif answer1== "Keine Anwort":
        return 0
    elif  int(answer1.split()[0]) < 3:
        answers1=st.button("Willst du mehr zu dem Thema wissen?", key="as1")
        if answers1:
            st.write("Companion: Alles klar! Soll ich dir vielleicht zu erst einemal erzählen was für Bildungswege es so gibt?")
            st.write("**Ausbildung**:")
            st.write("Eine Ausbildung ist eine praxisorientierte Bildungsform, bei der du eine bestimmte berufliche Qualifikation in einem bestimmten Bereich erwirbst. Du arbeitest in einem Unternehmen oder einer Organisation und besuchst gleichzeitig eine Berufsschule, um theoretisches Wissen zu erlangen. Ausbildungen dauern in der Regel zwischen zwei und dreieinhalb Jahren, je nach Berufsfeld.")
            st.write("**Studium**:")
            st.write("Ein Studium ist eine akademische Ausbildung, die sich auf theoretisches Wissen und Forschung in einem bestimmten Fachgebiet konzentriert. Du kannst an einer Universität, einer Fachhochschule oder einer anderen Hochschule studieren. Ein Studium dauert in der Regel zwischen drei und sechs Jahren und endet mit einem akademischen Grad, wie einem Bachelor oder Master.")
            st.write("**Duales Studium**:")
            st.write("Ein duales Studium kombiniert eine berufliche Ausbildung mit einem Hochschulstudium. Du arbeitest in einem Unternehmen und besuchst gleichzeitig eine Hochschule, um theoretisches Wissen zu erlangen. Duale Studiengänge bieten die Möglichkeit, praktische Erfahrungen zu sammeln und gleichzeitig einen akademischen Abschluss zu erlangen. Sie dauern in der Regel zwischen drei und viereinhalb Jahren.")
            st.write("Companion: Welche Option für dich geeignet ist, hängt von deinen Interessen, Fähigkeiten und Zielen ab. Wenn du gerne praktisch arbeitest und schnell ins Berufsleben einsteigen möchtest, könnte eine Ausbildung die richtige Wahl sein. Wenn du dich für theoretisches Wissen und Forschung interessierst und bereit bist, mehr Zeit in dein Studium zu investieren, könnte ein Studium passend sein. Ein duales Studium könnte die perfekte Balance zwischen Theorie und Praxis bieten, wenn du beides kombinieren möchtest. Es ist wichtig, alle Optionen zu prüfen und sorgfältig zu überlegen, welche am besten zu dir passt.")
            st.write("Wenn du dir jetzt sicherer bist kannst du oben weiter machen.")
        return 0

    elif int(answer1.split()[0]) > 2:
        return 1
    
# Function answer2
def reaction2(answer2, datafilter, skip):
    if skip:
        return 1,datafilter
    elif answer2== "Ausbildung":
        st.write("Companion: Wenn du dich für eine Ausbildung interessierst empfehle ich: https://www.was-studiere-ich.de/")
        return 0,datafilter
    elif answer2== "Ich weiß es gerade noch nicht, ich will mich erst einmal umsehen.":
        answers2=st.button("Willst du mehr zu dem Thema wissen?", key="as2")
        if answers2:
            st.write("Companion: Alles klar! Soll ich dir vielleicht zu erst einemal erzählen was für Bildungswege es so gibt?")
            st.write("**Ausbildung**:")
            st.write("Eine Ausbildung ist eine praxisorientierte Bildungsform, bei der du eine bestimmte berufliche Qualifikation in einem bestimmten Bereich erwirbst. Du arbeitest in einem Unternehmen oder einer Organisation und besuchst gleichzeitig eine Berufsschule, um theoretisches Wissen zu erlangen. Ausbildungen dauern in der Regel zwischen zwei und dreieinhalb Jahren, je nach Berufsfeld.")
            st.write("**Studium**:")
            st.write("Ein Studium ist eine akademische Ausbildung, die sich auf theoretisches Wissen und Forschung in einem bestimmten Fachgebiet konzentriert. Du kannst an einer Universität, einer Fachhochschule oder einer anderen Hochschule studieren. Ein Studium dauert in der Regel zwischen drei und sechs Jahren und endet mit einem akademischen Grad, wie einem Bachelor oder Master.")
            st.write("**Duales Studium**:")
            st.write("Ein duales Studium kombiniert eine berufliche Ausbildung mit einem Hochschulstudium. Du arbeitest in einem Unternehmen und besuchst gleichzeitig eine Hochschule, um theoretisches Wissen zu erlangen. Duale Studiengänge bieten die Möglichkeit, praktische Erfahrungen zu sammeln und gleichzeitig einen akademischen Abschluss zu erlangen. Sie dauern in der Regel zwischen drei und viereinhalb Jahren.")
            st.write("Companion: Welche Option für dich geeignet ist, hängt von deinen Interessen, Fähigkeiten und Zielen ab. Wenn du gerne praktisch arbeitest und schnell ins Berufsleben einsteigen möchtest, könnte eine Ausbildung die richtige Wahl sein. Wenn du dich für theoretisches Wissen und Forschung interessierst und bereit bist, mehr Zeit in dein Studium zu investieren, könnte ein Studium passend sein. Ein duales Studium könnte die perfekte Balance zwischen Theorie und Praxis bieten, wenn du beides kombinieren möchtest. Es ist wichtig, alle Optionen zu prüfen und sorgfältig zu überlegen, welche am besten zu dir passt.")
            st.write("Wenn du dir jetzt sicherer bist kannst du oben weiter machen.")
        return 0, datafilter

        
    elif answer2== "Duales Studium":
        st.write("Companion: Okay weiter gehts")
        datafilter=datafilter[datafilter['schulart'] == "Berufsakademie / Duale Hochschule"]
        print(datafilter.shape)
        return 1, datafilter
    elif answer2== "Studium":
        st.write("Companion: Okay weiter gehts")
        datafilter=datafilter[datafilter['schulart'] != "Berufsakademie / Duale Hochschule"]
        print(datafilter.shape)
        return 1, datafilter

#Function answer3
def reaction3(answer3, datafilter,skip,textq): 
    if skip:
        return 1, datafilter
    if "Ich weiß es gerade noch nicht, ich will mich erst einmal umsehen." in answer3:
         answers3=st.button("Willst du mehr zu dem Thema wissen?", key="as2")
         if answers3:
             st.write("Companion: Wenn du dir nach den Infos sicher bist kannst du oben einen Bereich auswählen der dich interessiert")
             dd= datafilter.drop_duplicates(subset=["info"])
             macrofieldtext=dd["info"].tolist()
             macro= dd["Macro_field"].tolist()
             c="NA"
             for a,b in zip(macro, macrofieldtext):
                 if a !=c:
                     st.write("**"+a+"**"+ ":")
                     c=a
                 st.write(b[24:])
         return 0, datafilter
    elif textq:
        datafiltertextq=datafilter
        datafiltertextq["mfilter"]=0
        for answermacro in answer3:
            data.loc[data['Macro_field'] == answermacro, 'mfilter'] = 1
        datafiltertextq=datafiltertextq[datafiltertextq['mfilter']==1]
        dd= datafiltertextq.drop_duplicates(subset=["info"])
        macrofieldtext=dd["info"].tolist()
        macro= dd["Macro_field"].tolist()
        c="NA"
        for a,b in zip(macro, macrofieldtext):
            if a !=c:
                st.write("**"+a+"**"+ ":")
                c=a
            st.write(b[24:])
        return 1,datafilter

             
    else: 
        return 1,datafilter
    
# Function answer4
def reaction4 (answer4, answer4b,datafilter,skip):
    if skip:
        return 1, datafilter
    if answer4=="Keine Anwort" and answer4b==True or answer4 !="Keine Anwort" and int(answer4.split()[0])<3 or answer4b==True:
        answers4=st.button("Willst du mehr zu dem Thema wissen?", key="as4")
        if answers4:
            st.write("Companion: Alles klar! Soll ich dir vielleicht zu erst einemal erzählen was alles in den Bereichen gemacht wird?")
            dd= datafilter.drop_duplicates(subset=["info"])
            macrofieldtext=dd["info"].tolist()
            macro= dd["Macro_field"].tolist()
            c="NA"
            for a,b in zip(macro, macrofieldtext):
                if a !=c:
                    st.write("**"+a+"**"+ ":")
                    c=a
                st.write(b[24:])
            
        return 0, datafilter
    elif answer4 !="Keine Anwort" and int(answer4.split()[0])>2 and answer4b==False:
         datafilter= datafilter[datafilter['Macro_field'].isin(answer3)]
         print("after macro field")
         print(datafilter.shape)
         return 1, datafilter
    elif answer4 =="Keine Anwort":
         return 0, datafilter

# Function answer6
def reaction6(answer6,answer6b, datafilter, nouns, skip):
    if skip:
        return 1, datafilter
    if answer6=="Keine Anwort" and answer6b==True or answer6 !="Keine Anwort" and int(answer6.split()[0])<3 or answer6b==True:
        st.write("Schau dir doch mal diesen Test an: https://www.was-studiere-ich.de/")
        return 0, datafilter

    elif answer6 !="Keine Anwort" and int(answer6.split()[0])>2 and answer6b==False:
        newfilter= questionInterest(nouns,datafilter)
        datafilter["filtervar1"]= newfilter
        datafilter=datafilter[datafilter['filtervar1'] == 1]
        print("after Fähig")
        print(datafilter.shape)
        return 1, datafilter
    elif answer6 =="Keine Anwort":
         return 0, datafilter

# Function answer7
def reaction7(answer7,answer7b, skip):
    if skip:
        return 0
    if answer7 =="Keine Anwort" and answer7b==True or answer7 !="Keine Anwort" and int(answer7.split()[0])<3 or answer7b==True:
         return 0
    elif answer7 !="Keine Anwort" and int(answer7.split()[0])>2 and answer7b==False:
         return 1
    elif answer7 =="Keine Anwort":
         return 3
    
# Function for osas
def filterosa(answer9,answer3, datafilter, osadata):
    output=[]
    for uni in answer9:
        id= int(datafilter["Uni_ID"][datafilter["UNIname"]== uni].unique())
        if id in osadata['uni_id'].values:
            print(id)
            print("yes")
            osadata2=osadata[osadata["uni_id"]== id]
            print(osadata2.shape)
            for macro in answer3:
                print(macro)
                if osadata2['Macro_field'].str.contains(macro).any():
                    linkosa= str(osadata2["Link_Fach"][osadata2['Macro_field']==macro].values[0])
                    print(linkosa)
                    answer= "Ich empfehle diesen Orientierungstest, basierend auf deinem Interesse für "+macro+" und deinem Wunsch an der "+uni+" zu studieren. Hier is der link zum Test: "+ linkosa
                    output.append(answer)
                else:

                    if osadata2['Macro_field'].str.contains("allgemein_uni").any():
                        linkosa= str(osadata2["Link_Uni_Allgemein"][osadata2['Macro_field']=="allgemein_uni"].values[0])
                        output.append("Ich empfehle diesen Orientierungstest basierend auf deinem Wunsch an der "+uni+" zu studieren: " +linkosa)
                    else:
                        osadata2=osadata[osadata["Hochschule"]== "Übergreifend"]
                        c=0
                        if osadata2['Macro_field'].str.contains(macro).any():
                            linkosa= str(osadata2["Link_Fach"][osadata2['Macro_field']==macro].values[0])
                            answer= "Ich empfehle diesen Orientierungstest, basierend auf deinem Interesse für "+macro+". Hier is der link zum Test: "+ linkosa
                            output.append(answer)
                        else:
                             linkosa= str(osadata2["Link_Studium_Allgemein"][osadata2['Macro_field']=="allgemein_studium"].values[0])
                             output.append("Ich empfehle diesen Orientierungstest: " +linkosa)

            
        else:
            osadata2=osadata[osadata["Hochschule"]== "Übergreifend"]
            c=0
            
            for macro in answer3:
                if osadata2['Macro_field'].str.contains(macro).any():
                    linkosa= str(osadata2["Link_Fach"][osadata2['Macro_field']==macro].values[0])
                    print(linkosa)
                    answer= "Ich empfehle diesen Orientierungstest, basierend auf deinem Interesse für "+macro+". Hier is der link zum Test: "+ linkosa
                    output.append(answer)
                else:
                    linkosa= str(osadata2["Link_Studium_Allgemein"][osadata2['Macro_field']=="allgemein_studium"].values[0])
                    output.append("Ich empfehle diesen Orientierungstest: " +linkosa)
    return set(output)

# Function OSA no location
def filterosa2(answer3, datafilter, osadata):
    output=[]
    osadata2=osadata[osadata["Hochschule"]== "Übergreifend"]
    for macro in answer3:
        if osadata2['Macro_field'].str.contains(macro).any():
            linkosa= str(osadata2["Link_Fach"][osadata2['Macro_field']==macro].values[0])
            print(linkosa)
            answer= "Ich empfehle diesen Orientierungstest, basierend auf deinem Interesse für "+macro+". Hier is der link zum Test: "+ linkosa
            output.append(answer)
        else:
            linkosa= str(osadata2["Link_Studium_Allgemein"][osadata2['Macro_field']=="allgemein_studium"].values[0])
            output.append("Ich empfehle diesen Orientierungstest: " +linkosa)
    return set(output)
    
#Start--------------------------------------------
st.title("Companion")

#Frageblock---------------------------------------
st.write("Companion: Hallo. Wie sicher bist du dir, welchen Bildungsweg (Ausbildung oder Studium) du als Nächstes einschlagen möchtest?")

answer1 = st.select_slider(
        label=' ',
        options=["Keine Anwort",'1 gar nicht','2 weniger','3 etwas','4 ziemlich', "5 sehr"],key="q1",value="Keine Anwort")
skip1= st.checkbox("Frage überspringen",key="s1")
print("s1")

if answer1:
    val1=reaction1(answer1, skip1)
    if val1==1:
        answer2= st.radio(
        label="Companion: Welche(n) Bildungsweg(e) kannst du dir vorstellen?",
        key="q2",
        options=["Ausbildung", "Duales Studium", "Studium", "Ich weiß es gerade noch nicht, ich will mich erst einmal umsehen."])
        skip3= st.checkbox("Frage überspringen",key="s3")        
        if answer2 or skip3:
            print(answer2)
            print(skip3)
            val2,datafilter= reaction2(answer2,datafilter,skip3)
            if  val2==1:
                macrofield=datafilter["Macro_field"].unique().tolist()
                macrofield.append("Ich weiß es gerade noch nicht, ich will mich erst einmal umsehen.")
                print(len(datafilter["Macro_field"].tolist()))
                answer3= st.multiselect('Companion: Welche Bereiche interessieren dich?',macrofield,default=None)
                skip4= st.checkbox("Frage überspringen",key="s4")
                textq= st.checkbox("Mehr Informationen zu den ausgewählten Bereichen?",key="tq")
                if answer3 or skip4:
                    print(answer3)
                    val3, datafilter=reaction3(answer3, datafilter, skip4, textq)
                    if val3==1:
                        answer4 = st.select_slider(label="Companion: Wie sicher bist du dir darüber, in welchen Bereichen deine Interessen liegen?",
                        options=["Keine Anwort",'1 gar nicht','2 weniger','3 etwas','4 ziemlich', "5 sehr"],key="q4",value="Keine Anwort")
                        answer4b=st.checkbox("Ich weiß es gerade noch nicht, ich will mich erst einmal umsehen.")
                        skip5= st.checkbox("Frage überspringen",key="s5")
                        if answer4 or skip5:
                            val4, datafilter=reaction4(answer4, answer4b,datafilter,skip5)
                            if val4==1:
                                answer98= st.multiselect("Companion: In welchen Bereichen liegen deine Fähigkeiten?",["Deutsch", "Mathe", "Englisch", "Bio"],default=None)
                                answer99 = st.select_slider(label="Companion: Wie sicher bist du dir darüber, in welchen Bereichen deine Fähigkeiten liegen?",
                                                               options=["Keine Anwort",'1 gar nicht','2 weniger','3 etwas','4 ziemlich', "5 sehr"],key="q99",value="Keine Anwort")
                                skipproxy= st.checkbox("Frage überspringen",key="sproxy")
                                answer99b=st.button("Ich weiß es gerade noch nicht, ich will mich erst einmal umsehen.", key="q99b")
                                answer5= st.text_input("Companion: In welchen Bereichen liegen deine Interessen?")
                                skip6= st.checkbox("Frage überspringen",key="s6")
                                if skip6:
                                    answer5= "Übersprungen"
                                if answer5:
                                    #doc = nlp(answer5)
                                    #nouns = [token.text for token in doc if token.pos_ == "NOUN"]
                                    nouns= extract_nouns(answer5)
                                    st.write("Companion: Du hast folgende Fähigkeiten/Interessen genannt:")
                                    for noun in nouns:
                                        st.write("- "+ noun)
                                    if len(nouns)==0:
                                        st.write("Schau dir doch mal diesen Test an: https://www.was-studiere-ich.de/")
                                    elif len(nouns)>0:
                                        answer6 = st.select_slider(label="Companion: Wie sicher bist du dir darüber, in welchen Bereichen deine Fähigkeiten/Interessen liegen?",
                                                               options=["Keine Anwort",'1 gar nicht','2 weniger','3 etwas','4 ziemlich', "5 sehr"],key="q6",value="Keine Anwort")
                                        answer6b=st.button("Ich weiß es gerade noch nicht, ich will mich erst einmal umsehen.", key="q6b")
                                        skip7= st.checkbox("Frage überspringen",key="s7") 
                                        if answer6 or skip7:
                                            val6, datafilter= reaction6(answer6,answer6b, datafilter, nouns,skip7)
                                            if val6==1:
                                                answer7 = st.select_slider(label="Companion: Super in einen letzten Schritt wäre jetzt noch die Frage, wie sicher bist du dir darüber, in welcher Region du deinen Bildungsweg fortführen möchtest?",
                                                options=["Keine Anwort",'1 gar nicht','2 weniger','3 etwas','4 ziemlich', "5 sehr"],key="q7",value="Keine Anwort")
                                                answer7b=st.button("Ich weiß es gerade noch nicht, ich will mich erst einmal umsehen.", key="q7b")
                                                skip8= st.checkbox("Frage überspringen",key="s8")
                                                if answer7 or skip8:
                                                    val7= reaction7(answer7,answer7b, skip8)
                                                    if val7==1:
                                                        location=datafilter["UNIname"].dropna().unique().tolist()
                                                        answer9= st.multiselect("Weißt du schon, wo?",location, default=None,max_selections=3)
                                                        skip9= st.checkbox("Frage überspringen",key="s9")
                                                        if answer9 and "Ich weiß es gerade noch nicht, ich will mich erst einmal umsehen." not in answer9 and skip9==False:
                                                            osaouput= filterosa(answer9,answer3, datafilter, osadata)
                                                            for l in osaouput:
                                                                st.write(l)
                                                            datafilter=datafilter[datafilter['UNIname'].isin(answer9)]
                                                            programm= datafilter["programname"].tolist()
                                                            uni= datafilter["UNIname"].tolist()
                                                            link= datafilter["Uniprogrammlink"].tolist()
                                                            st.write("*Companion: Momentan kommen diese Unis mit den folgenden Studiengängen infrage:*")
                                                            if len(programm)>5:
                                                                st.write("Um die Ergebnisse noch weiter einzugrenzen empfehle ich die anderen Fragen nochmal zu besuchen.")
                                                            for programmitem, uniitem , linkitem in zip(programm,uni, link):
                                                                if not pd.isna(uniitem):
                                                                    st.write(uniitem, ": ",programmitem)
                                                                    if not pd.isna(linkitem):
                                                                        st.write(linkitem)
                                                            print("FINAL SIZE")
                                                            print(datafilter.shape)
                                                        elif "Ich weiß es gerade noch nicht, ich will mich erst einmal umsehen." in answer9 or skip9:
                                                            osaouput= filterosa2(answer3, datafilter, osadata)
                                                            for l in osaouput:
                                                                st.write(l)
                                                            st.write("*Companion: Momentan kommen diese Unis mit den folgenden Studiengängen infrage:*")
                                                            programm= datafilter["programname"].tolist()
                                                            uni= datafilter["UNIname"].tolist()
                                                            link= datafilter["Uniprogrammlink"].tolist()
                                                            if len(programm)>5:
                                                                st.write("Um die Ergebnisse noch weiter einzugrenzen empfehle ich die anderen Fragen nochmal zu besuchen.")
                                                            for programmitem, uniitem , linkitem in zip(programm,uni, link):
                                                                if not pd.isna(uniitem):
                                                                    st.write(uniitem, ": ",programmitem)
                                                                    if not pd.isna(linkitem):
                                                                        st.write(linkitem)
                                                    elif val7==0:
                                                        osaouput= filterosa2(answer3, datafilter, osadata)
                                                        for l in osaouput:
                                                            st.write(l)
                                                        st.write("*Companion: Momentan kommen diese Unis mit den folgenden Studiengängen infrage:*")
                                                        programm= datafilter["programname"].tolist()
                                                        uni= datafilter["UNIname"].tolist()
                                                        link= datafilter["Uniprogrammlink"].tolist()
                                                        if len(programm)>5:
                                                                st.write("Um die Ergebnisse noch weiter einzugrenzen empfehle ich die anderen Fragen nochmal zu besuchen.")
                                                        for programmitem, uniitem , linkitem in zip(programm,uni, link):
                                                            if not pd.isna(uniitem):
                                                                st.write(uniitem, ": ",programmitem)
                                                                if not pd.isna(linkitem):
                                                                    st.write(linkitem)






    
            
 




    
            
 
