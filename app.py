from flask import Flask, render_template, request, send_file
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    text = request.form['text']
    width = request.form.get('width', 800, type=int)
    height = request.form.get('height', 400, type=int)
    
    # Generate the word cloud
    wordcloud = WordCloud(width=width, height=height, background_color='white').generate(text)

    # Create a byte stream buffer
    img = io.BytesIO()
    plt.figure(figsize=(width / 100, height / 100))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    
    # Save the word cloud to the byte stream
    plt.savefig(img, format='PNG', bbox_inches='tight', pad_inches=0)
    img.seek(0)
    plt.close()
    
    return send_file(img, mimetype='image/png', as_attachment=False)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

