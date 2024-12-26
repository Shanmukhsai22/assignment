from flask import Flask, request, jsonify
from flask_cors import CORS
from crawler import BusinessCrawler
from database import Database

app = Flask(__name__)
# Enable CORS for all routes
CORS(app)

crawler = BusinessCrawler()
db = Database()

# Test route to verify API is working
@app.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'API is working!'})

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to the API!'})

@app.route('/api/crawl', methods=['POST'])
def crawl_business():
    try:
        data = request.json
        if not data or 'business_name' not in data:
            return jsonify({'error': 'Business name is required'}), 400
        
        business_name = data['business_name'].strip()
        if not business_name:
            return jsonify({'error': 'Invalid business name'}), 400
        
        # Check if business exists in the database
        existing_data = db.get_business(business_name)
        if existing_data:
            return jsonify({'data': existing_data[0], 'source': 'database'})
        
        # Crawl the website for the business
        crawled_data = crawler.search_business(business_name)
        if not crawled_data:
            return jsonify({'error': 'Business not found'}), 404
        
        # Insert crawled data into the database
        db.insert_business(crawled_data)
        return jsonify({'data': crawled_data, 'source': 'crawled'})
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
