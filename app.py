from flask import Flask, jsonify, request
from util import (
    get_ics_events,
)

app = Flask(__name__)

@app.route('/parse-ics/<path:ics_url>', methods=['GET'])
def parse_ics(ics_url):
    if not ics_url:
        return jsonify({'error': 'ics_url parameter is required'}), 400
    
    try:
        events = get_ics_events(ics_url)
        return jsonify({'events': events})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()


