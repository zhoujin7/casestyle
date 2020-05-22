# coding=utf-8

import re


def camelcase(string):
    s_list = casepreprocess(string)
    if s_list:
        string = ''.join(s.title() for s in s_list)
        string = string[0].lower() + string[1:]
        return string
    return ''


def pascalcase(string):
    s_list = casepreprocess(string)
    if s_list:
        return ''.join(s.title() for s in s_list)
    return ''


def snakecase(string):
    s_list = casepreprocess(string)
    if s_list:
        return '_'.join(s_list)
    return ''


def constcase(string):
    return snakecase(string).upper()


def dashcase(string):
    s_list = casepreprocess(string)
    if s_list:
        return '-'.join(s_list)
    return ''


def casepreprocess(string):
    if isinstance(string, str):
        string = string.strip().replace('-', ' ')
        if string != '_' * len(string):
            underscore_at_start = ''
            if string.startswith('_'):
                j = 1
                for i, _ in enumerate(string):
                    if i < len(string):
                        if string[i + 1] == string[i]:
                            j += 1
                        else:
                            break
                underscore_at_start = '_' * j
            underscore_at_end = ''
            if string.endswith('_'):
                j = 1
                for i in range(len(string) - 1, -1, -1):
                    if i > 0:
                        if string[i - 1] == string[i]:
                            j += 1
                        else:
                            break
                underscore_at_end = '_' * j
        else:
            return []
        string = string.replace('_', ' ')
        string = '%s%s%s' % (underscore_at_start, string, underscore_at_end)
        # string = f'{underscore_at_start}{string}{underscore_at_end}'
        string = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', string)
        string = re.sub('([a-z0-9])([A-Z])', r'\1 \2', string).lower()
        s_list = string.split()
        return s_list
    else:
        raise TypeError("casepreprocess() argument must be str")
