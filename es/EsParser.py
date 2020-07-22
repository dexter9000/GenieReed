class EsParser:

    @classmethod
    def getFieldNames(cls, pattern):
        result = []
        for f in pattern['properties']:
            result.append(f)
        return sorted(result, key=str.lower)

    @classmethod
    def getFullFieldNames(cls, pattern):
        result = []
        properties = pattern['properties']
        for f in properties:
            if 'properties' in properties[f]:
                result.extend(cls._getFieldNamesWithParent(f, properties[f]['properties']))
            else:
                result.append(f)
        return sorted(result, key=str.lower)

    @classmethod
    def _getFieldNamesWithParent(cls, parent, fields):
        result = []
        for f in fields:
            fieldName = parent + '.' + str(f)
            if 'properties' in fields[f]:
                result.extend(cls._getFieldNamesWithParent(fieldName, fields[f]['properties']))
            else:
                result.append(fieldName)
        return result

    @classmethod
    def getFullFieldType(cls, pattern, field):
        properties = pattern['properties']
        if field in properties:
            if 'properties' in properties[field]:
                return ''  # TODO
            else:
                return properties[field]['type']
        else:
            return ''
