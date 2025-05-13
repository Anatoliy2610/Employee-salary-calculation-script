from formaters import choose_format


def open_file(file_path: str) -> list:
    result = []
    with open(file_path) as file:
        text = file.readlines()
        for item in text:
            result.append(item.split(","))
    return result


def parse_data(data: list) -> list:
    keys = [key.rstrip() for key in data[0]]
    result = []
    index_data = 1
    while index_data < len(data):
        person_data = {}
        for index, value in enumerate(data[index_data]):
            if keys[index] not in ("hourly_rate", "rate", "salary"):
                person_data[keys[index]] = value.rstrip()
            person_data["rate"] = value.rstrip()
        result.append(person_data)
        index_data += 1
    return result


def get_data_all_files(path_files: tuple) -> list:
    result = []
    for path in path_files:
        data_file = open_file(path)
        data = parse_data(data_file)
        result.extend(data)
    return result


def get_payout_for_department(all_data: list) -> dict:
    result = {}
    for person_data in all_data:
        department = person_data["department"]
        payout = f"${int(person_data['hours_worked']) * int(person_data['rate'])}"
        employee_data = {
            "name": person_data["name"],
            "hours": person_data["hours_worked"],
            "rate": person_data["rate"],
            "payout": payout,
        }
        result.setdefault(department, []).append(employee_data)
    return result


def get_employee_salaries(args: list, stylish: str = "payout") -> str:
    try:
        file_path = tuple(args)
        data_files = get_data_all_files(file_path)
        tree = get_payout_for_department(data_files)
        result = choose_format(tree=tree, format=stylish)
        return result
    except:
        return 'Проверьте правильность написания команды!'
