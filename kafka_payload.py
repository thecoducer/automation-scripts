def get_gringotts_payment_update_message(status, user_action_type, payment_id):
    message = (
        '{"status": "%s","userActionType": "%s","publisherUUID": "12237SFGFGN","id": "%s","paid": '
        '{"totalAmount": "5333.72","paymentOffers": [{"type": "NCEMI","amount": "717.01"}],"paymentInstruments": '
        '{"CASH": "5333.72","FCASH": "0.00"}}}'
    ) % (status, user_action_type, payment_id)
    return message

def get_delphi_kyc_update_message(plan_id, user_id, order_id, kyc_state, for_unlmtd):
    message = f"""
        {{"planId": {plan_id}, "userId": {user_id}, "orderId": {order_id}, "kycState": "{kyc_state}", "forUnlmtd": {for_unlmtd}, "publisherUUID": "f8deb3da-e954-4588-b01a-865f56735b98"}}
        """
    return message

