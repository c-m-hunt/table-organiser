import csv
from typing import List

from .setup import Table, Group
from .utils import remaining_seats, required_seats, filled_seats, can_add


def print_table_requirements_report(tables: List[Table]):
    capacity_count = {}
    for table in tables:
        capacity_count[table.capacity] = capacity_count.get(table.capacity, 0) + 1
    print("Table requirements:")
    for capacity in sorted(capacity_count.keys()):
        print(f"{capacity} seats: {capacity_count[capacity]}")
    print("----------------------------")


def print_start_report(groups: List[Group], tables: List[Table]):
    seats = remaining_seats(tables)
    req_seats = required_seats(groups)
    print(f"Remaining seats: {seats}")
    print(f"Required seats: {req_seats}")
    print("----------------------------")


def print_end_report(tables: List[Table]):
    seats = remaining_seats(tables)
    print("Remaining seats:", seats)
    print("Filled seats:", filled_seats(tables))
    print("----------------------------")


def write_output_report(tables: List[Table]):
    rows = []

    for i, table in enumerate(tables):
        rows.append([f"Table {i}", f"{table.filled_seats()} / {table.capacity}"])
        rows.extend([group.name, "", group.count, group.veg] for group in table.groups)
        rows.append(["", "", "", ""])
    with open("./data/output.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
