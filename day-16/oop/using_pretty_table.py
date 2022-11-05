from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Eletric"], ["Squirtle", "Water"], ["Charmander", "Fire"]
    ]
)


table.align = "l"
print(table)