def do_operation(first_value,operator,second_value):
    if operator == "+":
        return str(int(first_value) + int(second_value))
    else:
        return str(int(first_value) - int(second_value))

def arithmetic_arranger(problems, show_answers=False):
    output_first_line_list = []
    output_second_line_list = []
    dash_line = []
    output_answer_list = []
    separator = "    "
    if len(problems) > 5:
        return "Error: Too many problems."
    
    for problem in problems:
        problem = problem.split()
        first_line= problem[0]
        operator = problem[1]
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        second_line= problem[2]  
        
        if len(first_line)>=5 or len(second_line)>=5:
            return "Error: Numbers cannot be more than four digits."
        
        if not first_line.isdigit() or not second_line.isdigit():
            return "Error: Numbers must only contain digits."
                     
        bigger_number = max(len(first_line), len(second_line))
        difference = abs(len(first_line) - len(second_line))        
        answer_line = "-" * (bigger_number + 2)
        dash_line.append(answer_line)
        get_answer = do_operation(first_line, operator, second_line)
        spaces = bigger_number + 2 - len(get_answer)
                
        if len(first_line)>len(second_line):
            second_line = " " * (difference) + second_line 
            output_first_line_list.append("  " + first_line)
            output_second_line_list.append(operator +' '+ second_line) 
            output_answer_list.append(" " * spaces + get_answer)        
            
        elif len(first_line)==len(second_line):
            output_first_line_list.append("  " +first_line)
            output_second_line_list.append(operator +' '+ second_line)
            output_answer_list.append(" " * spaces + get_answer)
        else:
            first_line = " " * (difference) + first_line
            output_first_line_list.append("  " + first_line)
            output_second_line_list.append(operator +' '+ second_line) 
            output_answer_list.append(" " * spaces + get_answer)

    final_output = [separator.join(output_first_line_list), separator.join(output_second_line_list), separator.join(dash_line)]
    if show_answers:
        final_output.append(separator.join(output_answer_list))

    for i in final_output:
        print(i, end= '\n')

    #return "\n".join(final_output)
    
