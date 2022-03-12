def Add_OR_Modify_Coach(mode):
    import re
    if(mode=="r"):
        myfile=open("COACHDETAILS.txt",mode)
        print("\n   CoachName,CoachID,Datejoined,Dateterminated,Hourlyrate,SportCenterName,SportCenterCode,Sport,SportCode,Rating,Phone,Address")
        root=0
        for data in myfile:
            root+=1
            print(str(root)+".",data)
                    
        myfile=open("COACHDETAILS.txt",mode)

        ModifiedCoach=[]
        change=0

        cnt=0
        for line in myfile:
            S=line.rstrip()
            ModifiedCoach.append(str(S))
            cnt+=1
                    
        while True:
            try:
                while(change<1 or change>cnt):
                    change=int(input("Type the line that u would like to change--'From 1 to the max line existed': "))
                break

            except ValueError:
                print("Only Accept Whole Number!!!")

        files=open("COACHDETAILS.txt","r")
        coachdata=[]
        for line in files:
            lines=line.split(",")
            coachdata.append(lines[0])

        print("Coach Name:",coachdata[change-1])
        coachname=coachdata[change-1]

    else:
        myfile=open("COACHDETAILS.txt",mode)

        coachname=str(input("\nCoach Name: "))
        while not (re.match(r"^[A-Za-z\s]+$",coachname)):
            print("Only Alphabets are Allowed!!!")
            coachname=str(input("Coach Name: "))

    coachID=100
    while True:
        try:
            while(coachID<0 or coachID>99):
                coachID=int(input("Coach ID(A100-A199): A1"))
            break

        except ValueError:
            print("Only Accept Number!!!")

    coachID_str=str(coachID)
    print("Coach ID: A1"+str(coachID_str.zfill(2)))
        
    import calendar
    year=0
    while True:
        try:
            while (year<1960 or year>2021):
                year=int(input("Check year (Type from 1960-2021): "))
            break

        except ValueError:
            print("Only Accept Whole Number!!!")
        
    print (calendar.calendar(year))

    datejoined_year=0
    while True:
        try:
            while(datejoined_year<1960 or datejoined_year>2021):
                datejoined_year=int(input("Year joined(1960-2021): "))
            break

        except ValueError:
            print("Only Accept Whole Number!!!")

    datejoined_month=0
    while True:
        try:
            while(datejoined_month<1 or datejoined_month>12):
                datejoined_month=int(input("Month joined(1-12): "))
            break

        except ValueError:
            print("Only Accept Whole Number!!!")

    datejoined_day=0     
    while True:
        try:
            datejoined_day=int(input("Date joined: "))
            break

        except:
            print("Only Accept Whole Number!!!")

    if(datejoined_month==1 or datejoined_month==3 or datejoined_month==5 or datejoined_month==7 or datejoined_month==8 or datejoined_month==10 or datejoined_month==12):     
        while True:
            try:
                while(datejoined_day<1 or datejoined_day>31):
                    datejoined_day=int(input("Date joined(1-31): "))
                break

            except ValueError:
                print("Only Accept Whole Number!!!")

    elif(datejoined_month==4 or datejoined_month==6 or datejoined_month==9 or datejoined_month==11):
        while True:
            try:
                while(datejoined_day<1 or datejoined_day>30):
                    datejoined_day=int(input("Date joined(1-30): "))
                break

            except ValueError:
                print("Only Accept Whole Number!!!")

    elif(((datejoined_year%4)==0) and (datejoined_month==2)):
        while True:
            try:
                while(datejoined_day<1 or datejoined_day>29):
                    datejoined_day=int(input("Date joined(1-29): "))
                break

            except ValueError:
                print("Only Accept Whole Number!!!")
                
    else:
        while True:
            try:
                while(datejoined_day<1 or datejoined_day>28):
                    datejoined_day=int(input("Date joined(1-28): "))
                break

            except ValueError:
                print("Only Accept Whole Number!!!")
    
    continuing=0
    while True:
        try:
            while(continuing<1 or continuing>2):
                continuing=int(input("Is the coach still teaching? '1'for yes,'2' for no: "))
            break

        except ValueError:
            print("Only Accept Whole Number!!!")

    dateterminated_year=0
    dateterminated_month=0
    dateterminated_day=0
    if(continuing==1):
    
        dateterminated_year="XXXX"
        dateterminated_month="XX"
        dateterminated_day="XX"
    else:
        import calendar

        year=0
        while True:
            try: 
                while (year<1960 or year>2021):
                    year=int(input("Check year (Type from 1960-2021): "))
                break

            except ValueError:
                print("Only Accept Whole Number!!!")
        
        print (calendar.calendar(year))

        dateterminated_year=0
        while True:
            try:
                while(dateterminated_year<1960 or dateterminated_year>2021):
                    dateterminated_year=int(input("Year terminated(1960-2021): "))
                break

            except ValueError:
                print("Only Accept Whole Number!!!")

        dateterminated_month=0
        while True:
            try:
                while(dateterminated_month<1 or dateterminated_month>12):
                    dateterminated_month=int(input("Month terminated(1-12): "))
                break

            except ValueError:
                print("Only Accept Whole Number!!!")
            
        dateterminated_day=0
        while True:
            try:
                dateterminated_day=int(input("Day terminated: "))
                break

            except ValueError:
                print("Only Accept Whole Number!!!")
            
        if(dateterminated_month==1 or dateterminated_month==3 or dateterminated_month==5 or dateterminated_month==7 or dateterminated_month==8 or dateterminated_month==10 or dateterminated_month==12):     
            while True:
                try:
                    while(dateterminated_day<1 or dateterminated_day>31):
                        dateterminated_day=int(input("Date terminated(1-31): "))
                    break

                except ValueError:
                    print("Only Accept Whole Number!!!")

        elif(dateterminated_month==4 or dateterminated_month==6 or dateterminated_month==9 or dateterminated_month==11):
            while True:
                try:
                    while(dateterminated_day<1 or dateterminated_day>30):
                        datejoined_day=int(input("Date joined(1-30): "))
                    break

                except ValueError:
                    print("Only Accept Whole Number!!!")

        elif(((dateterminated_year%4)==0) and (dateterminated_month==2)):
            while True:
                try:
                    while(dateterminated_day<1 or dateterminated_day>29):
                        dateterminated_day=int(input("Date terminated(1-29): "))
                    break

                except ValueError:
                    print("Only Accept Whole Number!!!")
        else:
            while True:
                try:
                    while(dateterminated_day<1 or dateterminated_day>28):
                        dateterminated_day=int(input("Date terminated(1-28): "))
                    break

                except ValueError:
                    print("Only Accept Whole Number!!!")

    hourlyrate=0
    while True:
        try:
            while(hourlyrate<100 or hourlyrate>250):
                hourlyrate=int(input("Hourly rate(100-250): RM"))
            break

        except ValueError:
            print("Only Accept Whole Number!!!")

    sportcentren=["Sports Academy Ipoh","Sports Academy Meru","Sports Academy Canning","Sports Academy Hala"]
    sportcentrec=["S1","S2","S3","S4"]
    sportn=["Badminton","Tennis","Swimming","Cricket","Table Tennis","Gymnastics","Football","Basketball","Archery","Volleyball"]
    sportc=["B1","B2","B3","B4","B5","B6","B7","B8","B9","B10"]
        
    scn=str(input("Sport Center Name(Sports Academy Ipoh,Sports Academy Meru,Sports Academy Canning,Sports Academy Hala): "))
    while scn not in sportcentren:
        print("No such Sport Centre!!!")
        scn=str(input("Sport Center Name(Sports Academy Ipoh,Sports Academy Meru,Sports Academy Canning,Sports Academy Hala): "))

    obtain=sportcentren.index(scn)

    print("Sport Center Code:",sportcentrec[obtain])

    scc=sportcentrec[obtain]

    sportname=str(input("Sport(Badminton,Tennis,Swimming,Cricket,Table Tennis,Gymnastics,Football,Basketball,Archery,Volleyball): "))
    while sportname not in sportn:
        print("No such sport!!!")
        sportname=str(input("Sport(Badminton,Tennis,Swimming,Cricket,Table Tennis,Gymnastics,Football,Basketball,Archery,Volleyball): "))

    transfer=sportn.index(sportname)

    print("Sport Code:",sportc[transfer])
        
    sportcode=sportc[transfer]
        
    rating=0
    while True:
        try:
            while (rating<1 or rating>5):
                rating=int(input("Rating(1-5): "))
            break

        except ValueError:
            print("Only Accept Whole Number!!!")

    phone=input("Phone number(01XXXXXXXX): ")
    while not(phone[0]=="0" and phone[1]=="1" and (len(phone)==10) and phone.isdigit()):
        print("Need 10 digits inclusive of 0 being first and 1 being second")
        phone=input("Phone number(01XXXXXXXX): ")
        
    address=str(input("Address: "))
    while not re.match(r"^[A-Za-z0-9\s]+$",address):
        print("Only Alphabets and Numbers are Allowed!!!")
        address=str(input("Address: "))

    if(mode=="a"):
        save=0
        while True:
            try:
                while(save<1 or save>2):
                    save=int(input("Do u wish to save changes '1' for yes, '2' for no: "))
                break

            except ValueError:
                print("Only Accept Whole Number!!!")

        if(save==1):
            myfile.write(coachname+",A1"+str(coachID_str.zfill(2))+","+str(datejoined_day)+"-"+str(datejoined_month)+"-"+str(datejoined_year)+","+str(dateterminated_day)+"-"+str(dateterminated_month)+"-"+str(dateterminated_year)+",RM"+str(hourlyrate)+","+scn+","+scc+","+sportname+","+sportcode+","+str(rating)+","+str(phone)+","+address+"\n")
            print("New Coach Records Made Successfully")

        else:
            print("Oops No New Records Made :(")

    else:
        Newdata=[]
        Newdata.append(coachname+",A1"+str(coachID_str.zfill(2))+","+str(datejoined_day)+"-"+str(datejoined_month)+"-"+str(datejoined_year)+","+str(dateterminated_day)+"-"+str(dateterminated_month)+"-"+str(dateterminated_year)+",RM"+str(hourlyrate)+","+scn+","+scc+","+sportname+","+sportcode+","+str(rating)+","+str(phone)+","+address)

        for data in Newdata:
            something=data

        ModifiedCoach[change-1]=str(something)

        save=0
        while True:
            try:
                while(save<1 or save>2):
                    save=int(input("Do u wish to save changes '1' for yes, '2' for no: "))
                break

            except ValueError:
                print("Only Accept Whole Number!!!")

        if(save==1):
            myfile=open("COACHDETAILS.txt","w")
            for row in ModifiedCoach:
                myfile.write(row+"\n")
            print("Modification Made Successfully")

        else:
            print("No Modification Made")

