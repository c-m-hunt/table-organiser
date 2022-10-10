from typing import List

from table_planner.setup import Group, Table


def remaining_seats(tables: List[Table]):
    return sum(table.remaining_seats() for table in tables)


def required_seats(groups: List[Group]):
    return sum(group.count for group in groups)


def filled_seats(tables: List[Table]):
    return sum(table.filled_seats() for table in tables)


def can_add(table: Table, group: Group) -> bool:
    return table.remaining_seats() >= group.count
