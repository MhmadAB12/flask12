from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
   def indexx():
    if request.method == 'POST':
        return redirect(url_for('download'))
    return render_template('index.html')
    if request.method == 'POST':
        video_url = request.form['video_url']
        try:
            yt = YouTube(video_url)
            video = yt.streams.get_highest_resolution()

            video_title = yt.title
            video_filename = f"{video_title}.mp4"
            video_path = os.path.join(app.config['DOWNLOAD_FOLDER'], video_filename)

            video.download(output_path=app.config['DOWNLOAD_FOLDER'])

            return send_from_directory(app.config['DOWNLOAD_FOLDER'], video_filename, as_attachment=True)
        except Exception as e:
            return render_template('index.html', error=str(e))

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
