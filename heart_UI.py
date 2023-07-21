import pickle
import numpy as np
with open('heart_model','rb') as f:
    model=pickle.load(f)
import tkinter as tk
def Input_data():
    age=int(AgeEntry.get())
    sex=int(Sex_status_var.get())
    trestbps=int(TrestbpsEntry.get())
    chol=int(CholestrolEntry.get())
    thalch=int(ThachEntry.get())
    oldp=float(OldpeakEntry.get())
    cp1=bool(Cp1_status_var.get())
    cp2=bool(Cp2_status_var.get())
    cp3=bool(Cp3_status_var.get())
    fbs1=bool(Fbs1_status_var.get())
    restecg1=bool(Restecg1_status_var.get())
    restecg2=bool(Restecg2_status_var.get())
    exang1=bool(Exang1_status_var.get())
    slope1=bool(Slope1_status_var.get())
    slope2=bool(Slope2_status_var.get())
    thal1=bool(Thal1_status_var.get())
    thal2=bool(Thal2_status_var.get())
    thal3=bool(Thal3_status_var.get())
    ca1=bool(Ca1_status_var.get())
    ca2=bool(Ca2_status_var.get())
    ca3=bool(Ca3_status_var.get())
    ca4=bool(Ca3_status_var.get())




    print(age,sex,trestbps,chol,thalch,oldp,cp1,cp2,cp3,fbs1,restecg1,restecg2,exang1,slope1,slope2, ca1, ca2, ca3, ca4, thal1, thal2, thal3)
# input_data = (58,0,100,248,122,1.0,cp1,cp2,cp3,False,False,False,False,True,False,False,False,False,False,False,True,False)
    input_data = (age,sex,trestbps,chol,thalch,oldp,cp1,cp2,cp3,fbs1,restecg1,restecg2,exang1,slope1,slope2,ca1,ca2,ca3,ca4,thal1,thal2,thal3)
    input_data_as_numpy_array= np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    y=model.predict(input_data_reshaped)
    
    window1=tk.Tk()
    window1.geometry('300x200')
    window1.title('Heart  Predicter')
    frame=tk.Frame(window1)
    frame.pack()
    if y[0]==0:
        label=tk.Label(window1,text='no risk',font=('Arial',28))
        label.pack(padx=5,pady=5)
    else :
        label=tk.Label(window1,text='desiase',font=('Arial',28))
        label.pack(padx=5,pady=5)
window=tk.Tk()
window.geometry('600x600')
window.title('Heart Disesase Predicter')
frame=tk.Frame(window)
frame.pack()
 

user_info=tk.LabelFrame(frame,text='Patient DATA')
user_info.grid(row=0,column=0,padx=2,pady=2,sticky='news')
#label for input
#---------------------------Age----------------------------------------------------------------------
labelAge=tk.Label(user_info,text='Age of patient in number:')
labelAge.grid(row=0,column=0,pady=2)
AgeEntry=tk.Entry(user_info) 
AgeEntry.grid(row=0,column=1,padx=2,pady=2)
#--------------GENDER--------------------------------------------------------------------------------- 
Sex_status_var = tk.StringVar(value="0")
Sex_check = tk.Checkbutton(user_info, text="Male",
                                       variable=Sex_status_var, onvalue="1", offvalue="0")
Sex_check.grid(row=1,column=0,padx=2,pady=2)
Sex2_status_var = tk.StringVar(value="1")
Sex2_check = tk.Checkbutton(user_info, text="Female",
                                       variable=Sex2_status_var, onvalue="0", offvalue="1")
