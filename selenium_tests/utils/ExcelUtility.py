import csv

test_results = []

def add_result(
    scenario,
    test_id,
    description,
    steps,
    expected,
    actual,
    status,
    testdata="Not required"
):
    test_results.append({
        "Test Case Scenario": scenario,
        "Test Case ID": test_id,
        "Testcase Description": description,
        "Testcase Steps": steps,
        "Expected Result": expected,
        "Actual Result": actual,
        "Testdata": testdata,
        "Status": status
    })

def write_results_to_csv():
    with open("test_results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=test_results[0].keys())
        writer.writeheader()
        writer.writerows(test_results)
