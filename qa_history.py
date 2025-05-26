import sqlite3

conn = sqlite3.connect("gemini-2-flash.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM qa_history order by timestamp DESC LIMIT 10")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()


# or run in the terminal 
# sqlite3 gemini-2-flash.db
# SELECT * FROM qa_history order by timestamp desc LIMIT 2;

#or add app endpoint /history with custom reponses like
# @app.get("/history", response_model=List[QAHistoricItem])
# def get_history(
#     limit: int = Query(10, description="Number of records to return"),
#     db: Session = Depends(get_db)
# ):
#     return db.query(QAHistory).order_by(QAHistory.timestamp.desc()).limit(limit).all()