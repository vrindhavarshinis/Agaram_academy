application_form={

            "members":[
                {
                    "relation":"Father",
                    "name":"Suresh. M",
                    "occupation":"Business"
                },
                {
                    "relation":"Mother",
                    "name":"Saroja",
                    "occupation":"Tailor"
                },   
            ],
            "annual_income":400000
            
}

userinput=(input("Do you have any Siblings?"))
if userinput=="no" or userinput=="No":
    print("No changes is required")
    print("You are not eligible for Scholarship")
elif userinput=="yes" or userinput=="Yes":
    relation=(input("Enter your relationship with sibling:"))
    name=(input("Enter your sibling's Name:"))
    occupation=(input("Enter your sibling's Occupation: "))
    a={}
    a["relation"] = relation
    a["name"]=name
    a["occupation"]=occupation
    
  
    application_form["members"].append(a)
    print(application_form["members"])
    