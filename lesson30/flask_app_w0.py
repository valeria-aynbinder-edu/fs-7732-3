import datetime

from flask import Flask, jsonify, request

app = Flask("flask_app")

@app.route('/api/dates/<string:date>')
def date_info(date):
    # validate date
    try:
        ts = datetime.datetime.strptime(date, '%d-%m-%Y')
        ret_val = {
            'date': ts
        }
        if 'season' in request.args and request.args['season'].lower() == 'true':
            season = 'winter'
            if ts.month in (3, 4, 5):
                season = 'spring'
            elif ts.month in (6,7,8):
                season = 'summer'
            elif ts.month in (9, 10, 11):
                season = 'autumn'
            ret_val.update({'season': season})

        return ret_val, 200

    except ValueError:
        return {'error': 'bad date format'}, 400


if __name__ == '__main__':
    app.run(debug=True, port=4747)