import tkinter 
from tkinter import *

adj = noun = Pluralnoun = name = adj2 = clothing = noun2 = place = Pluralnoun2 = None
adj3 = bodypart = alphabet = celeb = Pluralnoun3 = adj4 = adj5 = verb = Pluralnoun4 = num = None


def play_click():
    global adj, noun, Pluralnoun, name, adj2, clothing, noun2, place, Pluralnoun2, adj3, bodypart, alphabet, celeb, Pluralnoun3, adj4, adj5, verb, Pluralnoun4, num
    
    play.place_forget()
     
    submit.place(x=300,y=300)
    adjlabel= Label(Screen, text=" Enter Adjective")
    adj=Entry(Screen)   
   
    
    nounlabel= Label(Screen, text=" Enter Noun")
    noun=Entry(Screen)
    
    Pluralnounlabel= Label(Screen, text=" Enter Plural Noun")
    Pluralnoun=Entry(Screen)  
    
    nameLabel= Label(Screen, text=" Name(female)")
    name=Entry(Screen)        
    
    adj2label= Label(Screen, text=" Enter Adjective")
    adj2=Entry(Screen)   
        
    clothinglabel= Label(Screen, text=" Enter clothing Item")
    clothing=Entry(Screen)     
    
    noun2label= Label(Screen, text=" Enter Noun")
    noun2=Entry(Screen)    
    
    placelabel= Label(Screen, text="Enter City")
    place=Entry(Screen)
    
    Pluralnoun2label= Label(Screen, text=" Enter Plural Noun")
    Pluralnoun2=Entry(Screen)      
    
    adj3label= Label(Screen, text=" Enter Adjective")
    adj3=Entry(Screen)     
    
    place2label= Label(Screen, text="Enter place")
    place2=Entry(Screen)    
    
    bodypartlabel= Label(Screen, text=" Enter Bodypart")
    bodypart=Entry(Screen)      
    
    alphabetlabel=Label(Screen, text=" Enter Alphabet")
    alphabet=Entry(Screen)      
    
    celeblabel=Label(Screen, text=" Enter Celebrity")
    celeb=Entry(Screen)          
    
    Pluralnoun3label= Label(Screen, text=" Enter Plural Noun")
    Pluralnoun3=Entry(Screen)  
    
    adj4label= Label(Screen, text=" Enter Adjective")
    adj4=Entry(Screen)       
    
    adj5label= Label(Screen, text=" Enter Adjective")
    adj5=Entry(Screen)      
    
    verblabel= Label(Screen, text=" Enter verb")
    verb=Entry(Screen)       
    
    Pluralnoun4label= Label(Screen, text=" Enter Plural Noun")
    Pluralnoun4=Entry(Screen)      
    
    numlabel= Label(Screen, text="Enter Number")
    num=Entry(Screen)    
    
    
    
    

    adjlabel.place(x=5,y=100)
    adj.place(x=100,y=100)    
    
    nounlabel.place(x=5,y=130)
    noun.place(x=100,y=130)
    
    Pluralnounlabel.place(x=5,y=160)
    Pluralnoun.place(x=105,y=160)  
    
    nameLabel.place(x=5,y=190)
    name.place(x=100,y=190)  
    
    adj2label.place(x=5,y=220)
    adj2.place(x=100,y=220) 
    
    clothinglabel.place(x=5,y=250)
    clothing.place(x=115,y=250)     
    
    noun2label.place(x=5,y=280)
    noun2.place(x=100,y=280)    
    
    placelabel.place(x=5,y=310)
    place.place(x=100,y=310)  
    
    Pluralnoun2label.place(x=5,y=340)
    Pluralnoun2.place(x=105,y=340)      
    
    adj3label.place(x=5,y=370)
    adj3.place(x=100,y=370)      
    
    place2label.place(x=5,y=400)
    place2.place(x=100,y=400)      
    
    bodypartlabel.place(x=5,y=430)
    bodypart.place(x=100,y=430)        
    
    alphabetlabel.place(x=5,y=460)
    alphabet.place(x=100,y=460)      
  
  
    celeblabel.place(x=5,y=490)
    celeb.place(x=100,y=490)   
    
    
    
    Pluralnoun3label.place(x=250,y=100)
    Pluralnoun3.place(x=355,y=100)    
    
    adj4label.place(x=250,y=130)
    adj4.place(x=355,y=130)     
    
    adj5label.place(x=250,y=160)
    adj5.place(x=355,y=160)   
    
  
    verblabel.place(x=250,y=190)
    verb.place(x=355,y=190)       
    
    Pluralnoun4label.place(x=250,y=220)
    Pluralnoun4.place(x=355,y=220)     
    
    numlabel.place(x=250,y=250)
    num.place(x=355,y=250)          

def submit():
    global adj, noun, Pluralnoun, name, adj2, clothing, noun2, place, Pluralnoun2, adj3, bodypart, alphabet, celeb, Pluralnoun3, adj4, adj5, verb, Pluralnoun4, num
    

    adj_value = adj.get()
    noun_value = noun.get()   
    Pluralnoun_value=Pluralnoun.get()
    name_value=name.get()
    adj2_value=adj2.get()
    clothing_value=clothing.get()
    noun2_value=noun2.get()
    place_value=place.get()
    Pluralnoun2_value=Pluralnoun2.get()
    adj3_value=adj3.get()
    place2_value=place2.get()
    bodypart_value=bodypart.get()
    alphabet_value=alphabet.get()
    celeb_value= celeb.get()
    Pluralnoun3_value=Pluralnoun3.get()
    adj4_value=adj4.get()
    adj5_value=adj5.get()
    verb_value =verb.get()
    Pluralnoun4_value=Pluralnoun4.get()
    num_value=num.get()

    mad_libs_text = f"There are many {adj_value} ways to choose a/an {noun_value} to read. "
    mad_libs_text+= f"\nFirst, you could ask for recommendations from your friends and {Pluralnoun_value}."
    mad_libs_text+= f"Just don't ask Aunt {name_value}- she only reads{adj2_value} books with {clothing_value}-ripping goddesses on the cover."
    mad_libs_text+=f"If your friends and family are no help, try checking out the {noun2_value} Review in The {place_value} Times."
    mad_libs_text+=f"If the {Pluralnoun2_value} featured there are too {adj3_value} for your taste, try something a little more low-{bodypart_value}, like {alphabet_value}: The {celeb_value} Magazine or {Pluralnoun3_value} Magazine."
    mad_libs_text+=f"You could also choose a book the {adj4_value}-fashioned way. "
    mad_libs_text+=f"Head to your local library or {place2_value} and browse the shelves until something catches your {} "
    


    for widget in Screen.winfo_children():
        if isinstance(widget, Label) or isinstance(widget, Entry):
            widget.place_forget()
        
    results = Label(Screen , text = mad_libs_text, wraplength=400)
    results.place(x=100, y=100)
        








Screen= tkinter.Tk()
Screen.title("Mad Libs generator")
Screen.geometry('600x600')
w=Label( Screen, text='Welcome to Mad Libs Generator  ')


play= Button(Screen , text=" Play",  width= 10 , height= 3, command= play_click )
submit=Button(Screen, text="Submit", width= 10 , height= 3,command=submit)


w.pack(padx=0, pady=10)

play.place(x=260,y=260)

Screen.mainloop()
