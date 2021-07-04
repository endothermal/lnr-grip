create view video_durations as (
    select v_starts.user_id,
           v_starts.device,
           v_starts.date_actioned as started_at,
           v_stops.date_actioned-v_starts.date_actioned as duration
    from video_actions v_starts
    left join video_actions v_stops
    on v_starts.user_id=v_stops.user_id
    and v_starts.device = v_stops.device
    and v_starts.date_actioned < v_stops.date_actioned
    where (v_starts.action="start")
    and (v_stops.action is null or v_stops.action="stop")
)
;

create view users_video_durations as (
    select user_id,
           cast(sum(duration) as UNSIGNED) as total_duration
    from video_durations
    group by user_id
)
;