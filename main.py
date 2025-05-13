from cli import common_parser
from data_processor import get_employee_salaries


def main():
    args = common_parser()
    print(get_employee_salaries(args.files, args.report))


if __name__ == "__main__":
    main()
