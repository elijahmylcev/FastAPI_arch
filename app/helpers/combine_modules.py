import importlib


def combine_modules_in_all(namespace, module_files, instance) -> list:
    result = list()

    for module in module_files:
        module_name = f"{namespace}.{module}"
        imported_modules = importlib.import_module(module_name)

        for obj_name in dir(imported_modules):
            obj = getattr(imported_modules, obj_name)
            if isinstance(obj, instance):
                result.append(obj)

    return result
