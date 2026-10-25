-- JSON Functions

SELECT json_object(
'emp_id',101,
'name','John',
'salary',75000
);

SELECT json_array(
'Python',
'SQL',
'AI'
);

SELECT json_extract(
'{"name":"John","salary":75000}',
'$.name'
);