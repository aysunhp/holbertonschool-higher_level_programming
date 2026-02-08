from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# JSON fayldan oxuma funksiyası
def read_json(file_path):
    with open(file_path) as f:
        return json.load(f)

# CSV fayldan oxuma funksiyası
def read_csv(file_path):
    products = []
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # id və price-ı doğru tipə çevir
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

# Route
@app.route('/products')
def products():
    source = request.args.get('source')  # json və ya csv
    id_param = request.args.get('id')  # optional id

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    # Fayldan məlumat oxu
    if source == 'json':
        data = read_json('products.json')
    else:
        data = read_csv('products.csv')

    # id varsa filter et
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
