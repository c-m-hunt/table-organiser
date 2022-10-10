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

tables = get_tables()
groups = get_groups()


def solve():
    for i in range(len(groups)):
        added = False
        group = groups[i]
        if group.count == 0:
            continue

        for table in tables:
            if can_add(table, group):
                table.groups.append(group)
                added = True
                break
        if not added:
            print(f"Unable to add group {group.name}")
    return tables


def main():
    print_table_requirements_report(tables)
    print_start_report(groups, tables)

    solve()

    tables.sort(key=lambda table: table.id)
    write_output_report(tables)

    print_end_report(tables)


if __name__ == "__main__":
    main()