def Add_OR_Modify_Sport(mode):
    if(mode=="r"):
        myfile=open("SPORTDETAILS.txt",mode)

        print("\n   Sport,SportCode,SportFees,CoachName")
        root=0
        for data in myfile:
            root+=1
            print(str(root)+".",data)

        myfile=open("SPORTDETAILS.txt",mode)
        ModifiedSport=[]

        cnt=0
        for line in myfile:
            S=line.rstrip()
            ModifiedSport.append(str(S))
            cnt+=1
            
        change=0
        while True:
            try:
                while(change<1 or change>cnt):
                    change=int(input("Type the line that u would like to change--'From 1 to the max line existed': "))
                break

            except ValueError:
                print("Only Accept Whole Number!!!")
    
    file=open("COACHDETAILS.txt","r")

    coach=[]
    sportnamelist=[]
    sportcodelist=[]
    hourlyratelist=[]
    
    for element in file:
        elements=element.strip()
        final=elements.split(",")
        coach.append(final[0])
        hourlyratelist.append(final[4])
        sportnamelist.append(final[7])
        sportcodelist.append(final[8])

    print("Coach:",coach)
        
    coachname=str(input("Coach Name: "))
    while coachname not in coach:
        print("No Such Coach!!!")
        coachname=str(input("Coach Name: "))

    passing=coach.index(coachname)

    sportname=sportnamelist[passing]

    print("Sport:",sportname)

    sportcode=sportcodelist[passing]

    print("Sport Code:",sportcode)

    sportfees=0
    while True:
        try:
            while (sportfees<200 or sportfees>500):
                sportfees=int(input("Sport Fees: RM"))
            break

        except ValueError:
            print("Only Accept Whole Number!!!")

    if(mode=="a"):
        save=0
        while True:
            try:
                while(save<1 or save>2):
                    save=int(input("Do u wish to save changes '1' for yes, '2' for no: "))
                break

            except ValueError:
                print("Only Accept Whole Number!!!")

        if (save==1):
            myfile=open("SPORTDETAILS.txt",mode)
            myfile.write(sportname+","+sportcode+",RM"+str(sportfees)+","+coachname+"\n")
            print("New Sport Records Made Successfully")

        else:
            print("Oops No New Records Made :(")

    else:
        Newinfo=[]
        Newinfo.append(sportname+","+sportcode+",RM"+str(sportfees)+","+coachname)

        for item in Newinfo:
            stuff=item

        ModifiedSport[change-1]=str(stuff)

        save=0
        while True:
            try:
                while(save<1 or save>2):
                    save=int(input("Do u wish to save changes '1' for yes, '2' for no: "))
                break

            except ValueError:
                print("Only Accept Whole Number!!!")

        if (save==1):
            myfile=open("SPORTDETAILS.txt","w")
            for row in ModifiedSport:
                myfile.write(row+"\n")
            print("Modification Made Successfully")

        else:
            print("No Modification Made")   
            
        myfile.close()


