import streamlit as st
import requests

API_URL="http://localhost:8000/predict"

st.title("Employee Attrition Prediction")
st.header("About")
st.text("Employee attrition is basically downfall in an organization where employees depart. They are the most important bodies of an organization who contributes in the growth of organization. So bthis help can help to predict the employee attrition so that company can take some steps to avoid attrition. ")

age=st.slider("Age",min_value=1,max_value=100,value=30)
businesstravel=st.selectbox("BusinessTravel",['Travel_Rarely', 'Travel_Frequently', 'Non-Travel'],index=0)
dr,d,dfh=st.columns([1,2,1])
dailyrate=dr.number_input("DailyRate",step=16)
department=d.selectbox("Department",['Sales', 'Research & Development', 'Human Resources'],index=0)
distancefromhome=dfh.number_input("DistanceFromHome",step=1)
edu,ef=st.columns(2)
education=edu.selectbox("Education",[1,2,3,4,5])
educationfield=ef.selectbox("EducationField",['Life Sciences', 'Other', 'Medical', 'Marketing',
       'Technical Degree', 'Human Resources'],index=0)
ec,en,es=st.columns(3)
employeecount=ec.selectbox("EmployeeCount",[1],index=0)
employeenumber=en.number_input("EmployeeNumber",step=1)
employeesatisfaction=es.selectbox("EnvironmentSatisfaction",[1,2,3,4])
g,hr=st.columns(2)
gender=g.radio("Gender",["Male","Female"])
hourlyrate=hr.number_input("HourlyRate",step=10)
ji,jl,jr=st.columns(3)
jobinvolvement=ji.selectbox("JobInvolvement",[1,2,3,4])
joblevel=jl.selectbox("JobLevel",[1,2,3,4,5])
jobrole=jr.selectbox("JobRole",['Sales Executive', 'Research Scientist', 'Laboratory Technician',
       'Manufacturing Director', 'Healthcare Representative', 'Manager',
       'Sales Representative', 'Research Director', 'Human Resources'])
js,ms=st.columns([1,2])
jobsatisfaction=js.selectbox("JobSatisfaction",[1,2,3,4])
maritalstatus=ms.selectbox("MaritalStatus",['Single', 'Married', 'Divorced'])
mi,mr=st.columns(2)
monthlyincome=mi.number_input(" MonthlyIncome",step=10000)
monthlyrate=mr.number_input("MonthlyRate",step=10000)
nc,oe,ot=st.columns(3)
numcompaniesworked=nc.selectbox("NumCompaniesWorked",[0,1,2,3,4,5,6,7,8,9])
over18=oe.selectbox("Over18",["Y"])
overtime=ot.selectbox("OverTime",['Yes', 'No'])
percentsalaryhike=psh=st.number_input("PercentSalaryHike",step=5)
pr,rs=st.columns(2)
performancerating=pr.selectbox("PerformanceRating",[1,2,3,4])
relationshipsatisfaction=rs.selectbox("RelationshipSatisfaction",[1,2,3,4])
standardhours=st.number_input("StandardHours",value=80)
so,twy=st.columns(2)
stockoptionlevel=so.selectbox("StockOptionLevel",[1,2,3,4])
totalworkingyears=twy.number_input("TotalWorkingYears",step=1)
trainingtimeslastyear=st.selectbox("TrainingTimesLastYear",[0,1,2,3,4,5,6])
worklifebalance=st.selectbox("WorkLifeBalance",[1,2,3,4])
yac,ytcr,yslp,ywcm=st.columns(4)
yearsatcompany=yac.number_input("YearsAtCompany",step=1)
yearsincurrentrole=ytcr.number_input("YearsInCurrentRole",step=1)
yearssincelastpromotion=yslp.number_input("YearsSinceLastPromotion",min_value=0,max_value=15,step=1)
yearswithcurrmanager=ywcm.number_input("YearsWithCurrManager",min_value=0,max_value=20,step=1)

if st.button("Predict"):
    input_data={
        "Age":age,
        "BusinessTravel":businesstravel,
        "DailyRate":dailyrate,
        "Department":department,
        "DistanceFromHome":distancefromhome,
        "Education":education,
        "EducationField":educationfield,
        "EmployeeCount":employeecount,
        "EmployeeNumber":employeenumber,
        "EnvironmentSatisfaction":employeesatisfaction,
        "Gender":gender,
        "HourlyRate":hourlyrate,
        "JobInvolvement":jobinvolvement,
        "JobLevel":joblevel,
        "JobRole":jobrole,
        "JobSatisfaction":jobsatisfaction,
        "MaritalStatus":maritalstatus,
        "MonthlyIncome":monthlyincome,
        "MonthlyRate":monthlyrate,
        "NumCompaniesWorked":numcompaniesworked,
        "Over18":over18,
        "OverTime":overtime,
        "PercentSalaryHike":percentsalaryhike,
        "PerformanceRating":performancerating,
        "RelationshipSatisfaction":relationshipsatisfaction,
        "StandardHours":standardhours,
        "StockOptionLevel":stockoptionlevel,
        "TotalWorkingYears":totalworkingyears,
        "TrainingTimesLastYear":trainingtimeslastyear,
        "WorkLifeBalance":worklifebalance,
        "YearsAtCompany":yearsatcompany,
        "YearsInCurrentRole":yearsincurrentrole,
        "YearsSinceLastPromotion":yearssincelastpromotion,
        "YearsWithCurrManager":yearswithcurrmanager
    }

    try:
        response=requests.post(API_URL,json=input_data)
        if response.status_code==200:
            result=response.json()
            st.success(f"Predected Employee Attrition:**{result['predicted_category']}**")
        else:
            st.error(f"API Error{response.status_code}-{response.text}")
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to FASTAPI server.Make sure it is running on port 8000")