Sex2_check.grid(row=1,column=1,padx=2,pady=2)
#-----------------------trserbps-----------------------------------------------------------------------
labelTrestbps=tk.Label(user_info,text='resting blood pressure in mm Hg (trestbps)')
labelTrestbps.grid(row=2,column=0,pady=2)
TrestbpsEntry=tk.Entry(user_info) 
TrestbpsEntry.grid(row=2,column=1,padx=2,pady=2)
#-----------------------------cholestrol-------------------------------------------------------
labelCholestrol=tk.Label(user_info,text='Patient serum cholestoral in mg/dl:')
labelCholestrol.grid(row=3,column=0,pady=2)
CholestrolEntry=tk.Entry(user_info) 
CholestrolEntry.grid(row=3,column=1,padx=2,pady=2)
#---------------------------Thach----------------------------------------------------------------------
labelThach=tk.Label(user_info,text='Thach of patient in number:')
labelThach.grid(row=4,column=0,pady=2)
ThachEntry=tk.Entry(user_info) 
ThachEntry.grid(row=4,column=1,padx=2,pady=2)

 #---------------------------Oldpeak----------------------------------------------------------------------
labelOldpeak=tk.Label(user_info,text='Oldpeak of patient in number:')
labelOldpeak.grid(row=5,column=0,pady=2)
OldpeakEntry=tk.Entry(user_info) 
OldpeakEntry.grid(row=5,column=1,padx=2,pady=2)
#----------------------------chest pain---------------------------------------------------------------
Cp1_status_var = tk.StringVar(value="")
Cp1_check = tk.Checkbutton(user_info, text="Chest pain type 1",
                                       variable=Cp1_status_var, onvalue="1", offvalue="")
Cp1_check.grid(row=6,column=0,padx=2,pady=2)
Cp2_status_var = tk.StringVar(value="")
Cp2_check = tk.Checkbutton(user_info, text="Chest pain type 2",
                                       variable=Cp2_status_var, onvalue="1", offvalue="")
Cp2_check.grid(row=6,column=1,padx=2,pady=2)
Cp3_status_var = tk.StringVar(value="")
Cp3_check = tk.Checkbutton(user_info, text="Chest pain type 3",
                                       variable=Cp3_status_var, onvalue="1", offvalue="")
Cp3_check.grid(row=7,column=1,padx=2,pady=2)
Cp0_status_var = tk.StringVar(value="")
Cp0_check = tk.Checkbutton(user_info, text="Chest pain type 0",
                                       variable=Cp0_status_var, onvalue="1", offvalue="")
Cp0_check.grid(row=7,column=0,padx=2,pady=2)

#----------------------------fbs---------------------------------------------------------------
Fbs1_status_var = tk.StringVar(value="")
Fbs1_check = tk.Checkbutton(user_info, text=" fasting blood sugar &greater:120 mg/dl ",
                                       variable=Fbs1_status_var, onvalue="1", offvalue="")
Fbs1_check.grid(row=8,column=0,padx=2,pady=2)
Fbs0_status_var = tk.StringVar(value="")
Fbs0_check = tk.Checkbutton(user_info, text=" fasting blood sugar &less: 120 mg/dl ",
                                       variable=Fbs0_status_var, onvalue="1", offvalue="")
Fbs0_check.grid(row=8,column=1,padx=2,pady=2)
#------------------------restecg----------------------------------------------------------------
Restecg0_status_var = tk.StringVar(value="")
Restecg0_check = tk.Checkbutton(user_info, text="Resting electrocardiographic results type 0",
                                       variable=Restecg0_status_var, onvalue="1", offvalue="")
Restecg0_check.grid(row=9,column=0,padx=2,pady=2)

Restecg1_status_var = tk.StringVar(value="")
Restecg1_check = tk.Checkbutton(user_info, text="Resting electrocardiographic results type 1",
                                       variable=Restecg1_status_var, onvalue="1", offvalue="")
Restecg1_check.grid(row=9,column=1,padx=2,pady=2)
Restecg2_status_var = tk.StringVar(value="")
Restecg2_check = tk.Checkbutton(user_info, text="Resting electrocardiographic results type 2",
                                       variable=Restecg2_status_var, onvalue="1", offvalue="")
Restecg2_check.grid(row=10,column=1,padx=2,pady=2)
#----------------------------------------------exang----------------------------------------
 
Exang1_status_var = tk.StringVar(value="")
Exang1_check = tk.Checkbutton(user_info, text=" exercise induced angina : yes ",
                                       variable=Exang1_status_var, onvalue="1", offvalue="")
