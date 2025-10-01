## 📌 **Date & Time Format Codes**

| Code        | Meaning                                            | Example      |
| ----------- | -------------------------------------------------- | ------------ |
| `%Y`        | Year (4-digit)                                     | `2025`       |
| `%y`        | Year (2-digit)                                     | `25`         |
| `%m`        | Month (zero-padded)                                | `01` to `12` |
| `%B`        | Full month name                                    | `October`    |
| `%b` / `%h` | Abbreviated month name                             | `Oct`        |
| `%d`        | Day of month (zero-padded)                         | `01` to `31` |
| `%e`        | Day of month (space-padded) *(platform dependent)* | ` 1`, `31`   |
| `%A`        | Full weekday name                                  | `Wednesday`  |
| `%a`        | Abbreviated weekday name                           | `Wed`        |
| `%w`        | Weekday as decimal (0=Sunday, 6=Saturday)          | `3`          |
| `%j`        | Day of the year (001–366)                          | `275`        |
| `%U`        | Week number of year (Sunday first day, 00–53)      | `40`         |
| `%W`        | Week number of year (Monday first day, 00–53)      | `39`         |

---

## ⏰ **Time Format Codes**

| Code | Meaning                           | Example      |
| ---- | --------------------------------- | ------------ |
| `%H` | Hour (24-hour clock, zero-padded) | `00`–`23`    |
| `%I` | Hour (12-hour clock, zero-padded) | `01`–`12`    |
| `%p` | AM / PM                           | `AM`, `PM`   |
| `%M` | Minute                            | `00`–`59`    |
| `%S` | Second                            | `00`–`59`    |
| `%f` | Microsecond (6 digits)            | `123456`     |
| `%z` | UTC offset                        | `+0300`      |
| `%Z` | Time zone name                    | `EAT`, `UTC` |

---

## 📅 **Special Codes**

| Code | Meaning                               | Example                    |
| ---- | ------------------------------------- | -------------------------- |
| `%c` | Locale’s date and time representation | `Wed Oct  1 09:30:00 2025` |
| `%x` | Locale’s date representation          | `10/01/25`                 |
| `%X` | Locale’s time representation          | `09:30:00`                 |
| `%%` | Literal `%` character                 | `%`                        |
