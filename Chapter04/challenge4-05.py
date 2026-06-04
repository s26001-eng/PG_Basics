def to_float(value):
    try:
        return float(value)
    except ValueError:
        print("float型に変換できません")


result = to_float("3.14")

print(result)
