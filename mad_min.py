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
            operand2 = random.randint(1,10)
            result = operand1 * operand2

            problem = f"{operand1} x {operand2} = _____"
            problem_list.append([problem, result])

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
    while len(a_str) > k:
        M.append(a_str[0:k])
        a_str = a_str[k:]

    M.append(a_str)
    
    
    return M

def generate_pdf():
    num_problems = 3*18
    p_list = generate_worksheet(num_problems)
    c = canvas.Canvas("mad_min_wksht_test01.pdf", pagesize=letter)
    column_width = 180
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
        i += 1

    A = gen_answer_matrix(p_list)
    c.setFont("Helvetica", 6)
    j = 0
    for a in A:
        c.drawString(WIDTH_OFFSET, HEIGHT - (2*HEIGHT_OFFSET)- (648) - (j*10), a)
        i+=1
        j+=1 

    c.showPage()
    c.save()


if __name__ == '__main__':
    generate_pdf()
