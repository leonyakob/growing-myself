from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from typing import TYPE_CHECKING, TypeAlias

Json: TypeAlias = None | bool | int | float | str | Sequence["Json"] | Mapping[str, "Json"]
JsonMap: TypeAlias = dict[str, Json]
Values: TypeAlias = Mapping[str, str | bool]

if TYPE_CHECKING:
    invalidate_snapshot: Callable[[Values, str, str], tuple[int, JsonMap]]
    parse_values: Callable[[Sequence[str]], tuple[str, dict[str, str | bool] | str]]
    review_receipt_append: Callable[[Values], tuple[int, JsonMap]]
    review_receipt_check: Callable[[Values], tuple[int, JsonMap]]
    review_runtime_final_check: Callable[[Values], tuple[int, JsonMap]]
    review_runtime_register: Callable[[Values], tuple[int, JsonMap]]
    review_runtime_snapshot: Callable[[Values], tuple[int, JsonMap]]
    wave_snapshot_check: Callable[[Values], tuple[int, JsonMap]]
    wave_snapshot_create: Callable[[Values], tuple[int, JsonMap]]
else:
    snapshot_module = __import__("ren_sheng_whole_book_wave_snapshot", fromlist=["invalidate_snapshot", "parse_values", "wave_snapshot_check", "wave_snapshot_create"])
    runtime_module = __import__("ren_sheng_whole_book_wave_runtime", fromlist=["review_receipt_append", "review_receipt_check", "review_runtime_final_check", "review_runtime_register", "review_runtime_snapshot"])
    invalidate_snapshot = snapshot_module.invalidate_snapshot
    parse_values = snapshot_module.parse_values
    wave_snapshot_check = snapshot_module.wave_snapshot_check
    wave_snapshot_create = snapshot_module.wave_snapshot_create
    review_receipt_append = runtime_module.review_receipt_append
    review_receipt_check = runtime_module.review_receipt_check
    review_runtime_final_check = runtime_module.review_runtime_final_check
    review_runtime_register = runtime_module.review_runtime_register
    review_runtime_snapshot = runtime_module.review_runtime_snapshot


def wave_command(argv: Sequence[str]) -> tuple[int, JsonMap]:
    command, parsed = parse_values(argv)
    if isinstance(parsed, str):
        return 2, {"command": "invalid", "status": "FAIL", "failures": [parsed], "counts": {}, "output_path": None}
    handlers: Mapping[str, Callable[[Values], tuple[int, JsonMap]]] = {
        "wave-snapshot-create": wave_snapshot_create,
        "wave-snapshot-check": wave_snapshot_check,
        "wave-drift-invalidate": lambda values: invalidate_snapshot(values, "wave-drift-invalidate", "INPUT_DRIFT"),
        "review-runtime-snapshot": review_runtime_snapshot,
        "review-runtime-register": review_runtime_register,
        "review-runtime-final-check": review_runtime_final_check,
        "wave-runtime-invalidate": lambda values: invalidate_snapshot(values, "wave-runtime-invalidate", "RUNTIME_PATH_DRIFT"),
        "review-receipt-append": review_receipt_append,
        "review-receipt-check": review_receipt_check,
        "wave-invalidate": lambda values: invalidate_snapshot(values, "wave-invalidate", str(values.get("reason", "BLOCKED"))),
    }
    handler = handlers.get(command)
    if handler is None:
        return 2, {"command": "invalid", "status": "FAIL", "failures": [f"unknown wave command: {command}"], "counts": {}, "output_path": None}
    return handler(parsed)
