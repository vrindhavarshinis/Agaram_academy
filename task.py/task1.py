students_marks=[
{
    "name":"Vrindha Varshini. S",
    "place":"Nagercoil",
    "major":"Maths",
    "marks":[
        {
            "sub_name":"English",
            "max_mark":100,
            "marks_scored":80
        },
        {
            "sub_name":"Tamil",
            "max_mark":100,
            "marks_scored":92
        },
        
        {
            "sub_name":"Maths",
            "max_mark":100,
            "marks_scored":100
        },
        
        {
            "sub_name":"Science",
            "max_mark":100,
            "marks_scored":100
        },
        {
            "sub_name":"Computer",
            "max_mark":100,
            "marks_scored":90
        },
        
        {
            "sub_name":"Social Science",
            "max_mark":100,
            "marks_scored":95
        },
        
     ],
    "age":20,
    "Hobbies":["craftmaking","cooking"],
    "gender":"Female",
    "ncc":True,
    "sports":["Handball","Volleyball"],
    "annual_income":100000
},
                
 {
    "name":"Priya.T",
    "place":"Nagercoil",
    "major":"Maths",
    "marks":[
        {
            "sub_name":"English",
            "max_mark":100,
            "marks_scored":70
        },
        {
            "sub_name":"Tamil",
            "max_mark":100,
            "marks_scored":52
        },
        
        {
            "sub_name":"Maths",
            "max_mark":100,
            "marks_scored":80
        },
        
        {
            "sub_name":"Science",
            "max_mark":100,
            "marks_scored":60
        },
        {
            "sub_name":"Computer",
            "max_mark":100,
            "marks_scored":93
        },
        
        {
            "sub_name":"Social Science",
            "max_mark":100,
            "marks_scored":95
        },
        
     ],
    "age":20,
    "Hobbies":["Book Reading","cooking"],
    "gender":"Female",
    "ncc":True,
    "sports":["Handball","Cricket"],
    "annual_income":120000
},
 
{
    "name":"Ram.S",
    "place":"Nagercoil",
    "major":"Maths",
    "marks":[
        {
            "sub_name":"English",
            "max_mark":100,
            "marks_scored":80
        },
        {
            "sub_name":"Tamil",
            "max_mark":100,
            "marks_scored":92
        },
        
        {
            "sub_name":"Maths",
            "max_mark":100,
            "marks_scored":72
        },
        
        {
            "sub_name":"Science",
            "max_mark":100,
            "marks_scored":88
        },
        {
            "sub_name":"Computer",
            "max_mark":100,
            "marks_scored":90
        },
        
        {
            "sub_name":"Social Science",
            "max_mark":100,
            "marks_scored":95
        },
        
     ],
    "age":20,
    "Hobbies":["playing guitar","singing"],
    "gender":"Male",
    "ncc":False,
    "sports":["Handball","Volleyball"],
    "annual_income":150000
},
{
    "name":"Meera.M",
    "place":"Nagercoil",
    "major":"Maths",
    "marks":[
        {
            "sub_name":"English",
            "max_mark":100,
            "marks_scored":80
        },
        {
            "sub_name":"Tamil",
            "max_mark":100,
            "marks_scored":92
        },
        
        {
            "sub_name":"Maths",
            "max_mark":100,
            "marks_scored":62,
        },
        
        {
            "sub_name":"Science",
            "max_mark":100,
            "marks_scored":83
        },
        {
            "sub_name":"Computer",
            "max_mark":100,
            "marks_scored":90
        },
        
        {
            "sub_name":"Social Science",
            "max_mark":100,
            "marks_scored":95
        },
        
     ],
    "age":20,
    "Hobbies":["craftmaking","Dancing"],
    "gender":"Female",
    "ncc":False,
    "sports":["Ball Badminton","Volleyball"],
    "annual_income":100000
},

{
    "name":"Dhanush",
    "place":"Nagercoil",
    "major":"Maths",
    "marks":[
        {
            "sub_name":"English",
            "max_mark":100,
            "marks_scored":80
        },
        {
            "sub_name":"Tamil",
            "max_mark":100,
            "marks_scored":92
        },
        
        {
            "sub_name":"Maths",
            "max_mark":100,
            "marks_scored":76
        },
        
        {
            "sub_name":"Science",
            "max_mark":100,
            "marks_scored":56
        },
        {
            "sub_name":"Computer",
            "max_mark":100,
            "marks_scored":90
        },
        
        {
            "sub_name":"Social Science",
            "max_mark":100,
            "marks_scored":95
        },
        
     ],
    "age":20,
    "Hobbies":["Dancing","Playing flute"],
    "gender":"Male",
    "ncc":True,
    "sports":["Football","Volleyball"],
    "annual_income":130000
},
]
highest_mathsandscience_total = 0
student_name=""



for each in students_marks:
    maths_highest= 0
    science_highest=0
    for m in each["marks"]:
        if (m["sub_name"] == "Maths") :
            m["marks_scored"] > maths_highest 
            maths_highest=m["marks_scored"]
            
        if m["sub_name"]=="Science":
            m["marks_scored"]>science_highest
            science_highest=m["marks_scored"]
            
        total=maths_highest+science_highest
        
        if total>highest_mathsandscience_total:
            highest_mathsandscience_total=total
            student_name=each["name"]

print("Highest total scorer in maths and science:", student_name)
print("Highest total score:", highest_mathsandscience_total)