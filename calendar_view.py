from datetime import date
import calendar

#digunakan untuk mengeprint calender untuk membantu proses absensi dan generate
def print_calendar_with_week_numbers(year, specific_month=None):
    for month in range(1, 13) if specific_month is None else [specific_month]:
        print(f"\n{calendar.month_name[month]} {year}")
        print("Mo Tu We Th Fr Sa Su  Week")

        first_day, num_days = calendar.monthrange(year, month)
        calendar_row = "   " * first_day
        
        for day in range(1, num_days + 1):
            calendar_row += f"{day:02} "
            current_date = f"{year}-{month:02}-{day:02}"
            week_number = date.fromisoformat(current_date).isocalendar()[1]

            if (first_day + day - 1) % 7 == 6:
                calendar_row += f" (W-{week_number:02})"
                print(calendar_row)
                calendar_row = ""

        if calendar_row.strip():
            week_number = date.fromisoformat(f"{year}-{month:02}-{num_days:02}").isocalendar()[1]
            calendar_row += f" (W-{week_number:02})"
            print(f"{calendar_row: <33}")

print_calendar_with_week_numbers(2023, specific_month=9)



