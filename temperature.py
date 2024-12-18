for i in range(1,11):
    temperature= random.radiant(20,100)
    print (f"Reading(i): temperature={temperature} C")
    
    if temperature>70:
        print ("Danger! high temperature detected. Stopping monitoring.")
        break #stop monitoring when temprature exceeds safe limits