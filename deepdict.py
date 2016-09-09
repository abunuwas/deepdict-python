deep_dict = {
			'cluster': 'a_cluster',
			'serviceName': 'service_name',
			'taskDefinition': 'task_definition',
			'desiredCount': 'desired_count',
			'clientToken': None,
			'deploymentConfiguration': {
				'maximumPercent': None,
				'minimumHealthyPercent': 'min_health'
			},
			'aField': {
				'Level': 'first_level',
				'data': {
					'Level': 'second_level',
					'data': {
						'Level': 'third_level',
						'data': {
							'Level': 'fourth_level',
							'data': {
								'Level': 'fifth_level',
								'data': {
									'Level': 'last',
									'data': None
								}
							}
						}
					}
				}
			}
}


def change(dic):
	return dict((key, value.upper()) for key, value in dic.items() if type(value) is str)


def get_tuples(dic):
	return list(dic.items())

def make_changes(dic):
	new_dict = change(dic)
	keys = dic.keys()
	outer = list(dic.items())
	for key, value in outer:
		if type(value) is dict:
			pass

def filter_arg(value, filter_params):
	if type(value) is dict:
		values = filter_args(value, filter_params)
	return all(value != param for param in filter_params)

def filter_args(args, filter_params=None):
	if filter_params is None:
		filter_params = ['', None]
	return dict((key, value) for key, value in args.items() if filter_arg(value, filter_params))


def get_dicts_bad(dic, container):
	for key, value in dic.items():
		if type(value) is dict:
			filtered = filter_args(value)
			container[key] = {}
			get_dicts(filtered, container[key])
		else:
			container.update({ key: value })
	return filter_args(container)

def get_dicts_middle(dic, container):
	for key, value in dic.items():
		if type(value) is dict:
			new_container = [key]
			container.append(new_container)
			#yield key
			#yield value
			#yield from get_dicts(value)
			#yield from get_dicts(value, new_container)
			get_dicts(value, new_container)
		else:
			container.append(tuple((key, value)))
			#yield container
			#yield(tuple((key, value)))
	return container

def get_dicts(dic, container):
	for key, value in dic.items():
		if type(value) is dict:
			new_container = [key]
			container.append(new_container)
			get_dicts(filter_args(value), new_container)
		else:
			container.append(tuple((key, value)))
	return container

'''
data = list(get_dicts(deep_dict))
for d in data:
	if type(d) is dict:
		pass
	else:
		print(d)
'''

def build_dict(collections, container):
	for collection in collections:
		if type(collection) is tuple:
			key, value = collection
			container[key] = value
		elif type(collection) is list:
			key = collection[0]
			values = collection[1:]
			container[key] = {}
			new_container = container[key]
			build_dict(values, new_container)
	return container

outer_filter = filter_args(deep_dict)
tuples = get_dicts(outer_filter, [])

dicts = build_dict(tuples, {})

for key, value in dicts.items():
	print(key, '>>>>', value)

#for element in get_dicts(deep_dict, []):
#	print(element[0])

#print(get_dicts(deep_dict, []))

#for key, value in get_dicts(deep_dict, {}).items():
#	print(key, value)

'''
keys = deep_dict.keys()
for value in deep_dict[key]:
	pass
'''

'''
outcome = [('taskDefinition', 'task_definition'), ('desiredCount', 'desired_count'), ['aField', ('Level', 'first_level'), ['data', ('Level', 'second_level'), ['data', ('Level', 'third_level'), ['data', ('Level', 'fourth_level'), ['data', ('Level', 'fifth_level'), ['data', ('Level', 'last'), ('data', None)]]]]]], ('cluster', 'a_cluster'), ('clientToken', None), ['deploymentConfiguration', ('maximumPercent', None), ('minimumHealthyPercent', 'min_health')], ('serviceName', 'service_name')]

for element in outcome[2]:
	print(element)
'''