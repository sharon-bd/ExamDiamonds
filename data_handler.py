import pandas as pd

#  מציג את התוצאות באופן קריא יותר PANDAS 
# המודול כולו מקל על קריאוּת הקוד
def read_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
#  מביא סטרינג[מחרוזת] מכל שורה מהקובץ readlines
    headers = lines[0].strip().split(',')
    data = []
    for line in lines[1:]:
        values = line.strip().split(',')
        data.append(dict(zip(headers, values)))
#     שני אלה מנפים את הנתונים המעניינים אותנו ,ללא סימני הפיסוק והרווחים שבקובץ  : strip split 
#     שלנו CSV   
    return headers, data

def create_dataframe(file_path):
    headers, data = read_data(file_path)
    df = pd.DataFrame(data)
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['carat'] = pd.to_numeric(df['carat'], errors='coerce')
    return df
