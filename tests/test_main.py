import pytest

from data_processor import get_employee_salaries


@pytest.mark.parametrize(
    "file_path, formatter, result_file_path",
    [
        (
            [
                "tests/fixtures/data1.csv",
                "tests/fixtures/data2.csv",
                "tests/fixtures/data3.csv",
            ],
            "payout",
            "tests/fixtures/result_data1_data2_data3.txt",
        ),
        (
            ["tests/fixtures/data1.csv", "tests/fixtures/data2.csv"],
            "payout",
            "tests/fixtures/result_data1_data2.txt",
        ),
        (
            ["tests/fixtures/data1.csv", "tests/fixtures/data3.csv"],
            "payout",
            "tests/fixtures/result_data1_data3.txt",
        ),
        (["tests/fixtures/data1.csv"], "payout", "tests/fixtures/result_data1.txt"),
        (
            ["tests/fixtures/data2.csv", "tests/fixtures/data3.csv"],
            "payout",
            "tests/fixtures/result_data2_data3.txt",
        ),
    ],
)
def test_get_employee_salaries(file_path, formatter, result_file_path):
    with open(result_file_path, "r") as file:
        exp_result = file.read()
    assert get_employee_salaries(file_path, formatter) == exp_result
