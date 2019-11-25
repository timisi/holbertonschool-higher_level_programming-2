-- Script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
-- Script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT state, MAX(value) AS avg_temp FROM temperatures GROUP BY state ORDER BY state;
