my_resume= {
        "name": "Vrindha Varshini. S",
        "contact_number":7904391212,
        "email":"vrindhavarshini@gamil.com",
        "date":"21-12-2023",
        "objectives":"Aim to be associated with a progressive organization which offers an excellent atmosphere to prove myself by utilizing all technical knowledge into practice and profit myself with experience and valuable knowledge for the development and growth of the organisation",
     

        "academic_details":[
            {"institution_name":"Women's Christian College",
             "course":"B.com",
             "percentage":86.4,
             "year":2021
          },
          {
              "institution_name":"S.M.R.V Higher Secondary School",
              "course":"Hsc",
              "percentage":85,
              "year":2017
          },
          {
              "institution_name":"S.M.R.V Higher Secoondary School",
              "course":"SSLC",
              "percentage":80,
              "year":2015

          } ],
    
    
        "experience":[
            {
                "company_name":"XY Company",
                "role":"Digital Marketing Manager",
                "year_of_experience":2
            },
            {
                "company_name":"YX Company",
                "role":"Social Media Manager",
                "year_of_experience":1
            }
        ],
    
    "projects":[
        {
          "title":"Social Media analysis ",
          "year":2022,
          "role":"Researcher"
          

        },
        {
            "title":"Digital Marketing",
            "year":2023,
            "role":"Data Analyst"
        }
    ],
    "certifications":[
        {
            "certificate_name":"Life Insurance a Tool of Risk Management",
            "given_institution":"Insurance Institute of Mumbai"
        },
        {
            "certificate_name":"Life Skills Development",
            "given_institution":"Bharat Sevak Samaj"
        },
        
        
    
    ],

    "skills":[
        "communication skills"," leaderrship","sales analysis", "Business process improvement"
    ],

    "personal_details":
        {
            "languages_known":["Tamil","English","Hindi"],
            "date_of_birth":"26-06-2003",
            "address":"No.1,Vellalar East Street, Vadasery",
            "hobbies":["craft making", "cooking"]

        }
    

    }

def add(list):
    
    
    userinput=input("Do you want to add Your Informations in Academic details:")

    if userinput=="yes" or userinput=="Yes":
    

     institutionname=input("Enter your Institute Name:")
     course=input("Enter your Course Name:")
     percentage=int(input("Enter your Percentage:"))
     year=int(input("Enter your Year of Passed Out: "))
     a={}
     a["institution_name"]=institutionname
     a["course"]=course
     a["percentage"]=percentage
     a["year"]=year
     list.append(a)
    
    return list


updatedlist=add(my_resume["academic_details"])
my_resume["academic_details"]=updatedlist


print(updatedlist)