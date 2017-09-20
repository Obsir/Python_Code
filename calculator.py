# @Time    : 2017/9/20 下午3:01
# @Author  : Obser
import re


def search_bracket(string):
    """
    The Calculation of expression in bracket
    :param string:
    :return:
    """
    pattern = r'\([^()]+\)'
    res = re.search(pattern, string)
    if not res:
        multi_div_res = calc_operation(string, calc_multi_div_str)
        plus_minus_res = calc_operation(multi_div_res, calc_plus_minus_str)
        return plus_minus_res, True
    res = re.sub(r'([()])', '', res.group())
    multi_div_res = calc_operation(res, calc_multi_div_str)
    plus_minus_res = calc_operation(multi_div_res, calc_plus_minus_str)
    return re.sub(pattern, plus_minus_res, string, 1), False


def calc_multi_div_str(string):
    """
    The calculation of multiplication and division
    :param string:
    :return:
    """
    pattern = r'(\+|\-)?(\d+\.?\d*\*[+-]?\d+\.?\d*|\d+\.?\d*/[+-]?\d+\.?\d*)'
    res = re.search(pattern, string)
    if not res:
        return string, True
    calc_str = res.group(2)
    if '*' in calc_str:
        nums = calc_str.split('*')
        calc_res = float(nums[0]) * float(nums[1])
    else:
        nums = calc_str.split('/')
        calc_res = float(nums[0]) / float(nums[1])
    if res.group(1) == '-' and calc_res > 0 or res.group(1) == '+' and calc_res < 0:
        calc_res = '-' + str(abs(calc_res))
    elif res.group(1) == '+' and calc_res > 0 or res.group(1) == '-' and calc_res < 0:
        calc_res = '+' + str(abs(calc_res))
    return re.sub(pattern, str(calc_res), string, 1), False


def calc_plus_minus_str(string):
    """
    The calculation of addition and subtraction
    :param string:
    :return:
    """
    pattern = r'\d+\.?\d*(\+|\-)+\d+\.?\d*'
    res = re.search(pattern, string)
    if not res:
        return string, True
    calc_str = res.group()
    if '+-' in calc_str:
        calc_str = calc_str.replace('+-', '-')
    if '--' in calc_str:
        calc_str = calc_str.replace('--', '+')
    if '+' in calc_str:
        nums = calc_str.split('+')
        calc_res = float(nums[0]) + float(nums[1])
    else:
        nums = calc_str.split('-')
        calc_res = float(nums[0]) - float(nums[1])
    return re.sub(pattern, str(calc_res), string, 1), False


def calc_operation(res, fun):
    """
    Recursive function for operation 'fun'
    :param res:
    :param fun:
    :return:
    """
    res_tunple = fun(res)
    while not res_tunple[1]:
        res_tunple = fun(res_tunple[0])
    return res_tunple[0]


def calc(res):
    """
    Calculation
    :param res:
    :return:
    """
    return calc_operation(res, search_bracket)


while True:
    expr = input("Please input your expression:>>")
    if expr == 'b':
        break
    print("result:", calc(expr.strip().replace(' ', '')))
    print("eval:", eval(expr))


# 测试
# pattern = r'(\+|\-)?(\d+\.?\d*\*[+-]?\d+\.?\d*|\d+\.?\d*/[+-]?\d+\.?\d*)'
# res = re.search(pattern, '1-2*-1388338.2476190478')
# calc_str = res.group(2)
# if '*' in calc_str:
#     nums = calc_str.split('*')
#     calc_res = float(nums[0]) * float(nums[1])
# else:
#     nums = calc_str.split('/')
#     calc_res = float(nums[0]) / float(nums[1])
# if res.group(1) == '-' and calc_res > 0 or res.group(1) == '+' and calc_res < 0:
#     calc_res = str(abs(calc_res))
# elif res.group(1) == '+' and calc_res > 0 or res.group(1) == '-' and calc_res < 0:
#     calc_res = '+' + str(abs(calc_res))
# print(calc_res)
# def calc_div(string):
#     pattern = r'(\+|\-)?()'
#     return re.search(pattern, string).group()


# string2 = "99*111"
#
# res = string
# while res:
#     res_str = res
#     res = calc_multi_div(res)
#     print(res)
# print(res_str)
#
# res = res_str
# while res:
#     res_str = res
#     res = calc_plus_minus(res)
#     print(res)
# print(res_str)
