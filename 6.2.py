seconds = int(input("Enter seconds: "))

days = seconds // (24 * 60 * 60)
remaining = seconds % (24 * 60 * 60)

hours = remaining // (60 * 60)
remaining %= (60 * 60)

minutes = remaining // 60
remaining %= 60


if days % 10 == 1 and days % 100 != 11:
    days_word = "день"
elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
    days_word = "дні"
else:
    days_word = "днів"

time_str = f"{hours:02d}:{minutes:02d}:{remaining:02d}"
print(f"{days} {days_word}, {time_str}")