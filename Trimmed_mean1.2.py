from statistics import mean 
Estimates = [19, 19, 19, 21, 21, 22, 23, 26, 31, 31, 32, 35, 36, 1, 1, 2, 2, 4, 7, 9, 12, 12, 14, 18, 18, 39, 39, 39, 40, 41, 42, 44, 45, 45, 45, 46, 52, 52, 54, 55, 55, 55, 56, 57, 58, 80, 80, 83, 85, 87, 93, 93, 93, 94, 94, 96, 96, 96, 62, 65, 66, 66, 66, 67, 70, 71, 71, 72, 75, 75, 79, 80, 97, 98, 98]
Estimates.sort()

tv =int( 0.1*len(Estimates))

Estimates = Estimates[tv:len(Estimates)-tv]

print(mean(Estimates))