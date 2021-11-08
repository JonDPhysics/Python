CRUD FOR MYSQL SYNTAX:
-Create 
-INSERT INTO table (table_columns1, table_columns2, etc) VALUES (value1, value2, etc)

-Retreive/Read  
        -SELECT column (*(all), column1, column2,...., column_) FROM table
        -SELECT *, concat_ws(column,other_column) AS name_of_column FROM shema.table;

-Update -UPDATE table SET column = value WHERE id = x

-Delete - DELETE FROM table WHERE id = x
        - DELETE FROM table WHERE id IN (x,x+1, x-1,...,x+/-n)