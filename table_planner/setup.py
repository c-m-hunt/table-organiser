from typing import List
from dataclasses import dataclass, field
import csv


@dataclass
class Group:
    name: str
    count: int
    veg: int


@dataclass
class Table:
    id: int
    capacity: int
    active: bool
    groups: list[Group] = field(default_factory=list)

    def remaining_seats(self):
        return self.capacity - self.filled_seats()

    def filled_seats(self):
        return sum(group.count for group in self.groups)


def get_tables() -> List[Table]:
    with open("./data/tables.csv", newline="") as csvfile:
        table_reader = csv.reader(csvfile, delimiter=",", quotechar='"')
        tables = [
            Table(int(row[0]), int(row[1]), bool(int(row[2]))) for row in table_reader
        ]
        return [t for t in tables if t.active]


def get_groups() -> List[Group]:
    with open("./data/groups.csv", newline="") as csvfile:
        group_reader = csv.reader(csvfile, delimiter=",", quotechar='"')
        groups = [
            Group(row[0], int(row[1]), int(row[2]) if row[2] != "" else 0)
            for row in group_reader
        ]
        groups.sort(key=lambda x: x.count, reverse=True)
        return [g for g in groups if g.count > 0]
