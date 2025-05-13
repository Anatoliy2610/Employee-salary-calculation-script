def format_employee_data(
    name: str, hours: str, rate: str, payout: str, symbol: str
) -> str:
    return (
        f"{'-' * 14} {name}"
        f"{symbol * (16 - len(name))}{hours}"
        f"{symbol * (10 - len(hours))}{rate}"
        f"{symbol * (9 - len(rate))}{payout}"
    )


def payout_format(tree: dict, symbol: str = " ") -> str:
    result = []
    header = f"{symbol * 15}name{symbol * 12}hours{symbol * 5}rate{symbol * 5}payout"
    result.append(header)
    for department, employees in tree.items():
        result.append(department)
        total_hours = 0
        total_payout = 0
        for data in employees:
            name = data["name"]
            hours = data["hours"]
            rate = data["rate"]
            payout = data["payout"]
            formatted_line = format_employee_data(name, hours, rate, payout, symbol)
            total_hours += int(hours)
            total_payout += int(payout[1:])
            result.append(formatted_line)
        result.append(
            f"{' ' * 31}{total_hours}{' ' * (19 - len(str(total_hours)))}${total_payout}"
        )
    return "\n".join(result)


def choose_format(tree: dict, format: str) -> str:
    if format == "payout":
        return payout_format(tree)
    return "Выбран неверный формат"
