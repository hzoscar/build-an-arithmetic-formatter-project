def arithmetic_arranger(problems, show_answers=False):

    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "99 + 1"])}')

def do_operation(first_value,operator,second_value):
    if operator == "+":
        return str(int(first_value) + int(second_value))
    else:
        return str(int(first_value) - int(second_value))

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49","99 + 1"]

def arithmetic_arranger(problems, show_answers=False):
    output_first_line_list = []
    output_second_line_list = []
    dash_line = []
    output_answer_list = []
    separator="    "

    for problem in problems:
        problem = problem.split()
        first_line= problem[0]
        operator = problem[1]
        second_line= problem[2]               
        len_answer_line = max(len(first_line), len(second_line))+2
        answer_line = "_" * len_answer_line
        dash_line.append(answer_line)
        
        if len(first_line)>len(second_line):
            second_line = " " * (len(first_line) - len(second_line)) + second_line 
            output_first_line_list.append("  " + first_line)
            output_second_line_list.append(operator +' '+ second_line) 
            output_answer_list.append("  " + " " * (len(first_line) - len(second_line))+do_operation(first_line, operator, second_line))        
            
        elif len(first_line)==len(second_line):
            output_first_line_list.append("  " +first_line)
            output_second_line_list.append(operator +' '+ second_line)
            output_answer_list.append("  " + do_operation(first_line, operator, second_line))
        else:
            first_line = " " * (len(second_line) - len(first_line)) + first_line
            output_first_line_list.append("  " +first_line)
            output_second_line_list.append(operator+' '+ second_line) 
            output_answer_list.append( "  " +" " * (len(second_line) - len(first_line))+ do_operation(first_line, operator, second_line))


    final_output = [separator.join(output_first_line_list), separator.join(output_second_line_list), separator.join(dash_line)]
    if show_answers:
        final_output.append(separator.join(output_answer_list))

    for i in final_output:
        print(i, end= '\n')

arithmetic_arranger(problems, show_answers= True)
#arithmetic_arranger(problems)