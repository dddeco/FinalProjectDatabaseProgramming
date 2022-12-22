import pyodbc
import pandas as pd

driver = '{ODBC Driver 17 for SQL Server}'
server = 'db1118.database.windows.net'
port = '{1433}'
database = 'db1118'
username='me'
password = '{Cdma1234,,}'
odbc_str ='DRIVER='+driver+';SERVER='+server+';PORT='+port+';DATABASE='+database+';UID='+username+';PWD='+password

conn =  pyodbc.connect(odbc_str)
#cursor = conn.cursor()

def WriteIn(url):
    df = pd.read_csv(url)
    cursor = conn.cursor()
    for index, rows in df.iterrows():
        cursor.execute(
     "INSERT INTO dbo.Predict (pred_id,age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,target) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            rows.pred_id, rows.age, rows.sex,rows.cp,rows.trestbps,rows.chol,rows.fbs,rows.restecg,rows.thalach,rows.exang,rows.oldpeak,rows.slope,
            rows.ca,rows.thal,rows.target
        )
    conn.commit()

if __name__ == '__main__':
    WriteIn('Pred.csv')