Exang1_check.grid(row=11,column=1,padx=2,pady=2)
Exang0_status_var = tk.StringVar(value="")
Exang0_check = tk.Checkbutton(user_info, text="   exercise induced angina  : no ",
                                       variable=Exang0_status_var, onvalue="1", offvalue="")
Exang0_check.grid(row=11,column=0,padx=2,pady=2)
#--------------------------------------------slope-----------------------------------------------------
Slope0_status_var = tk.StringVar(value="")
Slope0_check = tk.Checkbutton(user_info, text="slope of the peak exercise ST segment type 0",
                                       variable=Slope0_status_var, onvalue="1", offvalue="")
Slope0_check.grid(row=12,column=0,padx=2,pady=2)

Slope1_status_var = tk.StringVar(value="")
Slope1_check = tk.Checkbutton(user_info, text="slope of the peak exercise ST segment type 1",
                                       variable=Slope1_status_var, onvalue="1", offvalue="")
Slope1_check.grid(row=12,column=1,padx=2,pady=2)
Slope2_status_var = tk.StringVar(value="")
Slope2_check = tk.Checkbutton(user_info, text="slope of the peak exercise ST segment type 2",
                                       variable=Slope2_status_var, onvalue="1", offvalue="")
Slope2_check.grid(row=13,column=0,padx=2,pady=2)
#----------------------------------------------ca1----------------------------------------------------------------
Ca0_status_var = tk.StringVar(value="")
Ca0_check = tk.Checkbutton(user_info, text="number of major vessels colored by flourosopy is 0",
                                       variable=Ca0_status_var, onvalue="1", offvalue="")
Ca0_check.grid(row=14,column=0,padx=2,pady=2)

Ca1_status_var = tk.StringVar(value="")
Ca1_check = tk.Checkbutton(user_info, text="number of major vessels colored by flourosopy 1",
                                       variable=Ca1_status_var, onvalue="1", offvalue="")
Ca1_check.grid(row=14,column=1,padx=2,pady=2)
Ca2_status_var = tk.StringVar(value="")
Ca2_check = tk.Checkbutton(user_info, text="number of major vessels colored by flourosopy 2",
                                       variable=Ca2_status_var, onvalue="1", offvalue="")
Ca2_check.grid(row=15,column=0,padx=2,pady=2)
Ca3_status_var = tk.StringVar(value="")
Ca3_check = tk.Checkbutton(user_info, text="number of major vessels colored by flourosopy 3",
                                       variable=Ca3_status_var, onvalue="1", offvalue="")
Ca3_check.grid(row=15,column=1,padx=2,pady=2)
Ca4_status_var = tk.StringVar(value="")
Ca4_check = tk.Checkbutton(user_info, text="number of major vessels colored by flourosopy 4",
                                       variable=Ca4_status_var, onvalue="1", offvalue="")
Ca4_check.grid(row=16,column=0,padx=2,pady=2)



#------------------------------------------------thal------------------------------------------------------------
Thal1_status_var = tk.StringVar(value="")
Thal1_check = tk.Checkbutton(user_info, text="normal :1",
                                       variable=Thal1_status_var, onvalue="1", offvalue="")
Thal1_check.grid(row=17,column=0,padx=2,pady=2)
Thal2_status_var = tk.StringVar(value="")
Thal2_check = tk.Checkbutton(user_info, text="fixed defect:2",
                                       variable=Thal2_status_var, onvalue="1", offvalue="")
Thal2_check.grid(row=17,column=1,padx=2,pady=2)
Thal3_status_var = tk.StringVar(value="")
Thal3_check = tk.Checkbutton(user_info, text="revereable defect:3",
                                       variable=Thal3_status_var, onvalue="1", offvalue="")
Thal3_check.grid(row=18,column=1,padx=2,pady=2)
 


#Button for submit
button=tk.Button(frame,text='Sumbit',command=Input_data)
button.grid(row=2,column=0,padx=2,pady=2)
window.mainloop()
