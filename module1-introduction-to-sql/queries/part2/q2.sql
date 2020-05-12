SELECT
    count("User Id") as "at_least_100"
FROM
    review
WHERE
    Nature >= 100
    AND shopping >= 100