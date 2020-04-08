x = 9
gs = 2  # 결석
jg = 0  # 지각
jt = 0 + x  # 조퇴
oc = 0  # 외출
days = 21  # 단위기간

rslt = gs + ((jg + jt + oc) // 3)  # 결석일수
print('결석 %s일' % rslt)

total = days - rslt  # 출석일수
print('출석 %s일' % total)

minus = rslt / days * 100  # 결석률
rates = total / days * 100  # 출석률
print('출석률 = %s%%' % rates)
