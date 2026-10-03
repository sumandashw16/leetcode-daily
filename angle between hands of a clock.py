degree = 360
hour = 12
minutes = 60


hr, mn = (1,57)

hr_angle = (hr*30) + (mn/60)*30
print(hr_angle)

min_angle = 360 * (mn/60)
print(min_angle)

print(abs(min_angle - hr_angle))