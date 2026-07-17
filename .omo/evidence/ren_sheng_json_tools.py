from __future__ import annotations

import re
from typing import Final, TypeAlias

Json: TypeAlias = None | bool | int | float | str | list["Json"] | dict[str, "Json"]
JsonMap: TypeAlias = dict[str, Json]
NUMBER_RE: Final = re.compile(r"-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?")


def skip_ws(text: str, index: int) -> int:
    while index < len(text) and text[index] in " \t\r\n":
        index += 1
    return index


def parse_string(text: str, index: int, label: str) -> tuple[str, int]:
    if index >= len(text) or text[index] != '"':
        raise AssertionError(f"{label} expected JSON string")
    chars: list[str] = []
    index += 1
    while index < len(text):
        char = text[index]
        if char == '"':
            return "".join(chars), index + 1
        if char == "\\":
            index += 1
            if index >= len(text):
                raise AssertionError(f"{label} ended in JSON escape")
            escaped = text[index]
            if escaped in {'"', "\\", "/"}:
                chars.append(escaped)
            elif escaped == "b":
                chars.append("\b")
            elif escaped == "f":
                chars.append("\f")
            elif escaped == "n":
                chars.append("\n")
            elif escaped == "r":
                chars.append("\r")
            elif escaped == "t":
                chars.append("\t")
            elif escaped == "u":
                code = text[index + 1:index + 5]
                if len(code) != 4 or any(mark not in "0123456789abcdefABCDEF" for mark in code):
                    raise AssertionError(f"{label} had invalid unicode escape")
                chars.append(chr(int(code, 16)))
                index += 4
            else:
                raise AssertionError(f"{label} had invalid JSON escape")
        else:
            chars.append(char)
        index += 1
    raise AssertionError(f"{label} had unterminated JSON string")


def parse_number(text: str, index: int, label: str) -> tuple[int | float, int]:
    match = NUMBER_RE.match(text, index)
    if match is None:
        raise AssertionError(f"{label} expected JSON number")
    token = match.group(0)
    return (float(token) if any(marker in token for marker in ".eE") else int(token)), match.end()


def parse_array(text: str, index: int, label: str) -> tuple[list[Json], int]:
    values: list[Json] = []
    index = skip_ws(text, index + 1)
    if index < len(text) and text[index] == "]":
        return values, index + 1
    while True:
        value, index = parse_value(text, index, label)
        values.append(value)
        index = skip_ws(text, index)
        if index < len(text) and text[index] == "]":
            return values, index + 1
        if index >= len(text) or text[index] != ",":
            raise AssertionError(f"{label} expected array comma or close")
        index = skip_ws(text, index + 1)


def parse_object(text: str, index: int, label: str) -> tuple[JsonMap, int]:
    values: JsonMap = {}
    index = skip_ws(text, index + 1)
    if index < len(text) and text[index] == "}":
        return values, index + 1
    while True:
        key, index = parse_string(text, index, label)
        index = skip_ws(text, index)
        if index >= len(text) or text[index] != ":":
            raise AssertionError(f"{label} expected object colon")
        value, index = parse_value(text, index + 1, label)
        values[key] = value
        index = skip_ws(text, index)
        if index < len(text) and text[index] == "}":
            return values, index + 1
        if index >= len(text) or text[index] != ",":
            raise AssertionError(f"{label} expected object comma or close")
        index = skip_ws(text, index + 1)


def parse_value(text: str, index: int, label: str) -> tuple[Json, int]:
    index = skip_ws(text, index)
    if index >= len(text):
        raise AssertionError(f"{label} ended before JSON value")
    char = text[index]
    if char == '"':
        return parse_string(text, index, label)
    if char == "[":
        return parse_array(text, index, label)
    if char == "{":
        return parse_object(text, index, label)
    if text.startswith("true", index):
        return True, index + 4
    if text.startswith("false", index):
        return False, index + 5
    if text.startswith("null", index):
        return None, index + 4
    return parse_number(text, index, label)


def decode_json_map(text: str, label: str) -> JsonMap:
    value, index = parse_value(text, 0, label)
    if skip_ws(text, index) != len(text) or not isinstance(value, dict):
        raise AssertionError(f"{label} was not a JSON object")
    return value
