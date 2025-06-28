# 💸 Expense Tracker Web App

A mobile-friendly and user-interactive expense tracker web application built with **Python (Flask)**, **MySQL**, and **HTML/CSS/JS**. Track your daily expenses, view monthly/yearly reports with graphs, and download them as PDF.

---

## ✨ Features

- ✅ Add daily expenses with date, category, amount, and notes
- 📅 View expenses filtered by **month** or **year**
- 📊 Visualize monthly spending with interactive **charts**
- 📂 Download full yearly/monthly expense report as **PDF**
- 🔍 Search and filter expenses
- 📱 Fully **mobile-responsive** interface

---

## 🛠️ Tech Stack

| Layer        | Technologies Used |
|--------------|-------------------|
| Frontend     | HTML, CSS, JavaScript, Bootstrap |
| Backend      | Python, Flask |
| Database     | MySQL (PlanetScale / FreeSQLDatabase / Railway Plugin) |
| Charts       | Chart.js |
| PDF Export   | xhtml2pdf |
| Deployment   | Render / Railway / Vercel (Frontend only) |

---

## 📁 Project Structure
<pre> expense_tracker/
├── static/
│ └── style.css # CSS styling
├── templates/
│ ├── index.html # Home page (expense list)
│ ├── add_expense.html # Form to add new expense
│ └── report.html # Template for PDF report (PDF generation)
├── app.py # Main Flask application
├── db_config.py # MySQL DB configuration
├── requirements.txt # Python dependencies
└── README.md # Project documentation (this file)
 </pre>


---

## ⚙️ Setup Instructions

### 🔧 Prerequisites

- Python 3.8+
- pip
- MySQL server (locally or cloud-hosted)

---

### 💻 Local Setup

```bash
# Clone the repository
git clone https://github.com/your-username/expense_tracker.git
cd expense_tracker

# Install dependencies
pip install -r requirements.txt

# Setup database manually (or connect to hosted MySQL)
# Use schema below to create table

# Run the app
python app.py

🗄️ Database Schema
sql
Copy
Edit
CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    category VARCHAR(100),
    amount DECIMAL(10,2),
    note TEXT
);

🚀 Deployment
Option 1: Railway (Recommended for Free MySQL)
Create a new Railway project

Add MySQL Plugin

Set MYSQLHOST, MYSQLUSER, etc. from Railway ENV to your db_config.py

Start Command:

bash
Copy
Edit
gunicorn app:app

👤 Author
Pranab Mahata
📧 pranabmahata197@gmail.com
🌐 LinkedIn
