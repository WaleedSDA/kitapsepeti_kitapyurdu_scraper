from flask import Flask, request

app = Flask(__name__)


@app.route('/scrape', methods=['GET'])
def scrape():
    website = request.args.get('website', None)
    category_name = request.args.get('category_name', None)
    


if __name__ == '__main__':
    app.run()
