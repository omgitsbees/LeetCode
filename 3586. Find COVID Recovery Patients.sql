-- Solution to find COVID recovery patients
WITH positive_tests AS (
    -- Get first positive test date for each patient
    SELECT 
        patient_id,
        MIN(test_date) AS first_positive_date
    FROM covid_tests
    WHERE result = 'Positive'
    GROUP BY patient_id
),
negative_after_positive AS (
    -- Get first negative test after the first positive test for each patient
    SELECT 
        ct.patient_id,
        pt.first_positive_date,
        MIN(ct.test_date) AS first_negative_after_positive
    FROM covid_tests ct
    JOIN positive_tests pt ON ct.patient_id = pt.patient_id
    WHERE ct.result = 'Negative' 
    AND ct.test_date > pt.first_positive_date
    GROUP BY ct.patient_id, pt.first_positive_date
)
SELECT 
    p.patient_id,
    p.patient_name,
    p.age,
    DATEDIFF(nap.first_negative_after_positive, nap.first_positive_date) AS recovery_time
FROM patients p
JOIN negative_after_positive nap ON p.patient_id = nap.patient_id
ORDER BY recovery_time, patient_name;
