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

@staticmethod
def inputPhone(value):
        s = input(value).strip()
        if s == "":
            return None
        if not s.isdigit():
            print("Số điện thoại chỉ được chứa chữ số!")
            return Validation.inputPhone(value)
        return s