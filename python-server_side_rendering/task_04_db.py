from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# --- JSON oxuma funksiyası ---
def read_json(file_path):
    with open(file_path) as f:
        return json.load(f)

# --- CSV oxuma funksiyası ---
def read_csv(file_path):
    products = []
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

# --- SQLite oxuma funksiyası ---
def read_sqlite(file_path):
    try:
        conn = sqlite3.connect(file_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        products = []
        for r in rows:
            products.append({
                "id": r[0],
                "name": r[1],
                "category": r[2],
                "price": r[3]
            })
        conn.close()
        return products
    except sqlite3.Error as e:
        print("Database error:", e)
        return None

# --- Flask Route ---
@app.route('/products')
def products():
    source = request.args.get('source')  # json / csv / sql
    id_param = request.args.get('id')  # optional

    # Yanlış source yoxlaması
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    # Data oxu
    if source == 'json':
        data = read_json('products.json')
    elif source == 'csv':
        data = read_csv('products.csv')
    else:  # sql
        data = read_sqlite('products.db')
        if data is None:
            return render_template('product_display.html', error="Database error")

    # id ilə filter
    if id_param:
        try:
            id_int = int(id_param)
            filtered = [p for p in data if p['id'] == id_int]
            if not filtered:
                return render_template('product_display.html', error="Product not found")
            data = filtered
        except ValueError:
            return render_template('product_display.html', error="Invalid id")

    return render_template('product_display.html', products=data, error=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
