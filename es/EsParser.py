class EsParser:

    @classmethod
    def getFieldNames(self, pattern):
        result = []
        for f in pattern['properties']:
            result.append(f)
        return sorted(result, key=str.lower)

    @classmethod
    def getFullFieldNames(self, pattern):
        result = []
        properties = pattern['properties']
        for f in properties:
            if ('properties' in properties[f]):
                result.extend(self._getFieldNamesWithParent(f, properties[f]['properties']))
            else:
                result.append(f)
        return sorted(result, key=str.lower)

    @classmethod
    def _getFieldNamesWithParent(self, parent, fields):
        result = []
        for f in fields:
            fieldName = parent + '.' + str(f)
            if ('properties' in fields[f]):
                result.extend(self._getFieldNamesWithParent(fieldName, fields[f]['properties']))
            else:
                result.append(fieldName)
        return result

    @classmethod
    def getFullFieldType(self, pattern, field):
        properties = pattern['properties']
        if field in properties:
            if 'properties' in properties[field]:
                return ''  # TODO
            else:
                return properties[field]['type']
        else:
            return ''

    def getFieldInfo(self, field):
        pass