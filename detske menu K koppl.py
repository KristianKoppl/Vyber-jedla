import tkinter #naimportuje kniznicu tkinter
from random import * #naimportuje random kniznicu 
canvas = tkinter.Canvas(width=600, height=400,bg = 'white') #vitvory platno do premennej canvas
canvas.pack() #pprivola premennu canvas
subor = open('obediky.txt','w') #otvory sa subor obediky.txt na pisanie w (writing)


color=[] #vitvory premennu color ako zoznam 


def menu(): # vitvory podprogram menu
    x=100 #nastavi premennu x na 100 
    color=['green','red','blue','orange'] # zoznam color naplni stringom ... 
    for i in range(4): #for cyklus ktorý pojde 4-krát
        canvas.create_rectangle(x,150,x+100,250,fill= color[0+i]) #vytvori obdlznik ktori sa posunie po suradniciach a vitvory sa 4-krát a nastavi farbu 0+i čo znamena 0+ 1 + 1 + 1 + 1 
        x+=100 # prida hodnote x 100
    canvas.create_text(300,100,text='VÝBER JEDLA',font = 'Arial 30 bold') #vitvory text na suradniaciach... 
    


def vyber(event): #vitvory podprogram vyber ktory bude mat v parametroch evet
    global klik,podmysou # spravy globalnu premennu z 'klik' a 'podmysou'
    podmysou=[] # spravý z tuple  premennej zoznam
    x1, y1, x2, y2 = event.x, event.y, event.x, event.y # hodnotam x1 x2 y1 y2 priradi event x1,x2,y1,y2
    podmysou = canvas.find_overlapping(x1, y1, x2, y2) #funkcia ktorra oznacuje indexom rečeno tagom všetky prvky objekty na x1 x2 y1 a y2 suradniciach EVENT
    
    

entry1 = tkinter.Entry() #vytvory entry vstup do premmenej entry1 
entry1.pack() #privola entry1
s = 0 #vitvory premennu 's' s hodnotou 0 int
def save(event): # vitvorý podprogram save s parametrom event
    global s #nastavý s ako globálnu premennú
    s = 1 #nastavý s premennú na hodnotu 1
    
    with open('obediky.txt', 'a') as subor: #pri with funkcií neni potrebné zatvárať súbor, a bude zapisovať do suboru
        subor.write(entry1.get()+' ') #zapíše hodnoty z entry1
           
        
def vyber2(event): #vytvorý podprogram s parametrom event
    global  klik,podmysou # nastavý ako globalnú premennú: klik, podmysou 
    klik=0 #vitrvorý premennú b s hodnotou 0
    klik+= 1 # pridá premmenej b+1
    if s == 1:
        if podmysou[0] == 2 and klik == 1: # vitvorý podmienku pri ktorej musí platiť index zozoznamu 0 == 2 a b premenna 1
            with open('obediky.txt', 'a') as subor: #pri with funkcií neni potrebné zatvárať súbor, a bude zapisovať do suboru
                subor.write('z\n') # zapíše do súboru obediky.txt z a znak konca riadka /n
           
            
        if podmysou[0] == 3 and klik == 1: # vitvorý podmienku pri ktorej musí platiť index zozoznamu 0 == 3 a b premenna 1
            with open('obediky.txt', 'a') as subor: #pri with funkcií neni potrebné zatvárať súbor, a bude zapisovať do suboru
                subor.write('č\n') # zapíše do súboru obediky.txt č a znak konca riadka /n
            

        if podmysou[0] == 4 and klik == 1: # vitvorý podmienku pri ktorej musí platiť index zozoznamu 0 == 4 a b premenna 1
            with open('obediky.txt', 'a') as subor: #pri with funkcií neni potrebné zatvárať súbor, a bude zapisovať do suboru
                subor.write('m\n') # zapíše do súboru obediky.txt m a znak konca riadka /n
            
            
        if podmysou[0] == 5 and b == klik: # vitvorý podmienku pri ktorej musí platiť index zozoznamu 0 == 5 a b premenna 1
            with open('obediky.txt', 'a') as subor: #pri with funkcií neni potrebné zatvárať súbor, a bude zapisovať do suboru
                subor.write('ž\n') # zapíše do súboru obediky.txt ž a znak konca riadka /n

    if podmysou[0] == 0 and klik == 1 or podmysou[0] == 1 and klik == 1 or podmysou[0] == 6 and klik == 1 : #zakazuje vypisanie akehokolvek znaku co je mimo farieb (objednávok)
        subor.strip() #vymaže všetky znaky konca riadka z premennej subor teda zo suboru obediky.txt ak splnila sa podmienka nad timto
           





canvas.bind('<Motion>', vyber) #pohyb misi po canvase a privola podprogram 'vyber'
canvas.bind_all('<Button-3>', save) #nastavi button-3 na privolanie eventu a premennej save
label1 = tkinter.Label(text='Napíš meno:') #vitvorý text nad 'entry1' 'label1':'Napíš meno:'
label1.pack() # privola label1 ten text nad entry1
canvas.bind('<Button-1>', vyber2,) #nastavý button-1 ktorý privolá podprogram 'vyber2'
menu()#privolá funkciu menu
