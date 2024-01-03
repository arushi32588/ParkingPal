import mysql.connector as m
from datetime import datetime
tcount=10
def remove_parking():
          Vno=input("\tEnter vehicle number to Delete(XXXX-XX-XXXX) - ")
          con=m.connect(host='localhost',user='root',passwd='tripti15',database='parking')
          cur=con.cursor()
          st="delete from parkedvehicle where Vehicle_no='{}'".format(Vno)
          cur.execute(st)
          con.commit()
#remove_parking()          
         
def check():
          con=m.connect(host='localhost',user='root',passwd='tripti15',database='parking')
          cur=con.cursor()
          st='select level,slot from parkedvehicle'
          cur.execute(st)
          data=list(cur.fetchall())          
          con.close()
          print(data)
          
          if len(data)==0:
                    level=1
                    slot=1
          else:
                    lst=[]
                    for row in data:
                              lst.append(row[-1])  #adding all slot numbers to lst
                    lst.sort()
                    empty=[]
                    for i in range(len(lst)):  #lst=[1,2,4,5]
                              if i+1!=empty[i]:
                                        empty.append(i+1)
                    empty.sort(reverse=True)
                    slot=empty.pop()               
                    level=data[-1][0]
                    if empty!=[] and data[-1][1]==tcount:
                              level=2
                              slot=1
                    else:
                              slot=data[-1][1]+1
          return level,slot
          
def convertdatetosql(datetime_str):        
          
          datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
          dt=datetime_object

          print(type(datetime_object))
          print(datetime_object)  # printed in default format

def validate_date(date,time):
          result=1
          lst1=date.split('-')
          lst2=time.split(':')
          if len(lst1)==3:
                    if len(lst1[0])==4 and lst1[0].isdigit():
                              if len(lst1[1])==2 and lst1[1].isdigit():
                                        if len(lst1[2])==2 and lst1[2].isdigit():
                                                  if len(lst2)==3:
                                                            if len(lst2[0])==2 and lst2[0].isdigit():
                                                                      if len(lst2[1])==2 and lst2[1].isdigit():
                                                                                if len(lst2[2])==2 and lst2[2].isdigit():
                                                                                          result=0
                    
                    
          return result


def take_input():
          Vno=input("\tEnter vehicle number (XXXX-XX-XXXX) - ").upper()
          Vtype=str(input("\tEnter vehicle type(Bicycle=A/Bike=B/Car=C):")).lower()
          vname=input("\tEnter vehicle name - ")
          OName=input("\tEnter owner name - ")
          res=1
          while res:                    
                    date=input("\tEnter Date (yyyy-mm-dd) - ")
                    time=input("\tEnter Time (HH:MM:SS) - ")
                    res=validate_date(date,time)
          
          d=date+' '+time
          newdt=convertdatetosql(d)
          level,slot=check()
          def addtodb():                   
                    a=m.connect(host="localhost",user="root",passwd='tripti15',database="parking")
                    cur=a.cursor()
                    st="insert into parkedvehicle values ('{}','{}','{}','{}','{}',{},{})".format(Vno,Vtype,vname,OName,newdt,level,slot)
                    cur.execute(st)
                    m.commit()                 
                    m.close()
          #check()
          addtodb()
          
#take_input()

def amount():
    print("----------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\tParking Rate")
    print("----------------------------------------------------------------------------------------------------------------------")
    print("*1.Bicycle      Rs20 / Hour")
    print("*2.Bike         Rs40/ Hour")
    print("*3.Car          Rs60/ Hour")
    print("----------------------------------------------------------------------------------------------------------------------")


def three():
    
    print("----------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\tParked Vehicle")
    print("----------------------------------------------------------------------------------------------------------------------")
    print("Vehicle No.\tVehicle Type        Vehicle Name\t       Owner Name\t     Date\t\tTime")
    print("----------------------------------------------------------------------------------------------------------------------")
    
    con=m.connect(host='localhost',user='root',passwd='tripti15',database='parking')
    cur1=con.cursor()
    st1="select * from parkedvehicle"
        
    cur1.execute(st1)
    data=cur1.fetchall()
    print(data)
    




    

'''

def bill:
                    print(".............................................................. Generating Bill ..........................................................................")
                    no=True
                    while no==True:
                        Vno=input("\tEnter vehicle number to Delete(XXXX-XX-XXXX) - ").upper()
                        if Vno=="":
                            print("###### Enter Vehicle No. ######")
                        elif len(Vno)==12:
                            if Vno in Vehicle_Number:
                                i=Vehicle_Number.index(Vno)
                                no=not True
                            elif Vno not in Vehicle_Number:
                                print("###### No Such Entry ######")
                            else:
                                print("Error")
                        else:
                            print("###### Enter Valid Vehicle Number ######")
                    print("\tVehicle Check in time - ",Time[i])
                    print("\tVehicle Check in Date - ",Date[i])
                    print("\tVehicle Type - ",Vehicle_Type[i])
                    inp=True
                    amt=0
                    while inp==True:
                        hr=input("\tEnter No. of Hours Vehicle Parked - ").lower()
                        if hr=="":
                            print("###### Please Enter Hours ######")
                        elif int(hr)==0 and Vehicle_Type[i]=="Bicycle":
                            amt=20
                            inp=not True
                        elif int(hr)==0 and Vehicle_Type[i]=="Bike":
                            amt=40
                            inp=not True
                        elif int(hr)==0 and Vehicle_Type[i]=="Car":
                            amt=60
                            inp=not True
                        elif int(hr)>=1:
                            if Vehicle_Type[i]=="Bicycle":
                                amt=int(hr)*int(20)
                                inp=not True
                            elif Vehicle_Type[i]=="Bike":
                                amt=int(hr)*int(40)
                                inp=not True
                            elif Vehicle_Type[i]=="Car":
                                amt=int(hr)*int(60)
                                inp=not True
                    print("\t Parking Charge - ",amt)
                    ac=18/100*int(amt)
                    print("\tAdd. charge 18 % - ",ac)
                    print("\tTotal Charge - ",int(amt)+int(ac))
                    print("..............................................................Thank you for using our service...........................................................................")
                    a=input("\tPress Any Key to Proceed - ")
                six()

'''


#USE INPUT CHOICES

print("----------------------------------------------------------------------------------------") 
print("\t\tParking Management System")
print("----------------------------------------------------------------------------------------")
print("1.Vehicle Entry")
print("2.Remove Entry" )
print("3.View Parked Vehicle ")
print("4.View Left Parking Space ")
print("5.Amount Details ")
print("6.Bill")
print("7.Close Programme ")
print("8. Which level?")
print("+---------------------------------------------+")
ch=int(input("\tSelect option:"))

if ch==1:
    take_input()
if ch==2:
    remove_parking()
if ch==3:
    three()     
if ch==4:
    check()  
if ch==5:
    amount()
if ch== 6:
    bill()
if ch==7:
    print("CLOSING PROGRAMME")
if ch==8:
    check()
