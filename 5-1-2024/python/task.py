resume={}

# getname=(input("Enter Your Name:"))
# resume["name"]=getname

# getcontactno=int(input("Enter Your Mobile Number:"))
# resume["contact_number"]=getcontactno

# getemail=(input("Enter Your Email Id:"))
# resume["email_id"]=getemail

# getdate=(input("Enter date:"))
# resume["date:"]=getdate

# getobjetives=(input("Type Your Objectives:"))
# resume["objectives"]=getobjetives


# academicdetails=int(input("How many Education did you have?"))
# resume["academic_details"]={}  
# for each in range(0,academicdetails):
     
#     institutionname=(input("Enter Your Institution Name:"))
#     course=input("Enter your Course Name:")
#     percentage=int(input("Enter your Percentage:"))
#     year=int(input("Enter your Year of Passed Out: "))
     
#     resume["academic_details"]["institution_name"]=institutionname
#     resume["academic_details"]["course_name"]=course
#     resume["academic_details"]["percentage"]=percentage
#     resume["academic_details"]["year"]=year
    
    
# skill=int(input("How many skills did you have?"))
# resume["skills"]=[]
# for each in range(skill):
#     skill1=(input("Enter your skill:"))
    
    
#     resume["skills"].append(skill1)
    
# print(resume["skills"])
    

personaldetails=int(input("How many personal details did you have?"))
resume["personal_details"]={}

language=[]
languages=int(input("How Many Languages Do you know?"))
for each in range(languages):
     language1=(input("Enter language name:"))
     language.append(language1)
resume["personal_details"]["languagesknown"]=language



getdob=input("Enter your date of birth:")
resume["personal_details"]["date_of_birth"]=getdob


print(resume)