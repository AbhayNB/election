from config import app,db
import routes

app.secret_key = 'jbp_election'
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True,host='0.0.0.0')
