# Script demonstrates using multiprocessing module to transform custom object into a dictionary
import multiprocessing as mp


class Customer:
    def __init__(self, cust_id, age, gender, annual_income, total_spend, units_purchased, orders_made, site_visits):
        self.cust_id = cust_id
        self.age = age
        self.gender = gender
        self.annual_income = annual_income
        self.total_spend = total_spend
        self.units_purchased = units_purchased
        self.orders_made = orders_made
        self.site_visits = site_visits


def categorize_cust(cust):
    cust_info = [cust.cust_id, cust.age, cust.gender]
    order_info = [cust.total_spend, cust.units_purchased, cust.orders_made]
    site_visits = [cust.site_visits]

    return {
        'cust_info': cust_info,
        'order_info': order_info,
        'site_visits': site_visits
    }


def main():
    john = Customer(
        cust_id='1001',
        age=34,
        gender='Male',
        annual_income=104000,
        total_spend=5000,
        units_purchased=20,
        orders_made=4,
        site_visits=20
    )

    susie = Customer(
        cust_id='1002',
        age=26,
        gender='Female',
        annual_income=45000,
        total_spend=1000,
        units_purchased=10,
        orders_made=2,
        site_visits=3
    )

    sarah = Customer(
        cust_id='1003',
        age=40,
        gender='Female',
        annual_income=113000,
        total_spend=500,
        units_purchased=4,
        orders_made=4,
        site_visits=17
    )

    pool = mp.Pool()
    results = pool.map(categorize_cust, [john, susie, sarah])
    print(list(results))


if __name__ == '__main__':
    main()
