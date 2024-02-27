from flask import Flask, render_template, request, send_file
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    text = request.form['text']
    width = request.form.get('width', default=800, type=int)
    height = request.form.get('height', default=400, type=int)

    # Preprocess the text
    words = word_tokenize(text)
    filtered_words = [word for word in words if word.lower() not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]

    processed_text = ' '.join(lemmatized_words)

    # Generate the word cloud
    wordcloud = WordCloud(width=width, height=height, background_color='white').generate(processed_text)

    img = io.BytesIO()
    plt.figure(figsize=(width / 100, height / 100))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig(img, format='PNG', bbox_inches='tight', pad_inches=0)
    img.seek(0)
    plt.close()
    
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

