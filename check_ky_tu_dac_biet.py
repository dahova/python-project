def check_special_char(s):
    special_chars = "!@#$%&*,."
    return any(c in special_chars for c in s)

def check_invalid_char(s):  # Có thể edit
    invalid_chars = "[]{}?/\\|'\";:-_=+`~<>"
    return any(c in invalid_chars for c in s)

def validate_string(s):  # Có thể edit
    error = []

    # 1. Kiểm tra độ dài
    if not (8 <= len(s) <= 20):
        error.append("Chuỗi phải có từ 8 đến 20 ký tự.")

    # 2. Kiểm tra chữ hoa, chữ thường, số, ký tự đặc biệt
    if not any(c.islower() for c in s):
        error.append("Chuỗi phải có ít nhất 1 chữ thường.")
    if not any(c.isupper() for c in s):
        error.append("Chuỗi phải có ít nhất 1 chữ HOA.")
    if not any(c.isdigit() for c in s):
        error.append("Chuỗi phải có ít nhất 1 số.")
    if not check_special_char(s):
        error.append("Chuỗi phải có ít nhất 1 ký tự đặc biệt (!@#$%&*,.)")

    # 3. Kiểm tra ký tự không được phép
    if check_invalid_char(s):
        error.append("Chuỗi không được chứa các ký tự []{}?/\\|'\";:-_=+`~<>")

    # 4. Kiểm tra không có dấu cách
    if " " in s:
        error.append("Chuỗi không được chứa dấu cách.")

    return error

while True:
    s = input("Hãy nhập 1 chuỗi: ")
    error = validate_string(s)

    if not error:
        print("Chuỗi nhập hợp lệ.")
        break
    else:
        print("Chuỗi nhập chưa đúng.")
        for err in error:
            print("- " + err)

        # Yêu cầu nhập lại hoặc thoát
        choice = input("Nhập 'Ok' để thử lại hoặc 'Exit' để thoát: ").strip().lower()
        if choice == "exit":
            print("Chương trình kết thúc.")
            exit()
        elif choice == "ok":
            continue
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")
