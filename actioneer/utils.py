from inspect import signature, Parameter
from typing import List, Any, Union, _GenericAlias


def identity(value):
    return value


true_strings = frozenset(["true", "t", "yes", "y", "ye", "yeh", "yeah", "sure",
                          "✅", "on", "1"])
false_strings = frozenset(["false", "f", "no", "n", "nope", "nah", "❌", "off",
                           "0"])


def bool_from_str(inp):
    inp = inp.lower()
    if inp in false_strings:
        return False
    elif inp in true_strings:
        return True
    else:
        raise Exception("TODO")  # TODO


def get_ctxs(func, ctx: List[Any] = []):
    out = {}
    name_annots = {name: v.annotation for name, v in
                   signature(func).parameters.items()
                   if v.kind == Parameter.KEYWORD_ONLY}
    for name, annotation in name_annots.items():
        if getattr(annotation, "__origin__", "") is Union:
            done = False
            for union_type in annotation.__args__:
                for ctx_type in ctx:
                    if isinstance(ctx_type, union_type):
                        out[name] = ctx_type
                        done = True
                        break
                if done:
                    break
            continue
        for ctx_type in ctx:
            if isinstance(ctx_type, annotation):
                out[name] = ctx_type
                break
    return out


class Flags(dict):
    """Flag class"""

class Options(dict):
    """Options class"""
