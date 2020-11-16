
n=int(input())
zeros = 0
i = 5
while n / i >= 1:
    zeros += n // i
    i *= 5
print(zeros)


if "a"<"b":
    print("bigger b")
else:
    print("bigger a")