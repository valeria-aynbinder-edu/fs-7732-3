import json

import psycopg2
from flask import Flask, request, jsonify

app = Flask("bank_web_app")

# bank REST api
# get /customers
# get /customers/id


conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="bank",
    user="postgres",
    password="postgres")


@app.route("/api/v1/customers/<int:customer_id>", methods=['GET'])
def get_customer(customer_id):
    print(f"called /customers/customer_id/{customer_id}")
    try:
        with conn:
            with conn.cursor() as cur:
                sql = "SELECT * FROM customers WHERE id = %s"
                cur.execute(sql, (customer_id, ))
                result = cur.fetchone()
                print(f"result from fetchone: {result}")
                if result:
                    ret_data = {
                        'id': result[0],
                        'passport_num': result[1],
                        'name': result[2],
                        'address': result[3]
                    }
                    return jsonify(ret_data)
                else:
                    return {'error': f'customer with id {customer_id} does not exist'}, 404
    except psycopg2.DatabaseError as e:
        return {'error': f"Database error, {e}"}, 500
    except Exception as e:
        return {'error': f"Unexpected error, {e}"}, 500

@app.route("/api/v1/customers/<int:customer_id>/accounts", methods=['GET'])
def customer_accounts(customer_id):
    with conn:
        with conn.cursor() as cur:
            sql = """
            SELECT accounts.* FROM accounts JOIN account_owners
            ON account_owners.account_id = accounts.id 
            WHERE account_owners.customer_id = %s;
            """
            cur.execute(sql, (customer_id,))
            results = cur.fetchall()
            if results:
                ret_data = []
                for res in results:
                    ret_data.append({
                        'id': res[0],
                        'balance': res[1],
                        'max_limit': res[2],
                    })
                return jsonify(ret_data)
            else:
                return {'error': f'customer with id {customer_id} does not exist'}, 404

@app.route("/api/v1/customers/<int:customer_id>", methods=['PUT'])
def update_customer(customer_id):
    new_data = request.form
    updates_str_list = []
    allowed_fields = ('name', 'address')
    for field in new_data:
        if field in allowed_fields:
            updates_str_list.append(f"{field}=%s")
    sql = f"UPDATE customers SET {','.join(updates_str_list)} WHERE id=%s"
    with conn:
        with conn.cursor() as cur:
            cur.execute(sql, tuple(new_data.values()) + tuple([customer_id]))
            if cur.rowcount == 1:
                # update succeeded
                return app.response_class(status=200)
    return app.response_class(status=500)

# @app.route("/api/v1/account", methods=['POST', 'GET'])
# def accounts():
#     if request.method == 'GET':
#         pass
#     elif request.method == 'POST':
#         pass


@app.route("/api/v1/customers", methods=['POST'])
def get_customers():
    pass


# running from commandline or code
# debugging
if __name__ == '__main__':
    app.run(debug=True)
