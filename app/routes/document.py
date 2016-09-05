from flask import jsonify, request

from app import app, db
from app.models.board import BoardModel


@app.route('/board/')
def list_board():
    result = BoardModel.query.all()

    return jsonify(print_board(result))


@app.route('/board/add/')
def add_board():
    name = request.args.get('name')
    title = request.args.get('title')

    if name and title:
        new_board = BoardModel(
            name=name,
            title=title
        )

        db.session.add(new_board)
        db.session.commit()

        return "Success"

    else:
        return "Error!"


@app.route('/board/search/<board_title>')
def search_board(board_title):
    result = BoardModel.query. \
        filter_by(title=board_title). \
        all()

    if result:
        return jsonify(print_board(result))

    else:
        return "None Found!"


def print_board(result):
    board_list = []
    if result:
        for board in result:
            board_list.append({
                'id': board.id,
                'name': board.name,
                'title': board.title,
                'created_date': board.created_date
            })
    else:
        board_list.append({
            'msg': "None"
        })
    return board_list
