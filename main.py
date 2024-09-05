import os
# ישמש אותנו לגישה לניתוב קבצים
from utils import clear_screen
from actions import DiamondActions, perform_action
from data_handler import create_dataframe

# מודולים שונים בתוכנית שלנו  

def main():
    file_path = 'diamonds.csv'
    
# בדוק אם הקובץ קיים לפני שננסה לקרוא אותו
# כך שחסרונו לא יקריס את התוכנית
    if not os.path.isfile(file_path):
        print(f"Error: The file '{file_path}' was not found.")
        return

    df = create_dataframe(file_path)
    
    while True:
        clear_screen()
        print("Choose an action to perform on the diamond data:")
        print("1. Highest diamond price")
        print("2. Average diamond price")
        print("3. Number of Ideal diamonds")
        print("4. Unique diamond colors and their count")
        print("5. Median carat for Premium diamonds")
        print("6. Average carat by cut")
        print("7. Average price by color")
        print("8. Exit")


# קריאות לקובץ שתקלה בו לא תתקע את התוכנית 
        try:
            choice = int(input("Enter the number of the action you want to perform: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            input("Press Enter to try again...")
            continue

        if choice == 8:
            print("Exiting the program.")
            break

        decimal_places = None
        if choice in [1, 2, 5, 6, 7]:  # פעולות הדורשות מספר ספרות אחרי הנקודה
            try:
                decimal_places = int(input("Enter the number of decimal places for numerical results: "))
            except ValueError:
                print("Invalid input for decimal places. Using default format.")
                decimal_places = None
        
        try:
            action = DiamondActions(choice)
            result = perform_action(df, action, decimal_places)
            
            # הצגת התוצאות
            print(result)
            
            input("Press Enter to continue...")
        except ValueError:
            print("Invalid choice. Please choose a valid action.")
            input("Press Enter to try again...")

# הפעלת הפונקציה הראשית
if __name__ == "__main__":
    main()
