curr_h, curr_m, curr_s = map(int, input().split(':'))
start_h, start_m, start_s = map(int, input().split(':'))

curr_t = curr_h * 3600 + curr_m * 60 + curr_s
start_t = start_h * 3600 + start_m * 60 + start_s

cal_t = start_t - curr_t

if cal_t < 0 :
  cal_t += 24*3600
cal_h = cal_t // 3600
cal_m = (cal_t % 3600) // 60
cal_s = cal_t % 60

cal_h, cal_m, cal_s = map(str, (cal_h, cal_m, cal_s))

print(cal_h.zfill(2), ':' ,cal_m.zfill(2), ':', cal_s.zfill(2), sep='')

