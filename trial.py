update_query = f"""
                            UPDATE UpdatedTables
                            SET room_id = '{room_id}',
                                batch_id = '{batch}',
                                subjectcode = '{subjectcode}'
                            WHERE day = '{day}' AND starttime = '{timing.split("-")[0]}' AND endtime = '{timing.split("-")[1]}'
                        """