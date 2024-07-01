SELECT 
    studies.study_id,
    studies.study_name,
    trials.trial_id,
    trials.number AS trial_number,
    trial_params.param_name,
    trial_params.param_value,
    trial_values.value
FROM 
    trials
INNER JOIN 
    studies ON trials.study_id = studies.study_id
INNER JOIN 
    trial_params ON trials.trial_id = trial_params.trial_id
INNER JOIN 
    trial_values ON trials.trial_id = trial_values.trial_id
WHERE 
    trial_values.value IS NOT NULL
ORDER BY 
    studies.study_id, trials.number;
