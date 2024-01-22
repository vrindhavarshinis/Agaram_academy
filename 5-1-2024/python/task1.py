resume={}
askuser=int(input("Enter Number of Education:"))
resume["education"]=[]


    
def print_value(a,b):
    for each in range(a):
        institutionname=(input("Enter Your Institution Name:"))
        course=input("Enter your Course Name:")
        percentage=int(input("Enter your Percentage:"))
        year=int(input("Enter your Year of Passed Out: "))
        b.append({"institution_name":institutionname,
                  "course":course,
                  "percentage":percentage,
                  "year":year})

        
    
print_value(askuser,resume["education"])
print(resume)