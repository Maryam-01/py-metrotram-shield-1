from src.analyser import filtered_alerts
from src.analyser import parse_alert

def test_empty_list_returns_empty_list():
    #arrange
    input_log = []
    
    expected_logs = []
    #ACT
    filtered_logs = filtered_alerts(input_log)

    # ASSERT
    assert expected_logs == filtered_logs

def test_log_containing_error_returns_error():
    input_log = ["2024-06-01 08:03:44 ERROR Disk usage exceeded 90% on /dev/sda1"]
    expected_logs = ["2024-06-01 08:03:44 ERROR Disk usage exceeded 90% on /dev/sda1"]
    filtered_logs = filtered_alerts(input_log)
    assert expected_logs == filtered_logs

def test_log_containing_401_returns():
    input_log = ["2024-06-01 08:07:33 401   Unauthorised access attempt from IP 192.168.1.45"]
    expected_logs = ["2024-06-01 08:07:33 401   Unauthorised access attempt from IP 192.168.1.45"]
    filtered_logs = filtered_alerts(input_log)
    assert expected_logs == filtered_logs

def test_log_containing_no_error_returns_no_error():
    input_log = ["2024-06-01 08:05:01 INFO  Scheduled backup started"]
    expected_logs = []
    filtered_logs = filtered_alerts(input_log)
    assert expected_logs == filtered_logs




def test_multiple_mixed_error_and_non_error_should_only_return_errors():
    #arrange
    input_log = ["2024-06-01 08:03:44 ERROR Disk usage exceeded 90% on /dev/sda1",
                "2024-06-01 08:05:01 INFO  Scheduled backup started",
                "2024-06-01 08:07:33 401   Unauthorised access attempt from IP 192.168.1.45",
                "2024-06-01 08:09:10 INFO  Backup completed successfully",
                "2024-06-01 08:11:55 ERROR Database connection timeout after 30s"]
    
    expected_logs = [
        "2024-06-01 08:03:44 ERROR Disk usage exceeded 90% on /dev/sda1",
        "2024-06-01 08:07:33 401   Unauthorised access attempt from IP 192.168.1.45",
        "2024-06-01 08:11:55 ERROR Database connection timeout after 30s"
]
    #ACT
    filtered_logs = filtered_alerts(input_log)

    # ASSERT
    assert expected_logs == filtered_logs

def test_parse_alert_returns_correct_dictionary():

    input_line = "2024-06-01 08:01:12 INFO  User admin logged in successfully"
    expected = {
        "timestamp": "2024-06-01 08:01:12",
        "level" : "INFO",
        "message": "User admin logged in successfully"
    }

    result = parse_alert(input_line)
    assert result == expected







    






