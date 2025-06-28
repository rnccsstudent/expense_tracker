from dotenv import load_dotenv
load_dotenv()
from flask import Flask, render_template, request, redirect, send_file
from db_config import get_connection
from xhtml2pdf import pisa
from io import BytesIO
import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
    data = cursor.fetchall()
    return render_template('index.html', expenses=data)

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        date = request.form['date']
        category = request.form['category']
        amount = request.form['amount']
        note = request.form['note']
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO expenses (date, category, amount, note) VALUES (%s, %s, %s, %s)",
                       (date, category, amount, note))
        conn.commit()
        return redirect('/')
    return render_template('add_expense.html')

@app.route('/download_pdf')
def download_pdf():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
    data = cursor.fetchall()
    rendered = render_template('report.html', expenses=data)
    pdf = BytesIO()
    pisa.CreatePDF(rendered, dest=pdf)
    pdf.seek(0)
    return send_file(pdf, download_name="report.pdf", as_attachment=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Railway sets PORT env variable
    app.run(host='0.0.0.0', port=port, debug=True)
