from flask import Flask, send_file, request
import mad_min

app = Flask(__name__)

@app.route("/worksheet")
def worksheet():

    #max_num = int(request.args.get("max", 12))
    #problems = int(request.args.get("problems", 50))
    
    #filename = mad_min.generate_pdf(max_num=max_num, problems=problems)
    random_str = request.args.get("r",12)
    fn = "random_worksheet.pdf"
    print(f"From App: def worksheet() random_str = {random_str}")

    filename = mad_min.generate_pdf(fn,"r",2)
    
    return send_file(filename, as_attachment=True)

@app.route("/worksheet_single_digit")
def worksheet_single_digit():
    #"?single_digit=" + single_digit;
    s_digit_str = request.args.get("single_digit",12)
    s_digit_int = int(request.args.get("single_digit", 12))
    #max_num = int(request.args.get("max", 12))
    #problems = int(request.args.get("problems", 50))
    fn = "single_digit_" + s_digit_str + ".pdf"
    print(f"generating pdf from worksheet_single_digit: int {s_digit_int}, str {s_digit_str} and fn {fn} ")
    
    filename = mad_min.generate_pdf(fn, "s", s_digit_int)
    
    return send_file(filename, as_attachment=True)


if __name__ == "__main__":
    print("For Render you need to exclude the app.run().")
    print("To run on your local machine, enable app.run() by un-commenting.")


#For uploading to Render you need to remove the app.run()
#For running locally you need to have app.run() enabled
    #app.run()