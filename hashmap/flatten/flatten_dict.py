def flatten_dict(d, result={}, prv_keys=[]):
    for k, v in d.items():
        if isinstance(v, type(dict)):
            flatten_dict(v, result, prv_keys + [k])
        else:
            result['.'.join(prv_keys + [k])] = v
    return result

dict = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }

ans = flatten_dict(dict)
print(ans)