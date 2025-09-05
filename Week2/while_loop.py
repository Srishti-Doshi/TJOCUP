print("Hello Everyone, We are starting patients may come in ..")
n = 1;
patient = 1;

while(patient == 1):
    print("Patient with token number ", n, "please come in")
    patient = input("patient availability next = ")
    patient = int(patient)
    if(patient == 1):
        n = n+1
        
    

print("All patients Treated!")
    