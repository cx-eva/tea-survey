from flask import Flask, render_template, request
from utils.helpers import get_current_time
from recommender.tea_recommender import TeaRecommender

app = Flask(__name__)
tea_recommender = TeaRecommender()

@app.route('/')
def index():
    current_time = get_current_time()
    return render_template('index.html', current_time=current_time)

@app.route('/questionnaire', methods=['GET', 'POST'])
def questionnaire():
    if request.method == 'POST':
        # 收集表单数据
        form_data = {
            'age': request.form.get('age'),
            'gender': request.form.get('gender'),
            'symptoms': request.form.getlist('symptoms'),
            'taste_preference': request.form.get('taste_preference'),
            'goals': request.form.get('goals')
        }
        
        # 获取推荐结果
        recommendations = tea_recommender.get_recommendations(form_data)
        return render_template('result.html', recommendations=recommendations, tea_recommender=tea_recommender)
    
    return render_template('questionnaire.html')

@app.route('/about')
def about():
    return render_template('about.html')

def tea_customization():
    return render_template('tea_customization.html')

if __name__ == '__main__':
    app.run(debug=True)