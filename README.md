# decoding
msg = json.dumps({'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

                                'id': self.robot_id,

                                'action': 'location change',

                                 variable_name: variable_value}).encode('utf-8')

 

This is the format of the message.. In our case, variable_name = ‘audio’ and variable_value is ‘formData’ in the recorder.js.
