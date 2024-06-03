import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='invoices'
)


cursor = conn.cursor()


def input_invoice():
    pass



def all_invoice():
    invoice = (
        " SELECT * FROM invoice"
    )
    cursor.execute(invoice)
    invoices = cursor.fetchall()
    columns = cursor.column_names
    invoice_result = []
    # Print each job record as a dictionary
    for invoice in invoices:
        invoice_data = dict(zip(columns, invoice))
        invoice_result.append(invoice_data)
    return invoice_result