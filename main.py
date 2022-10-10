from typing import List
from table.setup import get_tables, get_groups, Table, Group

def remaining_seats(tables: List[Table]):
    return sum(table.remaining_seats() for table in tables)

def required_seats(groups: List[Group]):
    return sum(group.count for group in groups)

def filled_seats(tables: List[Table]):
    return sum(table.filled_seats() for table in tables)

# Backtracking solving algorithm to evenly distribute groups of people
# across tables.
def solve():
    tables = get_tables()
    groups = get_groups()
    
    seats = remaining_seats(tables)
    req_seats = required_seats(groups)
    print(f"Remaining seats: {seats}")
    print(f"Required seats: {req_seats}")
    print()

    for i in range(len(groups)):
        added = False
        group = groups[i]
        if group.count == 0:
            continue    

        # Sort tables by remaining seats
        tables.sort(key=lambda table: table.remaining_seats(), reverse=True)
        for table in tables:
            if table.remaining_seats() == group.count:
                table.groups.append(group)
                added = True
                break
        if not added:
            # Add to tables but don't leave a single space
            for table in tables:
                if table.remaining_seats() >= group.count and (table.remaining_seats() + group.count) > 1:
                    table.groups.append(group)
                    added = True
                    break
        if not added:
            # Now just add to tables
            for table in tables:
                if table.remaining_seats() >= group.count:
                    table.groups.append(group)
                    added = True
                    break
        if not added:
            print(f"Unable to add group {group.name}")
    return tables

def main():
    tables = solve()
    tables.sort(key=lambda table: table.id)
    for table in tables:
        print(f"Table {table.id}, {table.filled_seats()} / {table.capacity}")
        for group in table.groups:
            print(f"{group.name},, {group.count}")
        print()

    print("Remaining seats:", remaining_seats(tables))
    print("Filled seats:", filled_seats(tables))

if __name__ == "__main__":
    main()