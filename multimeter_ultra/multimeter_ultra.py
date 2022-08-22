
from tkinter import*
from tkinter.ttk import * 
from tkinter import simpledialog
from tkinter import messagebox
from tkinter.messagebox import showinfo
ws= Tk()

class rekenwerk:
    
    def pw_µA_DC():
        ws.title("gemeten waarde")
        C = float(simpledialog.askstring("Input", "hoeveel micro Ampere heb je gemeten?", parent=ws))
        if C > 0 and C <= 4000:
            D = 0.001*C+4*0.1
        elif C > 4000 and C <= 400000:
            D = 0.001*C+4*10
        elif C > 400000 and C <= 1000000:
            D = 0.003*C+4*1000
        elif C > 1000000 and C <= 5000000:
            D = 0.01*C+4*1000
        elif C > 5000000 and C <= 10000000:
            D = 0.03*C+10*1000
        showinfo('de onzekerheid', 'de onzekerheid bij de gemeten eenheid is: ({}'.format(C) + ' ± {}'.format(D) + ') µA')       
    def pw_mA_DC():
        ws.title("gemeten waarde")
        C = float(simpledialog.askstring("Input", "hoeveel mili Ampere heb je gemeten?", parent=ws))
        if C > 0 and C <= 4:
            D = 0.001*C+4*0.0001
        elif C > 4 and C <= 400:
            D = 0.001*C+4*0.01
        elif C > 400 and C <= 1000:
            D = 0.003*C+4*1
        elif C > 1000 and C <= 5000:
            D = 0.01*C+4*1
        elif C > 5000 and C <= 10000:
            D = 0.03*C+10*1
        showinfo('de onzekerheid', 'de onzekerheid bij de gemeten eenheid is: ({}'.format(C) + ' ± {}'.format(D) + ') mA')      
    def pw_Am_DC():
        ws.title("gemeten waarde")
        C = float(simpledialog.askstring("Input", "hoeveel Ampere heb je gemeten?", parent=ws))
        if C > 0 and C <= 0.004:
            D = 0.001*C+4*0.0000001
        elif C > 0.004 and C <= 0.4:
            D = 0.001*C+4*0.00001
        elif C > 0.4 and C <= 1:
            D = 0.003*C+4*0.001
        elif C > 1 and C <= 5:
            D = 0.01*C+4*0.001
        elif C > 5 and C <= 10:
            D = 0.03*C+10*0.001
        showinfo('de onzekerheid', 'de onzekerheid bij de gemeten eenheid is: ({}'.format(C) + ' ± {}'.format(D) + ') A')
    
    def pw_µA_AC():
        ws.title("gemeten waarde")
        C = float(simpledialog.askstring("Input", "hoeveel micro Ampere heb je gemeten?", parent=ws))
        if C > 0 and C <= 1000:
            D = 0.005*C+4*1
        elif C > 1000 and C <= 100000:
            D = 0.005*C+4*100
        elif C > 100000 and C <= 1000000:
            D = 0.008*C+4*10000
        elif C > 1000000 and C <= 5000000:
            D = 0.015*C+4*10000
        elif C > 5000000 and C <= 10000000:
            D = 0.03*C+4*10000
        showinfo('de onzekerheid', 'de onzekerheid bij de gemeten eenheid is: ({}'.format(C) + ' ± {}'.format(D) + ') µA')      
    def pw_mA_AC():
        ws.title("gemeten waarde")
        C = float(simpledialog.askstring("Input", "hoeveel mili Ampere heb je gemeten?", parent=ws))
        if C > 0 and C <= 1:
            D = 0.005*C+4*0.001
        elif C > 1 and C <= 100:
            D = 0.005*C+4*0.1
        elif C > 100 and C <= 1000:
            D = 0.008*C+4*10
        elif C > 1000 and C <= 5000:
            D = 0.015*C+4*10
        elif C > 5000 and C <= 10000:
            D = 0.03*C+4*10
        showinfo('de onzekerheid', 'de onzekerheid bij de gemeten eenheid is: ({}'.format(C) + ' ± {}'.format(D) + ') µA')   
    def pw_Am_AC():
        ws.title("gemeten waarde")
        C = float(simpledialog.askstring("Input", "hoeveel Ampere heb je gemeten?", parent=ws))
        if C > 0 and C <= 0.001:
            D = 0.005*C+4*0.000001
        elif C > 0.001 and C <= 0.1:
            D = 0.005*C+4*0.0001
        elif C > 0.1 and C <= 1:
            D = 0.008*C+4*0.01
        elif C > 1 and C <= 5:
            D = 0.015*C+4*0.01
        elif C > 5 and C <= 10:
            D = 0.03*C+4*0.01
        showinfo('de onzekerheid', 'de onzekerheid bij de gemeten eenheid is: ({}'.format(C) + ' ± {}'.format(D) + ') µA')   
    
    def pw_µV_DC():
        ws.title("gemeten waarde")
        C = float(simpledialog.askstring("Input", "hoeveel micro Volt heb je gemeten?", parent=ws))
        if C > 0 and C <= 400000:
            D = 0.0008*C+4*10
        elif C > 400000 and C <= 4000000:
            D = 0.0008*C+4*100
        elif C > 4000000 and C <= 40000000:
            D = 0.0008*C+4*1000
        elif C > 40000000 and C <= 400000000:
            D = 0.0008*C+4*10000
        elif C > 400000000 and C <= 1000000000:
                D = 0.0009*C+4*100000
        showinfo('de onzekerheid', 'de onzekerheid bij de gemeten eenheid is: ({}'.format(C) + ' ± {}'.format(D) + ') µV')       
    def pw_mV_DC():
        ws.title("gemeten waarde")
        C = float(simpledialog.askstring("Input", "hoeveel mili Volt heb je gemeten?", parent=ws))
        if C > 0 and C <= 400:
            D = 0.0008*C+4*0.01
        elif C > 400 and C <= 4000:
            D = 0.0008*C+4*0.1
        elif C > 4000 and C <= 40000:
            D = 0.0008*C+4*1
        elif C > 40000 and C <= 400000:
            D = 0.0008*C+4*10
        elif C > 400000 and C <= 1000000:
                D = 0.0009*C+4*100
        showinfo('de onzekerheid', 'de onzekerheid bij de gemeten eenheid is: ({}'.format(C) + ' ± {}'.format(D) + ') mV')      
    def pw_Vm_DC():
        ws.title("gemeten waarde")
        C = float(simpledialog.askstring("Input", "hoeveel Volt heb je gemeten?", parent=ws))
        if C > 0 and C <= 0.4:
            D = 0.0008*C+4*0.00001
        elif C > 0.4 and C <= 4:
            D = 0.0008*C+4*0.0001
        elif C > 4 and C <= 40:
            D = 0.0008*C+4*0.001
        elif C > 40 and C <= 400:
            D = 0.0008*C+4*0.01
        elif C > 400 and C <= 1000:
                D = 0.0009*C+4*0.1
        showinfo('de onzekerheid', 'de onzekerheid bij de gemeten eenheid is: ({}'.format(C) + ' ± {}'.format(D) + ') V')
    def pw_kV_DC():
        ws.title("gemeten waarde")
        C = float(simpledialog.askstring("Input", "hoeveel kilo Volt heb je gemeten?", parent=ws))
        if C > 0 and C <= 0.0004:
            D = 0.0008*C+4*0.00000001
        elif C > 0.0004 and C <= 0.004:
            D = 0.0008*C+4*0.0000001
        elif C > 0.004 and C <= 0.04:
            D = 0.0008*C+4*0.000001
        elif C > 0.04 and C <= 0.4:
            D = 0.0008*C+4*0.00001
        elif C > 0.4 and C <= 1:
                D = 0.0009*C+4*0.0001
        showinfo('de onzekerheid', 'de onzekerheid bij de gemeten eenheid is: ({}'.format(C) + ' ± {}'.format(D) + ') kV')
        ws.title("gemeten waarde")
        C = float(simpledialog.askstring("Input", "hoeveel mega Volt heb je gemeten?", parent=ws))
        if C > 0 and C <= 0.0000004:
            D = 0.0008*C+4*0.00000000001
        elif C > 0.0000004 and C <= 0.000004:
            D = 0.0008*C+4*0.0000000001
        elif C > 0.000004 and C <= 0.00004:
            D = 0.0008*C+4*0.000000001
        elif C > 0.00004 and C <= 0.0004:
            D = 0.0008*C+4*0.00000001
        elif C > 0.0004 and C <= 0.001:
                D = 0.0009*C+4*0.0000001
        showinfo('de onzekerheid', 'de onzekerheid bij de gemeten eenheid is: ({}'.format(C) + ' ± {}'.format(D) + ') MV')
    
    def pw_µV_AC():
        ws.title("Hertz?")
        C = float(simpledialog.askstring("Input", "hoeveel Hertz heb je gemeten?", parent=ws))
        if C > 45 and C <= 400:
            C = float(simpledialog.askstring("Input", "hoeveel micro ampere heb je gemeten?", parent=ws))
            if C > 0 and C <= 400000:
                D = 0.005*C+4*100
            elif C > 400000 and C <= 4000000:
                D = 0.005*C+4*1000
            elif C > 4000000 and C <= 40000000:
                D = 0.005*C+4*10000
            elif C > 40000000 and C <= 400000000:
                D = 0.005*C+4*100000
            elif C > 400000000 and C <= 750000000:
                    D = 0.01*C+4*1000000
            showinfo('de onzekerheid', 'de onzekerheid bij de gemeten eenheid is: ({}'.format(C) + ' ± {}'.format(D) + ') µV') 
        elif C > 400 and C <= 5000:
            C = float(simpledialog.askstring("Input", "hoeveel micro Volt heb je gemeten?", parent=ws))
            if C > 0 and C <= 400000:
                D = 0.01*C+4*100
            elif C > 400000 and C <= 4000000:
                D = 0.02*C+4*1000
            elif C > 4000000 and C <= 40000000:
                D = 0.02*C+4*10000
            elif C > 40000000 and C <= 400000000:
                D = 0.03*C+4*100000 
            showinfo('de onzekerheid', 'de onzekerheid bij de gemeten eenheid is: ({}'.format(C) + ' ± {}'.format(D) + ') µV') 
        elif C > 5000 and C <= 20000:
            C = float(simpledialog.askstring("Input", "hoeveel micro Volt heb je gemeten?", parent=ws))
            if C > 0 and C <= 400000:
                D = 0.03*C+4*100
            elif C > 400000 and C <= 4000000:
                D = 0.05*C+4*1000
            elif C > 4000000 and C <= 40000000:
                D = 0.05*C+4*10000
            elif C > 40000000 and C <= 400000000:
                D = 0.05*C+4*100000 
            showinfo('de onzekerheid', 'de onzekerheid bij de gemeten eenheid is: ({}'.format(C) + ' ± {}'.format(D) + ') µV')   
    def pw_mV_AC():
        ws.title("Hertz?")
        C = float(simpledialog.askstring("Input", "hoeveel Hertz heb je gemeten?", parent=ws))
        if C > 45 and C <= 400:
            C = float(simpledialog.askstring("Input", "hoeveel mili Volt heb je gemeten?", parent=ws))
            if C > 0 and C <= 400:
                D = 0.005*C+4*0.1
            elif C > 400 and C <= 4000:
                D = 0.005*C+4*1
            elif C > 4000 and C <= 40000:
                D = 0.005*C+4*10
            elif C > 40000 and C <= 400000:
                D = 0.005*C+4*100
            elif C > 400000 and C <= 750000:
                    D = 0.01*C+4*1000
            showinfo('de onzekerheid', 'de onzekerheid bij de gemeten eenheid is: ({}'.format(C) + ' ± {}'.format(D) + ') µV') 
        elif C > 400 and C <= 5000:
            C = float(simpledialog.askstring("Input", "hoeveel mili Volt heb je gemeten?", parent=ws))
            if C > 0 and C <= 400:
                D = 0.01*C+4*0.1
            elif C > 400 and C <= 4000:
                D = 0.02*C+4*1
            elif C > 4000 and C <= 40000:
                D = 0.02*C+4*10
            elif C > 40000 and C <= 400000:
                D = 0.03*C+4*100 
            showinfo('de onzekerheid', 'de onzekerheid bij de gemeten eenheid is: ({}'.format(C) + ' ± {}'.format(D) + ') mV') 
        elif C > 5000 and C <= 20000:
            C = float(simpledialog.askstring("Input", "hoeveel mili Volt heb je gemeten?", parent=ws))
            if C > 0 and C <= 400:
                D = 0.03*C+4*0.1
            elif C > 400 and C <= 4000:
                D = 0.05*C+4*1
            elif C > 4000 and C <= 40000:
                D = 0.05*C+4*10
            elif C > 40000 and C <= 400000:
                D = 0.05*C+4*100 
            showinfo('de onzekerheid', 'de onzekerheid bij de gemeten eenheid is: ({}'.format(C) + ' ± {}'.format(D) + ') V') 
    def pw_Vm_AC():
         ws.title("Hertz?")
         C = float(simpledialog.askstring("Input", "hoeveel Hertz heb je gemeten?", parent=ws))
         if C > 45 and C <= 400:
             C = float(simpledialog.askstring("Input", "hoeveel Volt heb je gemeten?", parent=ws))
             if C > 0 and C <= 0.4:
                 D = 0.005*C+4*0.0001
             elif C > 0.4 and C <= 4:
                 D = 0.005*C+4*0.001
             elif C > 4 and C <= 40:
                 D = 0.005*C+4*0.01
             elif C > 40 and C <= 400:
                 D = 0.005*C+4*0.1
             elif C > 400 and C <= 750:
                     D = 0.01*C+4*1
             showinfo('de onzekerheid', 'de onzekerheid bij de gemeten eenheid is: ({}'.format(C) + ' ± {}'.format(D) + ') µV') 
         elif C > 400 and C <= 5000:
             C = float(simpledialog.askstring("Input", "hoeveel Volt heb je gemeten?", parent=ws))
             if C > 0 and C <= 0.4:
                 D = 0.01*C+4*0.0001
             elif C > 0.4 and C <= 4:
                 D = 0.02*C+4*0.001
             elif C > 4 and C <= 40:
                 D = 0.02*C+4*0.01
             elif C > 40 and C <= 400:
                 D = 0.03*C+4*0.1 
             showinfo('de onzekerheid', 'de onzekerheid bij de gemeten eenheid is: ({}'.format(C) + ' ± {}'.format(D) + ') mV') 
         elif C > 5000 and C <= 20000:
             C = float(simpledialog.askstring("Input", "hoeveel Volt heb je gemeten?", parent=ws))
             if C > 0 and C <= 0.4:
                 D = 0.03*C+4*0.0001
             elif C > 0.4 and C <= 4:
                 D = 0.05*C+4*0.001
             elif C > 4 and C <= 40:
                 D = 0.05*C+4*0.01
             elif C > 40 and C <= 400:
                 D = 0.05*C+4*0.1 
             showinfo('de onzekerheid', 'de onzekerheid bij de gemeten eenheid is: ({}'.format(C) + ' ± {}'.format(D) + ') V') 
    def pw_kV_AC():
        ws.title("Hertz?")
        C = float(simpledialog.askstring("Input", "hoeveel Hertz heb je gemeten?", parent=ws))
        if C > 45 and C <= 400:
            C = float(simpledialog.askstring("Input", "hoeveel Volt heb je gemeten?", parent=ws))
            if C > 0 and C <= 0.0004:
                D = 0.005*C+4*0.0000001
            elif C > 0.0004 and C <= 0.004:
                D = 0.005*C+4*0.000001
            elif C > 0.004 and C <= 0.04:
                D = 0.005*C+4*0.00001
            elif C > 0.04 and C <= 0.4:
                D = 0.005*C+4*0.0001
            elif C > 0.4 and C <= 0.75:
                D = 0.01*C+4*0.001
            showinfo('de onzekerheid', 'de onzekerheid bij de gemeten eenheid is: ({}'.format(C) + ' ± {}'.format(D) + ') µV') 
        elif C > 400 and C <= 5000:
            C = float(simpledialog.askstring("Input", "hoeveel Volt heb je gemeten?", parent=ws))
            if C > 0 and C <= 0.0004:
                D = 0.01*C+4*0.0000001
            elif C > 0.0004 and C <= 0.004:
                D = 0.02*C+4*0.000001
            elif C > 0.004 and C <= 0.04:
                D = 0.02*C+4*0.00001
            elif C > 0.04 and C <= 0.4:
                D = 0.03*C+4*0.0001
            showinfo('de onzekerheid', 'de onzekerheid bij de gemeten eenheid is: ({}'.format(C) + ' ± {}'.format(D) + ') mV') 
        elif C > 5000 and C <= 20000:
            C = float(simpledialog.askstring("Input", "hoeveel Volt heb je gemeten?", parent=ws))
            if C > 0 and C <= 0.0004:
                D = 0.03*C+4*0.0000001
            elif C > 0.0004 and C <= 0.004:
                D = 0.03*C+4*0.000001
            elif C > 0.004 and C <= 0.04:
                D = 0.05*C+4*0.00001
            elif C > 0.04 and C <= 0.4:
                D = 0.05*C+4*0.0001
            showinfo('de onzekerheid', 'de onzekerheid bij de gemeten eenheid is: ({}'.format(C) + ' ± {}'.format(D) + ') V')
        ws.title("Hertz?")
        C = float(simpledialog.askstring("Input", "hoeveel Hertz heb je gemeten?", parent=ws))
        if C > 45 and C <= 400:
            C = float(simpledialog.askstring("Input", "hoeveel Volt heb je gemeten?", parent=ws))
            if C > 0 and C <= 0.0000004:
                D = 0.005*C+4*0.0000000001
            elif C > 0.0000004 and C <= 0.000004:
                D = 0.005*C+4*0.000000001
            elif C > 0.000004 and C <= 0.00004:
                D = 0.005*C+4*0.00000001
            elif C > 0.00004 and C <= 0.0004:
                D = 0.005*C+4*0.0000001
            elif C > 0.0004 and C <= 0.00075:
                D = 0.01*C+4*0.000001
            showinfo('de onzekerheid', 'de onzekerheid bij de gemeten eenheid is: ({}'.format(C) + ' ± {}'.format(D) + ') µV') 
        elif C > 400 and C <= 5000:
            C = float(simpledialog.askstring("Input", "hoeveel Volt heb je gemeten?", parent=ws))
            if C > 0 and C <= 0.0000004:
                D = 0.01*C+4*0.0000000001
            elif C > 0.0000004 and C <= 0.000004:
                D = 0.02*C+4*0.000000001
            elif C > 0.000004 and C <= 0.00004:
                D = 0.02*C+4*0.00000001
            elif C > 0.00004 and C <= 0.0004:
                D = 0.03*C+4*0.0000001
            showinfo('de onzekerheid', 'de onzekerheid bij de gemeten eenheid is: ({}'.format(C) + ' ± {}'.format(D) + ') mV') 
        elif C > 5000 and C <= 20000:
            C = float(simpledialog.askstring("Input", "hoeveel Volt heb je gemeten?", parent=ws))
            if C > 0 and C <= 0.0000004:
                D = 0.03*C+4*0.0000000001
            elif C > 0.0000004 and C <= 0.000004:
                D = 0.03*C+4*0.000000001
            elif C > 0.000004 and C <= 0.00004:
                D = 0.05*C+4*0.00000001
            elif C > 0.00004 and C <= 0.0004:
                D = 0.05*C+4*0.0000001
            showinfo('de onzekerheid', 'de onzekerheid bij de gemeten eenheid is: ({}'.format(C) + ' ± {}'.format(D) + ') V')
    
    def popup_win_mR():
        ws.title("gemeten waarde")
        C = float(simpledialog.askstring("Input", "hoeveel mili weerstand heb je gemeten?", parent=ws))
        if C > 0 and C <= 400000:
            D = 0.0015*C+6*10
        elif C > 400000 and C <= 4000000:
            D = 0.001*C+4*100
        elif C > 4000000 and C <= 40000000:
            D = 0.001*C+4*1000
        elif C > 40000000 and C <= 400000000:
            D = 0.0015*C+4*10000
        elif C > 400000000 and C <=4000000000:
            D = 0.003*C+6*100000
        elif C > 4000000000 and C <=40000000000:
            D = 0.01*C+10*1000000
        showinfo('de onzekerheid', 'de onzekerheid bij de gemeten eenheid is: ({}'.format(C) + ' ± {}'.format(D) + ') mΩ')
    def popup_win_Rm():
        ws.title("gemeten waarde")
        C = float(simpledialog.askstring("Input", "hoeveel weerstand heb je gemeten?", parent=ws))
        if C > 0 and C <= 400:
            D = 0.0015*C+6*0.01
        elif C > 400 and C <= 4000:
            D = 0.001*C+4*0.1
        elif C > 4000 and C <= 40000:
            D = 0.001*C+4*1
        elif C > 40000 and C <= 400000:
            D = 0.0015*C+4*10
        elif C > 400000 and C <=4000000:
            D = 0.003*C+6*100
        elif C > 4000000 and C <=40000000:
            D = 0.01*C+10*1000
        showinfo('de onzekerheid', 'de onzekerheid bij de gemeten eenheid is: ({}'.format(C) + ' ± {}'.format(D) + ') Ω')
    def popup_win_kR():
        ws.title("gemeten waarde")
        C = float(simpledialog.askstring("Input", "hoeveel kilo Ohm heb je gemeten?", parent=ws))
        if C > 0 and C <= 0.4:
            D = 0.0015*C+6*0.00001
        elif C > 0.4 and C <= 4:
            D = 0.001*C+4*0.0001
        elif C > 4 and C <= 40:
            D = 0.001*C+4*0.001
        elif C > 40 and C <= 400:
            D = 0.0015*C+4*0.01
        elif C > 400 and C <=4000:
            D = 0.003*C+6*0.1
        elif C > 4000 and C <=40000:
            D = 0.01*C+10*1
        showinfo('de onzekerheid', 'de onzekerheid bij de gemeten eenheid is: ({}'.format(C) + ' ± {}'.format(D) + ') kΩ')
    def popup_win_MR():  
        ws.title("gemeten waarde")
        C = float(simpledialog.askstring("Input", "hoeveel kilo Ohm heb je gemeten?", parent=ws))
        if C > 0 and C <= 0.0004:
            D = 0.0015*C+6*0.00000001
        elif C > 0.0004 and C <= 0.004:
            D = 0.001*C+4*0.0000001
        elif C > 0.004 and C <= 0.04:
            D = 0.001*C+4*0.000001
        elif C > 0.04 and C <= 0.4:
            D = 0.0015*C+4*0.00001
        elif C > 0.4 and C <=4:
            D = 0.003*C+6*0.0001
        elif C > 4 and C <=40:
            D = 0.01*C+10*0.001
        showinfo('de onzekerheid', 'de onzekerheid bij de gemeten eenheid is: ({}'.format(C) + ' ± {}'.format(D) + ') MΩ')

