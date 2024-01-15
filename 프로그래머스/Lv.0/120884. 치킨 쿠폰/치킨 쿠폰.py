def solution(chicken):
    coupon = chicken
    answer = -1
    chickens = 0
    while coupon > 9:
        chickens += coupon // 10
        coupon = coupon // 10 + coupon % 10
        print(chickens, ' ', coupon)

    return chickens