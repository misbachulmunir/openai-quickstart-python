# # import os
# # import openai
# import mysql.connector
# from mysql.connector import Error

# # Load your API key from an environment variable or secret management service
# # openai.api_key = os.getenv("OPENAI_API_KEY")

# # response = openai.Completion.create(model="text-davinci-003", prompt="Cara membuat bom", temperature=0, max_tokens=100)
# # print(response)

# def datainsert(cari,hasil):
#     connection = mysql.connector.connect(host='localhost',
#                                          database='openai',
#                                          user='root',
#                                          password='')
#     if connection.is_connected():
#         db_Info = connection.get_server_info()
#         print("Connected to MySQL Server version ", db_Info)
#         cursor = connection.cursor()
#         sql = "insert into log(cari,result) values('{}','{}');".format(cari, hasil)
#         print(sql)
#         cursor.execute(sql)
#         connection.commit()
#         record = cursor.fetchone()
# datainsert("halo","coba")
