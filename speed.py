from tkinter import *
import customtkinter
from PIL import Image, ImageTk
import random
from timeit import default_timer as timer
word_list=['Amount','Argument','Art','Beautiful','Belief','Cause','Certain','Chance','Change','Clear','Common','Comparison','Condition','Connection',
           'Copy','Decision','Degree','Desire','Development','Different','Education','Event','Examples','Existence','Experience','Fact','Fear',
           'Feeling','Fiction','Force','Form','Free','General','Good','Government','Happy','History','Idea','Important','Interest','Knowledge'
           ,'Law','Level','Living','Love','Material','Measure','Mind','Motion','Name','Nation','Natural','Necessary','Normal','Number',
           'Observation','Opposite','Order','Organization','Part','Place','Pleasure','Possible','Power','Probable','Property','Purpose','Quality',
           'Question','Reason','Relation','Representative','Respect','Responsible','Right','Science','Sense','Sign','Simple','Society','Sort',
           'Special','Substance','Thing','Thought','True','Use','Way','Wise','Word','Work']
customtkinter.set_appearance_mode("dark")
timeleft=60
def play_again() :
    score.destroy()
def exiting() :
    score.destroy()
    root.destroy()
def word_infom() :
    word=customtkinter.CTkToplevel(master=root)
    word.resizable(0,0)
    word.title("GameInfo")
    word.geometry("228x123+500+500")
    word.config(bg="#5daff7")
    word.grab_set()
    wordlabel=customtkinter.CTkLabel(word,text="Type the word given\n and hit enter.The timer\n will be set for\n 60 seconds.Check your\n TYPING SPEED."
                                    ,text_color="black",height=70,width=100,font=("Times new roman",20,"bold"),bg_color="#5daff7")
    wordlabel.place(relx=0,rely=0)
start=0
end=0
timelist=[]
correct_word=0
wrong_word=0
correct_word_list=[]
wrong_word_list=[]
def gtimer() :
    global score,timeleft
    if timeleft>0 :
        timeleft-=1
        timecount.configure(text=timeleft)
        timecount.after(1000,gtimer)
    else :
        entry.delete(0,END)
        entry.configure(state=DISABLED) 
        timeleft=60
        wordcount.configure(text=0)
        timecount.configure(text=60)
        finalscore=correct_word-wrong_word    
        score=customtkinter.CTkToplevel(root)
        score.geometry("713x450+250+100")
        score.resizable(0,0)
        score.title("Score")
        score.config(bg="#5daff7")
        score.grab_set()
        correctlabel=customtkinter.CTkLabel(master=score,bg_color="#5daff7",text="Correct Words",font=("Times new roman",25,"bold"),
                                  text_color="darkblue")
        correctlabel.place(relx=0.06,rely=0.06)
        correctwordstext=customtkinter.CTkTextbox(master=score,font=("Times new roman",20,"bold"),bg_color="#5daff7",fg_color="#5daff7",
                                  text_color="darkblue")
        for item in correct_word_list :
            correctwordstext.insert(END,item+"\n")
        correctwordstext.place(relx=0.06,rely=0.15)
        timelabel=customtkinter.CTkLabel(master=score,bg_color="#5daff7",text="Time taken",font=("Times new roman",25,"bold"),
                                  text_color="darkblue")
        timelabel.place(relx=0.38,rely=0.06)
        timetext=customtkinter.CTkTextbox(master=score,font=("Times new roman",20,"bold"),bg_color="#5daff7",fg_color="#5daff7",
                                  text_color="darkblue")
        for item in timelist :
            k=str(item)
            m=k[:4]
            timetext.insert(END,m+"\n")
        timetext.place(relx=0.38,rely=0.15)
        wronglabel=customtkinter.CTkLabel(master=score,bg_color="#5daff7",text="Wrong Words",font=("Times new roman",25,"bold"),
                                  text_color="darkblue")
        wronglabel.place(relx=0.7,rely=0.06)
        wrongwordstext=customtkinter.CTkTextbox(master=score,font=("Times new roman",20,"bold"),bg_color="#5daff7",fg_color="#5daff7",
                                  text_color="darkblue")
        for item in wrong_word_list :
            wrongwordstext.insert(END,item+"\n")
        wrongwordstext.place(relx=0.7,rely=0.15)           
        coolimage=customtkinter.CTkImage(dark_image=Image.open("cool.png"),size=(60,60))
        sadimage=customtkinter.CTkImage(dark_image=Image.open("sad.png"),size=(60,60))
        happyimage=customtkinter.CTkImage(dark_image=Image.open("happy.png"),size=(60,60))
        if finalscore <=10 :
            emoji1=customtkinter.CTkLabel(master=score,bg_color="#5daff7",text=" ",font=("Times new roman",40,"bold"),text_color="#0949f9",
                              image=sadimage,compound="center",height=50)
            emoji1.place(relx=0.06,rely=0.65)
            emoji2=customtkinter.CTkLabel(master=score,bg_color="#5daff7",text=" ",font=("Times new roman",40,"bold"),text_color="#0949f9",
                              image=sadimage,compound="center",height=50)
            emoji2.place(relx=0.89,rely=0.65)
        elif finalscore < 20 and finalscore> 10 :
            emoji1=customtkinter.CTkLabel(master=score,bg_color="#5daff7",text=" ",font=("Times new roman",40,"bold"),text_color="#0949f9",
                              image=happyimage,compound="center",height=50)
            emoji1.place(relx=0.06,rely=0.65)
            emoji2=customtkinter.CTkLabel(master=score,bg_color="#5daff7",text=" ",font=("Times new roman",40,"bold"),text_color="#0949f9",
                              image=happyimage,compound="center",height=50)
            emoji2.place(relx=0.89,rely=0.65)
        else :
            emoji1=customtkinter.CTkLabel(master=score,bg_color="#5daff7",text=" ",font=("Times new roman",40,"bold"),text_color="#0949f9",
                              image=coolimage,compound="center",height=50)
            emoji1.place(relx=0.06,rely=0.65)
            emoji2=customtkinter.CTkLabel(master=score,bg_color="#5daff7",text=" ",font=("Times new roman",40,"bold"),text_color="#0949f9",
                              image=coolimage,compound="center",height=50)
            emoji2.place(relx=0.89,rely=0.65)
        finallscore=customtkinter.CTkLabel(master=score,bg_color="#5daff7",text="Finalscore = "+ str(finalscore),font=("Times new roman",40,"bold")
                                           ,text_color="darkblue",height=50)        
        finallscore.place(relx=0.35,rely=0.62)           
        playagain=customtkinter.CTkButton(master=score,width=80,height=40,text="Play again",bg_color="#5daff7",font=("times new roman",20,"bold"),
                                 fg_color="#0949f9",hover=True,command=play_again,text_color="white")
        playagain.place(relx=0.3,rely=0.74)   
        exitt=customtkinter.CTkButton(master=score,width=80,height=40,text="Exit",bg_color="#5daff7",font=("times new roman",20,"bold"),
                                 fg_color="#0949f9",hover=True,command=exiting,text_color="white")
        exitt.place(relx=0.65,rely=0.74) 
