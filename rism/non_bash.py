import re


def format_nbl(non_bash_languages):
    if len(non_bash_languages) == 1:
        nbl_str = non_bash_languages[0].title()

    if len(non_bash_languages) == 2:
        first_lang = non_bash_languages[0]
        sec_lang = non_bash_languages[1]

        nbl_str = f"{first_lang} and {sec_lang}"

    else:
        nbl_str = ""

        for nbl in non_bash_languages[:-1]:
            nbl_str += f"{nbl}, "

        last_lang = non_bash_languages[-1]
        nbl_str += f"and {last_lang}"

    return nbl_str


def detect_non_bash_code(chatgpt_output):
    # Pattern to match code blocks
    pattern = r"```(\w+)\n(.*?)```"

    matches = re.findall(pattern, chatgpt_output, re.DOTALL)

    non_bash_languages = []

    for nb_match in matches:
        language = nb_match[0]

        # Check if the language is not bash
        if language.lower() != "bash":
            non_bash_languages.append(language)

    return non_bash_languages
