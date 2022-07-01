from adapters.amazonde import get_price as get_amazonde_price


def get_func(entry):
    if entry["name"] == "amazon.de":
        return get_amazonde_price

    raise NotImplemented(f"adapters::base.py::get_func not implemented for {entry}")


def get_price(locations_entry):
    if locations_entry.get("name") is None:
        raise ValueError("adapters::base.py::get_price name not present")

    if locations_entry.get("url") is None:
        raise ValueError("adapters::base.py::get_price url not present")

    fnc = get_func(locations_entry)
    return fnc(locations_entry)
