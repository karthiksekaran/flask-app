import enum
from flask import Flask, jsonify, request

#client
app = Flask(__name__)
book_list = [
    {
        "id":1,
        "title":"Data Structure",
        "language":"English",
        "author":"Karumanchi",
    },
    {
        "id":2,
        "title":"Python Machine Learning",
        "language":"English",
        "author":"Sebastian",
    },
]

#WSGI Server - Books 
@app.route('/books', methods=['GET', 'POST'])

#View Function

def books():
    if request.method == 'GET':
        if len(book_list)>0:
            return jsonify(book_list), 201
        else:
            'Nothing Found', 404
    if request.method == 'POST':
        new_title = request.form['title']
        new_language = request.form['language']
        new_author = request.form['author']
        iD = book_list[-1]['id']+1

        new_book = {
            'id':iD,
            'title':new_title,
            'language':new_language,
            'author':new_author
        }
        book_list.append(new_book)
        return jsonify(book_list), 201

@app.route('/books/<int:id>',  methods=['GET', 'PUT', 'DELETE'])

def update(id):
    if request.method == 'GET':
        for book in book_list:
            if book['id'] == id:
                return jsonify(book)
            pass

    if request.method == 'DELETE':
        for index, book in enumerate(book_list):
            if book['id'] == id:
                book_list.pop(index)
                return jsonify(book_list)

    if request.method == 'PUT':
        for book in book_list:
            if(book['id'] == id):
                book['title'] = request.form['title']
                book['language'] = request.form['language']
                book['author'] = request.form['author']
            
            update_data = {
                'id' : id,
                'title' : book['title'], 
                'language' : book['language'],
                'author' : book['author']
                }
            return jsonify(update_data)

if __name__ == '__main__':
    app.run()