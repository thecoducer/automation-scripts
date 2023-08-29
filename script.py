import pandas as pd
import psycopg2
from confluent_kafka import Producer

import utils
import kafka_payload
import queries
import const

payment_id = input("Enter payment id = ")

connection = utils.connect_to_database(const.host, const.user, const.password, const.database_name)
if connection:
    cursor = connection.cursor()
    
    plan_id_query = queries.get_plan_id_query(payment_id)
    plan_id = utils.fetch_one_row(cursor, plan_id_query)
    print("\nPlan ID = ", plan_id)
    
    user_id_query = queries.get_user_id_query(plan_id)
    user_id = utils.fetch_one_row(cursor, user_id_query)
    print("\nUser ID = ", user_id)

    connection.close()

producer = utils.create_producer(const.broker)

cart_checkout_payment_success_message = kafka_payload.get_gringotts_payment_update_message("COMPLETED", "CART_CHECKOUT", payment_id)
utils.publish_message(producer, const.payment_update_topic, cart_checkout_payment_success_message)

kyc_update_message = kafka_payload.get_delphi_kyc_update_message(plan_id, user_id, "null", "APPROVED", "true")
utils.publish_message(producer, const.kyc_update_topic, kyc_update_message)

utils.close_producer(producer)



