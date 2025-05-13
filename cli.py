import argparse


def common_parser():
    parser = argparse.ArgumentParser(
        description="Скрипт для подсчета зарплаты сотрудников"
    )
    parser.add_argument("files", nargs="+", help="Список CSV файлов")
    parser.add_argument(
        "-r",
        "--report",
        default="payout",
        help="установите формат вывода",
    )
    return parser.parse_args()
