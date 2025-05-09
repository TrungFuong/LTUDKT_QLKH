def inputIntOrPass(value):
    s = input(value)
    if s.strip() == "":
        return None;
    try:
        return int(s)
    except ValueError:
        print("Phải là số nguyên!");
        return inputIntOrPass(value);

def inputFloatOrPass(value):
    s = input(value)
    if s.strip() == "":
        return None;
    try:
        return float(s);
    except ValueError:
        print("Phải là số thực!");
        return inputFloatOrPass(value);