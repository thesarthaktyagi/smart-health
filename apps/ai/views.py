from django.shortcuts import render, redirect
import joblib
import numpy as np
import pickle

# All the artifacts
forest = joblib.load('E:\\smart_health\\apps\\ai\\cancer_model.pkl')
heart_model = joblib.load('E:\\smart_health\\apps\\ai\\heart_model.pkl')
diabetes_model = joblib.load('E:\\smart_health\\apps\\ai\\diabetes_model.pkl')
kidney_model = joblib.load('E:\\smart_health\\apps\\ai\\kidney_model.pkl')
liver_model = joblib.load('E:\\smart_health\\apps\\ai\\liver_model.pkl')

# Cancer department


def cancer(request):
    return render(request, 'ai/cancer.html')


def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1, size)
    if(size == 5):
        # loaded_model = joblib.load(
        #     "E:\\smart_health\\apps\\ai\\model.pkl")
        result = forest.predict(to_predict)
    return result[0]


def predict(request):
    if request.method == "POST":
        to_predict_list = [request.POST.get('concave_points_mean'), request.POST.get(
            'area_mean'), request.POST.get('radius_mean'), request.POST.get('perimeter_mean'), request.POST.get('concavity_mean')]
        # to_predict_list = list(to_predict_list.values())
        print(to_predict_list)
        to_predict_list = list(map(float, to_predict_list))
        print(to_predict_list)
        # cancer
        if(len(to_predict_list) == 5):
            result = ValuePredictor(to_predict_list, 5)

    if(int(result) == 1):
        prediction = "Sorry you have chances of getting the disease. Please consult the doctor immediately"
        news = 'bad'
    else:
        prediction = "No need to fear. You have no dangerous symptoms of the disease"
        news = 'good'
    return render(request, "ai/result.html", {'prediction_text': prediction, 'news': news})

# Heart Department


def heart(request):
    return render(request, 'ai/heart.html')


def HeartValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1, size)
    if(size == 7):
        # loaded_model = joblib.load(
        #     "E:\\smart_health\\apps\\ai\\model.pkl")
        result = heart_model.predict(to_predict)
    return result[0]


def heartPredict(request):
    if request.method == "POST":
        to_predict_list = [request.POST.get('cp'), request.POST.get(
            'trestbps'), request.POST.get('chol'), request.POST.get('fbs'), request.POST.get('restecg'), request.POST.get('thalach'), request.POST.get('exang')]
        # to_predict_list = list(to_predict_list.values())
        print(to_predict_list)
        to_predict_list = list(map(float, to_predict_list))
        print(to_predict_list)
        # cancer
        if(len(to_predict_list) == 7):
            result = HeartValuePredictor(to_predict_list, 7)

    if(int(result) == 1):
        prediction = "Sorry you have chances of getting the disease. Please consult the doctor immediately"
        news = 'bad'
    else:
        prediction = "No need to fear. You have no dangerous symptoms of the disease"
        news = 'good'
    return render(request, "ai/heart-result.html", {'prediction_text': prediction, 'news': news})

# Diabetes Department


def diabetes(request):
    return render(request, 'ai/diabetes.html')


def DiabetesValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1, size)
    if(size == 6):
        # loaded_model = joblib.load(
        #     "E:\\smart_health\\apps\\ai\\model.pkl")
        result = diabetes_model.predict(to_predict)
    return result[0]


def diabetesPredict(request):
    if request.method == "POST":
        to_predict_list = [request.POST.get('Pregnancies'), request.POST.get(
            'Present_Price'), request.POST.get('BloodPressure'), request.POST.get('BMI'), request.POST.get('DiabetesPedigreeFunction'), request.POST.get('Age')]
        # to_predict_list = list(to_predict_list.values())
        print(to_predict_list)
        to_predict_list = list(map(float, to_predict_list))
        print(to_predict_list)
        # cancer
        if(len(to_predict_list) == 6):
            result = DiabetesValuePredictor(to_predict_list, 6)

    if(int(result) == 1):
        prediction = "Sorry you have chances of getting the disease. Please consult the doctor immediately"
        news = 'bad'
    else:
        prediction = "No need to fear. You have no dangerous symptoms of the disease"
        news = 'good'
    return render(request, "ai/diabetes-result.html", {'prediction_text': prediction, 'news': news})


# Kidney Department
def kidney(request):
    return render(request, 'ai/kidney.html')


def KidneyValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1, size)
    if(size == 7):
        # loaded_model = joblib.load(
        #     "E:\\smart_health\\apps\\ai\\model.pkl")
        result = kidney_model.predict(to_predict)
    return result[0]


def kidneyPredict(request):
    if request.method == "POST":
        to_predict_list = [request.POST.get('Year'), request.POST.get(
            'sg'), request.POST.get('al'), request.POST.get('su'), request.POST.get('rbc'), request.POST.get('pc'), request.POST.get('pcc')]
        # to_predict_list = list(to_predict_list.values())
        print(to_predict_list)
        to_predict_list = list(map(float, to_predict_list))
        print(to_predict_list)
        # cancer
        if(len(to_predict_list) == 7):
            result = KidneyValuePredictor(to_predict_list, 7)

    if(int(result) == 1):
        prediction = "Sorry you have chances of getting the disease. Please consult the doctor immediately"
        news = 'bad'
    else:
        prediction = "No need to fear. You have no dangerous symptoms of the disease"
        news = 'good'
    return render(request, "ai/kidney-result.html", {'prediction_text': prediction, 'news': news})

# Liver Department


def liver(request):
    return render(request, 'ai/liver.html')


def LiverValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1, size)
    if(size == 7):
        # loaded_model = joblib.load(
        #     "E:\\smart_health\\apps\\ai\\model.pkl")
        result = liver_model.predict(to_predict)
    return result[0]


def liverPredict(request):
    if request.method == "POST":
        to_predict_list = [request.POST.get('Total_Bilirubin'), request.POST.get(
            'Direct_Bilirubin'), request.POST.get('Alkaline_Phosphotase'), request.POST.get('Alamine_Aminotransferase'), request.POST.get('Total_Protiens'), request.POST.get('Albumin'), request.POST.get('Albumin_and_Globulin_Ratio')]
        # to_predict_list = list(to_predict_list.values())
        print(to_predict_list)
        to_predict_list = list(map(float, to_predict_list))
        print(to_predict_list)
        # cancer
        if(len(to_predict_list) == 7):
            result = LiverValuePredictor(to_predict_list, 7)

    if(int(result) == 1):
        prediction = "Sorry you have chances of getting the disease. Please consult the doctor immediately"
        news = 'bad'
    else:
        prediction = "No need to fear. You have no dangerous symptoms of the disease"
        news = 'good'
    return render(request, "ai/liver-result.html", {'prediction_text': prediction, 'news': news})
