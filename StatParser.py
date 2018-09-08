import odbc
import modules.StatParser_module as sp

# params
delay = 300.0  # sec
repeat = 0  # count
end = False  # exit code

# db connection
connect = odbc.odbc('oasis')
db = connect.cursor()

sp.stat_parser(delay, False, repeat, db)
