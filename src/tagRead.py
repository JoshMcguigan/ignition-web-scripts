def doPost(request,session):
	tagPaths = system.util.jsonDecode(request['postData'])['tagPaths']
	tagValues = []

	qualifiedValues = system.tag.readAll(tagPaths)
	tagValues = [{'value': qv.value, 'quality': qv.quality.toString(), 'timestamp': qv.timestamp} for qv in qualifiedValues]

	tagData = {}
	for i, tagPath in enumerate(tagPaths):
		tagData[tagPath] = tagValues[i]
        
	return {'json': system.util.jsonEncode(tagData)}
