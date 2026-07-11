def weeks(days):
    match days:
        case "day 1":
            return "monday"
        case "day 2":
            return "tuesday"
        case "day 3":
            return "wednesday"
        
        case "day 4":
            return "thrusday"
        case "day 5":
            return "friday"
        case "day 6":
            return "saturday"
        case "day 7":
            return "sunday"
        
        case _:
            return "7 din he hote ha chu*iya"
        
        
day = input("Enter days: ")
        
print(weeks(day))      


  
        