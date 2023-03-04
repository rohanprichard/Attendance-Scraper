import pandas as pd

def calc(d):

    del d['Hour 1']
    del d['Date']

    pres = 0
    abse = 0
    un = 0
    od = 0
    ml = 0
    tot = 0
    for i in d.columns:
        temp = 0
        
        try:
            temp = d[i].value_counts()['P']
        except: 
            temp = 0
            
        pres += temp
        tot += temp
        
        try:
            temp = d[i].value_counts()['A']
        except: 
            temp = 0
            
        abse += temp
        tot += temp

        try:
            temp = d[i].value_counts()['U']
        except: 
            temp = 0
        
        tot += temp
        un += temp
        
        try:
            temp = d[i].value_counts()['O']
        except: 
            temp = 0
        
        od += temp
        tot += temp

        try:
            temp = d[i].value_counts()['M']
        except: 
            temp = 0
        
        ml += temp
        tot += temp

    print("\n\nPhysical: ",round((((pres)/tot)*100),2),"%", end="\t")
    print("OD:",round(((od/tot)*100),2),"%\tML:",round(((ml/tot)*100),2),"%", "\tUnmarked:", round(((un/tot)*100),2),"%\tAbsent:",round(((abse/tot)*100),2),"%")
    print("\nAttendance (Unmarked + Absent):",round((100-(((abse+un)/tot) * 100)),2),"%")
    print("Attendance (Absent):",round((100-((abse/tot) * 100)),2),"%\n")
    print("Final Attendance:",round((((pres+od+ml+un)/tot) * 100),2),"%\n\n\n")
        
