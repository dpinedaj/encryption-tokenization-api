from typing import Any, Union, List

def validate_value(value: Any) -> Union[List[str], str]:
    if value is None:
        return None
    return [str(val) for val in value]\
        if type(value) in (list, tuple)\
        else str(value)

def parse_list_str(value: Any) -> List[str]:
    if type(value) not in (list, tuple):
        value = [value]
    value = list(set(value))
    return [str(val) for val in value if val is not None]