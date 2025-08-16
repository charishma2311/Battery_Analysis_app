from flask import Flask, request, render_template, send_file
import pandas as pd
import matplotlib.pyplot as plt
import os

from battery_analysis import analyze_battery_csv  # ← Import your analyzer

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if file and file.filename.endswith('.csv'):
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        # Run smart analysis and get plot paths
        plot_paths = analyze_battery_csv(filepath, output_dir=UPLOAD_FOLDER)
        plot_urls = ["/plot/" + os.path.basename(p) for p in plot_paths]

        return render_template('dashboard.html', plot_urls=plot_urls)

    return render_template('dashboard.html', message="Invalid file format.")

@app.route('/plot/<filename>')
def plot(filename):
    return send_file(os.path.join(UPLOAD_FOLDER, filename), mimetype='image/png')

@app.route('/logout', methods=['POST'])
def logout():
    return render_template('login.html')  # Or redirect to login page

if __name__ == '__main__':
    app.run(debug=True)
