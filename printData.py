from datetime import datetime
from datetime import timedelta
YESTERDAY = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')


def printSleepData(sleep_data):
    """Prints users sleep data"""
    summary_date = sleep_data["summary_date"]
    print('>>> Sleep details <<<') if summary_date == YESTERDAY else print(f'>>> Sleep details [{summary_date}] <<<')
    print(f"- Sleep score: {sleep_data['score']}")
    
    bedtime_start = sleep_data['bedtime_start'].split('T')[1].split('+')[0]
    bedtime_end = sleep_data['bedtime_end'].split('T')[1].split('+')[0]
    print(f"- Bedtime: {bedtime_start} - {bedtime_end}")

    duration = formatDecimalToHours(sleep_data['duration']/60/60)
    actual = formatDecimalToHours(sleep_data['total']/60/60)
    print(f"- Sleep duration: {duration} (actual: {actual})")

    print(f"- Resting heart rate: {sleep_data['hr_lowest']}")
    print(f"- Average heart rate: {sleep_data['hr_average']}")
    print()


def printActivityData(activity_data):
    """Prints users activity data"""
    print('>>> Activity details <<<') if activity_data['summary_date'] == datetime.today().strftime('%Y-%m-%d') else print(f'>>> Activity details [{activity_data["summary_date"]}] <<<')
    print(f"- Activity score: {activity_data['score']}")
    print(f"- Steps: {activity_data['steps']}")
    print(f"- Inactivity alerts: {activity_data['inactivity_alerts']}")
    print(f"- Calories burnt: {activity_data['cal_total']}")
    print('- Rest mode is on.') if activity_data['rest_mode_state'] == 1 else print('- Rest mode is off.')
    print()


def printReadinessData(readiness_data):
    """Prints users readiness data"""
    print('>>> Readiness details <<<') if readiness_data['summary_date'] == YESTERDAY else print(f'>>> Readiness details [{readiness_data["summary_date"]}] <<<')
    print(f"- Readiness score: {readiness_data['score']}")
    print(f"- Activity balance: {readiness_data['score_activity_balance']}")
    print(f"- Recovery index: {readiness_data['score_recovery_index']}")
    print(f"- Sleep balance: {readiness_data['score_sleep_balance']}")
    print()


def formatDecimalToHours(time):
    """Returns decimal value converted to hours:minutes:seconds format"""
    hours = int(time)
    minutes = (time*60) % 60
    seconds = (time*3600) % 60
    return "%d:%02d:%02d" % (hours, minutes, seconds)