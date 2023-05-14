from fpdf import FPDF

def generate_report(pat_data):
    pat_data1 = pat_data[0]
    pat_data2 = pat_data[1]
    Day1 = str('['+str(pat_data1[0])+','+str(pat_data2[0])+']')
    Day2 = str('['+str(pat_data1[1])+','+str(pat_data2[1])+']')
    Day3 = str('['+str(pat_data1[2])+','+str(pat_data2[2])+']')
    Day4 = str('['+str(pat_data1[3])+','+str(pat_data2[3])+']')
    Day5 = str('['+str(pat_data1[4])+','+str(pat_data2[4])+']')
    Day6 = str('['+str(pat_data1[5])+','+str(pat_data2[5])+']')
    Day7 = str('['+str(pat_data1[6])+','+str(pat_data2[6])+']')
    Day8 = str('['+str(pat_data1[7])+','+str(pat_data2[7])+']')
    Day9 = str('['+str(pat_data1[8])+','+str(pat_data2[8])+']')
    Day10 = str('['+str(pat_data1[9])+','+str(pat_data2[9])+']')
    Day11 = str('['+str(pat_data1[10])+','+str(pat_data2[10])+']')
    advice = 'Waiting for update'
    Dob = str(str('Name: ')+str(pat_data[2]) + str(' Age: ') + str(pat_data[3]))
    init_count = 'Waiting for update'
    date_first = 'Waiting for update'
    latest_count = 'Waiting for update'
    date_latest = 'Waiting for update'
    confidence = str(str('Confidence: ')+str(pat_data[5]) + str('%'))
    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size = 22)

    pdf.cell(200, 10, txt = "DenV Advisor Report", ln = 1, align = 'C')

    pdf.image("img/power.png", x = 100, y = 18,w = 20)

    pdf.set_font("Courier", size = 12)
    pdf.cell(200, 10, txt = "Date and Time: ", ln = 3, align = 'L')
    pdf.cell(200, 10, txt = Dob, ln = 4, align = 'L')
    pdf.cell(200, 10, txt = init_count, ln = 5, align = 'L')
    pdf.cell(200, 10, txt = date_first, ln = 6, align = 'L')
    pdf.cell(200, 10, txt = latest_count, ln = 7, align = 'L')
    pdf.cell(200, 10, txt = date_latest, ln = 8, align = 'L')
    pdf.cell(200, 10, txt = "Medical complications: ", ln = 9, align = 'L')
    pdf.cell(200, 10, txt = "Predicted values: [ Day, lower limit, upper limit]: ", ln = 11, align = 'L')
    pdf.cell(200, 10, txt = Day1, ln = 13, align = 'L')
    pdf.cell(200, 10, txt = Day2, ln = 14, align = 'L')
    pdf.cell(200, 10, txt = Day3, ln = 15, align = 'L')
    pdf.cell(200, 10, txt = Day4, ln = 16, align = 'L')
    pdf.cell(200, 10, txt = Day5, ln = 17, align = 'L')
    pdf.cell(200, 10, txt = Day6, ln = 18, align = 'L')
    pdf.cell(200, 10, txt = Day7, ln = 19, align = 'L')
    pdf.cell(200, 10, txt = Day8, ln = 20, align = 'L')
    pdf.cell(200, 10, txt = Day9, ln = 21, align = 'L')
    pdf.cell(200, 10, txt = Day10, ln = 22, align = 'L')
    pdf.cell(200, 10, txt = Day11, ln = 23, align = 'L')
    pdf.cell(200, 10, txt = "Advisory: ", ln = 25, align = 'L')
    pdf.cell(200, 10, txt = advice, ln = 26, align = 'L')
    pdf.cell(200, 10, txt = confidence, ln = 27, align = 'L')
    pdf.cell(200, 10, txt = "Disclaimer", ln = 28, align = 'C')
    f = open("disclmr.atom", "r")
    for x in f:
        pdf.cell(200, 10, txt = x, ln = 29, align = 'J')
    pdf.output("report.pdf") 

#pat_data = [Day1,Day2,Day2,Day2,Day2,Day2,Day2,Day2,Day2,Day2,Day2,Day2,Day2,Day2,Day2,Day2,Day2,Day2,Day2,Day2,]