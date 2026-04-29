from flask import Flask, request, send_file, render_template
import tempfile
import os
import processor
import webbrowser
import threading

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")

    if not file:
        return "No file uploaded.", 400

    with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp:
        file.save(tmp.name)
        tmp_path = tmp.name

    try:
        output_path = processor.process(tmp_path)
    except ValueError as e:
        os.unlink(tmp_path)
        return f"Error: {e}", 400
    except Exception as e:
        os.unlink(tmp_path)
        return f"Unexpected error: {e}", 500

    os.unlink(tmp_path)

    return send_file(
        output_path,
        as_attachment=True,
        download_name=os.path.basename(output_path),
        mimetype="text/csv"
    )

def open_browser():
    webbrowser.open("http://localhost:5000")

if __name__ == "__main__":
    threading.Timer(1, open_browser).start()
    app.run(debug=False)