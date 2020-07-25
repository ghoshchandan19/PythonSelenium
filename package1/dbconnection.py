import psycopg2


def getOtp():
        try:
            connection = psycopg2.connect(user="qaread",
                                          password="Qread@1357",
                                          host="10.103.1.209",
                                          port="5406",
                                          database="hdfcmf-qa-postgres")
            cursor = connection.cursor()
            postgreSQL_select_Query = "select otp from otp order by otp_generated_time desc limit 1"

            cursor.execute(postgreSQL_select_Query)
            print("Selecting rows from mobile table using cursor.fetchall")
            mobile_records = cursor.fetchall()

            print("Print each row and it's columns values")
            for row in mobile_records:
                ID = row[0]
                print(ID)
                print("Id = ", row[0], )
                print("Model = ", row[1])
                print("Price  = ", row[2], "\n")

        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)

        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
            return ID







