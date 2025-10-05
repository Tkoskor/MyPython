import random                  
from datetime import datetime

output_file = 'andmed.txt' 
z = 0       
arvudetabel=[]    
kuupäev = datetime.now().strftime("%Y-%m-%d %H:%M:%S")      


def arvutused(arvud):                    
    summa = 0                       
    for arv in arvud:               
        summa += int(arv)                
    keskmine = summa / len(arvud)   
    suurim = max(arvud)            

    return f'Summa: {summa}\nKeskmine: {keskmine}\nSuurim arv: {suurim}' 


andmed_info = open(output_file, 'w', encoding='utf-8')
andmed_info.write(f'Kuupäev: {kuupäev}\nArvud: ')
while z<20:
    if z==0:
        number=str(random.randint(1, 100))
        z+=1
        andmed_info.write(number)
    else:
        number=str(random.randint(1, 100))
        z+=1
        andmed_info.write(" " + number)

andmed_info.close
andmed_info = open(output_file, 'r')
             

with open('andmed.txt','rt') as f: 
     next(f)
     for line in f:
         numbrid = [int(i) for i in line.strip()[1:200].split()[1:200]]
print("Failist loetud arvud:", numbrid)
print(arvutused(numbrid))
