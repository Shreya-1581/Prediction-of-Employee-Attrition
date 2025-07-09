from fastapi import FastAPI,Path,Query
from fastapi.responses import JSONResponse
from model.predict import predict_output,model,MODEL_VERSION
from Schema.user_input import UserInput
from Schema.prediction_response import PredictionResponse

app=FastAPI()

@app.get("/")
def home():
    return {"Message":"Prediction of Employee Attrition"}

@app.get("/health")
def helath_check():
    return {
        "status":"OK",
        "version":MODEL_VERSION,
        "model_loaded":model is not None
    }

@app.post("/predict",response_model=PredictionResponse)
def predict_attrition(data:UserInput):
    user_input={
        "Age":data.Age,
        "BusinessTravel":data.BusinessTravel,
        "DailyRate":data.DailyRate,
        "Department":data.Department,
        "DistanceFromHome":data.DistanceFromHome,
        "Education":data.Education,
        "EducationField":data.EducationField,
        "EmployeeCount":data.EmployeeCount,
        "EmployeeNumber":data.EmployeeNumber,
        "EnvironmentSatisfaction":data.EnvironmentSatisfaction,
        "Gender":data.Gender,
        "HourlyRate":data.HourlyRate,
        "JobInvolvement":data.JobInvolvement,
        "JobLevel":data.JobLevel,
        "JobRole":data.JobRole,
        "JobSatisfaction":data.JobSatisfaction,
        "MaritalStatus":data.MaritalStatus,
        "MonthlyIncome":data.MonthlyIncome,
        "MonthlyRate":data.MonthlyRate,
        "NumCompaniesWorked":data.NumCompaniesWorked,
        "Over18":data.Over18,
        "OverTime":data.OverTime,
        "PercentSalaryHike":data.PercentSalaryHike,
        "PerformanceRating":data.PerformanceRating,
        "RelationshipSatisfaction":data.RelationshipSatisfaction,
        "StandardHours":data.StandardHours,
        "StockOptionLevel":data.StockOptionLevel,
        "TotalWorkingYears":data.TotalWorkingYears,
        "TrainingTimesLastYear":data.TrainingTimesLastYear,
        "WorkLifeBalance":data.WorkLifeBalance,
        "YearsAtCompany":data.YearsAtCompany,
        "YearsInCurrentRole":data.YearsInCurrentRole,
        "YearsSinceLastPromotion":data.YearsSinceLastPromotion,
        "YearsWithCurrManager":data.YearsWithCurrManager
    }
    try:
        prediction = predict_output(user_input)
        return JSONResponse(
            status_code=200,
            content={"predicted_category": str(prediction)} 
        )
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})