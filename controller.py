import calculator as calc
import user_interface
import logger as log
import parser_exp as pars

def run():
    value_type = user_interface.input_value_type()
    mode_work = user_interface.input_mode()
    log.log_type(value_type)
    log.log_mode(mode_work)
    exp_string=''
    if mode_work=='2':
        exp_string=user_interface.input_digits()
    if mode_work=='1':
        exp_string=user_interface.expression()
    expression=pars.exp_to_list(exp_string)
    log.log_exp(exp_string)
    result=calc.calculate(expression,value_type)
    log.log_result(result)
    user_interface.print_result(exp_string,result[0])