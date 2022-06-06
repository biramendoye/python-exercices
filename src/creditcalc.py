import math
import argparse


def get_periods(principal: float, monthly_payment: float, interest: float):
    """Get the number of monthly payments"""
    i = interest / (12 * 100)
    base = 1 + i
    n = math.ceil(math.log(monthly_payment / (monthly_payment - i * principal), base))
    return n


def get_annuity_payment(principal: float, months: int, interest: float):
    i = interest / (12 * 100)
    base = 1 + i
    delta = i * math.pow(base, months)
    delta = delta / (math.pow(base, months) - 1)
    return math.ceil(principal * delta)


def get_loan_principal(annuity_payment: float, months: int, interest: float):
    i = interest / (12 * 100)
    base = 1 + i
    delta = i * math.pow(base, months)
    delta = delta / (math.pow(base, months) - 1)

    return math.floor(annuity_payment / delta)


def pluralize(number: int, noun: str, plural: str = "s"):
    if number > 1:
        return noun + plural
    else:
        return noun


def info(months: int):
    if months < 12:
        print(f"It will take {months} {pluralize(months, 'month')} to repay this loan")
    else:
        years = months // 12
        months = months % 12
        if months == 0:
            print(f"It will take {years} {pluralize(years, 'year')} to repay this loan")
        else:
            print(
                f"It will take {years} {pluralize(years, 'year')} and {months} {pluralize(months, 'month')} to repay this loan"
            )


def handle_cli_args():
    parser = argparse.ArgumentParser(description="Calculate monthly payment for a loan")
    parser.add_argument(
        "--type",
        type=str,
        choices=["annuity", "diff"],
        help='indicates the type of payment: "annuity" or "diff" (differentiated).',
    )
    parser.add_argument("--payment", type=float, help="the monthly payment amount.")
    parser.add_argument(
        "--principal", type=float, help="calculations of both types of payment."
    )
    parser.add_argument("--interest", type=float, help="the loan interest.")
    parser.add_argument(
        "--periods", type=float, help="the number of months needed to repay the loan."
    )
    return parser.parse_args()


def main():
    args = handle_cli_args()

    if args.type != "annuity" and args.type != "diff":
        print("Incorrect parameters")
        return
    if args.type == "diff" and args.payment:
        print("Incorrect parameters")
        return
    if args.payment is not None and args.payment < 0:
        print("Incorrect parameters")
        return
    if args.principal is not None and args.principal < 0:
        print("Incorrect parameters")
        return
    if args.periods is not None and args.periods < 0:
        print("Incorrect parameters")
        return
    if args.interest is None or args.interest < 0:
        print("Incorrect parameters")
        return

    if args.type == "diff":
        if (
            args.interest is not None
            or args.periods is not None
            or args.principal is not None
        ):
            i = args.interest / (12 * 100)
            n = int(args.periods)
            p = args.principal
            somme = 0
            for m in range(1, n + 1):
                res = (p / n) + (i * (p - (p * (m - 1) / n)))
                somme += math.ceil(res)
                print(f"Month {m}: payment is {math.ceil(res)}")
            print(f"\nOverpayment = {math.ceil(somme - p)}")
    elif args.type == "annuity":
        if args.payment is None:
            res = get_annuity_payment(args.principal, int(args.periods), args.interest)
            print(f"Your annuity payment = {res}!")
            print(
                f"\nOverpayment = {math.ceil(res * int(args.periods) - args.principal)}"
            )
        elif args.principal is None:
            res = get_loan_principal(args.payment, int(args.periods), args.interest)
            print(f"Your loan principal = {res}!")
            print(
                f"\nOverpayment = {math.ceil(args.payment * int(args.periods) - res)}"
            )
        elif args.periods is None:
            res = get_periods(args.principal, args.payment, args.interest)
            info(res)
            print(f"\nOverpayment = {math.ceil(args.payment * res - args.principal)}")
        else:
            print("Incorrect parameters")


if __name__ == "__main__":
    main()
