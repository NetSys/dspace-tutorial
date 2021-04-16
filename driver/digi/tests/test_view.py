import os
import yaml
import copy
import pprint as pp

from digi.view import (
    ModelView,
    TypeView,
    DotView,
)


# TBD pytest
def test():
    os.environ.update({
        "GROUP": "mock.digi.dev",
        "VERSION": "v1",
        "PLURAL": "rooms",
        "NAME": "room",
        "NAMESPACE": "default",
    })
    test_yaml = """
    control:
      brightness:
        intent: 0.8
        status: 0
      mode:
        intent: sleep
        status: sleep
    mount:
      mock.digi.dev/v1/lamps:
        default/lamp-test:
          spec:
            control:
              power: 
                intent: "on"
    """

    # TBD root tests
    orig_v = yaml.load(test_yaml, Loader=yaml.FullLoader)
    v = copy.deepcopy(orig_v)
    print("# Using model view, before:", v)
    with ModelView(v) as mv:
        mv["lamp-test"]["control"]["power"]["intent"] = "off"
    print(f"-----\nafter: {v}\n")

    v = copy.deepcopy(orig_v)
    print("# Using type view, before:", v)
    with TypeView(v) as tv:
        tv["lamps"]["lamp-test"]["control"]["power"]["intent"] = "off"
    print(f"-----\nafter: {v}\n")

    v = copy.deepcopy(orig_v)
    print("with type + dot view chain, before:", v)
    with TypeView(v) as tv, DotView(tv) as dv:
        dv.lamps.lamp_test.control.power.intent = "off"
    print(f"-----\nafter: {v}\n")


if __name__ == '__main__':
    test()
