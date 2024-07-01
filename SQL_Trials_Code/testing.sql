CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `MichaelAzure`@`%` 
    SQL SECURITY DEFINER
VIEW `study_trials_view` AS
    SELECT 
        `trials`.`trial_id` AS `trial_id`,
        `trials`.`study_id` AS `study_id`,
        `studies`.`study_name` AS `study_name`,
        `trial_params`.`param_name` AS `param_name`,
        `trial_params`.`param_value` AS `param_value`,
        COALESCE(`trial_values`.`value`, 'Failed') AS `score`
    FROM
        (((`trials`
        JOIN `studies` ON ((`trials`.`study_id` = `studies`.`study_id`)))
        JOIN `trial_params` ON ((`trials`.`trial_id` = `trial_params`.`trial_id`)))
        LEFT JOIN `trial_values` ON ((`trials`.`trial_id` = `trial_values`.`trial_id`)))
        