def Add_OR_Modify_SportSchedule(mode):
    if(mode=="r"):
        myfile=open("SPORTSCHEDULEDETAILS.txt",mode)

        print("\n   Sport,Day,Time,SportCenterName")
        root=0
        for data in myfile:
            root+=1
            print (str(root)+".",data)
        
        myfile=open("SPORTSCHEDULEDETAILS.txt",mode)
        ModifiedSportSchedule=[]

        cnt=0
        for line in myfile:
            S=line.rstrip()
            ModifiedSportSchedule.append(str(S))
            cnt+=1
        
        change=0
        while True:
            try:
                while(change<1 or change>cnt):
                    change=int(input("Type the line that u would like to change--'From 1 to the max line existed': "))
                break

            except ValueError:
                print("Only Accept Whole Number!!!") 

    file=open("COACHDETAILS.txt","r")

    coach=[]
    sportnamelist=[]
    scnlist=[]
    
    for element in file:
        elements=element.strip()
        final=elements.split(",")
        coach.append(final[0])
        sportnamelist.append(final[7])
        scnlist.append(final[5])

    print("\nCoach:",coach)
        
    coachname=str(input("Coach Name: "))
    while coachname not in coach:
        print("No Such Coach!!!")
        coachname=str(input("Coach Name: "))

    passing=coach.index(coachname)

    sportname=sportnamelist[passing]

    print("Sport:",sportname)
    
    day=str(input("Day(Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday): "))

    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    while day not in days:
        day=str(input("Day(Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday): "))
        
    starthour=0
    while True:
        try:
            while(starthour<1 or starthour>24):
                starthour=int(input("Starting Hour(1-24): "))
            break

        except ValueError:
            print("Only Accept Whole Number!!!")

    starthour_str=str(starthour)

    startmin=100
    while True:
        try:
            while (startmin<0 or startmin>59):
                startmin=int(input("Starting Minute(0-59): "))
            break

        except ValueError:
            print("Only Accept Whole Number!!!")

    startmin_str=str(startmin)
        
    finishhour=0
    while True:
        try:
            while (finishhour<1 or finishhour>24):
                finishhour=int(input("Finishing Hour(1-24): "))
            break

        except ValueError:
            print("Only Accept Whole Number!!!")

    finishhour_str=str(finishhour)
        
    finishmin=100
    while True:
        try:
            while (finishmin<0 or finishmin>59):
                finishmin=int(input("Finishing Minute(0-59): "))
            break

        except ValueError:
            print("Only Accept Whole Number!!!")

    finishmin_str=str(finishmin)

    print(str(starthour_str.zfill(2)),":",str(startmin_str.zfill(2)),"-",str(finishhour_str.zfill(2)),":",str(finishmin_str.zfill(2)))

    scn=scnlist[passing]

    print("Sport Center Name:",scn)

    if(mode=="a"):
        save=0
        while True:
            try:
                while(save<1 or save>2):
                    save=int(input("Do u wish to save changes '1' for yes, '2' for no: "))
                break

            except ValueError:
                print("Only Accept Whole Number!!!")

        if(save==1):
            myfile=open("SPORTSCHEDULEDETAILS.txt",mode) 
            myfile.write(sportname+","+day+","+str(starthour_str.zfill(2))+":"+str(startmin_str.zfill(2))+"-"+str(finishhour_str.zfill(2))+":"+str(finishmin_str.zfill(2))+","+scn+","+coachname+"\n")
            print("New Sport Schedule Records Made Successfully")

        else:
            print("Oops No New Records Made :(")

    else:
        Newinfos=[]
        Newinfos.append(sportname+","+day+","+str(starthour_str.zfill(2))+":"+str(startmin_str.zfill(2))+"-"+str(finishhour_str.zfill(2))+":"+str(finishmin_str.zfill(2))+","+scn+","+coachname)
    
        for element in Newinfos:
            New=element
            print(New)
     
        ModifiedSportSchedule[change-1]=str(New)

        save=0
        while True:
            try:
                while(save<1 or save>2):
                    save=int(input("Do u wish to save changes '1' for yes, '2' for no: "))
                break

            except ValueError:
                print("Only Accept Whole Number!!!")

        if (save==1):
            myfile=open("SPORTSCHEDULEDETAILS.txt","w")
            for row in ModifiedSportSchedule:
                myfile.write(row+"\n")
            print("Modification Made Successfully")

        else:
            print("No Modification Made")   

