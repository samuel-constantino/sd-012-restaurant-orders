class TrackOrders:
    def __init__(self):
        self.orders = []
        self.orders_count = 0

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return self.orders_count

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])
        self.orders_count += 1

    def get_most_ordered_dish_per_customer(self, customer):
        customer_orders = {}
        for order in self.orders:
            if order[0] == customer:
                if order[1] not in customer_orders:
                    customer_orders[order[1]] = 1
                else:
                    customer_orders[order[1]] += 1

        dishes = list(customer_orders.keys())
        counts = list(customer_orders.values())
        max_count = max(counts)
        max_count_position = counts.index(max_count)
        most_popular_dish = dishes[max_count_position]
        return most_popular_dish

    def get_never_ordered_per_customer(self, customer):
        total_dishes = set()
        dishes_ordered_by_customer = set()

        for order in self.orders:
            if order[1] not in total_dishes:
                total_dishes.add(order[1])
            if (
                order[0] == customer
                and order[1] not in dishes_ordered_by_customer
            ):
                dishes_ordered_by_customer.add(order[1])
        return total_dishes.difference(dishes_ordered_by_customer)

    def get_days_never_visited_per_customer(self, customer):
        every_days = set()
        days_with_customer = set()
        for order in self.orders:
            if order[2] not in every_days:
                every_days.add(order[2])
            if (
                order[0] == customer
                and order[2] not in days_with_customer
            ):
                days_with_customer.add(order[2])
        return every_days.difference(days_with_customer)

    def get_busiest_day(self):
        orders_by_day = {}
        for order in self.orders:
            day_of_order = order[2]
            if day_of_order not in orders_by_day:
                orders_by_day[day_of_order] = 1
            else:
                orders_by_day[day_of_order] += 1

        days = list(orders_by_day.keys())
        counts = list(orders_by_day.values())
        most_order = max(counts)
        most_order_position = counts.index(most_order)
        busiest_day = days[most_order_position]
        return busiest_day

    def get_least_busy_day(self):
        orders_by_day = {}
        for order in self.orders:
            day_of_order = order[2]
            if day_of_order not in orders_by_day:
                orders_by_day[day_of_order] = 1
            else:
                orders_by_day[day_of_order] += 1

        days = list(orders_by_day.keys())
        counts = list(orders_by_day.values())
        less_order = min(counts)
        less_order_position = counts.index(less_order)
        least_busy_day = days[less_order_position]
        return least_busy_day
