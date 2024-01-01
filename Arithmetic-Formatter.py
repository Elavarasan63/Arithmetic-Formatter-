def arithmetic_arranger(problems, show_answer=False):
  if len(problems) > 5:
    return "Error: Too many problems."

  arranged_problems = {
      "first_line": "",
      "second_line": "",
      "dash_line": "",
      "answer_line": ""
  }

  for problem in problems:
    operator1, operator, operator2 = problem.split()

    if operator not in ["+", "-"]:
      return "Error: Operator must be '+' or '-'."
    if not operator1.isdigit() or not operator2.isdigit():
      return "Error: Numbers must only contain digits."
    if len(operator1) > 4 or len(operator2) > 4:
      return "Error: Numbers cannot be more than four digits."

    width = max(len(operator1), len(operator2)) + 2
    arranged_problems["first_line"] += f"{operator1.rjust(width)}    "
    arranged_problems[
        "second_line"] += f"{operator} {operator2.rjust(width - 2)}    "
    arranged_problems["dash_line"] += "-" * width + "    "

    if show_answer:
      if operator == "+":
        answer = str(int(operator1) + int(operator2))
      else:
        answer = str(int(operator1) - int(operator2))
      arranged_problems["answer_line"] += f"{answer.rjust(width)}    "

  arranged_output = arranged_problems["first_line"].rstrip() + "\n"
  arranged_output += arranged_problems["second_line"].rstrip() + "\n"
  arranged_output += arranged_problems["dash_line"].rstrip()

  if show_answer:
    arranged_output += "\n" + arranged_problems["answer_line"].rstrip()

  return arranged_output

