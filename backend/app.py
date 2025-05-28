# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)  # Enable CORS for all domains for development

# # Config SQLite DB
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketing.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# # DB model
# class MarketingEntry(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     business_type = db.Column(db.String(150), nullable=False)
#     target_audience = db.Column(db.String(150), nullable=False)
#     key_selling_points = db.Column(db.Text, nullable=False)
#     generated_content = db.Column(db.Text, nullable=False)

# # Initialize DB (run once)
# @app.before_first_request
# def create_tables():
#     db.create_all()

# @app.route('/generate', methods=['POST'])
# def generate():
#     data = request.get_json()

#     business_type = data.get('business_type')
#     target_audience = data.get('target_audience')
#     key_selling_points = data.get('key_selling_points')

#     if not all([business_type, target_audience, key_selling_points]):
#         return jsonify({'error': 'Missing fields'}), 400

#     # Simple dummy marketing content generation logic
#     generated_content = (
#         f"Introducing our {business_type} tailored specifically for {target_audience}. "
#         f"Our key strengths include {key_selling_points}. "
#         "Experience the best quality and value with us!"
#     )

#     # Store in DB
#     entry = MarketingEntry(
#         business_type=business_type,
#         target_audience=target_audience,
#         key_selling_points=key_selling_points,
#         generated_content=generated_content
#     )
#     db.session.add(entry)
#     db.session.commit()

#     return jsonify({'marketing_content': generated_content})


# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketing.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class MarketingEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_type = db.Column(db.String(150), nullable=False)
    target_audience = db.Column(db.String(150), nullable=False)
    key_selling_points = db.Column(db.Text, nullable=False)
    generated_content = db.Column(db.Text, nullable=False)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()

    business_type = data.get('business_type')
    target_audience = data.get('target_audience')
    key_selling_points = data.get('key_selling_points')

    if not all([business_type, target_audience, key_selling_points]):
        return jsonify({'error': 'Missing fields'}), 400

    generated_content = (
        f"Introducing our {business_type} tailored specifically for {target_audience}. "
        f"Our key strengths include {key_selling_points}. "
        "Experience the best quality and value with us!"
    )

    entry = MarketingEntry(
        business_type=business_type,
        target_audience=target_audience,
        key_selling_points=key_selling_points,
        generated_content=generated_content
    )
    db.session.add(entry)
    db.session.commit()

    return jsonify({'marketing_content': generated_content})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
