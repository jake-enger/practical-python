contacts = {
    "number":4,
    "students":
    [
        {"name":"Jake Enger","email":"jake@example.com"},
        {"name":"John Oak","email":"professoroak@example.com"},
        {"name":"Stevie Wonder","email":"wonderthis@example.com"},
        {"name":"Porter Robinson","email":"nurturetheworld@example.com"}
    ] 
}

for students in contacts["students"]:
    print(students["email"])