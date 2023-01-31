import importlib
from colorama import init as colorama_init
from colorama import Fore, Style

def import_dev_config():  # this way, 'version' can only be used to import dev_config
    from __main__ import version
    print(f"neutral: version = {{{version}}}")
    return importlib.import_module(f"data.{version}_data.dev_config")


my_module = import_dev_config()
text_color = my_module.text_color

# print(f"my_module.text_color = {my_module.text_color}")
def get_text():
    with open("data/text_to_print", "r") as file:
        to_return = "".join([f"\t{line}" for line in file.readlines()])
    match my_module.text_color:
        case "red":
            return f"{Fore.RED}{to_return}{Style.RESET_ALL}"
        case "blue":
            return f"{Fore.BLUE}{to_return}{Style.RESET_ALL}"
        case "green":
            return f"{Fore.GREEN}{to_return}{Style.RESET_ALL}"
        case _:
            return f"{Fore.YELLOW}{to_return}{Style.RESET_ALL}"
