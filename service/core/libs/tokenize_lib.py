from service.core.models.tokenize import Tokenize
from service.core.handlers.db_session import session
from service.core.libs.commons import parse_list_str
from typing import Union, List, Tuple
from service.core.handlers.key_handler import KeyHandler
import hmac
import hashlib
import base64


def tokenize_value(value: str) -> str:
    dig = hmac.new(KeyHandler().encryption_key.encode(),
                   msg=value.encode(),
                   digestmod=hashlib.sha256).digest()
    return base64.b64encode(dig).decode()


def tokenize_values(values: Union[List[str], str], table_name: str) -> List[Tuple[str, str]]:
    table = Tokenize(table_name)
    values = parse_list_str(values)
    result = [()]
    if values:
        result = [table.lookup_value("value", value) for value in values]
        result = [res for res in result if res is not None and len(res)>0]
        if len(result) > 0:
            resolved_values = [res[0] for res in result]
        else:
            resolved_values = []
        unresolved_values = list(set(values) - set(resolved_values))
        new_values = [(val, tokenize_value(val)) for val in unresolved_values]
        for reg in new_values:
            new_value = table(value=reg[0], token=reg[1])
            session.add(new_value)
            result.append(reg)
        session.commit()
    return result


def detokenize_values(tokens: Union[List[str], str], table_name: str) -> List[Tuple[str, str]]:
    table = Tokenize(table_name)
    tokens = parse_list_str(tokens)
    result = [()]
    if tokens:
        result = [table.lookup_value("token", token) for token in tokens]
        assert len(result) > 0, "Not Valid Candidate for tokens"
    return result