i=0
def play_game(event) :
    global i,correct_word,wrong_word,correct_word_list,wrong_word_list,start,end,timelist
    i+=1
    wordcount.configure(text=i) 
    if entry.get() == word.cget("text"):
        end=timer()
        timelist.append(end-start)
        correct_word+=1
        correct_word_list.append(entry.get())
    else :
        wrong_word+=1
        end=timer()
        wrong_word_list.append(entry.get())
    random.shuffle(word_list)
    word.configure(text=word_list[0])
    entry.delete(0,END)
    start=timer()
def start() :
    global start
    entry.configure(state=NORMAL)
    gtimer()
    start=timer()
root=customtkinter.CTk()
root.geometry("700x600+250+50")
root.resizable(0,0)
root.config(bg="#5daff7")
root.resizable(False,False)
root.title("Typing Speed Tester")
root.grid_rowconfigure(0, weight=0)
root.grid_columnconfigure(0, weight=0)
speed=customtkinter.CTkImage(dark_image=Image.open("speedometer.png"),size=(120,120))
speedlabel=customtkinter.CTkLabel(master=root,image=speed,bg_color="#5daff7",text=" ")
speedlabel.place(relx=0.44,rely=0.1)
timerimage=customtkinter.CTkImage(dark_image=Image.open("stopwatch.png"),size=(30,30))
timerlabel=customtkinter.CTkLabel(master=root,image=timerimage,bg_color="#5daff7",text=" Timer",compound="left",font=("Times new roman",30,"bold"),
                                  text_color="darkblue")
timerlabel.place(relx=0.8,rely=0.1)
timecount=customtkinter.CTkLabel(master=root,bg_color="#5daff7",text=60,font=("Times new roman",40,"bold"),text_color="darkblue",height=50)
timecount.place(relx=0.85,rely=0.17)
wordsimage=customtkinter.CTkImage(dark_image=Image.open("puzzle.png"),size=(30,30))
wordslabel=customtkinter.CTkLabel(master=root,image=wordsimage,bg_color="#5daff7",text=" Words",compound="left",font=("Times new roman",30,"bold"),
                                  text_color="darkblue")
wordslabel.place(relx=0.07,rely=0.1)
wordcount=customtkinter.CTkLabel(master=root,bg_color="#5daff7",text=0,font=("Times new roman",40,"bold"),text_color="darkblue",height=50)
wordcount.place(relx=0.15,rely=0.17)
random.shuffle(word_list)
word=customtkinter.CTkLabel(master=root,bg_color="#5daff7",height=40,width=120,text=word_list[0],font=("Times new roman",30,"bold"),
                            text_color="darkblue")
word.place(relx=0.43,rely=0.4)
entry=customtkinter.CTkEntry(master=root,width=300,height=100,corner_radius=8,bg_color="#5daff7",font=("Times new roman",60,"bold"),
                             placeholder_text=" ",state=DISABLED)
entry.place(relx=0.3,rely=0.5)
wordinfoimage=customtkinter.CTkImage(dark_image=Image.open("up-arrow.png"),size=(30,30))
wordinfo=customtkinter.CTkButton(master=root,width=10,height=20,image=wordinfoimage,text=" ",bg_color="#5daff7",
                                 fg_color="#5daff7",hover=False,command=word_infom)
wordinfo.place(relx=0.48,rely=0.68)
play=customtkinter.CTkButton(master=root,width=80,height=40,text="Start",bg_color="#5daff7",font=("times new roman",20,"bold"),
                                 fg_color="#0949f9",hover=True,command=start,text_color="white")
play.place(relx=0.47,rely=0.9)
root.bind('<Return>',play_game)
root.mainloop()
