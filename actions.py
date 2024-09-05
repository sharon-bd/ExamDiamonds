
from enum import Enum

# הגדרת enum עבור פעולות שונות עם מזהה מספרי לכל פעולה
class DiamondActions(Enum):
    HIGHEST_PRICE = 1  # פעולה להצגת המחיר הגבוה ביותר
    AVERAGE_PRICE = 2  # פעולה להצגת המחיר הממוצע
    IDEAL_COUNT = 3    # פעולה לספירת יהלומים עם חיתוך "Ideal"
    UNIQUE_COLORS = 4  # פעולה להצגת מספר הצבעים הייחודיים
    MEDIAN_CARAT_PREMIUM = 5  
    
    #  פעולה להצגת מדד משקל (קראט) של יהלומים עם חיתוך פרימיום.המדד המוצג הוא חישוב חציוני  
    # כלומר: בתוך אוכלוסיית  יהלומי ה"פרימיום"-חצי מהם עם קרט גבוה מהנתון,וחציו השני גבוה מהנתון
    AVERAGE_CARAT_BY_CUT = 6  # פעולה להצגת המשקל הממוצע לפי סוג חיתוך
    AVERAGE_PRICE_BY_COLOR = 7  # פעולה להצגת המחיר הממוצע לפי צבע
    EXIT = 8           # פעולה לסיום התוכנית

# פונקציה לביצוע פעולה על DataFrame של יהלומים
def perform_action(df, action, decimal_places=None):
    # טיפול בפעולה להצגת המחיר הגבוה ביותר
    if action == DiamondActions.HIGHEST_PRICE:
        highest_price = df['price'].max()
        return f"Highest diamond price: {highest_price}" if decimal_places is None else f"Highest diamond price: {highest_price:.{decimal_places}f}"

    # טיפול בפעולה להצגת המחיר הממוצע
    elif action == DiamondActions.AVERAGE_PRICE:
        average_price = df['price'].mean()
        return f"Average diamond price: {average_price}" if decimal_places is None else f"Average diamond price: {average_price:.{decimal_places}f}"

    # טיפול בפעולה לספירת יהלומים עם חיתוך "Ideal"
    elif action == DiamondActions.IDEAL_COUNT:
        ideal_count = df[df['cut'] == 'Ideal'].shape[0]
        return f"Number of Ideal diamonds: {ideal_count}"

    # טיפול בפעולה להצגת מספר הצבעים הייחודיים
    elif action == DiamondActions.UNIQUE_COLORS:
        unique_colors = df['color'].nunique()
        color_list = df['color'].unique()
        return f"Number of unique colors: {unique_colors}\nColors: {color_list}"

    # טיפול בפעולה להצגת מדד משקל (קראט) של יהלומים עם חיתוך "Premium"
    elif action == DiamondActions.MEDIAN_CARAT_PREMIUM:
        median_carat_premium = df[df['cut'] == 'Premium']['carat'].median()
        return f"Median carat for Premium diamonds: {median_carat_premium}" if decimal_places is None else f"Median carat for Premium diamonds: {median_carat_premium:.{decimal_places}f}"

    # טיפול בפעולה להצגת המשקל הממוצע לפי סוג חיתוך
    elif action == DiamondActions.AVERAGE_CARAT_BY_CUT:
        avg_carat_by_cut = df.groupby('cut')['carat'].mean()
        result = "Average carat by cut:\n"
        for cut, avg_carat in avg_carat_by_cut.items():
            result += f"{cut}: {avg_carat}" if decimal_places is None else f"{cut}: {avg_carat:.{decimal_places}f}\n"
        return result

    # טיפול בפעולה להצגת המחיר הממוצע לפי צבע
    elif action == DiamondActions.AVERAGE_PRICE_BY_COLOR:
        avg_price_by_color = df.groupby('color')['price'].mean()
        result = "Average price by color:\n"
        for color, avg_price in avg_price_by_color.items():
            result += f"{color}: {avg_price}" if decimal_places is None else f"{color}: {avg_price:.{decimal_places}f}\n"
        return result