def Display(filing):
    result = filing + ".txt"
    myfile=open(result,"r")
    for info in myfile:
        print(info)
    myfile.close()

def Search(filename,searchrecord,no):
    result=filename + ".txt"
    myfile=open(result,"r")
    for line in myfile:
        L=line.split(",")
        if searchrecord == L[no]:
            print(line)

def sort(num,check,filename): # sort function
    myfile=open("COACHDETAILS.txt","r")
    sortedfile = []
    sort_list = [] # new list 
    lines = [] # lines list
    for line in myfile: # for each in file
        lines.append(line) # append full line to lines 
        split_line = line.split(",") # split line into list 
        if check: # if value is integer
            if(num == 4):
                sort_list.append(int(split_line[num].replace("RM","")))
            else:
                sort_list.append(int(split_line[num])) # append index num of list to sort list
                
        else: # if value is not integer
            sort_list.append(str(split_line[num])) # append index num of list to sort list
    n = len(sort_list) # length of list is equal to n
    for x in range(n): # for x in range of list
        for y in range(n-x-1): # for y in range of x - len - 1
            if sort_list[y] > sort_list[y + 1]: # if index y is larger than index y + 1 
                sort_list[y], sort_list[y+1] = sort_list[y+1], sort_list[y] # replace index y with index y + 1
    myfile.close # close file
    print()# print empty line for visuals
    print("CoachName,CoachID,Datejoined,Dateterminated,Hourlyrate,SportCenterName,SportCenterCode,Sport,SportCode,Rating,Phone,Address")
    for x in sort_list: # for each in the sorted list
        for line in lines: # for each line in full lines list
            split_line = line.split(",") # split the line
            if check: # if value is integer
                if(num == 4):
                    if int(split_line[num].replace("RM","")) == x: # if the split line list index matches value in sorted list loop
                        lines.remove(line)   
                        print(line.rstrip())
                        sortedfile.append(line.rstrip())
      
                else:
                    if int(split_line[num]) == x:
                        lines.remove(line)   
                        print(line.rstrip())
                        sortedfile.append(line.rstrip())
                        
            else: # if value is not integer
                if split_line[num] == x: # if the split line list index matches value in sorted list loop
                    lines.remove(line)       
                    print(line.rstrip())
                    sortedfile.append(line.rstrip())

    #write sorted data into file
    myfiles = open(filename,"w")
    for sortedinfo in sortedfile:
        myfiles.write(sortedinfo + "\n")
    myfiles.close()
    
          
