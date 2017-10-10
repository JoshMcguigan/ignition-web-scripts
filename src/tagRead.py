def doPost(request,session):
	tagPaths = system.util.jsonDecode(request['postData'])['tagPaths']
	tagValues = []

	qualifiedValues = system.tag.readAll(tagPaths)
	tagValues = [{'value': qv.value, 'quality': qv.quality.toString(), 'timestamp': qv.timestamp} for qv in qualifiedValues]

	tagData = {}
	for i in range(len(tagPaths)):
		tagData[tagPaths[i]] = tagValues[i]
        
	return {'json': system.util.jsonEncode(tagData)}
