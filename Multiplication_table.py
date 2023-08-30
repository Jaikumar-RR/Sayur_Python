Multiplicands_range = [7,16]
table_range = 12
for multiplicand in range(Multiplicands_range[0],Multiplicands_range[1]+1):
    print(f"Table {multiplicand}")
    for multiplier in range(1,table_range+1):
        print(f"{multiplicand} * {multiplier} : {multiplicand*multiplier}")
    print(f"{'-'*15}")