def DeleteInfo(files):
    filename = files + ".txt"
    myfile=open(filename,"r")

    root=0
    for data in myfile:
        root+=1
        print(str(root)+".",data)

    ModifiedInfo=[]
    deleting=0

    myfile=open(filename,"r")
    cnt=0
    for line in myfile:
        S=line.rstrip()
        ModifiedInfo.append(str(S))
        cnt+=1     
    
    while True:
        try:
            while(deleting<1 or deleting>cnt):
                deleting=int(input("Type the line that u would like to delete--'From 1 to the max line existed': "))
            break

        except ValueError:
            print("Only Accept Whole Number!!!")

    ModifiedInfo.pop(deleting-1)

    save=0
    while True:
        try:
            while(save<1 or save>2):
                save=int(input("Do u wish to save changes '1' for yes, '2' for no: "))
            break

        except ValueError:
            print("Only Accept Whole Number!!!")

    if (save==1):
        myfile=open(filename,"w")
        for row in ModifiedInfo:
            myfile.write(row+"\n")
        print("Coach Record Deleted Successfully")

    else:
        print("No Coach Record Deleted")
        
    myfile.close()

def Display_RegisteredCoach(L):
    
    myfile=open("COACHDETAILS.txt","r")

    print("\nCoachName,CoachID,Datejoined,Dateterminated,Hourlyrate,SportCenterName,SportCenterCode,Sport,SportCode,Rating,Phone,Address")
    for row in myfile:
        S=row.strip()
        M=S.split(",")
        if(L[4]==M[0]):
            print(row)

    myfile.close()
       
def Display_SelfRecord(cnt):
    studentdata=[]
    myfile=open("STUDENTLOGINSTORE.txt","r")

    print("\nFormat:\tStudentName,Password,StudentID,Sport,CoachName")
    for line in myfile:
        L=line.strip()
        studentdata.append(L)
    print("Original Data: ",studentdata[cnt-1])

    myfile.close()

def Display_RegisteredSportSchedule(L):
    
    myfile=open("SPORTSCHEDULEDETAILS.txt","r")

    print("\nSportName,Day,Time,SportCenterName,CoachName")
    for row in myfile:
        S=row.strip()
        N=S.split(",")
        if(L[4]==N[4]):
            print(row)

    myfile.close()


