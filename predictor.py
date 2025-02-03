from flask import Flask, render_template, request
from database import matches_collection
from scraper import scrape_match_data
from predictor import predict_match_outcome

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    
    if request.method == "POST":
        team_name = request.form["team_name"]
        match_data = scrape_match_data(team_name)
        
        if match_data:
            prediction = predict_match_outcome(match_data)
            matches_collection.insert_one({"team": team_name, "prediction": prediction})
    
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
