doPost(request,session):
    browseTags = system.tag.browseTags(system.util.jsonDecode(request['postData'])[u'rootPath'])
	tags = [];
	containers = [];
	for tag in browseTags:
	 if (tag.isFolder() or tag.isUDT()):
	 	containers.append(tag.name)
	 else:
	 	tags.append(tag.name)

	tagData = {"tags":tags, "containers":containers}

	return {'json': system.util.jsonEncode(tagData)}