def Modify_SelfRecord(cnt):
    import re
   
    studentdata=[]
    newstudentdata=[]
    listing=[]
    sportlist=[]
    
    myfile=open("STUDENTLOGINSTORE.txt","r")

    for line in myfile:
        L=line.strip()
        studentdata.append(L)
        
    print("\nStudentName,Password,StudentID,SportName,CoachName")
    print("Original Data: ",studentdata[cnt-1])

    username=str(input("Student Name: "))
    while not re.match(r"^[A-Za-z\s]+$",username):
        print("Only Alphabets are Allowed!!!")
        username=str(input("Student Name: "))

    password=input("Student Password: ")
    while not re.match(r"^[A-Za-z0-9\s]+$",password):
        print("Only Alphabets and Numbers are Allowed!!!")
        password=input("Student Password: ")
        
    studentID=input("Student ID: TP")
    while not((len(studentID)==6) and studentID.isdigit()):
        print("Only Numbers!!!")
        studentID=input("Student ID: TP")

    file=open("COACHDETAILS.txt","r")

    for data in file:
        datas=data.strip()
        coach=datas.split(",")
        listing.append(coach[0])
        sportlist.append(coach[7])

    print("Coach:")
    print(listing)
    coachname=str(input("Coach Name: "))

    while coachname not in listing:
        print("Not available")
        coachname=str(input("Coach Name: "))

    correct=listing.index(coachname)

    sportname=sportlist[correct]

    print("Sport Name:",sportname)
    
    newstudentdata.append(username+","+password+",TP"+str(studentID)+","+sportname+","+coachname)

    for item in newstudentdata:
        new=item

    studentdata[cnt-1]=new

    save=0
    while True:
        try:
            while(save<1 or save>2):
                save=int(input("Do u wish to save changes '1' for yes, '2' for no: "))
            break

        except ValueError:
            print("Only Accept Whole Number!!!")

    if (save==1):
        myfile=open("STUDENTLOGINSTORE.txt","w")
        for row in studentdata:
            myfile.write(row+"\n")
        print("Modification Made Successfully")

    else:
        print("No Modification Made")

    myfile.close()
    

def Feedback_Rating(L):
    import re

    myfile=open("FEEDBACKRATING.txt","a")

    feedback=str(input("Feedback: "))
    while not re.match(r"^[A-Za-z\s]+$",feedback):
        print("Only Alphabets are allowed!!!")
        feedback=str(input("Feedback: "))
    
    rating=0
    while True:
        try:
            while (rating<1 or rating>5):
                rating=int(input("Rating: "))
            break

        except ValueError:
            print("Only Accept Whole Number!!!")
    
    save=0
    while True:
        try:
            while(save<1 or save>2):
                save=int(input("Do u wish to save changes '1' for yes, '2' for no: "))
            break

        except ValueError:
            print("Only Accept Whole Number!!!")

    if (save==1):
        myfile.write(str(L[0])+","+str(L[4])+","+feedback+","+str(rating)+"\n")
        print("Feedback saved successfully")

    else:
        print("Feedback not saved")

    myfile.close()

    
def Admin_function():
    
    print("\n*****WELCOME TO ADMIN LOGIN SYSTEM*****")

    admin=str(input("Admin Name: "))
    password=str(input("Password: "))
            
    if(admin=="AC123" and password=="123abc"):
        Admin_Homepage()

    else:
        print("Wrong Login Info!!!")
            

