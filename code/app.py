from flask import Flask, render_template, request
from run_ml import predict_week_mean_temp_ml

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/predict_wk_tmp',methods=['POST'])
def predict_wk_tmp():
    # Get the data from the POST request.
    if request.method == "POST":
        # print(request.form["Population"])
        Population_rate = int(request.form["Population"])
        SO2_conc = float(request.form["SO2_conc"])
        PM10_conc = float(request.form["PM10_conc"])
        PM2_5_conc = float(request.form["PM2_5_conc"])
        NO2_conc = float(request.form["NO2_conc"])
        Month = int(request.form["Month"])
        Week = int(request.form["Week"])
        
        month_day_ts = Month+(Week/30)
        print("call my ml model predict_week_mean_temp_ml()")
        predict_week_mean_temp = predict_week_mean_temp_ml(Population_rate,SO2_conc,PM10_conc,PM2_5_conc,NO2_conc,month_day_ts) # call my ml model
        print(predict_week_mean_temp)

        mean_temp = predict_week_mean_temp[0]
        #mean_temp=345.67
        print(mean_temp)

        results = f'Mean temperature for Month {Month} Week {Week} is {mean_temp} deg F'
        print(results)
        
        return render_template("result.html", results=results)
