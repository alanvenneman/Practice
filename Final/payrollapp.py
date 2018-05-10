from Payroll import Payroll
from WorkedHoursError import WorkedHoursError


payroll_today = Payroll()
hours_worked = input(eval(payroll_today.set_hours()))
if hours_worked < 0 or hours_worked > 40:
    raise WorkedHoursError
