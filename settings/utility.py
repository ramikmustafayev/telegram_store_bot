def _convert(list_convert):
    return [itm[0] for itm in list_convert]



def total_cost(all_quantity,all_price):
    order_total_cost=0
    for inx, itm in enumerate(all_price):
        order_total_cost+=all_quantity[inx]*all_price[inx]
    return order_total_cost

def get_total_cost(DB):
    all_product_id=DB.select_all_products_id()
    all_price=[DB.select_single_product_price(itm) for  itm in all_product_id ]
    all_quantity=[DB.select_order_quantity(itm) for itm in all_product_id]
    return total_cost(all_quantity,all_price)


def total_quantity(all_quantity):
    order_total_quantity = 0

    for itm in all_quantity:
        order_total_quantity += itm

    return order_total_quantity


def get_total_quantity(DB):
    all_product_id=DB.select_all_order_id()
    all_quantity=[DB.select_order_quantity(itm) for itm in all_product_id]
    return total_quantity(all_quantity)