def Admin_Homepage():
    import time
    
    while True:
        print ("\n",time.asctime( time.localtime(time.time()) ))
        print("*****WELCOME TO ADMIN HOMEPAGE*****")
        print("1.Add Record\n2.Display Record\n3.Search Record\n4.Sort and Display Record\n5.Modify Record\n6.Delete Record\n7.Exit")

        enter=0    
        while True:
            try:
                while(enter<1 or enter>7):
                    enter=int(input("Pls pick your functionalities(Type from 1-7): "))
                break

            except ValueError:
                print("Only Accept Whole Number!!!")

        while(enter==1):
            print("\n*****ADDING RECORD SYSTEM*****")
            print("1.Coach\n2.Sport\n3.Sport Schedule\n4.Exit")
            entering=0
            while True:
                try:
                    while(entering<1 or entering>4):       
                        entering=int(input("Pick the record that needs to be added (Type from 1-4): "))
                    break

                except ValueError:
                    print("Only Accept Whole Number!!!")

            if(entering==1):
                Add_OR_Modify_Coach("a")
                                        
            elif(entering==2):
                Add_OR_Modify_Sport("a")
                        
            elif(entering==3):
                Add_OR_Modify_SportSchedule("a")      
                    
            else:
                break
  
        while(enter==2):
            print("\n*****DISPLAY RECORD SYSTEM*****")
            print("1.Coach\n2.Sport\n3.Registered Students\n4.Feedback and Rating\n5.Exit")
            display=0
            while True:
                try:
                    while(display<1 or display>5):
                        display=int(input("Pick the record that needs to be displayed (Type from 1-5): "))
                    break

                except ValueError:
                    print("Only Accept Whole Number!!!")
                        
            if(display==1):
                print("\nCoachName,CoachID,Datejoined,Dateterminated,Hourlyrate,SportCenterName,SportCenterCode,Sport,SportCode,Rating,Phone,Address")
                Display("COACHDETAILS")
                       
            elif(display==2):
                print("\nSportName,SportCode,SportFees,CoachName")
                Display("SPORTDETAILS")
                        
            elif(display==3):
                print("\nStudentName,Password,StudentID,SportName,CoachName")
                Display("STUDENTLOGINSTORE")
                        
            elif(display==4):
                print("\nStudentName,CoachName,Feedback,Rating")
                Display("FEEDBACKRATING")
                       
            else:
                break
            
        while(enter==3):
            print("\n*****SEARCH SPECIFIC RECORD SYSTEM*****")
            print("1.Coach by Coach ID\n2.Coach by overall performance(Rating)\n3.Sport by Sport ID\n4.Student by Student ID\n5.Exit")
            search=0
            while True:
                try:
                    while(search<1 or search>5):
                        search=int(input("Pick the record that u would like to search for(Type from 1-5): "))
                    break

                except ValueError:
                    print("Only Accept Whole Number!!!")

            if(search==1):
                coachID=input("\nSearch Coach by respective coach ID: ")
                print("CoachName,CoachID,Datejoined,Dateterminated,Hourlyrate,SportCenterName,SportCenterCode,Sport,SportCode,Rating,Phone,Address")
                Search("COACHDETAILS",coachID,1)
                        
            elif(search==2):
                rating=input("\nSearch Coach by respective rating: ")
                print("CoachName,CoachID,Datejoined,Dateterminated,Hourlyrate,SportCenterName,SportCenterCode,Sport,SportCode,Rating,Phone,Address")
                Search("COACHDETAILS",rating,9)
                        
            elif(search==3):
                sportcode=input("\nSearch Sport by respective sport code: ")
                print("SportName,SportCode,SportFees,CoachName")
                Search("SPORTDETAILS",sportcode,1)
                            
            elif(search==4):
                studentID=input("\nSearch Student by respective student ID: ")
                print("StudentName,Password,StudentID,SportName,CoachName")
                Search("STUDENTLOGINSTORE",studentID,2)
                        
            elif(search==5):
                break

        while(enter==4):
            print("\n*****SORT AND DISPLAY RECORD SYSTEM*****")
            print("1.Coaches in ascending order by names\n2.Coaches Hourly Pay Rate in ascending order\n3.Coaches Overall Performance in ascending order\n4.Exit")
            sortdisplay=0
            while True:
                try:
                    while(sortdisplay<1 or sortdisplay>4):
                        sortdisplay=int(input("Pick the type that u wish to sort(Type from 1-4): "))
                    break

                except ValueError:
                    print("Only Accept Whole Number!!!")

            if(sortdisplay==1):
                sort(0,False,"SORTCOACHNAME.txt")
                        
            elif(sortdisplay==2):
                sort(4,True,"SORTPRICE.txt")
                        
            elif(sortdisplay==3):
                sort(9,True,"SORTRATING.txt")
                            
            else:
                break

        while(enter==5):
            print("\n*****MODIFY RECORD SYSTEM*****")
            print("1.Coach\n2.Sport\n3.Sport Schedule\n4.Exit")
            modify=0
            while True:
                try:
                    while(modify<1 or modify>4):
                        modify=int(input("Pick the record that needs to be modified(Type from 1-4): "))
                    break

                except ValueError:
                    print("Only Accept Whole Number!!!")
                        
            if(modify==1):
                Add_OR_Modify_Coach("r")
                                
            elif(modify==2):
                Add_OR_Modify_Sport("r")
                       
            elif(modify==3):
                Add_OR_Modify_SportSchedule("r")
                        
            else:
                break

        while(enter==6):
            print("\n*****DELETE RECORD SYSTEM*****")
            print("1.Coach\n2.Sport\n3.Sport Schedule\n4.Exit")
            delete=0
            while True:
                try:
                    while(delete<1 or delete>4):
                        delete=int(input("Pick the record that needs to be deleted(Type from 1-4): "))
                    break

                except ValueError:
                    print("Only Accept Whole Number!!!")

            if(delete==1):
                print("\n   CoachName,CoachID,Datejoined,Dateterminated,Hourlyrate,SportCenterName,SportCenterCode,Sport,SportCode,Rating,Phone,Address")
                DeleteInfo("COACHDETAILS")

            elif(delete==2):
                print("\n   Sport,SportCode,SportFees,CoachName")
                DeleteInfo("SPORTDETAILS")

            elif(delete==3):
                print("\n   Sport,Day,Time,SportCenterName")
                DeleteInfo("SPORTSCHEDULEDETAILS")

            else:
                break
                        
        if(enter==7):
            print("Thank You!!! Pls Come Again^_^")
            break      

def MainMenu_function():
    while True:
        print("\n*****WELCOME TO REAL CHAMPIONS SPORTS ACADEMY*****")            
        print("Enter User Type\n1.Admin\n2.Student\n3.Exit")
        opt=0
        while True:
            try:
                while(opt<1 or opt>3):
                    opt=int(input("Enter no of user type from 1-3: "))
                break

            except ValueError:
                print("Only Accept Whole Number!!!")

        if(opt==1):
            Admin_function()

        elif(opt==2):
            AllStudent_function()
            
        else:
            print("GOODBYE!!! ^_^")
            break


