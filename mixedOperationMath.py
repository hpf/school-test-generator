import random
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import datetime

# 生成混合运算口算题:乘除加减混合运行，乘除在九九表内
def generate_question(tag=False):
  
    # 随机选择口算题模板
    templates=['a x b + c', 'a x b - c','a ÷ b + c','a ÷ b - c','c-a x b','c-a ÷ b']
    
    if tag:
        templates.append('a x (b + c)')
        templates.append('a x (b - c)')
        templates.append('a ÷ (b - c)')
        templates.append('a ÷ (b + c)')

    template = random.choice(templates)
    # 根据模板生成口算题

    if template == 'a x b + c':
        a=random.randint(1, 9)
        b=random.randint(1, 9)
        c=random.randint(1,100-a*b)
        result = a * b + c
        question = f'{a} x {b} + {c}'
        
    elif template == 'a x b - c':
        a=random.randint(1, 9)
        b=random.randint(1, 9)
        c=random.randint(1,a*b)
        result = a * b + c
        question = f'{a} x {b} - {c}'

    elif template == 'a x (b - c)':
        a=random.randint(1, 9)
        b=random.randint(1, 100)
        c=random.randint(1, 99)
        while b - c > 9 and b-c<=0:
            b=random.randint(1, 100)
            c=random.randint(1, 99)
        result = a * (b - c)
        question = f'{a} x ({b} - {c})'
        
    elif template == 'a x (b + c)':
        a=random.randint(1, 9)
        b=random.randint(1, 9)
        c=random.randint(1, 9)
        while b + c > 9:
            b=random.randint(1, 9)
            c=random.randint(1, 9)
        result = a * (b + c)
        question = f'{a} x ({b} + {c})'
        
    elif template == 'a ÷ b + c':
        b=random.randint(1, 9)
        a=random.randint(1,9) * b
        c=random.randint(1,100-a//b)
        result = a / b + c
        question = f'{a} ÷ {b} + {c}'

    elif template == 'a ÷ b - c':
        b=random.randint(1, 9)
        a=random.randint(1,9) * b
        c=random.randint(1,a//b)
        result = a / b + c
        question = f'{a} ÷ {b} - {c}'

    elif template == 'a ÷ (b + c)':
        b=random.randint(1, 9)
        c=random.randint(1, 9)
        while b+c>9:
            b=random.randint(1, 9)
            c=random.randint(1, 9)
        a=random.randint(1, 9) * (b+c)
        result = a / b + c
        question = f'{a} ÷ ({b} + {c})'

    elif template == 'a ÷ (b - c)':
        b=random.randint(1, 100)
        c=random.randint(1, 100)
        while b-c>9 or b-c<1:
            b=random.randint(1, 100)
            c=random.randint(1, 100)
        a=random.randint(1, 9) * (b-c)

        result = a / b + c
        question = f'{a} ÷ ({b} - {c})'    
    
    elif template == 'c-a x b':
        a=random.randint(1, 9)
        b=random.randint(1, 9)
        c=random.randint(a*b, 100)
        result = c-a*b
        question = f'{c} - {a} x {b}'

    elif template == 'c-a ÷ b':
        b=random.randint(1, 9)
        a=random.randint(1,9) * b
        c=random.randint(a//b, 100)
        result = a - b / c
        question = f'{c} - {a} ÷ {b}'


    return question + ' = ', result

#输出中间线
def draw_horizontal_line(c):
    # 获取页面宽度和高度
    page_width, page_height = A4

    # 计算横杠的位置和宽度
    line_y = page_height / 2
    line_width = page_width - 100
    line_x = (page_width - line_width) / 2
    # 画一条横杠
    c.line(line_x, line_y, line_x + line_width, line_y)

#保存为pdf
def output_list_to_pdf(my_list):
    # 格式化日期字符串
    date_str = datetime.datetime.now().strftime("%Y%m%d")

    # 创建PDF文件
    c = canvas.Canvas("maths_{}.pdf".format(date_str))

    # 设置字体和字号
    c.setFont("Helvetica", 14)

    # 定义每列的宽度和间距
    col_width = 150
    col_spacing = 50

    # 定义起始坐标
    x = 50
    y = 50
    #draw_horizontal_line(c)
    row=0
    # 逐个输出列表元素
    for i, item in enumerate(my_list):
        # 每页最多输出30个元素
        if i % 90 == 0 and i != 0:
            # 画一条横杠
            #draw_horizontal_line(c)
            c.showPage()
            x = 50
            y = 50

        # 计算元素在哪一列
        col_num = i % 3
        
        # 输出元素
        c.drawString(x + col_num * (col_width + col_spacing), y, str(item))

        # 更新坐标
        if col_num == 2:
            #行数+1
            row+=1
            y += 25
            if row==16:
                row=0
                y+=3    

    #draw_horizontal_line(c)
    # 保存并关闭PDF文件
    c.save()

if __name__ == '__main__':
    quarz=[]
    #输入要多少题
    n = int(input("请输入要生成的题目数量："))
    for i in range(n):
        question, result = generate_question()
        if(result>1 or result<101):
            quarz.append(question)
    
    output_list_to_pdf(quarz)
