from typing import List
from table_planner import (
    print_end_report,
    print_start_report,
    write_output_report,
    get_tables,
    get_groups,
    Table,
    Group,
    can_add,
)
from table_planner.report import print_table_requirements_report


class TableSolver:
    def __init__(self, tables: List[Table], groups: List[Group]):
        self.tables = tables
        self.groups = groups
        self.current_group_idx = 0
        print_table_requirements_report(tables)
        print_start_report(groups, tables)
        self.depth = 0

    def solve_tables(self):
        self.solve()

    def solve(self) -> bool:
        next_unallocated_group_idx = self.get_next_unallocated_group_idx()
        if next_unallocated_group_idx is None:
            return True
        group = self.groups[next_unallocated_group_idx]
        for table in self.tables:
            if can_add(table, group):
                table.groups.append(group)
                group.allocated = True
                if self.solve():
                    return True
                del table.groups[len(table.groups) - 1]
                group.allocated = False
        return False

    def get_next_unallocated_group_idx(self) -> int:
        return next(
            (i for i, group in enumerate(self.groups) if group.allocated is False), None
        )

    def print_results(self):
        self.tables.sort(key=lambda table: table.id)
        print_end_report(self.tables)
        write_output_report(self.tables)


def main():
    tables = get_tables()
    groups = get_groups()
    solver = TableSolver(tables, groups)
    if solver.solve():
        solver.print_results()
    else:
        print("Cannot solve tables")


if __name__ == "__main__":
    main()
