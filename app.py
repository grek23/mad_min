from flask import Flask, send_file
import mad_min

app = Flask(__name__)

@app.route("/worksheet")
def worksheet():
    filename = mad_min.generate_pdf()
    return send_file(filename, as_attachment=True)

#if __name__ == "__main__":
#    #mad_min.generate_pdf()
#    app.run()