class DMM1:
    
    ws.title("DMM onzekerheid berekenen, door Jort Joris Leroij   Technische Natuurkunde - hhs Delft")
    ws.geometry("2400x1200")
    ws.config(bg='#5FB691')
    Label(ws, text="de onnauwkeurigheid berekenen van de digitale multimeter", font= ('Helvetica 15 bold')).pack(pady=20)

    label2= Label()
    button_µA= Button()
    button_mA= Button()
    button_A= Button()
    button_µU= Button()
    button_mU= Button()
    button_U= Button()
    button_mΩ= Button()
    button_Ω= Button()
    button_kΩ= Button()
    button_MΩ= Button()

    def pw_A_DC():
        DMM1.HOME()  
        DMM1.label2= Label(ws, text="selecteer een grootheid voor het direct current amperage", font= ('Helvetica 15 bold'))
        DMM1.label2.pack(pady=20)
             
        DMM1.button_µA= Button(ws, text= "µA", style='W.TButton', command= rekenwerk.pw_µA_DC)
        DMM1.button_mA= Button(ws, text= "mA", style='W.TButton', command= rekenwerk.pw_mA_DC)
        DMM1.button_A= Button(ws, text= "A", style='W.TButton', command= rekenwerk.pw_Am_DC)
     
        DMM1.button_µA.pack(pady=10)
        DMM1.button_mA.pack(pady=10)
        DMM1.button_A.pack(pady=10)
    def pw_A_AC():
        DMM1.HOME()  
        DMM1.label2= Label(ws, text="selecteer een grootheid voor het alternating current amperage", font= ('Helvetica 15 bold'))
        DMM1.label2.pack(pady=20)
     
        DMM1.button_µA= Button(ws, text= "µA", style='W.TButton', command= rekenwerk.pw_µA_AC)
        DMM1.button_mA= Button(ws, text= "mA", style='W.TButton', command= rekenwerk.pw_mA_AC)
        DMM1.button_A= Button(ws, text= "A", style='W.TButton', command= rekenwerk.pw_Am_AC)
     
        DMM1.button_µA.pack(pady=10)
        DMM1.button_mA.pack(pady=10)
        DMM1.button_A.pack(pady=10)
       
    def pw_V_DC():
       DMM1.HOME() 
       DMM1.label2= Label(ws, text="selecteer een grootheid voor het direct current voltage", font= ('Helvetica 15 bold'))
       DMM1.label2.pack(pady=20)
    
       DMM1.button_µU= Button(ws, text= "µV", style='W.TButton', command= rekenwerk.pw_µV_DC)
       DMM1.button_mU= Button(ws, text= "mV", style='W.TButton', command= rekenwerk.pw_mV_DC)
       DMM1.button_U= Button(ws, text= "V", style='W.TButton', command= rekenwerk.pw_Vm_DC)
    
       DMM1.button_µU.pack(pady=10)
       DMM1.button_mU.pack(pady=10)
       DMM1.button_U.pack(pady=10)
    def pw_V_AC():
        DMM1.HOME() 
        DMM1.label2= Label(ws, text="selecteer een grootheid voor het alternating current voltage", font= ('Helvetica 15 bold'))
        DMM1.label2.pack(pady=20)
     
        DMM1.button_µU= Button(ws, text= "µV", style='W.TButton', command= rekenwerk.pw_µV_AC)
        DMM1.button_mU= Button(ws, text= "mV", style='W.TButton', command= rekenwerk.pw_mV_AC)
        DMM1.button_U= Button(ws, text= "V", style='W.TButton', command= rekenwerk.pw_Vm_AC)
     
        DMM1.button_µU.pack(pady=10)
        DMM1.button_mU.pack(pady=10)
        DMM1.button_U.pack(pady=10)
    
    def pw_R():
       DMM1.HOME() 
       DMM1.label2= Label(ws, text="selecteer een grootheid voor de weerstand", font= ('Helvetica 15 bold'))
       DMM1.label2.pack(pady=20)
    
       DMM1.button_mΩ= Button(ws, text= "mΩ", style='W.TButton', command= rekenwerk.popup_win_mR)
       DMM1.button_Ω= Button(ws, text= "Ω", style='W.TButton', command= rekenwerk.popup_win_Rm)
       DMM1.button_kΩ= Button(ws, text= "kΩ", style='W.TButton', command= rekenwerk.popup_win_kR)
       DMM1.button_MΩ= Button(ws, text= "MΩ", style='W.TButton', command= rekenwerk.popup_win_MR)
    
       DMM1.button_mΩ.pack(pady=10)
       DMM1.button_Ω.pack(pady=10)
       DMM1.button_kΩ.pack(pady=10)
       DMM1.button_MΩ.pack(pady=10)
    
    def startknoppen():
        st = Style()
        st.configure('W.TButton', height=10, width=20, bg='#567', fg='Red', font= ('Helvetica 16 bold'))
        
        Button(ws, text= "Amperage (DC)", style='W.TButton', command= DMM1.pw_A_DC).pack(pady=10)
        Button(ws, text= "Amperage (AC)", style='W.TButton', command= DMM1.pw_A_AC).pack(pady=10)
        Button(ws, text= "voltage      (DC)", style='W.TButton', command= DMM1.pw_V_DC).pack(pady=10)
        Button(ws, text= "voltage      (AC)", style='W.TButton', command= DMM1.pw_V_AC).pack(pady=10)
        Button(ws, text= "weerstand        ", style='W.TButton', command= DMM1.pw_R).pack(pady=10)
    
    def HOME():
        DMM1.button_µA.pack_forget()
        DMM1.button_mA.pack_forget()
        DMM1.button_A.pack_forget()
        DMM1.button_µU.pack_forget()
        DMM1.button_mU.pack_forget()
        DMM1.button_U.pack_forget()
        DMM1.button_mΩ.pack_forget()
        DMM1.button_Ω.pack_forget()
        DMM1.button_kΩ.pack_forget()
        DMM1.button_MΩ.pack_forget()
        
        DMM1.label2.pack_forget()
    
DMM1.startknoppen()

ws.mainloop()
