import re
from tkinter import*
root=Tk()
root.title("Data Searching tool")
root.geometry("600x400")
root.config(bg="#1e1e1e")

found=False

def check_choice():
    choice=yon_entry.get().lower()
    if choice=="yes":
        search_message.pack_forget()
        search_label.pack_forget()
        search_entry.pack_forget()
        sub2.pack_forget()
        
        name_label.pack(pady=5)
        name_entry.pack()
        email_label.pack(pady=5)
        email_entry.pack()
        num_label.pack(pady=5)
        num_entry.pack()
        sub1.pack(pady=5)


    elif choice=="no":

        search_label.pack(pady=5)
        search_entry.pack()
        sub2.pack(pady=5)
        search_message.pack()
        
        
        name_label.pack_forget()
        name_entry.pack_forget()
        name_message.pack_forget()
        email_label.pack_forget()
        email_entry.pack_forget()
        email_message.pack_forget()
        num_label.pack_forget()
        num_entry.pack_forget()
        num_message.pack_forget()
        sub1.pack_forget()

def check1():
            name=name_entry.get()
            if re.search(r"^[a-zA-Z ]+$", name):
                name_message.config(text="Valid Name !")
                name_message.pack()
            else:
                name_message.config(text="Only Letters Are allowed")
                name_message.pack()


            email=email_entry.get()
            if re.search(r"^[a-zA-Z0-9._%+-]+@gmail\.com$",email):
                email_message.config(text="Valid Email !")
                email_message.pack()
            else:
                email_message.config(text="Enter a valid Email")
                email_message.pack()

            num=num_entry.get()
            if re.search(r"^\d{10}$",num):
                num_message.config(text="Valid Number !")
                num_message.pack()
            else:
                num_message.config(text="Enter a Valid Number")
                num_message.pack()

            found=False
            with open("sem2_project_file","a") as f:
                 f.write(name + "," + email + "," + num + "\n")
                      
                      
def check2():
     found=False
     result=""
     entered_name=search_entry.get().strip()
     
     with open("sem2_project_file","r") as f:
          for line in f:
               line=line.strip()
               data=line.split(",")
               
               if entered_name.lower()=="all":
                    result += line +"\n"
                    found=True

               elif data[0].lower()==entered_name.lower():
                    result += line + "\n"
                    found=True

     if found:
        search_message.config(text=result)
        #search_message.pack()
     else:
        search_message.config(text="No Data Found !")
        #search_message.pack()


               
               
frame = Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")    
            

main_message=Message(root,text="Do You want to Enter Data (Yes/No)?",width=150,bg="black",fg="white",padx=10,pady=5)
main_message.place(relx=0.04, rely=0.05)

yon_entry=Entry(root,relief="raised",borderwidth=3,bg="#1e1e1e",width=25,fg="white")
yon_entry.place(relx=0.04, rely=0.17)
submit=Button(root,text="Submit",command=check_choice,fg="black")
submit.pack(side="bottom",anchor="e",padx=10,pady=5)

name_label=Label(root,text="Enter Name: ",width=17,bg="black",fg="white",padx=10,pady=5)
#name_label.pack()
name_entry=Entry(root,relief="raised",borderwidth=3,bg="#1e1e1e",width=24,fg="white")
#name_entry.pack()
name_message=Message(root,text="",width=150,bg="#1e1e1e",fg="white")


email_label=Label(root,text="Enter your Email: ",width=17,bg="black",fg="white",padx=10,pady=5)
#email_label.pack()
email_entry=Entry(root,relief="raised",borderwidth=3,bg="#1e1e1e",width=24,fg="white")
#email_entry.pack()
email_message=Message(root,text="",width=150,bg="#1e1e1e",fg="white")


num_label=Label(root,text="Enter your Number",width=17,bg="black",fg="white",padx=10,pady=5)
#num_label.pack()
num_entry=Entry(root,relief="raised",borderwidth=3,bg="#1e1e1e",width=24,fg="white")
#num_entry.pack()
num_message=Message(root,text="",width=150,bg="#1e1e1e",fg="white")
sub1=Button(root,text="Save ✅",command=check1)
#sub1.pack()


search_label=Label(root,text="Search Data: ",bg="black",fg="white",padx=10,width=14)
#search_label.pack()
search_entry=Entry(root,bg="#1e1e1e",fg="white")
#search_entry.pack()
sub2=Button(root,text="Search",command=check2)
#sub2.pack()

search_message=Message(root,text="",bg="#1e1e1e",fg="white",width=400)

mainloop()