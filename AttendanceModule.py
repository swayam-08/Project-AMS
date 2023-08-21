
def mark_attendance(studList, attendances,date):
    for roll_n, name in studList.items():
        while True:
            attendance = input(f"Mark attendance for {name} ({roll_n}) [P/A]: ").upper()
            if attendance == 'P':
                attendances[roll_n][date] = True
                break
            elif attendance == 'A':
                attendances[roll_n][date] = False
                break
            else:
                print("Invalid input. Please enter 'P' for present or 'A' for absent.")
    print("!!!!Attendance marked Successfully!!!!")            

def view_attendance(studList, attendances,roll_n):
    if roll_n in attendances:
        return attendances[roll_n]
    return {}


def generate_report(studList,attendances,roll_n, period):
    attendance_data = attendances.get(roll_n, {})
    
    if period == 'daily':
        latest_date=max(attendance_data.keys()) if attendance_data else None
        if latest_date:
            latest_status="Present" if attendance_data[latest_date] else "Absent"
            report=f"Latest Daily Attendance Report for {studList.get(roll_n,'unknown')}:\n"
            report+=f"Date:{latest_date},Status:{latest_status}\n"
        else:
            report=f"No Daily attendance recorded fir {studList.get(roll_n,'unknown')}\n"


    elif period == 'weekly':
        latest_dates = sorted(attendance_data.keys(), reverse=True)
        latest_week_dates = latest_dates[:7]
        present_week_days = sum(1 for date in latest_week_dates if attendance_data[date])
        total_week_days = len(latest_week_dates)
        report = f"Weekly Attendance Report for {studList.get(roll_n, 'Unknown')}:\n"
        report += f"Present Days: {present_week_days}, Total Days: {total_week_days}\n"
        report += f"Attendance Percentage: {(present_week_days / total_week_days) * 100:.2f}%\n"

    elif period == 'monthly':
        today = input("Enter the current date (YYYY-MM-DD): ")
        year, month, _ = today.split('-')
        last_month = f"{year}-{str(int(month)).zfill(2)}"

        print("Monthly Attendance Report")
        print("=" * 30)

        
        month_dates = [date for date in attendance_data.keys() if date.startswith(last_month)]
        if len(month_dates) > 31:
            month_dates = month_dates[-31:]

        present_month_days = sum(1 for date in month_dates if attendance_data[date])
        total_month_days = len(month_dates)

        attendance_percentage = (present_month_days / total_month_days) * 100

        report = f"Roll Number: {roll_n}\n"
        report += f"Student Name: {studList[roll_n]}\n"
        report += f"Present Days: {present_month_days}/{total_month_days}\n"
        report += f"Attendance Percentage: {attendance_percentage:.2f}%\n"
        report += "=" * 30

    return report


def generate_all_reports(studList,attendances,period):
    for roll_n in studList:
        report = generate_report(studList,attendances,roll_n, period)
        print(report)
        print('-' * 30)
