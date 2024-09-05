import os

# כאן המודול משמש לניקוי המסך
# הקובץ יוכל לשמש אותנו בעתיד לתכונות דומות בהמשך
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
