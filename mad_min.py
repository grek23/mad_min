import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

WIDTH, HEIGHT = letter
HEIGHT_OFFSET = 36  # 36 = 0.5inches in the pdf canvas units
WIDTH_OFFSET = 36
CHAR_SIZE = 12/72  # for size 12 font, a char should take up this many inches in height


def generate_worksheet(num_problems):
    column_width = 15
    problems_per_group = 3
    problem_list = []

    for i in range(num_problems // problems_per_group):

        for j in range(problems_per_group):
            operand1 = random.randint(1, 99)
            #operand2 = 7 #random.randint(0, 9)
            operand2 = random.randint(1,20)
            result = operand1 * operand2

            problem = f"{operand1} x {operand2} = _____"
            problem_list.append([problem, result])
            # print(f"{problem:{column_width}}", end="")

        #print()
    return problem_list

def gen_answer_matrix(p_list):
    a_str = ""
    j = 1
    for p in p_list:
        a_str += f"{j}) {p[1]}, "
        j += 1
    a_str = a_str[0:len(a_str)-2]

    
    k = 173
    M = []
    print(f"Length of a_str = {len(a_str)}")
    while len(a_str) > k:
        print(f"Length of a_str = {len(a_str)}")
        M.append(a_str[0:k])
        a_str = a_str[k:]
        
        #k += 173
    M.append(a_str)
    
    
    return M


def main():
    print("Mad Minute")
    num_problems = 3*18  # Number of problems in the worksheet
    p_list = generate_worksheet(num_problems)

    c = canvas.Canvas("mad_min_wksht_7_04.pdf", pagesize=letter)
    column_width = 180
    # problems_per_group = 3

    #print(f"width = {WIDTH}, and height = {HEIGHT}, and height offset = {HEIGHT_OFFSET}")

    # c.drawString(WIDTH - 100, HEIGHT - 100, "Hello Grek")
    #print(f"p_list {p_list}")

    # print header to pdf
    header_str = "Name_________________        Mad Minute"
    c.drawString(WIDTH_OFFSET, HEIGHT - HEIGHT_OFFSET, header_str)

    i = 0
    cnt = 0
    answers = ""
    while (i < len(p_list)//3) and (cnt < len(p_list)):
        j = 0
        while j < 3:
            out_str = f"{cnt+1})  " + p_list[cnt][0]
            answers += f" {cnt+1}) " + str(p_list[cnt][1]) + ","
            c.drawString(WIDTH_OFFSET + j*column_width, HEIGHT -
                         (2*HEIGHT_OFFSET) - (i*36), out_str)  # p_list[cnt][0])
            cnt += 1
            j += 1
            #print(f"i = {i}, j = {j}, cnt = {cnt}, len p_list = {len(p_list)}")
        i += 1

    #answer string
    

    A = gen_answer_matrix(p_list)
    c.setFont("Helvetica", 6)
    j = 0
    for a in A:
        c.drawString(WIDTH_OFFSET, HEIGHT - (2*HEIGHT_OFFSET)- (648) - (j*10), a)
        print(f"i = {i} and i *36 = {i*36}")
        i+=1
        j+=1
    print(f"A= \n{A}")

    
    #c.drawString(WIDTH_OFFSET, HEIGHT - (2*HEIGHT_OFFSET)-(i*36), a_str)

    #print(f"a_string = {a_str}")

    c.showPage()
    c.save()
    #print(f"answers = {answers[0:len(answers)-1]}")


if __name__ == '__main__':
    main()