def ExistingStudentLogin_function():
    print("*****STUDENT LOGIN*****")
    myfile=open("STUDENTLOGINSTORE.txt","r")
    username=str(input("Student Name: "))
    password=str(input("Student Password: "))
    cnt=1
    for line in myfile:
        S=line.strip()
        L=S.split(",")
        if((L[0]==username)and (L[1]==password)):
            print("Correct")
            ExistingStudentHomepage(cnt,L)
            break
        cnt+=1                                   

    else:
        print("Wrong Login Info!!!BYE")


def ExistingStudentHomepage(cnt,L):

    while True:
        print("\nSelect from 1 to 6:\nDetail of 1.Coach\n\t  2.Self-Record\n\t  3.Registered Sport Schedule only\n\n4.Modify Self Record\n\n5.Provide feedback and Star to Coach\n\n6.Exit") 
        choose=0
        while True:
            try:
                while(choose<1 or choose>6): 
                    choose=int(input("Select your choice:"))
                break

            except ValueError:
                print("Only Accept Whole Number!!!")

        if(choose==1):
            Display_RegisteredCoach(L)
        
        elif(choose==2):
            Display_SelfRecord(cnt)
            
        elif(choose==3):
            Display_RegisteredSportSchedule(L)
                
        elif(choose==4):
            Modify_SelfRecord(cnt)
           
        elif(choose==5):
            Feedback_Rating(L)      

        else:
            break
        
def AllStudent_function():
    import time
    while True:
        print ("\n",time.asctime( time.localtime(time.time()) ))
        print("*****To Registered and Non-Registered Students*****\n   Welcome All to REAL CHAMPIONS SPORTS ACADEMY")
        print("Would you like to view details of 1.Sport\n\t\t\t\t  2.Sport Schedule\n\n\t\t\t\t  3.If new student Register to Access other Details\n\n\t\t\t\t  4.For existing students\n\n\t\t\t\t  5.Exit")
        path=0
        while True:
            try:    
                while(path<1 or path>5):
                    path=int(input("Select your option: "))
                break
            except ValueError:
                print ("Only Accept Whole Number!!!")
            
        if(path==1):
            print("\nSportName,SportCode,SportFees,CoachName")
            Display("SPORTDETAILS")

        elif(path==2):
            print("\nSportName,Day,Time,SportCenterName,CoachName")
            Display("SPORTSCHEDULEDETAILS")

        elif(path==3):
            NewStudent_function()
                     
        elif(path==4):
            ExistingStudentLogin_function()
            
        else:
            break

def NewStudent_function():
    import re
    print("\nNew Student ^^^^^Welcome to REAL CHAMPIONS SPORTS ACADEMY^^^^^")
    print("Pls enter your details ^_^")

    username=str(input("Student Name: "))
    while not re.match(r"^[A-Za-z\s]+$",username):
        print("Only Alphabets are Allowed!!!")
        username=str(input("Student Name: "))

    password=input("Student Password: ")
    while not re.match(r"^[A-Za-z0-9]+$",password):
        print("Only Alphabets and Numbers are Allowed!!!")
        password=input("Student Password: ")

    myfile=open("STUDENTLOGINSTORE.txt","r")

    studentTP=[]

    for data in myfile:
        datas=data.strip()
        datass=datas.split(",")
        studentTP.append(datass[2])
    
    studentID=str(input("Student ID(TPXXXXXX): TP"))

    for element in studentTP:
        elements=element.replace("TP",'')
        while not ((studentID != elements) and ((len(studentID)==6) and studentID.isdigit())):
            print("Only Accept 6 Numbers or Student ID u entered has been taken")
            studentID=str(input("Student ID(TPXXXXXX): TP"))   

    file=open("COACHDETAILS.txt","r")

    listing=[]
    sportlist=[]

    for data in file:
        datas=data.strip()
        coach=datas.split(",")
        listing.append(coach[0])
        sportlist.append(coach[7])

    print("\nCoach:")
    print(listing)
    
    coachname=str(input("Coach Name: "))

    while coachname not in listing:
        print("Not available")
        coachname=str(input("Coach Name: "))

    correct=listing.index(coachname)

    sportname=sportlist[correct]

    print("Sport Name:",sportname)

    save=0
    while True:
        try:
            while(save<1 or save>2):
                save=int(input("Do u wish to save changes '1' for yes, '2' for no: "))
            break

        except ValueError:
            print("Only Accept Whole Number!!!")

    if(save==1):
        myfile=open("STUDENTLOGINSTORE.txt","a")
        myfile.write(username+","+password+",TP"+str(studentID)+","+sportname+","+coachname+"\n")
        print("Data Saved Successfully")

    else:
        print("Oops :( Data Not Saved")

    myfile.close()

MainMenu_function() #Starting Point
