from flask import jsonify, request
from flask_restful import Resource, reqparse
from sqlalchemy.orm.exc import NoResultFound

from app import db, api
from app.models.board import BoardModel


@api.resource('/board/')
class Board(Resource):
    def get(self):

        param_parser = reqparse.RequestParser()
        param_parser.add_argument('q', required=False, default=None)
        args = param_parser.parse_args()

        if not args.q:
            result = BoardModel.query.all()

        else:
            try:
                result = BoardModel.query.filter_by(name=args.q).all()

            except NoResultFound:
                result = []
                result.append({
                    'msg': "Not found"
                })

        return jsonify(print_board(result))

    def post(self):
        request_body = request.get_json()

        if request_body['name'] and request_body['title']:
            new_board = BoardModel(
                name=request_body['name'],
                title=request_body['title']
            )

            db.session.add(new_board)
            db.session.commit()

            return "Success"

        else:
            return "Error!"


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
