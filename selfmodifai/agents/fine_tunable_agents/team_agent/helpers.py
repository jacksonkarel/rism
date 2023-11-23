import re


def code_from_gpt(content):
    pattern = r"```(\w+)\n(.*?)```"

    code_files = re.findall(pattern, content, re.DOTALL)

    return code_files
