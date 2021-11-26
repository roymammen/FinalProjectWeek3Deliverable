import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:Mcsi123$5@localhost:5432/lax_aqi_temp_db")
lax_temp_df = pd.read_sql("SELECT * FROM lax_aqi_temp_db;", engine)

def predict_week_mean_temp_ml(Population_rate,SO2_conc,PM10_conc,PM2_5_conc,NO2_conc,month_day_ts):
    #lax_temp_df = pd.read_csv("./lax_temp_aqi_ml_db.csv")

    X = lax_temp_df[['population','lat','lon','so2_conc','pm10_conc','pm2_5_conc','no2_conc','month_day_ts']]
    y = lax_temp_df['avgtemp']

    Population = lax_temp_df['population'].iat[-1]
    Population += (lax_temp_df['population'].iat[-1] * Population_rate/100)
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=1)

    rf = RandomForestRegressor()
    rf.fit(X_train,y_train)
    print(f"Training Data Score: {rf.score(X_train, y_train)}")
    print(f"Testing Data Score: {rf.score(X_test, y_test)}")

    return rf.predict([[12447000,34.1365,-117.92391,SO2_conc,PM10_conc,PM2_5_conc,NO2_conc,month_day_ts]])
