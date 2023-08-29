def get_plan_id_query(payment_id):
    return f"""
        select plan_id from sms.orders where cart_checkout_id = 
        (select id from sms.cart_checkouts where payment_details->>'id' = '{payment_id}')
        """
        
def get_user_id_query(plan_id):
    return f"""
        select user_details->>'id' from sms.orders where plan_id = {plan_id}
        """